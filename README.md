# LeadForge AI

LeadForge AI is a lead discovery and intelligence platform built with Django.

The goal of the project is to discover public business leads, analyze their websites, enrich lead information, and help identify higher-value prospects for services such as web design, development, SEO, digital marketing, and related business services.

---

## Current Features

- Django-based lead management system
- PostgreSQL database
- Custom user model
- Dark / Light / System theme
- Lead search creation
- Location-based business discovery
- Niche-based lead discovery
- OpenStreetMap / Overpass integration
- Multiple Overpass endpoint fallback
- Business website discovery
- Public phone extraction
- Public email extraction when available
- Website analysis and enrichment
- Website title extraction
- Meta description extraction
- Basic website quality signals
- Search status workflow
- Lead deduplication
- Responsive dashboard UI
- Search detail page
- Discovered leads table
- Secure URL validation for website analysis

---

## Current Discovery Flow

```text
User Creates Lead Search
        ↓
Query Planner
        ↓
Discovery Source
        ↓
OpenStreetMap / Overpass
        ↓
Lead Normalization
        ↓
Duplicate Detection
        ↓
Save Leads to PostgreSQL
        ↓
Website Enrichment
        ↓
Search Completed