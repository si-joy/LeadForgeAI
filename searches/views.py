from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render

from leads.models import Lead

from .forms import LeadSearchForm
from .models import LeadSearch


@login_required
def dashboard(request):
    user = request.user

    leads = Lead.objects.filter(created_by=user)
    searches = LeadSearch.objects.filter(created_by=user)

    context = {
        "total_leads": leads.count(),
        "qualified_leads": leads.filter(
            status=Lead.Status.QUALIFIED
        ).count(),
        "total_searches": searches.count(),
        "avg_score": leads.exclude(
            ai_score__isnull=True
        ).aggregate(
            avg=Avg("ai_score")
        )["avg"],
        "recent_leads": leads.select_related("search")[:5],
    }

    return render(
        request,
        "dashboard.html",
        context,
    )


@login_required
def search_list(request):
    searches = (
        LeadSearch.objects
        .filter(created_by=request.user)
        .annotate(leads_count=Count("leads"))
        .order_by("-created_at")
    )

    return render(
        request,
        "searches/list.html",
        {
            "searches": searches,
        },
    )


@login_required
def create_search(request):
    if request.method == "POST":
        form = LeadSearchForm(request.POST)

        if form.is_valid():
            lead_search = form.save(commit=False)
            lead_search.created_by = request.user
            lead_search.status = LeadSearch.Status.DRAFT
            lead_search.lead_limit = form.cleaned_data["lead_limit"]
            lead_search.save()

            messages.success(
                request,
                "Lead search created successfully.",
            )

            return redirect(
                "searches:detail",
                pk=lead_search.pk,
            )

    else:
        form = LeadSearchForm()

    return render(
        request,
        "searches/create.html",
        {
            "form": form,
        },
    )


@login_required
def search_detail(request, pk):
    lead_search = get_object_or_404(
        LeadSearch.objects.annotate(
            leads_count=Count("leads")
        ),
        pk=pk,
        created_by=request.user,
    )

    recent_leads = (
        lead_search.leads
        .select_related("search")
        .order_by("-created_at")[:10]
    )

    return render(
        request,
        "searches/detail.html",
        {
            "lead_search": lead_search,
            "recent_leads": recent_leads,
        },
    )


@login_required
def start_discovery(request, pk):
    if request.method != "POST":
        return redirect(
            "searches:detail",
            pk=pk,
        )

    lead_search = get_object_or_404(
        LeadSearch,
        pk=pk,
        created_by=request.user,
    )

    if lead_search.status not in {
        LeadSearch.Status.DRAFT,
        LeadSearch.Status.FAILED,
    }:
        messages.warning(
            request,
            "This search cannot be started in its current state.",
        )

        return redirect(
            "searches:detail",
            pk=lead_search.pk,
        )

    lead_search.status = LeadSearch.Status.QUEUED
    lead_search.started_at = None
    lead_search.completed_at = None

    lead_search.save(
        update_fields=[
            "status",
            "started_at",
            "completed_at",
            "updated_at",
        ]
    )

    messages.success(
        request,
        "Search has been queued for discovery.",
    )

    return redirect(
        "searches:detail",
        pk=lead_search.pk,
    )