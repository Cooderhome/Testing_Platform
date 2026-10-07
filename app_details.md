# BUILD PROMPT: VISUAL WEB APPLICATION CRITIC & TESTING PLATFORM

## 1. PRODUCT NAME

Build a professional web application called:

# AppCritic

### Tagline

**Point. Comment. Track. Report. Improve.**

AppCritic is a visual web application testing, criticism, usability review, QA, and reporting platform.

The purpose of the platform is to allow a tester — including a non-technical user — to test another web application visually and interactively.

The tester should be able to:

1. Create or select a testing project.
2. Open the target web application.
3. Enter "Critic Mode".
4. Hover over or click any visible element.
5. Automatically identify the selected location/element.
6. Add a comment, observation, bug, suggestion, or criticism.
7. Select category and severity.
8. Automatically capture a screenshot/evidence.
9. Save the finding.
10. Continue testing.
11. Review all findings on a dashboard.
12. Assign findings to developers.
13. Track fixes and retest them.
14. Generate professional reports for developers, managers, and senior officials.

The application must prioritize:

* Simplicity
* Ease of use
* Visual feedback
* Evidence
* Traceability
* Professional reporting
* Clear workflows
* Minimal technical knowledge required

---

# 2. IMPORTANT PRODUCT PRINCIPLE

The tester should NOT need to understand:

* HTML
* CSS
* JavaScript
* DOM
* CSS selectors
* Browser developer tools
* Programming
* Database systems

The platform should automatically collect technical information where possible.

The tester should mainly have to:

> OPEN → CLICK → COMMENT → SAVE

Everything else should be automated or simplified.

---

# 3. TECHNOLOGY STACK

Use a simple maintainable architecture.

## Backend

Use:

* Python
* Django
* Django REST Framework where an API is useful
* PostgreSQL

Do NOT use microservices for the MVP.

Do NOT create unnecessary complexity.

Use Django's:

* authentication
* ORM
* admin
* permissions
* forms
* sessions

where appropriate.

---

# 4. FRONTEND

For the initial version use:

* Django Templates
* HTML5
* CSS
* JavaScript
* Bootstrap 5 or a clean modern CSS system
* HTMX where useful

Avoid React/Next.js for the initial MVP unless there is a strong technical reason.

The application should be easy to deploy and maintain.

The UI should feel like a modern SaaS application.

---

# 5. DATABASE

Use PostgreSQL.

Create a clean relational data model.

Core entities:

## User

Fields:

* id
* username
* email
* first_name
* last_name
* password
* role
* organization
* is_active
* created_at

Roles:

* ADMIN
* TESTER
* DEVELOPER
* MANAGER
* EXECUTIVE
* VIEWER

---

## Organization

Fields:

* id
* name
* description
* logo
* created_at

---

## Project

Represents an application being tested.

Fields:

* id
* organization
* name
* description
* target_url
* environment
* status
* created_by
* created_at
* updated_at

Environment choices:

* Development
* Testing
* Staging
* Production

Warn users before testing production systems.

---

## Application

Optional separate entity for applications.

Fields:

* id
* project
* name
* base_url
* technology
* description
* owner
* created_at

Technology examples:

* Django
* Flask
* Java
* Spring
* React
* Angular
* Vue
* PHP
* .NET
* Other

Do not require the tester to know the technology.

---

## TestingSession

Fields:

* id
* project
* tester
* title
* description
* started_at
* ended_at
* status
* environment
* browser
* operating_system

Statuses:

* Planned
* Active
* Paused
* Completed
* Archived

---

## Module

Represents a functional area of the target application.

Examples:

* Dashboard
* Login
* Data Discovery
* Search
* CDR Analytics
* Investigation
* Reports
* Administration

Fields:

* id
* project
* name
* description
* order
* created_at

---

## Finding

This is the central entity.

Fields:

* id
* project
* testing_session
* module
* reporter
* assigned_to
* title
* description
* category
* severity
* priority
* status
* expected_behavior
* actual_behavior
* recommendation
* page_url
* page_title
* element_identifier
* element_text
* element_tag
* element_selector
* x_position
* y_position
* viewport_width
* viewport_height
* browser
* operating_system
* created_at
* updated_at
* resolved_at
* verified_at

Categories:

* BUG
* USABILITY
* UI_UX
* DATA_QUALITY
* PERFORMANCE
* ACCESSIBILITY
* SECURITY
* FUNCTIONAL
* REQUIREMENT
* IMPROVEMENT
* OTHER

Statuses:

* NEW
* TRIAGED
* ASSIGNED
* IN_PROGRESS
* FIXED
* READY_FOR_RETEST
* RETESTING
* VERIFIED
* REOPENED
* CLOSED
* WONT_FIX
* DUPLICATE

Severity:

* CRITICAL
* HIGH
* MEDIUM
* LOW
* INFORMATIONAL

---

# 6. FINDING EVIDENCE

Create an Evidence model.

Fields:

* id
* finding
* file
* evidence_type
* description
* uploaded_by
* created_at

Evidence types:

* SCREENSHOT
* VIDEO
* DOCUMENT
* LOG
* OTHER

The platform should automatically capture screenshots when the tester creates a finding where technically possible.

---

# 7. ANNOTATION MODEL

Create an Annotation model.

An annotation identifies where on a webpage a finding was created.

Fields:

* id
* finding
* page_url
* page_title
* selector
* element_tag
* element_text
* x
* y
* width
* height
* viewport_width
* viewport_height
* scroll_x
* scroll_y
* created_at

The annotation should allow the system to visually mark the location.

---

# 8. COMMENTS

Create threaded comments.

Fields:

* id
* finding
* user
* comment
* created_at
* updated_at

Users should be able to discuss findings.

Example:

Tester:

> The search filter disappears when returning to this page.

Developer:

> Fixed in build 1.4.2.

Tester:

> Retested. Working correctly.

---

# 9. STATUS HISTORY

Every important finding change should be recorded.

Create FindingStatusHistory:

* finding
* old_status
* new_status
* changed_by
* comment
* timestamp

This creates an audit trail.

---

# 10. CRITIC MODE

This is the signature feature.

The platform should provide a clear button:

# START CRITIC MODE

When activated:

* display a subtle floating toolbar
* allow the tester to hover over webpage elements
* highlight the element under the mouse
* show a small indicator
* allow the tester to click the element
* open the "New Finding" form

Example:

+----------------------------------------------+
| Target Application                           |
|                                              |
|       Search Data                            |
|       [______________] [SEARCH]              |
|                              ^               |
|                              |               |
|                         Clicked element      |
|                                              |
+----------------------------------------------+

After clicking:

+----------------------------------------------+
| NEW FINDING                                  |
+----------------------------------------------+
| Category                                     |
| [ Usability                         v ]      |
|                                              |
| Severity                                     |
| [ Medium                            v ]      |
|                                              |
| What did you notice?                         |
| [****************************************]   |
| [****************************************]   |
|                                              |
| Expected behavior                            |
| [****************************************]   |
|                                              |
| Recommendation                               |
| [****************************************]   |
|                                              |
| [ Screenshot automatically captured ]        |
|                                              |
|              [ CANCEL ] [ SAVE FINDING ]      |
+----------------------------------------------+

---

# 11. DO NOT FORCE THE TESTER TO FILL EVERYTHING

This is extremely important.

The minimum finding form should only require:

* Category
* Comment

Everything else can be optional.

The system should automatically populate:

* URL
* Page title
* timestamp
* browser
* viewport
* selected element
* element text
* screenshot
* tester
* project
* session

The user can expand "More details" for:

* Expected behavior
* Actual behavior
* Recommendation
* Severity
* Priority

---

# 12. QUICK FINDING MODE

Add a very fast option:

# Quick Note

The tester clicks an element and writes:

> "This label is confusing."

Click:

# SAVE

The system creates the finding.

Later the tester or manager can complete the structured information.

This makes the platform usable during exploratory testing.

---

# 13. SCREENSHOT SYSTEM

When a finding is created:

1. Capture the visible webpage where possible.
2. Highlight the selected element.
3. Add an annotation marker.
4. Save screenshot as evidence.
5. Associate it with the finding.

Example:

Screenshot:

```text
+----------------------------------------+
| Data Discovery                         |
|                                        |
| Search: [___________] 🔴 01            |
|                                        |
| Results                                |
|                                        |
+----------------------------------------+

01
Search button is not visually obvious.
```

The original screenshot should also be preserved if technically possible.

Never alter the original evidence.

---

# 14. TARGET APPLICATION SUPPORT

The system must be designed with browser security restrictions in mind.

Do NOT assume that arbitrary external websites can simply be embedded in an iframe and modified.

Implement support using:

## Primary approach

Browser extension / content script.

The browser extension should communicate with the Django backend API.

Architecture:

Browser
|
| Extension
|
v
Target Web Application
|
| REST API
v
Django Backend
|
v
PostgreSQL

The extension should:

* inject Critic Mode
* detect hovered elements
* detect clicked elements
* collect page URL
* collect page title
* collect element information
* capture annotation coordinates
* communicate findings to the backend

---

# 15. BROWSER EXTENSION

Create a Chrome/Edge-compatible extension.

Use Manifest V3.

Structure:

browser-extension/

```
manifest.json
background.js
content.js
popup.html
popup.js
styles.css
```

Features:

* Login/connect to AppCritic
* Select project
* Select testing session
* Start Critic Mode
* Stop Critic Mode
* Create finding
* Display finding markers
* Send evidence to API

The extension must NOT collect page information when Critic Mode is disabled.

Only collect information required for the active testing session.

---

# 16. SECURITY PRINCIPLE FOR EXTENSION

Privacy is extremely important.

The extension must:

* require explicit activation
* only collect information during an active testing session
* clearly show when Critic Mode is active
* never silently collect browsing history
* never capture passwords
* never capture authentication tokens
* never capture payment information
* never capture unrelated browser tabs
* never transmit page content unnecessarily

Provide a visible:

# CRITIC MODE ACTIVE

indicator.

Add:

# STOP CRITIC MODE

button.

---

# 17. PROJECT DASHBOARD

Create a beautiful dashboard.

Example:

+---------------------------------------------------------+
| AppCritic                                               |
+---------------------------------------------------------+
| Dashboard | Projects | Findings | Reports | Users      |
+---------------------------------------------------------+

PROJECTS

+-------------------+-------------------+------------------+
| DataFusion        | Tender Platform   | Clinic System    |
| 42 findings       | 18 findings       | 7 findings       |
| 8 open            | 4 open            | 2 open           |
| [Open]            | [Open]            | [Open]           |
+-------------------+-------------------+------------------+

---

# 18. PROJECT PAGE

Show:

Project name

Target URL

Environment

Testing sessions

Finding statistics

Charts

Recent findings

Open issues

Resolved issues

Modules

Reports

Example:

+------------------------------------------------------+
| DataFusion                                           |
| Data Discovery & Investigation Platform             |
|                                                      |
| [Start Testing] [View Findings] [Generate Report]   |
+------------------------------------------------------+

+----------+----------+----------+----------+
| 52       | 8        | 32       | 12       |
| Findings | High     | Resolved | Open     |
+----------+----------+----------+----------+

---

# 19. FINDINGS DASHBOARD

Provide powerful filtering.

Filters:

* Project
* Session
* Module
* Tester
* Developer
* Category
* Severity
* Priority
* Status
* Date
* Environment

Table:

| ID     | Title          | Category  | Severity | Module    | Status | Assigned |
| ------ | -------------- | --------- | -------- | --------- | ------ | -------- |
| DF-001 | Search unclear | Usability | Medium   | Discovery | Open   | Dev A    |
| DF-002 | Graph fails    | Bug       | High     | Analytics | Fixed  | Dev B    |

Clicking a row opens the complete finding.

---

# 20. FINDING DETAIL PAGE

Create a professional detail page.

Display:

## DF-001

### Search action is difficult to identify

Badges:

USABILITY

MEDIUM

OPEN

Then:

### Location

Project:

DataFusion

Module:

Data Discovery

Page:

/data-discovery

Element:

Search button

### Observation

[tester comment]

### Expected

[expected behavior]

### Actual

[actual behavior]

### Recommendation

[recommendation]

### Evidence

Screenshot

### Activity

Tester created finding.

Developer assigned.

Developer marked fixed.

Tester retested.

Tester verified.

---

# 21. VISUAL FINDING MARKERS

When a tester revisits a page in Critic Mode, display markers.

Example:

```text
        🔴 1
             ┌─────────────┐
             │ Search      │
             └─────────────┘

                 🟡 2

             ┌─────────────┐
             │ Filter      │
             └─────────────┘
```

Colors should correspond to severity.

Click marker:

Open finding.

Allow:

* View
* Edit
* Comment
* Change status

---

# 22. TEST CASE MANAGEMENT

The platform should not only record bugs.

Add test cases.

TestCase fields:

* id
* project
* module
* title
* objective
* preconditions
* test_data
* steps
* expected_result
* priority
* status

Example:

DF-TC-001

Title:

Search using valid identifier.

Steps:

1. Open Data Discovery.
2. Enter approved test identifier.
3. Select date range.
4. Click Search.

Expected:

Matching records are displayed.

---

# 23. TEST EXECUTION

A tester should be able to execute a test case.

Display:

PASS

FAIL

BLOCKED

NOT TESTED

If FAIL:

Automatically offer:

# Create Finding

The platform should prepopulate:

* Test case
* module
* expected result
* tester
* session

This connects testing to issue tracking.

---

# 24. TESTING SESSION

A session represents a testing activity.

Example:

# DataFusion Regression Test — Build 2.4.0

Tester:

John

Date:

30 September 2026

Environment:

Staging

Modules:

Data Discovery
CDR Analytics
Investigation

Test cases:

120

Passed:

98

Failed:

15

Blocked:

7

Findings:

23

---

# 25. REPORT GENERATION

Create a dedicated:

# REPORT CENTER

Users can select:

Report type:

* Executive Report
* Developer Report
* QA Report
* Usability Report
* Data Quality Report
* Module Report
* Testing Session Report
* Full Project Report

Formats:

* PDF
* DOCX
* XLSX
* HTML

---

# 26. EXECUTIVE REPORT

Keep it simple.

Do not overwhelm senior officials with technical details.

Include:

## Executive Summary

Short description of the testing activity.

## Testing Scope

Modules and environment tested.

## Findings Summary

Charts.

## Major Risks

Short descriptions.

## Major Recommendations

Prioritized actions.

## Testing Coverage

Modules and workflows tested.

## Trend

Compare previous testing sessions.

## Appendix

Detailed findings if required.

---

# 27. DEVELOPER REPORT

Include technical details:

* Finding ID
* URL
* module
* selector
* element
* browser
* viewport
* reproduction steps
* expected result
* actual result
* screenshot
* severity
* priority
* environment
* tester
* timestamp
* comments
* status history

---

# 28. MANAGEMENT DASHBOARD

Create an executive dashboard.

Cards:

Total Findings

Open Findings

Critical

High

Resolved

Verification Pending

Then charts:

Findings by category

Findings by module

Findings by severity

Resolution trend

Testing coverage

Do not create misleading "quality scores" unless the organization defines the methodology.

---

# 29. REPORT TEMPLATES

Allow administrators to configure report templates.

Fields:

* Organization logo
* Report title
* Prepared by
* Review period
* Application
* Environment
* Confidentiality label
* Executive summary
* Findings
* Recommendations
* Appendix

---

# 30. AI ASSISTANCE

Add AI only after the core system works.

AI features:

## Convert note to professional finding

Input:

"The search button is confusing."

Output suggestion:

Title:
Search action is not sufficiently clear.

Category:
Usability.

Description:
The primary search action may not be immediately identifiable to a new user.

Recommendation:
Improve visual prominence and labeling of the primary search action.

The tester must approve the generated content.

---

## AI duplicate detection

When creating:

"The search button is difficult to find."

The system can suggest:

"Similar finding DF-023 already exists."

Do not automatically merge findings.

Allow the tester to decide.

---

## AI report summary

Generate a draft summary from approved findings.

The report must clearly distinguish:

* Observed facts
* Tester observations
* Recommendations

AI must not invent test results.

---

# 31. NOTIFICATION SYSTEM

Notify users when:

* Finding assigned
* Finding commented
* Finding fixed
* Finding ready for retest
* Finding reopened
* Report generated

Use in-app notifications first.

Email can be added later.

---

# 32. ROLE PERMISSIONS

## Admin

Everything.

## Tester

* Create sessions
* Execute tests
* Create findings
* Add evidence
* Comment
* Retest
* Verify

## Developer

* View assigned findings
* Comment
* Change development status
* Mark fixed

## Manager

* View projects
* View reports
* Assign findings
* Review progress

## Executive

* View executive dashboards
* View reports
* No technical editing required

## Viewer

Read-only.

---

# 33. AUDIT LOG

Record important actions.

Examples:

User created finding.

User changed severity.

Developer assigned.

Developer marked fixed.

Tester reopened.

Tester verified.

Report generated.

Store:

* user
* action
* object
* timestamp
* IP where appropriate
* metadata

Do not record sensitive page content unnecessarily.

---

# 34. USER EXPERIENCE PRINCIPLES

The application must follow these principles:

### Principle 1

One primary action per screen.

### Principle 2

Don't make users fill information the system already knows.

### Principle 3

Use plain language.

Instead of:

"DOM selector"

show:

"Selected element".

Instead of:

"HTTP response exception"

show:

"Something went wrong while loading this page."

Technical information can appear under "Technical details".

### Principle 4

Always provide feedback after actions.

### Principle 5

Never silently lose tester work.

### Principle 6

Make evidence easy to access.

### Principle 7

Use consistent terminology everywhere.

---

# 35. RESPONSIVE DESIGN

The main dashboard must work on:

* Desktop
* Laptop
* Tablet

The browser testing interface is primarily desktop-oriented because precise element annotation is easier with a mouse.

---

# 36. ACCESSIBILITY

Implement:

* keyboard navigation
* visible focus states
* semantic HTML
* adequate contrast
* labels for form controls
* accessible error messages
* screen-reader-friendly controls where practical

---

# 37. ERROR HANDLING

Never show raw stack traces to normal users.

Bad:

"IntegrityError: duplicate key value..."

Good:

"Unable to save this finding. Please try again."

Technical details should only be available to authorized administrators.

---

# 38. PERFORMANCE

The application should remain responsive with:

* thousands of findings
* large projects
* many testing sessions
* many screenshots

Use:

* database indexes
* pagination
* lazy loading
* optimized queries
* compressed images
* background jobs for large report generation when necessary

Do not load thousands of screenshots on one page.

---

# 39. API

Create a clean REST API.

Example endpoints:

POST /api/auth/login/

GET /api/projects/

POST /api/projects/

GET /api/projects/{id}/

GET /api/projects/{id}/findings/

POST /api/findings/

GET /api/findings/{id}/

PATCH /api/findings/{id}/

POST /api/findings/{id}/comments/

POST /api/findings/{id}/evidence/

POST /api/findings/{id}/retest/

POST /api/reports/generate/

The browser extension should use authenticated API requests.

---

# 40. ADMIN PANEL

Customize Django Admin.

Admins should be able to manage:

* users
* organizations
* projects
* applications
* modules
* testing sessions
* findings
* categories
* severity levels
* reports
* audit logs

Make the admin useful for system administration, but do not make normal testers use Django Admin.

---

# 41. SECURITY

Implement:

* CSRF protection
* secure authentication
* password hashing
* session management
* role-based permissions
* object-level authorization
* secure file upload validation
* maximum upload sizes
* safe filename handling
* secure report access
* access logging
* environment variables for secrets
* HTTPS in production

Never place database passwords or API keys in source code.

---

# 42. FILE UPLOAD SECURITY

Screenshots and evidence must be validated.

Restrict:

* file type
* MIME type
* size
* filename

Store uploads safely.

Do not execute uploaded files.

---

# 43. PROJECT STRUCTURE

Use a clean Django structure:

appcritic/
│
├── manage.py
│
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/
├── organizations/
├── projects/
├── testing/
├── findings/
├── evidence/
├── reports/
├── notifications/
├── audit/
├── api/
│
├── templates/
│
├── static/
│
├── media/
│
├── browser_extension/
│
├── requirements.txt
├── .env.example
└── README.md

Keep the application modular but not unnecessarily fragmented.

---

# 44. INITIAL SCREENS

Build these screens first:

1. Login
2. Dashboard
3. Projects
4. Project Detail
5. Testing Sessions
6. Start Testing
7. Critic Mode
8. New Finding
9. Findings
10. Finding Detail
11. Test Cases
12. Test Execution
13. Reports
14. Report Detail
15. Users
16. Settings

---

# 45. DASHBOARD DESIGN

Use a professional modern interface.

Sidebar:

Dashboard

Projects

Testing Sessions

Findings

Test Cases

Reports

Users

Settings

Bottom:

User Profile

Logout

Top bar:

Project selector

Environment indicator

Notifications

User menu

---

# 46. VISUAL STYLE

Use a professional enterprise/SaaS design.

Avoid excessive decoration.

Use:

* clean cards
* consistent spacing
* readable typography
* clear hierarchy
* subtle borders
* restrained colors
* severity badges
* clear icons
* responsive tables

Severity colors:

CRITICAL → red

HIGH → orange

MEDIUM → yellow

LOW → green/neutral

Do not rely only on color. Include text labels.

---

# 47. ONBOARDING

A new tester should understand the application quickly.

First login:

Show:

# Welcome to AppCritic

"Test any supported web application by opening a project, starting a testing session, and using Critic Mode to record observations."

Then three steps:

1. Select Project
2. Start Testing
3. Click + Comment

Include a small demo.

---

# 48. EMPTY STATES

Never show blank pages.

Example:

No projects:

"Your organization has no testing projects yet."

[Create Project]

No findings:

"No findings have been recorded in this session."

[Start Testing]

No reports:

"No reports have been generated yet."

[Generate Report]

---

# 49. DEMO DATA

Create a management command:

python manage.py seed_demo

Create a demonstration project:

"DataFusion Demo"

Modules:

* Dashboard
* Data Discovery
* CDR Analytics
* Investigation
* Relationship Graph
* Reports

Create sample findings.

This makes it easy to demonstrate the system immediately.

---

# 50. TESTING THE TESTING PLATFORM

The platform itself must have tests.

Implement:

## Unit tests

Models

Services

Permissions

Report generation

## Integration tests

Finding creation

Evidence upload

Status transitions

## UI tests

Login

Project creation

Finding creation

Report generation

## Security tests

Unauthorized access

Object-level permissions

File upload validation

## Regression tests

Important workflows after changes.

---

# 51. README

Create a professional README containing:

* Product overview
* Features
* Architecture
* Installation
* Environment variables
* PostgreSQL setup
* Django migration
* Demo data
* Running development server
* Browser extension setup
* Testing
* Deployment
* Security considerations
* User roles
* Report generation
* Troubleshooting

---

# 52. DEVELOPMENT PHASES

Do not attempt to build everything simultaneously.

## PHASE 1 — Foundation

Build:

* Django project
* PostgreSQL
* Authentication
* Organizations
* Projects
* Roles
* Dashboard

## PHASE 2 — Testing System

Build:

* Testing sessions
* Modules
* Test cases
* Test execution
* Findings

## PHASE 3 — Critic Mode

Build:

* Browser extension
* Element selection
* Annotation
* Screenshot capture
* Finding creation

## PHASE 4 — Workflow

Build:

* Assignment
* Comments
* Status transitions
* Retesting
* Verification
* Audit trail

## PHASE 5 — Reporting

Build:

* Executive reports
* Developer reports
* QA reports
* PDF
* DOCX
* XLSX

## PHASE 6 — AI

Build:

* AI finding improvement
* Duplicate suggestions
* Report summaries

AI is optional and must not be required for core operation.

---

# 53. MOST IMPORTANT MVP WORKFLOW

Before adding advanced features, make this workflow excellent:

TESTER

↓

Login

↓

Select DataFusion

↓

Select Testing Session

↓

Click "Start Critic Mode"

↓

Open target application

↓

Hover over element

↓

Click element

↓

Finding window appears

↓

Write:

"This filter is confusing."

↓

Select:

Usability

↓

Save

↓

Screenshot automatically captured

↓

Finding appears as marker

↓

Developer sees finding

↓

Developer fixes it

↓

Status = Ready for Retest

↓

Tester retests

↓

Tester verifies

↓

Finding = Closed

↓

Generate Report

This entire workflow should feel simple and reliable.

---

# 54. DEFINITION OF DONE

The MVP is considered complete when a non-technical tester can perform the following without developer assistance:

1. Log in.
2. Open a project.
3. Start a testing session.
4. Activate Critic Mode.
5. Open the target application.
6. Select an element.
7. Create a finding.
8. Add a comment.
9. Capture evidence.
10. Save the finding.
11. Find the issue later.
12. Assign it to a developer.
13. Developer comments.
14. Developer marks it fixed.
15. Tester retests.
16. Tester verifies it.
17. Manager views the dashboard.
18. Manager generates an executive report.
19. Developer generates a technical report.

If these 19 steps work smoothly, the platform has achieved its core purpose.

---

# 55. FINAL PRODUCT VISION

The finished product should feel like:

> **A digital clipboard for software testers.**

The tester should not think:

"I need to create a bug ticket."

Instead they should think:

> "I found something here."

Then:

**Click → Comment → Save.**

The platform handles:

* evidence
* location
* metadata
* issue ID
* workflow
* assignment
* tracking
* retesting
* reporting
* audit history

The result is a professional bridge between:

**USER → TESTER → DEVELOPER → MANAGER → EXECUTIVE**

Build the MVP first. Keep the interface extremely simple. Do not add unnecessary features before the core "click → comment → evidence → report" workflow is reliable.
