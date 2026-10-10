from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render

from leads.models import Lead

from .models import LeadSearch


@login_required
def dashboard(request):
    user = request.user

    leads = Lead.objects.filter(
        created_by=user,
    )

    searches = LeadSearch.objects.filter(
        created_by=user,
    )

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
        "recent_leads": leads.select_related(
            "search"
        )[:5],
    }

    return render(
        request,
        "dashboard.html",
        context,
    )