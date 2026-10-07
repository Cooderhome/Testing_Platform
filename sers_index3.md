Create a professional, standalone interactive HTML application called:

"Data Fusion Platform – Interactive Architecture & Data Flow Simulator"

The purpose of this application is to demonstrate the architecture of a large-scale Data Fusion Platform to senior officials, architects, analysts, developers, and decision makers.

IMPORTANT:
This must NOT be a static architecture diagram.

It must be a fully interactive architecture visualization where the user can:
- View animated data flowing through the architecture
- Drag and reposition components
- Create new components
- Delete components
- Create connections between components
- Delete connections
- Change the direction of connections
- Change the type of data flowing between components
- Change the processing behavior
- Enable/disable components
- Add comments explaining architectural changes
- See the effect of changes immediately
- Compare the original architecture with the modified architecture
- Save/export the modified architecture
- Reset to the original architecture

Use ONLY:
- HTML5
- CSS3
- Vanilla JavaScript
- SVG for connections and animated data flow
- No React
- No Vue
- No Angular
- No npm
- No backend
- No external database
- Everything should run by opening index.html in a browser

==================================================
1. OVERALL DESIGN
==================================================

Create a modern professional command-center style interface suitable for presenting to higher officials.

Visual style:
- Dark professional navy background
- Blue/cyan data-flow accents
- Purple for analytics
- Green for successful/healthy processing
- Orange/red for warnings and failures
- Glassmorphism panels
- Clean enterprise dashboard
- Professional typography
- Subtle animations
- Avoid excessive gaming-style effects

The page should look like a real Data Fusion Platform architecture management console.

Main screen layout:

--------------------------------------------------
TOP HEADER
--------------------------------------------------

Title:
"DATA FUSION PLATFORM"

Subtitle:
"Interactive Architecture & Data Flow Simulator"

Top-right controls:

[▶ Start Flow]
[⏸ Pause]
[⟳ Reset]
[Simulation]
[Architecture]
[Review]
[Export]

Also display:

System Status: ● HEALTHY
Data Rate: 24,850 events/sec
Processing Load: 67%
Kafka Queue: 12,450 messages
Active Sources: 5
Active Services: 3

==================================================
2. MAIN ARCHITECTURE CANVAS
==================================================

The center of the page should contain a large interactive architecture canvas.

Use SVG for all connections.

Create these major architecture zones:

1. DATA SOURCES
2. INGESTION & PROCESSING
3. ELASTICSEARCH
4. KAFKA / STREAM BUFFER
5. INCREMENTAL READER
6. NEO4J GRAPH DATABASE
7. ANALYSIS SERVICES
8. VISUALIZATION / ANALYST WORKSPACE

--------------------------------------------------
DATA SOURCES
--------------------------------------------------

Create separate nodes:

CDR / Telecom
API Sources
Finance / Banking
OSINT
Flight / Travel
Other Intelligence Sources

Each source should display:

icon
name
status
event rate

Example:

CDR
● ACTIVE
8,500 events/sec

Finance
● ACTIVE
4,200 events/sec

OSINT
● ACTIVE
1,200 events/sec

The user must be able to add another source.

Example:

"+ Add Data Source"

==================================================
3. INGESTION & PROCESSING
==================================================

Create a large Logstash processing node.

Inside it show:

RAW DATA
↓
MAP
↓
FILTER
↓
CLEAN
↓
NORMALIZE
↓
PARSE
↓
ENRICH

Display:

"Logstash Processing Layer"

Show animated events entering Logstash.

The animation should visually demonstrate that raw events become structured data.

Example animation:

CDR event
→ Logstash
→ mapping
→ cleaning
→ parsing
→ Elasticsearch

When the user clicks Logstash, show a side panel:

Component:
Logstash

Role:
Data ingestion and transformation

Functions:
- Field mapping
- Filtering
- Parsing
- Data normalization
- Enrichment

Status:
Healthy

Events/sec:
24,000

==================================================
4. ELASTICSEARCH
==================================================

Create an Elasticsearch cluster visualization.

Show:

Elasticsearch Cluster

Node 1
Node 2
Node 3

Display:

Indexed Documents
Search Rate
Indexing Rate
Storage
Shard Count

Example:

Documents:
124,850,220

Indexing:
18,400/sec

Search:
5,200/sec

Make this component visually represent the main searchable data store.

Connections:

Logstash → Elasticsearch

Elasticsearch → Domain Analysis

Elasticsearch → Incremental Reader

Elasticsearch ↔ Neo4j

==================================================
5. KAFKA BACKPRESSURE SYSTEM
==================================================

Create a visually important Kafka section.

Display:

KAFKA MESSAGE BROKER

Topics:

cdr-events
finance-events
flight-events
osint-events
fusion-events

Show messages moving through Kafka.

Example:

████████████████
12,450 messages waiting

Display:

Producer Rate
Consumer Rate
Consumer Lag
Queue Depth

The animation must show what happens when the analysis service becomes overloaded.

Example:

Normal:

Elasticsearch
      ↓
Analysis Service

High Load:

Elasticsearch
      ↓
Incremental Reader
      ↓
Kafka
      ↓
Analysis Service

When service load exceeds a configurable threshold, animate events being redirected into Kafka.

==================================================
6. INCREMENTAL READER
==================================================

Create a component:

"Incremental Reader"

Display:

Last processed timestamp
Last processed document ID
Batch size
Current offset
Processing rate
Pending records

Example:

Batch Size: 1,000
Offset: 845,920
Processing: 950/sec

The user must be able to change:

Batch Size:
[1000]

Threshold:
[70%]

Polling Interval:
[2 sec]

When the user changes these values, update the animation and statistics.

==================================================
7. NEO4J GRAPH DATABASE
==================================================

Create a large interactive Neo4j component.

Title:

"Neo4j Intelligence Graph"

Display a small animated graph:

Person A
   |
calls
   |
Phone B
   |
owns
   |
Account C
   |
transaction
   |
Account D
   |
flight
   |
Person E

The graph must be interactive.

Users should be able to:

+ Create Node

+ Create Relationship

+ Edit Node

+ Edit Attributes

+ Delete Node

+ Delete Relationship

Example node types:

Person
Phone
Account
Company
Vehicle
Location
Flight
Transaction
Organization
Device

Example relationship types:

CALLS
OWNS
TRANSFERRED_TO
TRAVELED_ON
LOCATED_AT
WORKS_FOR
CONNECTED_TO
RELATED_TO

Allow users to add attributes:

Name
ID
Phone Number
Account Number
Location
Timestamp
Risk Score
Source
Confidence

==================================================
8. CRITICAL NEO4J → ELASTICSEARCH REFERENCE FLOW
==================================================

This is extremely important.

When a user creates or modifies a graph entity, visually show:

USER GRAPH CHANGE

        ↓

NEO4J

        ↓

GRAPH CHANGE EVENT

        ↓

REFERENCE / ENRICHMENT PIPELINE

        ↓

ELASTICSEARCH REFERENCE INDEX

Create a dedicated Elasticsearch index:

"graph_reference_index"

Show this clearly.

For example:

User creates:

Person A
   |
OWNS
   |
Account 123

The system should animate:

Neo4j
↓
Graph Change Event
↓
Reference Processor
↓
Elasticsearch
↓
graph_reference_index

Display:

"Graph reference successfully synchronized"

The user should understand that Neo4j is the analyst-controlled relationship layer while Elasticsearch is the searchable reference/enrichment layer.

==================================================
9. ANALYSIS SERVICES
==================================================

Create three major services:

DOMAIN ANALYSIS

FUSION ANALYSIS

CROSS-DOMAIN ANALYSIS

--------------------------------------------------

DOMAIN ANALYSIS

Examples:

CDR Analysis
Financial Analysis
Flight Analysis
OSINT Analysis

Display:

Events processed
Patterns detected
Alerts generated

--------------------------------------------------

FUSION ANALYSIS

Combine:

CDR
+
Finance
+
Flight
+
OSINT
+
Neo4j

Example animation:

Phone Number
↓
Person
↓
Bank Account
↓
Transaction
↓
Flight
↓
Location

Display:

"Entity relationship discovered"

--------------------------------------------------

CROSS-DOMAIN ANALYSIS

Show:

CDR + Finance
CDR + Flight
Finance + Flight
OSINT + Finance
CDR + OSINT
All Domains

Display:

Correlation count
Patterns
Risk score
Confidence

==================================================
10. USER-CONTROLLED CONNECTIONS
==================================================

This is one of the most important features.

Allow the user to enter "Architecture Edit Mode".

In this mode:

- Click a node
- Click another node
- Create connection

Show a modal:

"Create Connection"

Fields:

Source:
[Elasticsearch]

Destination:
[Cross-Domain Analysis]

Data Type:
[Reference Data]

Flow Type:
[Real-Time / Batch / Event / Reference]

Frequency:
[Continuous]

Priority:
[High]

Description:
[textarea]

Then:

[Create Connection]

The new connection should immediately appear on the canvas.

Animate data moving along the new connection.

==================================================
11. CONNECTION EDITING
==================================================

When the user clicks an existing connection, show:

Connection Details

Source:
Elasticsearch

Destination:
Domain Analysis

Data:
CDR Events

Flow:
Real-Time

Rate:
8,500/sec

Status:
Active

Controls:

[Edit]
[Disable]
[Reverse Direction]
[Delete]

If the connection is deleted, show an explanation dialog:

"Why are you removing this connection?"

Text area:

"Enter reason..."

Example:

"Removed direct Elasticsearch → Cross-Domain Analysis flow because high query volume was affecting Elasticsearch performance. Data will now pass through Kafka."

Require the user to enter a reason before saving.

==================================================
12. ARCHITECTURE CHANGE MANAGEMENT
==================================================

Every modification must be recorded.

Create a right-side panel:

"Architecture Change Log"

Example:

CHANGE #001

User:
Architecture Team

Time:
10:42:18

Change:
Added Kafka between Elasticsearch and Fusion Analysis

Reason:
"Prevent analysis services from being overloaded during high-volume ingestion."

Impact:
Reduced service overload risk

Status:
Applied

--------------------------------------------------

CHANGE #002

Change:
Added Neo4j → Elasticsearch reference synchronization

Reason:
"Allow analyst-created graph relationships to become searchable enrichment data."

Impact:
Improved cross-domain correlation

==================================================
13. COMMENT ON ARCHITECTURE
==================================================

Allow comments on:

- Nodes
- Connections
- Zones
- Data flows
- Architecture changes

When clicking:

"Add Comment"

Show:

Author:
[Current User]

Comment:

[textarea]

Category:

[Performance]
[Security]
[Data Quality]
[Scalability]
[Architecture]
[Operational]
[Other]

Priority:

[Low]
[Medium]
[High]
[Critical]

Example:

"Kafka should be placed between Elasticsearch and Cross-Domain Analysis because analysis queries can become expensive during ingestion spikes."

Display comments as small markers attached to the relevant architecture component.

==================================================
14. SIMULATION MODE
==================================================

Create a powerful simulation mode.

Controls:

Data Volume:
[Low] [Normal] [High] [Extreme]

System Load:
[20%] [40%] [60%] [80%] [100%]

Enable Failure Simulation:

☐ Elasticsearch overloaded
☐ Kafka consumer slow
☐ Analysis service unavailable
☐ Neo4j unavailable
☐ Logstash ingestion spike
☐ Network delay

When a failure is selected, visually animate the architecture response.

Example:

Analysis Service becomes overloaded.

Then:

Elasticsearch
      ↓
Incremental Reader
      ↓
Kafka
      ↓
Queue increases
      ↓
Analysis Service

Show:

"BACKPRESSURE ACTIVE"

Kafka Queue:

12,450
→
28,300
→
45,200

When the analysis service recovers:

45,200
→
30,000
→
12,000
→
0

Display:

"QUEUE DRAINING"

==================================================
15. DATA FLOW ANIMATION
==================================================

Data must be visually represented as moving particles.

Different colors/types:

CDR event
Finance event
Flight event
OSINT event
Graph reference event
Alert

Each event should move along SVG connection lines.

The speed should correspond to the configured data rate.

Example:

CDR:
Fast stream

Finance:
Medium stream

OSINT:
Slow stream

Graph reference:
Occasional stream

When a connection is disabled, stop particles on that connection.

When a connection is overloaded, change its visual state to warning.

==================================================
16. ALERT GENERATION
==================================================

Create an alert area.

Example:

⚠ CROSS-DOMAIN PATTERN DETECTED

Entity:
Person A

Relationships:

Phone
↓
Bank Account
↓
Transaction
↓
Flight

Risk Score:
87%

Confidence:
92%

Sources:
CDR
Finance
Flight
Neo4j

Buttons:

[Investigate]
[Open Graph]
[View Timeline]
[View Source Data]

==================================================
17. ARCHITECTURE COMPARISON MODE
==================================================

Add:

"Compare Architecture"

The user should be able to compare:

ORIGINAL

versus

MODIFIED

Show:

Added Components
Removed Components
Added Connections
Removed Connections
Changed Parameters
Changed Data Flow

Example:

Added:
Kafka

Added:
Neo4j → Elasticsearch Reference Flow

Removed:
Direct Elasticsearch → Cross-Domain Analysis

Changed:
Kafka Batch Size
500 → 2,000

==================================================
18. BEFORE / AFTER VISUALIZATION
==================================================

Create a split-screen comparison.

LEFT:

CURRENT / ORIGINAL ARCHITECTURE

RIGHT:

PROPOSED ARCHITECTURE

Animate differences.

Added components:
green highlight

Removed components:
red highlight

Changed connections:
orange highlight

Unchanged:
gray/blue

At the bottom show:

Estimated Impact

Scalability:
+35%

Failure Resilience:
+42%

Search Load:
-18%

Processing Latency:
+5%

IMPORTANT:
These percentages must NOT be hardcoded as factual claims.
Clearly label them as:

"Simulation Estimate"

and calculate them from the simulated parameters where possible.

==================================================
19. ARCHITECTURE REVIEW PANEL
==================================================

Create a professional review panel for higher officials.

Title:

"Architecture Review"

Sections:

Strengths

Risks

Recommended Changes

Decision

Example:

STRENGTHS

✓ Multi-source ingestion
✓ Centralized search
✓ Graph-based relationship analysis
✓ Backpressure handling
✓ Cross-domain analytics

RISKS

⚠ Elasticsearch overload
⚠ Kafka consumer lag
⚠ Neo4j/Elasticsearch synchronization
⚠ Unauthorized graph manipulation
⚠ Data quality inconsistency
⚠ Cross-domain query complexity

RECOMMENDATIONS

✓ Use Kafka for backpressure
✓ Implement schema/version control
✓ Implement graph change events
✓ Add RBAC
✓ Add audit logging
✓ Monitor consumer lag
✓ Validate graph modifications
✓ Implement Elasticsearch index lifecycle management

==================================================
20. USER ROLES
==================================================

Create a simple role selector:

Viewer
Analyst
Architect
Administrator

Viewer:
- View architecture
- Run simulation
- View comments

Analyst:
- Add graph nodes
- Add relationships
- Add comments
- Run simulations

Architect:
- Modify architecture
- Add/remove connections
- Change flow behavior
- Add comments

Administrator:
- Everything

This is a front-end simulation only.
Clearly indicate:

"Demo Authorization Layer"

==================================================
21. SAVE / LOAD ARCHITECTURE
==================================================

Implement localStorage.

Buttons:

[Save Architecture]

[Load Architecture]

[Export JSON]

[Import JSON]

[Export Report]

The exported JSON should contain:

nodes
connections
node attributes
connection attributes
comments
change history
simulation settings
architecture version

Example:

{
  "version": "2.1",
  "nodes": [],
  "connections": [],
  "comments": [],
  "changes": []
}

==================================================
22. ARCHITECTURE VERSIONING
==================================================

Show:

Architecture Version:

v1.0 Original

v1.1 Kafka Added

v1.2 Neo4j Integration

v1.3 Cross-Domain Optimization

Allow:

[Create Version]

When creating a version ask:

Version Name:
Description:
Reason for Change:

Store the snapshot in localStorage.

Allow the user to switch between versions.

==================================================
23. DATA FLOW LEGEND
==================================================

Create a legend:

━━━ Real-time Data

- - - Batch Data

━━━ Reference Data

━━━ Graph Relationship

━━━ Alert

Green:
Healthy

Orange:
Warning

Red:
Failure

Blue:
Normal Data

Purple:
Analytics

==================================================
24. PRESENTATION MODE
==================================================

Add a "Presentation Mode".

When activated:

- Hide editing controls
- Hide technical configuration panels
- Expand architecture canvas
- Increase font sizes
- Show only important metrics
- Automatically animate data flow

Create a guided sequence:

STEP 1
"Data enters from multiple domains."

STEP 2
"Logstash cleans, maps and normalizes the data."

STEP 3
"Elasticsearch stores and indexes the data."

STEP 4
"When analysis demand increases, Kafka provides controlled buffering."

STEP 5
"Neo4j represents complex relationships."

STEP 6
"Analysts can create and modify intelligence relationships."

STEP 7
"Graph changes are synchronized back as searchable reference data."

STEP 8
"Domain and cross-domain services discover patterns."

STEP 9
"Alerts and intelligence are presented to analysts."

Add:

[Previous]
[Next]
[Auto Play]

==================================================
25. EXECUTIVE VIEW
==================================================

Create a simplified "Executive View".

Do not show technical details.

Instead show:

DATA SOURCES
      ↓
DATA PROCESSING
      ↓
UNIFIED DATA
      ↓
RELATIONSHIP INTELLIGENCE
      ↓
ANALYTICS
      ↓
PATTERN DETECTION
      ↓
ALERTS & DECISIONS

Show only:

Data Sources
Data Processed
Relationships Discovered
Patterns Detected
Alerts Generated
System Health

Include a simple statement:

"Integrated Data → Connected Relationships → Cross-Domain Intelligence → Actionable Decisions"

==================================================
26. TOOLBAR
==================================================

Create a floating toolbar:

Select
Move
Connect
Add Node
Add Comment
Delete
Simulate
Inspect
Compare

When "Connect" is selected:

Click source → click destination → connection dialog opens.

When "Add Node" is selected:

Click canvas → node creation dialog.

==================================================
27. NODE CREATION DIALOG
==================================================

Fields:

Node Name
Node Type
Description
Status
Data Rate
Processing Capacity

Node Type options:

Data Source
Processor
Database
Message Broker
Analytics Service
Graph Database
Visualization
External System

Buttons:

[Create]
[Cancel]

==================================================
28. PROFESSIONAL INTERACTION
==================================================

Add:

- Smooth drag animations
- Zoom
- Pan
- Fit to screen
- Minimap
- Hover tooltips
- Context menus
- Search architecture components
- Highlight connected components
- Highlight data path
- Show upstream/downstream dependencies

When clicking a node:

Highlight every component receiving data from it.

When clicking a connection:

Highlight the entire data path.

Example:

CDR
→ Logstash
→ Elasticsearch
→ Incremental Reader
→ Kafka
→ Domain Analysis
→ Fusion Analysis
→ Alert

==================================================
29. DATA FLOW TRACE
==================================================

Add a feature:

"Trace Data"

The user selects:

Source:
CDR

Destination:
Cross-Domain Analysis

The system calculates and highlights:

CDR
↓
Logstash
↓
Elasticsearch
↓
Incremental Reader
↓
Kafka
↓
Fusion Analysis
↓
Cross-Domain Analysis

Display:

Path Length
Components
Estimated Latency
Data Rate
Potential Bottlenecks

==================================================
30. CRITICAL ARCHITECTURE PRINCIPLE
==================================================

The visualization must clearly communicate these architectural concepts:

1. Elasticsearch is the high-volume searchable data platform.

2. Kafka provides decoupling and backpressure.

3. Incremental Reader prevents analysis services from being overwhelmed.

4. Neo4j represents relationships and analyst-created intelligence.

5. Analysts can manually create:
   - Nodes
   - Relationships
   - Attributes

6. Neo4j changes generate controlled graph-change/reference events.

7. Those reference changes can be indexed into a dedicated Elasticsearch
   reference index.

8. Domain Analysis handles individual domains.

9. Fusion Analysis combines related entities and evidence.

10. Cross-Domain Analysis identifies relationships and patterns across:
    CDR + Finance + Flight + OSINT + Graph intelligence.

11. The architecture must support failure isolation.

12. Every important architecture modification must have a reason/comment.

==================================================
31. IMPORTANT SAFETY / GOVERNANCE DESIGN
==================================================

Because analysts can manipulate graph data, show these controls:

Audit Log
Who changed it?
What changed?
When?
Why?

Before/after values.

Example:

USER:
Analyst 004

ACTION:
Created Relationship

FROM:
Person A

TO:
Account B

RELATIONSHIP:
OWNS

REASON:
"Confirmed through financial investigation."

TIME:
10:42:32

Do NOT permanently delete important graph data.

Instead support:

Soft Delete

Archived

Restored

Version History

==================================================
32. RESPONSIVE DESIGN
==================================================

Desktop:
Full architecture canvas

Tablet:
Collapsible side panels

Mobile:
Simplified executive view

The architecture canvas should remain usable with mouse and touch.

==================================================
33. VISUAL QUALITY
==================================================

The final application should look like a professional intelligence/data-fusion command center.

Do NOT make it look like:

- A basic school project
- A simple flowchart
- A static PowerPoint diagram
- A generic CRUD dashboard

It should feel like a real enterprise architecture simulation platform.

Use:

- SVG
- CSS animations
- glowing data particles
- smooth transitions
- status indicators
- professional cards
- clear typography
- subtle shadows
- grid background
- animated connection lines

==================================================
34. DEMO SCENARIO
==================================================

On first load, automatically populate this scenario:

CDR
Finance
Flight
OSINT

→ Logstash

→ Elasticsearch

→ Incremental Reader

→ Kafka

→ Domain Analysis

→ Fusion Analysis

→ Cross-Domain Analysis

And:

Elasticsearch
↕
Neo4j

Neo4j:
Person
Phone
Account
Transaction
Flight

Then demonstrate:

1. CDR data enters the system.
2. Logstash processes it.
3. Elasticsearch indexes it.
4. Analysis services consume data.
5. Analysis load increases.
6. Incremental Reader detects high load.
7. Kafka begins buffering.
8. Analysis services process batches.
9. Neo4j contains relationships.
10. Analyst creates a new relationship.
11. Neo4j generates a graph change event.
12. Reference data is indexed into Elasticsearch.
13. Cross-domain analysis discovers a new relationship.
14. An alert is generated.
15. Analyst investigates the alert.

==================================================
35. FINAL PRESENTATION GOAL
==================================================

The final HTML should allow a senior official to understand the entire platform without reading technical documentation.

The visual story should be:

"Many data sources"

        ↓

"One controlled ingestion pipeline"

        ↓

"Clean and unified data"

        ↓

"Scalable storage and search"

        ↓

"Controlled high-volume processing"

        ↓

"Relationship intelligence"

        ↓

"Domain + Fusion + Cross-Domain analysis"

        ↓

"Pattern detection"

        ↓

"Alerts"

        ↓

"Analyst investigation"

        ↓

"Decision support"

At the end of Presentation Mode display:

"FROM RAW DATA TO ACTIONABLE INTELLIGENCE"

and:

"Integrated Data → Connected Relationships → Cross-Domain Intelligence → Better Decisions"

==================================================
TECHNICAL REQUIREMENTS
==================================================

Return a COMPLETE working index.html.

Everything must be contained in one HTML file.

Use inline:

<style>
...
</style>

and:

<script>
...
</script>

Do not require a server.

Do not use npm.

Do not use build tools.

Do not use React.

Do not use external JavaScript frameworks.

Use SVG for the architecture graph and animated data-flow connections.

Use localStorage for persistence.

Make the code well structured and commented.

Separate the JavaScript into logical sections:

- State Management
- Node Management
- Connection Management
- SVG Rendering
- Data Flow Animation
- Simulation Engine
- Comment System
- Change History
- Version Management
- Local Storage
- Export / Import
- Presentation Mode
- Executive Mode

Make all important values configurable at the top of the JavaScript.

The final result must be immediately usable by opening:

index.html

in Chrome or Edge.