# Sprint 9 - Architecture Refactor

Date: 2026-06-30

## Objective

Refactor the backend into a scalable architecture before implementing additional features.

## Completed

- Reorganized scraper modules into:
  - scrapers/search
  - scrapers/crawlers
  - scrapers/extractors

- Moved backend test scripts into a dedicated backend/tests package.

- Updated all project imports.

- Verified all tests after refactoring.

## Improvements

- Cleaner project structure.
- Better separation of responsibilities.
- Easier future maintenance.
- Simplified extension for additional search providers.

---

# Sprint 10 - Search Manager

## Objective

Decouple the lead pipeline from a specific search provider.

## Completed

- Added Search Manager.
- Pipeline now communicates only with Search Manager.
- Search Manager currently uses DDGS.
- Added duplicate removal.

## Benefits

Future search providers can be added without modifying the pipeline.

---

# Sprint 10.1 - Official Website Finder

## Objective

Improve lead quality by replacing directory websites with official company websites.

## Completed

- Created Official Website Finder service.
- Added automatic lookup of official company websites.
- Pipeline now attempts to replace directory links before crawling.

## Result

Higher quality leads and improved email discovery.

---

# Sprint 10.2 - Dependency Standardization

## Objective

Remove deprecated DuckDuckGo dependency.

## Completed

- Migrated search components to the ddgs package.
- Removed dependency on duckduckgo_search.
- Standardized project search implementation.

## Current Status

Pipeline is stable.

Current limitation:

Directory websites still appear in search results and require smarter classification.

## Sprint 11 Update

Initial rule-based Company Name Cleaner was tested against real-world search results.

Result:

- Successfully identified limitations of simple keyword removal.
- Rule-based cleaning produced incorrect outputs for several common title formats.

Decision:

Redesign the module as a Company Name Parser using candidate extraction and scoring instead of simple text replacement.


## Sprint 11 Review

The candidate-based Company Name Parser improved extraction accuracy but still struggled with several real-world title formats.

Decision:

Rather than continuing to infer company names from search result titles, the project will prioritize extracting authoritative metadata directly from company websites.

This change is expected to improve:

- Company name accuracy
- Phone extraction
- Address extraction
- Social media detection
- Lead quality
# Sprint 11.1

## Architecture Improvement

Created a dedicated `backend/extractors` package.

Purpose:

Separate data extraction from website crawling.

Responsibilities:

- Crawlers → Download web pages.
- Extractors → Parse structured information from downloaded pages.

This architecture improves modularity and makes future extractors (phone, address, social links, metadata) easier to implement and test.

# Sprint 11.2

## Metadata Extractor (Phase 1)

Implemented the first version of the Website Metadata Extractor.

Current extraction:

- HTML Title
- Meta Description
- Open Graph Site Name

Purpose:

Provide a reliable source for company identification directly from the official website.
# Sprint 11.3

## Major Milestone

Successfully extracted authoritative business metadata directly from the company's official website.

Test Result:

Website:
https://bharatplastic.org/

Extracted:

- Company Name
- HTML Title
- Meta Description

Observation:

The extracted company name is significantly more accurate than the original search result title.

Decision:

Website metadata is now considered the primary source of truth for company identification. Search result titles will be used only as a fallback.

# Sprint 12

## Phone Extractor (Phase 1)

Implemented the first version of the phone extraction module.

Features:

- Extracts Indian phone number formats using regular expressions.
- Designed as a standalone extractor for later integration into the metadata pipeline.

Status:

Prototype completed. Awaiting validation across multiple business websites.

# Sprint 12 Review

## Phone Extractor Evaluation

Initial testing successfully extracted phone numbers from company websites.

Observation:

The extractor identified duplicate representations of the same phone number (e.g., with and without country code).

Decision:

Introduce a dedicated normalization layer to standardize extracted data before validation and storage.

Future normalization modules:

- Phone
- Email
- Company Name
- Website
- Address