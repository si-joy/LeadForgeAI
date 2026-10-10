from django import forms

from .models import LeadSearch


class LeadSearchForm(forms.ModelForm):
    lead_limit = forms.IntegerField(
        min_value=10,
        max_value=5000,
        initial=100,
        help_text="Maximum number of leads to collect.",
    )

    class Meta:
        model = LeadSearch

        fields = [
            "name",
            "niche",
            "location",
            "keywords",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Web Design Agencies in Toronto"
                }
            ),
            "niche": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Restaurants, Clinics, Shopify Stores"
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Toronto, Canada"
                }
            ),
            "keywords": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "e.g. outdated website, redesign, webflow",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"