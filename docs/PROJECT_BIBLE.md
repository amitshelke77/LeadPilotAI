# LeadPilot AI - Project Bible

## Objective

Build a client-ready AI Business Automation Platform capable of:

- Company Search
- Website Discovery
- Website Scraping
- Email Extraction
- Phone Extraction
- Excel Export
- AI Business Research
- AI Email Writing

---

## Tech Stack

Python

Streamlit

FastAPI

SQLite

Playwright

BeautifulSoup

Pandas

Gemini

OpenRouter

---

## Development Philosophy

- Modular Architecture
- Complete File Replacements
- Client First
- Reusable Components
- Production Ready

---

## Current Status

Sprint 1

✅ Environment Setup

✅ Git Initialized

✅ Folder Structure

⬜ Dashboard

⬜ Company Search

⬜ Website Discovery

⬜ Email Extraction

⬜ Excel Export

⬜ AI Module

⬜ Deployment

---

## Long Term Goal

Acquire the first paying freelance client using LeadPilot AI.

Save this in docs/PROJECT_BIBLE.md later

LeadPilot AI - Memory Snapshot #4

Current Status:

Local project created

Python environment configured

Dependencies installed

Git initialized

GitHub repository connected

Project Bible created

Initial commits pushed successfully

Architecture Decisions:

Streamlit frontend

FastAPI backend (later)

SQLite database

Modular architecture

Job-based workflow

Reusable business automation modules

Current Sprint:

⬜ Build Dashboard UI

Long-Term Goal:

Get the first paying freelance client using LeadPilot AI.




LeadPilot AI
Version: v0.1.0

Completed

✅ Environment Setup
✅ Git
✅ GitHub
✅ Dashboard
✅ Sidebar
✅ Header
✅ Navigation

Current Sprint

Dashboard UI Polish

Next Sprint

Company Finder

Future

Website Discovery
Email Finder
Google Maps Scraper
Excel Export
AI Research

Goal

First Freelance Client

LeadPilotAI v0.2

✅ Dashboard
✅ Company Finder UI
✅ Backend structure
✅ DataFrame output

Next:
Backend architecture
Maps integration
Website scraper
Email extractor
Excel export

# Sprint 3 Progress (29 June 2026)

## Completed

### Project Foundation

* Python virtual environment configured
* Git repository initialized
* GitHub repository connected
* Modular project architecture established

### Frontend

* Professional Streamlit dashboard
* Sidebar navigation
* Header component
* Custom CSS support
* Company Finder interface

### Backend

* `company_search.py` service created
* `exporter.py` service created
* Backend service architecture established

### Features

* Industry input
* Location input
* Maximum results slider
* Search workflow
* DataFrame display
* Excel export
* Download button

### Improvements

* Fixed Streamlit rerun issue using `st.session_state`
* Export now works reliably
* Results persist after searching

## Current Status

LeadPilot AI now has its first complete end-to-end workflow:

User Input
→ Backend Processing
→ Results Table
→ Excel Export
→ Download

This establishes the foundation for all future automation modules.

## Next Sprint

Goal: Replace dummy company data with real business data.

Modules to build:

* maps_search.py
* website_scraper.py
* email_extractor.py
* exporter.py (enhanced)

Target Workflow:

Industry + Location
↓
Find Real Companies
↓
Website Discovery
↓
Email Extraction
↓
Excel Export

## Long-Term Vision

LeadPilot AI will become a complete AI-powered B2B lead generation platform capable of:

* Company discovery
* Website discovery
* Email extraction
* PDF extraction
* AI research
* Workflow automation
* Multi-format exports

Primary objective:
Generate real freelance income by automating lead generation and business research tasks.


# Sprint 4 - Architecture Upgrade

## Date
29 June 2026

## Completed

### UI
- Dashboard completed
- Sidebar completed
- Header completed
- Company Finder UI completed

### Backend
- Service architecture created
- Company model introduced
- Lead pipeline introduced
- Excel export completed
- Session state implemented

### Improvements
- Switched from deprecated `duckduckgo-search` to `ddgs`
- Started building production-grade search engine
- Preparing multi-source lead generation architecture

## Current Folder Structure

backend/
├── models/
├── pipeline/
├── services/

frontend/
├── components/
├── styles/

exports/
docs/

## Current Goal

Build a production-ready lead generation engine capable of:

Industry
    ↓
Company Search
    ↓
Website Discovery
    ↓
Email Extraction
    ↓
Excel Export

## Future Modules

- Google Maps
- DDGS Search
- Website Scraper
- Email Extractor
- AI Company Research
- PDF Report Generator

## Milestone

LeadPilot AI is transitioning from a UI prototype into a real automation platform.

# Sprint 4 Progress Update

## Major Milestone

LeadPilot AI successfully performed its first real internet search using DDGS.

### Verified Output

* Real company names returned
* Real company websites discovered
* Search engine architecture validated

### Completed Modules

* Dashboard
* Company Finder UI
* Excel Export
* Lead Pipeline
* DDGS Web Search

### Next Module

Email Extraction

Workflow:

Industry + Location

↓

DDGS Search

↓

Website

↓

Email Extraction

↓

Excel Export

## Future Improvements

* AI company summaries
* Phone number extraction
* Contact page detection
* Multi-source search
* Lead quality scoring

## Project Status

LeadPilot AI has moved beyond a prototype and is now processing real-world business data. The next milestone is extracting verified contact information from company websites to create client-ready lead lists.


# Sprint 4 Update

## Completed

* DDGS integration completed
* Real company website discovery working
* Basic email extraction implemented
* Began website crawling module

## Observation

Many companies do not publish email addresses on their homepage.

LeadPilot AI will therefore adopt a two-stage crawling strategy:

Homepage
↓

Locate Contact Page

↓

Extract Emails

This significantly improves lead quality and aligns with how professional lead generation tools operate.

## Next Tasks

* Contact page detection
* Email extraction from contact page
* Website validation
* Integrate with Company Finder UI


# Sprint 5 - Browser Automation Upgrade

## Decision

The project is migrating from HTTP-only scraping (`requests`) to browser automation using Playwright.

## Reason

Modern company websites increasingly rely on JavaScript frameworks (React, Vue, Angular) that do not expose complete page content to simple HTTP requests.

Using Playwright provides:

* JavaScript rendering
* Dynamic content support
* Better contact page discovery
* Higher email extraction success rate
* More reliable data collection

## Expected Benefits

* Higher lead quality
* Better compatibility with modern websites
* Stronger foundation for future AI automation features

## Current Status

Completed:

* DDGS search
* Website discovery
* Excel export
* Lead pipeline

In Progress:

* Browser-based website crawler
* Email extraction engine

Goal:
Produce client-ready lead lists with significantly higher success rates.

# Sprint 5 Milestone

## Browser Automation

Playwright and Chromium have been successfully installed and verified.

Test Result:

* Browser launched successfully.
* Navigation test passed.
* Page title extraction confirmed.

This establishes the foundation for browser-based automation.

## Strategic Decision

Before implementing additional scraping features, the project will transition to a finalized architecture.

Objectives:

* Stable folder organization
* Clear module responsibilities
* Production-grade coding standards
* Easier testing and maintenance
* Faster feature development

## Current Status

Working Components:

* Streamlit UI
* Company Finder
* DDGS Search
* Excel Export
* Lead Pipeline
* Browser Automation (Playwright)

Next Objective:
Refactor into a scalable architecture and build the first complete lead generation pipeline.


# Sprint 5 - Architecture Review

## Repository Review

The project structure has been reviewed and approved.

The existing layout is clean and provides a strong foundation for future development.

## Architecture Decision

Backend responsibilities will be separated into:

- Services (business logic)
- Scrapers (data collection)
- Models (data structures)
- Pipeline (data processing)
- Exporters (Excel/PDF)
- AI (LLM integrations)
- Utils (shared helpers)

This separation improves maintainability and scalability.

## Documentation

The project documentation now consists of:

- PROJECT_BIBLE.md — Long-term vision and milestones
- DEVLOG.md — Daily progress and technical decisions
- ROADMAP.md — Planned development phases
- ARCHITECTURE.md — Folder structure and coding standards
- MASTER_PLAN.md — Complete feature roadmap

## Goal

Build a production-ready AI Business Automation Platform suitable for:
- Freelancing
- Portfolio presentation
- Job applications
- Future SaaS expansion

# Sprint 6 - Backend Modularization

## Objective

Separate backend responsibilities into dedicated modules following professional software architecture.

### Scrapers

Responsible for collecting information from external sources.

### Services

Responsible for business logic and data processing.

### Exporters

Responsible for exporting data into user-friendly formats.

## Benefits

- Better maintainability.
- Easier testing.
- Cleaner codebase.
- Simpler future feature development.

This establishes the foundation for scalable development of LeadPilot AI.
# Sprint 6 Planning

## Current Progress

### Completed
- Modular backend architecture
- DDGS company search
- Contact page detection
- Browser automation with Playwright
- Streamlit dashboard
- Excel export
- Documentation structure

### Next Sprint

Develop the Lead Pipeline.

Pipeline Flow:

User Input
↓

Company Search

↓

Website Discovery

↓

Browser Automation

↓

Email Extraction

↓

Phone Extraction

↓

Company Data Model

↓

Excel Export

↓

AI Company Summary

## Objective

Transition from independent modules into one complete end-to-end lead generation workflow capable of generating client-ready lead lists.

# Sprint 6 Complete

## Repository Status

LeadPilot AI has completed its foundational architecture.

### Backend
- Modular package structure
- Scrapers
- Services
- Exporters
- Pipeline
- AI module (placeholder)
- Config module
- Utilities

### Frontend
- Dashboard
- Sidebar
- Header
- Company Finder

### Integrations
- DDGS Search
- Playwright
- BeautifulSoup
- Pandas
- Excel Export

### Documentation
- PROJECT_BIBLE.md
- DEVLOG.md
- ROADMAP.md
- ARCHITECTURE.md

### Current Version

LeadPilot AI v0.6

The project has transitioned from a prototype into a structured software engineering project suitable for continued development and portfolio presentation.

Next milestone:
Implement the first complete end-to-end lead generation pipeline and integrate it into the Streamlit interface.

# Sprint 7 - First End-to-End Pipeline

## Milestone

LeadPilot AI successfully executed its first complete lead generation pipeline.

Pipeline:

Industry + Location

↓

Company Search (DDGS)

↓

Website Discovery

↓

Contact Page Detection

↓

Email Extraction

↓

Structured Lead Output

## Test Results

Input:
Plastic Manufacturers
Pune

Output:
- 5 company websites discovered
- Multiple contact pages identified
- Multiple verified email addresses extracted

## Next Objectives

- Browser-based scraping using Playwright
- Multi-page crawling
- Phone extraction
- AI company summaries
- Lead scoring
- Streamlit integration
# Development Workflow

To maintain code quality and repository history, every sprint follows the same lifecycle:

1. Implement a feature.
2. Test all affected modules.
3. Update documentation.
4. Commit with a descriptive message.
5. Push to GitHub.

This ensures every commit represents a stable milestone and allows easy rollback if required.

# Sprint 8 - Smart Crawling

## Objective

Increase lead extraction quality by crawling multiple high-value pages instead of relying on a single contact page.

## New Component

site_crawler.py

Responsibilities:
- Discover internal links
- Prioritize business-relevant pages
- Return ranked URLs for downstream extraction

## Architecture Principle

Each backend package has a single responsibility:

- Scrapers: Collect data
- Services: Process data
- Pipeline: Orchestrate workflow
- AI: Generate insights
- Exporters: Save results

This separation improves scalability and maintainability.

# Sprint 8

## Smart Website Crawling

LeadPilot now crawls multiple high-value pages instead of relying on a single contact page.

Pipeline:

Website

↓

Homepage

↓

Internal Link Discovery

↓

Priority Ranking

↓

Multi-page Email Extraction

Benefits:

- Higher email discovery rate
- Better data quality
- Reduced dependence on dedicated contact pages

Future improvements:

- Phone extraction
- Website quality filtering
- AI summaries
- Lead scoring
# Sprint 8.1 - Crawler Optimization

## Improvements

The crawler now ignores non-HTML resources.

Ignored file types:
- PDF
- Images
- Office documents
- Archives
- Media files

Ignored external platforms:
- Facebook
- Instagram
- LinkedIn
- YouTube
- Twitter

## Benefits

- Faster crawling
- Better resource usage
- Higher chance of discovering contact information
- Cleaner lead extraction pipeline

# Architecture Revision - v2

## Scraper Layer Refactoring

The scraping subsystem has been reorganized into three responsibilities:

- search/
  Responsible for discovering company websites.

- crawlers/
  Responsible for navigating websites and collecting pages.

- extractors/
  Responsible for extracting structured data such as emails and phone numbers.

This improves maintainability and makes it easier to add new providers without affecting existing code.

## Testing

All backend test scripts will gradually move into a dedicated `backend/tests/` package to separate production code from development utilities.

# Sprint 9 Complete

## Refactoring

Completed restructuring of the scraper subsystem.

### New Layout

scrapers/
    search/
    crawlers/
    extractors/

tests/

Benefits:

- Better modularity
- Cleaner imports
- Easier maintenance
- Scalable architecture for future providers

# Sprint 10 - Search Manager

Introduced a Search Manager layer between the pipeline and search providers.

Current Provider:
- DDGS

Future Providers:
- Google Maps
- Brave Search
- Bing
- Serper API

Benefits:
- Pipeline no longer depends on a specific search engine.
- Easier expansion.
- Centralized result deduplication.
## Sprint 10 Progress

### Search Manager
- Introduced a Search Manager layer between the pipeline and search providers.
- Pipeline now depends on the Search Manager instead of a specific search provider.

### Website Filtering
- Continued refining directory detection.
- Real-world testing identified additional directory domains (e.g., WebIndia123).
- Filtering will continue to evolve based on production test results.
# Sprint 10.1

Added Official Website Finder service.

Purpose:

Convert company names into official websites before crawling.

Benefits:

- Higher email discovery rate
- Fewer directory pages
- Better lead quality
- Cleaner exports

# Sprint 10.2

## Dependency Migration

Completed migration from the deprecated `duckduckgo_search` package to `ddgs`.

Benefits:
- Uses the actively maintained package.
- Eliminates deprecation warnings.
- Standardizes search functionality across the project.

## Next Priority

Implement Company Name Extraction to improve official website discovery and overall lead quality.

# Sprint 11 Planning

## Goal

Improve lead quality before expanding features.

### Planned Modules

1. Company Name Cleaner
2. Website Classifier
3. Phone Extractor
4. Address Extractor
5. Google Maps Integration

Reason:

A clean and accurate lead database is more valuable than adding AI features to poor-quality data.

# Current Development Phase

LeadPilot AI has completed its foundational architecture.

The focus has shifted from infrastructure development to lead quality.

Upcoming priorities:

1. Company Name Cleaner
2. Website Classifier
3. Phone Extraction
4. Address Extraction
5. Google Maps Integration
6. AI Enrichment
7. CRM Integration

The long-term objective is to create a production-grade lead generation platform capable of discovering and enriching thousands of business leads.

### Company Name Parser

The project will use a parsing approach instead of a rule-based cleaner.

Pipeline:

Search Result Title
        ↓
Candidate Extraction
        ↓
Candidate Scoring
        ↓
Validation
        ↓
Best Company Name

Reason:

Real-world website titles are highly inconsistent and cannot be reliably cleaned using keyword removal alone.
## Website Metadata Extractor

LeadPilot AI will use website metadata as the primary source of truth.

Priority metadata:

- HTML Title
- Open Graph tags
- JSON-LD Organization schema
- Meta Description
- Contact Information
- Logo
- Social Media
- Business Identifiers

Search engine titles will be treated as a fallback rather than the primary source of company information.

## Backend Architecture Principle

LeadPilot follows a separation-of-concerns design.

Modules:

- Search → Find candidate websites.
- Services → Business logic.
- Crawlers → Retrieve web pages.
- Extractors → Extract structured business data.
- Pipeline → Coordinate the complete workflow.
- AI → Generate summaries and outreach content.

Each module has a single responsibility and should remain independently testable.

## Metadata First Strategy

LeadPilot prefers authoritative website metadata over search engine titles.

Priority order:

1. JSON-LD Organization
2. Open Graph Site Name
3. HTML Title
4. Search Result Title

This strategy minimizes incorrect company names and improves lead quality.
## Source of Truth Hierarchy

LeadPilot AI prioritizes business information using the following order:

1. JSON-LD Organization Schema
2. Open Graph Metadata
3. HTML Metadata
4. Contact Page Content
5. Website Footer
6. Search Engine Results

Whenever conflicting information exists, the highest-priority available source is used.
## Business Intelligence Extractors

LeadPilot extracts structured business information through specialized modules.

Current roadmap:

- Metadata Extractor
- Phone Extractor
- Email Extractor
- Address Extractor
- Social Media Extractor
- Logo Extractor
- JSON-LD Extractor

Each extractor should remain independent and reusable within the pipeline.

## Data Processing Pipeline

LeadPilot separates data processing into four stages:

1. Extraction
2. Normalization
3. Validation
4. Storage

This design minimizes duplicate logic and ensures all exported business data follows a consistent format regardless of its original representation.


## Normalization Layer

LeadPilot separates extraction from normalization.

Extractors collect raw data.

Normalizers standardize data into a canonical format before validation and storage.

Benefits:

- Cleaner exports
- Reduced duplication
- Easier validation
- Better AI input quality

## Canonical Data

Every extracted value should be converted into a canonical representation before entering the pipeline.

Example:

+91 9860256222
+91-9860256222
919860256222

↓

9860256222

Canonical data reduces duplicates and simplifies validation, storage, AI processing, and exports.
## Canonical Website

LeadPilot treats all pages of a company as one canonical website.

Example:

https://company.com/about

https://company.com/contact

https://www.company.com

↓

https://company.com

This reduces duplicate crawls and improves performance across the pipeline.

## Company Identity Resolution

Company names may appear differently across web pages.

LeadPilot resolves a canonical company name by combining multiple independent signals and assigning confidence scores.

This enables consistent reporting and prevents duplicate company records.

## Company Identity Strategy

LeadPilot resolves company identity using a priority order rather than relying on a single source.

Priority:

1. JSON-LD Organization
2. Open Graph Metadata
3. Standard Metadata
4. HTML Title
5. Domain Analysis
6. AI Fallback

This approach improves accuracy and reduces false positives from marketing page titles.

## Structured Data First

Whenever structured business data (JSON-LD) is available, LeadPilot prefers it over heuristic extraction from HTML.

Priority order:

1. JSON-LD
2. Open Graph
3. Standard Meta Tags
4. HTML Title
5. Domain Heuristics
6. AI Fallback

This improves accuracy while reducing false positives.

## JSON-LD Compatibility

LeadPilot supports both simple and advanced Schema.org implementations.

Supported patterns include:

- Single @type values
- Multiple @type arrays
- Nested @graph collections

This improves compatibility with modern CMS platforms and SEO plugins.

## Data Enrichment Architecture

LeadPilot follows a layered enrichment pipeline.

Website
    ↓
Crawler
    ↓
Extractors
    ↓
Normalizers
    ↓
Merge Engine
    ↓
Business Profile
    ↓
AI Enrichment
    ↓
Lead Output

Extractors never overwrite fields directly. They only collect evidence.

The enrichment layer determines the final value for each field based on source priority, normalization, and confidence.