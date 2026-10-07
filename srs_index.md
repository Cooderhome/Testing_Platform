Create a **single-page interactive HTML educational application** that visually explains common bank transaction-monitoring patterns to a complete beginner—even a child who has never studied banking, finance, AML, or data analysis.

## Main Goal

Build an animated visual learning experience called:

# "Follow the Money 💰"

The user should learn the following 18 concepts by watching simple animated money movements rather than reading technical explanations:

1. Transaction Velocity
2. Rapid Pass-Through
3. Structuring Pattern
4. Dormant Account Reactivation
5. New Beneficiary
6. Beneficiary Concentration
7. Recurring Transfer
8. Transaction Burst
9. Rounded-Value Pattern
10. Balance Turnover
11. Merchant Concentration
12. Unusual-Hour Transactions
13. Account Relationship Strength
14. Cash-In / Cash-Out Pattern
15. Corporate / Account Profile Mismatch
16. Multi-Tier Corporate Smurfing
17. Behavioral Velocity Baseline
18. Manager-Corporate Flow Discrepancy

IMPORTANT:
These are transaction-monitoring patterns, NOT automatic proof of illegal activity.

The application must repeatedly communicate visually that:

"🚨 A pattern is a reason to LOOK CLOSER, not proof that something is wrong."

Use simple language such as:

"Something changed."
"Money moved unusually fast."
"This account suddenly became busy."
"Most money went to one place."
"Let's investigate why."

Avoid complicated AML terminology unless the technical term is shown together with a simple explanation.

---

# TECHNOLOGY

Build everything in one self-contained HTML file.

Use:

* HTML5
* CSS3
* Vanilla JavaScript
* SVG for animated transaction diagrams
* CSS animations
* JavaScript animations
* No backend
* No database
* No build system
* No React
* No npm
* No external dependencies if possible

The final file should work by simply opening:

index.html

---

# VISUAL STYLE

Make it look like a modern educational animation/game.

Style:

* Clean
* Friendly
* Colorful
* Professional enough for a banking investigation platform
* Easy for children to understand
* Large cards
* Large icons
* Rounded corners
* Soft shadows
* Smooth animations
* Minimal text
* Clear visual hierarchy

Use familiar emoji/icons where useful:

🏦 Bank
👤 Person
🏢 Company
💰 Money
💳 Card
🏪 Merchant
👔 Manager
📦 Supplier
🚨 Alert
🔍 Investigation
⏰ Time
🔗 Relationship

Do not make it look like a scary crime dashboard.

---

# MAIN SCREEN

Create a top navigation/header:

"💰 FOLLOW THE MONEY"

Subtitle:

"Learn how transaction patterns are detected"

Under it display:

"18 Patterns • Animated Examples • Beginner Friendly"

Then create a large central animated visualization.

The screen should have:

LEFT SIDE:
A vertical list of the 18 patterns.

CENTER:
Large animated transaction scene.

RIGHT SIDE:
A simple explanation card.

BOTTOM:
Animation controls.

Controls:

▶ Play
⏸ Pause
🔄 Replay
← Previous
→ Next

Also include:

"Auto Play"

and:

"Simple / Technical"

toggle.

---

# PATTERN NAVIGATION

Display the 18 concepts as large clickable cards.

Example:

┌────────────────────────────┐
│ ⚡                         │
│ Transaction Velocity       │
│ "How fast is money moving?"│
└────────────────────────────┘

When the user clicks a card:

1. The current animation stops.
2. The screen smoothly transitions.
3. The new scenario loads.
4. The money movement animation begins.
5. A short explanation appears.
6. The "What are we noticing?" section updates.

Highlight the currently selected concept.

---

# IMPORTANT ANIMATION RULE

Every scenario should visually follow this structure:

STEP 1
Show the normal situation.

STEP 2
Animate money moving.

STEP 3
Show something unusual.

STEP 4
Pause the animation.

STEP 5
Show a simple explanation.

STEP 6
Show the investigator question.

For example:

"👀 What changed?"

"Why might an investigator look at this?"

Never immediately say:

"This is illegal."

Instead say:

"This pattern may deserve a closer look."

---

# SCENE 1 — TRANSACTION VELOCITY ⚡

Title:

"Transaction Velocity"

Simple explanation:

"How quickly are transactions happening?"

Animation:

Show:

👤 Customer

↓

🏦 Account

Normal mode:

One coin arrives every few seconds.

Then accelerate the animation.

💰
💰
💰
💰
💰
💰
💰

Display:

"Normal: 5 transactions/day"

Then:

"Now: 50 transactions in a short time!"

Show a speedometer-style animation:

SLOW → NORMAL → FAST → VERY FAST

Highlight the account with an animated pulse.

Bottom explanation:

"The account suddenly became much busier than usual."

Investigator question:

"👀 What caused the sudden increase?"

---

# SCENE 2 — RAPID PASS-THROUGH 🏃💨

Show:

🏢 Company A

↓

💰💰💰

🏦 Account X

↓

💰💰💰

🏢 Company B

Animate the money entering Account X.

Immediately after entering, animate it leaving.

Display a timer:

00:00
00:03
00:07

Then:

"Money arrived..."

"...and quickly left."

Show:

"Money stayed for only 7 minutes."

Simple explanation:

"An account receives money and quickly sends most of it somewhere else."

Investigator question:

"Why did the money move through the account so quickly?"

---

# SCENE 3 — STRUCTURING PATTERN 🧩

Show a large amount:

💰 ETB 500,000

Then show the alternative:

💰 95,000
+
💰 90,000
+
💰 98,000
+
💰 92,000
+
💰 97,000

Animate the large amount visually breaking into smaller pieces.

Display:

"One large amount"

→

"Many smaller transactions"

Simple explanation:

"Instead of moving one large amount, money appears in several smaller transactions."

Investigator question:

"Why was the money divided?"

IMPORTANT:
Do not imply that every smaller transaction is suspicious.

---

# SCENE 4 — DORMANT ACCOUNT REACTIVATION 😴➡️⚡

Create an account sleeping.

🏦
😴
"Little activity"

Animate a calendar:

Month 1
Month 2
Month 3
Month 4
Month 5
Month 6

Very little activity.

Then suddenly:

⚡ WAKE UP!

💰💰💰
💰💰💰
💰💰💰

Display:

"6 months quiet"

Then:

"Suddenly: heavy activity"

Simple explanation:

"An account that was mostly quiet suddenly becomes very active."

---

# SCENE 5 — NEW BENEFICIARY 🆕

Show:

👤 Customer

Existing connections:

👤 Wife
🏢 Supplier A
🏢 Supplier B

Then introduce:

❓ New Account

Animate:

👤 Customer → ❓ New Account

Show:

"First time sending money here"

Then:

"Large transaction"

Simple explanation:

"A beneficiary is a person or account receiving money."

Investigator question:

"Who is this new recipient and why was the payment made?"

---

# SCENE 6 — BENEFICIARY CONCENTRATION 🎯

Show one customer connected to five recipients.

👤

├── 👤 A
├── 🏢 B
├── 🏢 C
├── 🏢 D
└── 🏢 E

Animate small payments to B, C, D, E.

Then send many large payments to A.

Make A visually larger.

Display:

"85% of outgoing money → Account A"

Simple explanation:

"Most of the money is going to one recipient."

Investigator question:

"Why does this recipient receive so much?"

---

# SCENE 7 — RECURRING TRANSFER 🔄

Create a calendar.

Monday
Tuesday
Wednesday
Thursday
Friday

Animate:

Friday → 💰 → Account B

Next Friday → 💰 → Account B

Next Friday → 💰 → Account B

Next Friday → 💰 → Account B

Show a repeating arrow.

Display:

"Same day"
"Same recipient"
"Similar amount"

Simple explanation:

"The same type of transfer keeps happening in a recognizable pattern."

---

# SCENE 8 — TRANSACTION BURST 💥

Show normal:

💰
pause
💰
pause
💰

Then suddenly:

💰💰💰💰💰💰💰💰💰💰💰

Use a burst animation.

Display:

"10 transactions in 2 minutes"

Simple explanation:

"Many transactions happened in a very short time."

---

# SCENE 9 — ROUNDED-VALUE PATTERN 🔢

Show:

ETB 100,000
ETB 250,000
ETB 500,000
ETB 1,000,000

Make the zeroes visually large.

Compare with:

ETB 103,472
ETB 247,830
ETB 498,215

Explain:

"Many transactions use perfectly round amounts."

Add:

"Round amounts can be completely normal. Context matters."

---

# SCENE 10 — BALANCE TURNOVER 🔄💰

Show:

🏦 Account

Starting balance:

ETB 50,000

Then animate:

* ETB 5,000,000

Then:

* ETB 4,900,000

Then:

* ETB 3,000,000

Then:

* ETB 2,950,000

The balance stays relatively small while huge amounts pass through.

Visual metaphor:

Use a water pipe.

Money enters:

💰💰💰💰💰💰

passes through:

🏦

and leaves:

💰💰💰💰💰💰

Simple explanation:

"A lot of money moves through the account compared with the amount normally kept there."

---

# SCENE 11 — MERCHANT CONCENTRATION 🏪

Show:

👤 Customer

Connected to:

🏪 Shop A
⛽ Fuel Station
🍔 Restaurant
✈️ Airline

Send most spending toward one merchant.

Display:

"Shop A = 90% of spending"

Simple explanation:

"Most of the customer's spending happens at one merchant."

---

# SCENE 12 — UNUSUAL-HOUR TRANSACTIONS 🌙

Create a large clock.

Normal:

09:00
12:00
15:00
17:00

Then nighttime:

02:13 AM

Animate:

🌙
🏦
💰

Display:

"02:13 AM"

Then:

"Is this normal for this customer?"

Simple explanation:

"The transaction happened at a time that is unusual compared with the customer's normal behavior."

IMPORTANT:
Do not say nighttime transactions are automatically suspicious.

---

# SCENE 13 — ACCOUNT RELATIONSHIP STRENGTH 🔗

Show:

Account A → Account B

Animate many historical transactions.

Display:

"245 transactions"
"18 months"

Make the connection line thick.

Then show:

Account A → Account C

Only one transaction.

Make that line thin.

Display:

"1 transaction"

Visual explanation:

THICK LINE = strong historical relationship

THIN LINE = weak/new relationship

---

# SCENE 14 — CASH-IN / CASH-OUT 💵

Show:

🏧 ATM

Cash enters:

💵💵💵

into:

🏦 Account

Then cash leaves:

💵💵💵

Use a loop animation:

CASH IN
↓
ACCOUNT
↓
CASH OUT
↓
ACCOUNT
↓
CASH OUT

Simple explanation:

"Cash repeatedly enters and leaves the account."

---

# SCENE 15 — CORPORATE / ACCOUNT PROFILE MISMATCH 🏢❓

Show customer profile:

🏪 Small Grocery Store

Expected:

"Small local payments"

Then show actual activity:

🏢 Company
↓
ETB 8,000,000
↓
🏦 Account
↓
ETB 7,900,000
↓
Another company

Display:

"Expected behavior ≠ Observed behavior"

Simple explanation:

"The account activity looks very different from the customer's declared business profile."

Investigator question:

"What explains the difference?"

---

# SCENE 16 — MULTI-TIER CORPORATE SMURFING 🏢➡️🏢➡️🏢

Create a network:

🏢 Company A
↓
🏢 Company B
↓
🏢 Company C
↓
🏢 Company D
↓
👤 Person

Animate money moving through each layer.

Then zoom out.

Show the complete chain.

Simple explanation:

"Money moves through several connected companies before reaching another destination."

IMPORTANT:
Explain that the pattern itself does not prove wrongdoing.

Add:

"Sometimes complex company networks are completely legitimate."

---

# SCENE 17 — BEHAVIORAL VELOCITY BASELINE 📊

This is very important.

Show a customer's normal behavior as a simple graph.

NORMAL:

10
12
14
11
13
15

Then suddenly:

80

Animate the line rising sharply.

Display:

"Normal: ~13 transactions/day"

"Today: 80"

Simple explanation:

"We compare the customer with their own normal behavior."

Show:

PAST BEHAVIOR
↓

CUSTOMER'S BASELINE

↓

TODAY

↓

BIG CHANGE

---

# SCENE 18 — MANAGER-CORPORATE FLOW DISCREPANCY 👔🏢

Make this scenario especially clear because it is more complicated.

Show:

🏢 ABC Construction Ltd.

Manager:

👔 Manager

Normal company flow:

🏢 Company

├── 👷 Employees
├── 📦 Suppliers
├── ⚡ Utilities
└── 🏛️ Government

Then show:

🏢 Company
↓
💰 ETB 4,000,000
↓
👔 Manager's personal account
↓
💰 ETB 3,800,000
↓
🏢 Another company

Pause.

Highlight the unusual path.

Explain:

"We noticed a large flow between the company and the manager's personal account."

Then explicitly say:

"This does NOT automatically mean something is wrong."

Possible legitimate explanations:

✓ Salary
✓ Dividend
✓ Reimbursement
✓ Loan
✓ Authorized business expense

Then:

"An investigator checks the documents and business reason."

This section should teach the user to investigate rather than automatically accuse someone.

---

# INVESTIGATOR MODE

Add a button:

🔍 "Show Me How an Investigator Thinks"

When clicked, transform the interface.

For each scenario show three questions:

### 1. WHAT HAPPENED?

Example:

"ETB 4M moved from a company to a manager."

### 2. WHAT CHANGED?

"That amount is much larger than normal manager payments."

### 3. WHAT SHOULD WE CHECK?

"Salary records, dividend records, invoices, contracts, and company authorization."

Never automatically conclude:

"Illegal."

Use:

"Needs context."

---

# TIMELINE VIEW

Add a button:

"🕒 Show Timeline"

When clicked, show animated chronological events.

Example:

09:00
💰 ETB 2M received

09:05
💰 ETB 1.9M sent

09:10
🆕 New beneficiary

09:12
💰 ETB 500K sent

09:15
💥 Transaction burst

Animate each event from left to right.

Allow the user to drag a timeline slider.

---

# NETWORK VIEW

Add another mode:

"🕸️ Show Money Network"

Display animated nodes:

👤 Person
🏦 Account
🏢 Company
🏪 Merchant

Connect them with animated lines.

When money moves:

💰 should travel along the line.

When the user clicks a node:

Show:

Name
Type
Transactions
Total In
Total Out
Relationship strength
First transaction
Last transaction

---

# SIMPLE EXPLANATION PANEL

Every pattern should have:

### What is it?

One-sentence explanation.

### Example

A realistic but fictional transaction scenario.

### What changed?

Highlight the unusual behavior.

### Why look closer?

Explain what an investigator might want to understand.

### Remember

"An unusual pattern is a signal to investigate, not proof of wrongdoing."

---

# ANIMATION LEGEND

Add a small legend:

🟢 Normal activity

🟡 Something changed

🔵 Money movement

🟣 Relationship

🔴 Investigation signal

⚪ Background information

Do not use red to imply "criminal."

Use it only to mean:

"Needs attention."

---

# INTERACTIVE QUIZ

At the end add:

## 🧠 Can You Spot the Pattern?

Show a simple animated scenario.

Example:

```text
Monday
Account receives ETB 500K

5 minutes later
Account sends ETB 490K

Tuesday
Account receives ETB 700K

3 minutes later
Account sends ETB 690K
```

Ask:

"What pattern do you notice?"

Options:

A. Rapid pass-through
B. Merchant concentration
C. Dormant account
D. Recurring transfer

After clicking:

Show the correct concept with an explanation.

Create 5–10 randomized questions.

Track:

Score: 7 / 10

But do NOT make the score mean that someone is a good/bad investigator.

---

# STORY MODE

Add a major button:

🎬 "START THE STORY"

This should guide the user through a fictional account called:

"Account X"

Story:

### Chapter 1

Account X is quiet.

### Chapter 2

It suddenly receives money.

### Chapter 3

Money moves quickly.

### Chapter 4

New beneficiaries appear.

### Chapter 5

Several companies become connected.

### Chapter 6

The investigator opens the network.

### Chapter 7

The investigator checks the customer's normal behavior.

### Chapter 8

The investigator asks for supporting documents.

At the end:

"🎯 Investigation complete"

Then display:

"What did we actually learn?"

Use:

"Patterns were detected."

"Patterns require context."

"An investigator reviews the evidence before reaching conclusions."

---

# UI LAYOUT

Desktop:

```text
┌───────────────────────────────────────────────────────────────┐
│ 💰 FOLLOW THE MONEY                         🌓 ⚙️             │
├──────────────┬──────────────────────────────┬───────────────┤
│              │                              │               │
│ PATTERNS     │       ANIMATION              │ EXPLANATION   │
│              │                              │               │
│ ⚡ Velocity  │     🏦                       │ What is it?    │
│ 🏃 Pass      │      ↓                       │               │
│ 🧩 Struct    │     💰                       │ Example       │
│ 😴 Dormant   │      ↓                       │               │
│ 🆕 Benefic   │     🏢                       │ What changed? │
│ ...          │                              │               │
│              │                              │ 🔍 Investigate│
├──────────────┴──────────────────────────────┴───────────────┤
│ ← Previous     ▶ Play     ⏸ Pause     🔄 Replay    Next →  │
└───────────────────────────────────────────────────────────────┘
```

On mobile:

Stack vertically:

1. Pattern selector
2. Animation
3. Explanation
4. Investigator questions
5. Controls

---

# EXTRA VISUAL FEATURES

Add:

* Smooth money particle animations
* Moving coins
* Animated arrows
* Pulsing accounts
* Animated clocks
* Calendar animations
* Progress bars
* Timeline animations
* Network graph
* Zoom in/out
* Tooltips
* Hover effects
* Click interactions
* Keyboard navigation
* Dark/light mode
* Responsive design

Use CSS and SVG rather than static images wherever possible.

---

# DATA STRUCTURE

Store the scenarios in JavaScript as objects so that adding/editing patterns later is easy.

Example structure:

```javascript
const patterns = [
    {
        id: "velocity",
        title: "Transaction Velocity",
        icon: "⚡",
        question: "How quickly is money moving?",
        explanation: "...",
        investigatorQuestion: "...",
        steps: [...]
    }
];
```

Make the rendering engine generic so that I can add new patterns without rewriting the entire application.

---

# IMPORTANT DESIGN PRINCIPLE

The application should teach:

OBSERVE → COMPARE → ASK → INVESTIGATE

Not:

OBSERVE → ACCUSE

The user should leave understanding:

"Bank transaction monitoring is about finding unusual patterns and understanding the story behind the money."

---

# FINAL SECTION

At the bottom display:

## 🔍 The Investigator's Rule

Large text:

"An unusual transaction is not automatically a bad transaction."

Then:

"Look at the customer."
"Look at the history."
"Look at the relationships."
"Look at the timing."
"Look at the money flow."
"Look for supporting evidence."

Final animation:

💰 → 🏦 → 👤 → 🏢 → 🔍

Then:

"Follow the money. Understand the story."

---

# TECHNICAL REQUIREMENTS

The generated application must:

* Be one standalone HTML file.
* Work offline.
* Have no console errors.
* Have no missing assets.
* Use responsive CSS.
* Use accessible buttons.
* Have keyboard navigation.
* Have smooth transitions.
* Avoid excessive text.
* Keep animations understandable.
* Include all 18 scenarios.
* Include Previous / Next navigation.
* Include Play / Pause / Replay.
* Include timeline mode.
* Include network mode.
* Include Story Mode.
* Include Investigator Mode.
* Include the interactive quiz.
* Include a progress indicator such as:

"Pattern 7 of 18"

* Include a "Reset Experience" button.
* Make every scenario visually distinct.
* Use fictional names and fictional transaction data.
* Clearly label all transaction data as illustrative.

Most importantly:

**The application must teach the concepts visually first and explain them with simple language second.**

A child should be able to watch the animation and say:

"Oh! The money came in and quickly went out."

before ever needing to understand the term:

"Rapid Pass-Through."

That is the core design goal.
