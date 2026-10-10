from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import redirect, render

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
    lead_search = LeadSearch.objects.filter(
        pk=pk,
        created_by=request.user,
    ).first()

    if not lead_search:
        return redirect("dashboard")

    return render(
        request,
        "searches/detail.html",
        {
            "lead_search": lead_search,
        },
    )