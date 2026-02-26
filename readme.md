.

💰 Finance Manager (CLI-Based Expense System)

A command-line Personal Finance Manager built in Python to simulate a structured backend-style CRUD system with persistent JSON storage.

This project focuses on strengthening core software engineering fundamentals before transitioning into AI and data systems.


📌 Project Purpose

Before building AI models, it is critical to understand:

1.Data structuring

2.State management

3.CRUD architecture

4.Persistent storage handling

5.Clean system design

This project was built to reinforce those foundations.

🚀 Features
🔹 Expense Management (CRUD)

Add Expense

Generates a UUID for each entry

Validates input

Automatically timestamps entries

Persists to JSON

Edit Expense

Update amount

Update description

Update category

Supports partial updates

Changes are saved immediately

Delete Expense by ID

O(1) lookup using dictionary storage

Safe deletion with validation

JSON updated instantly

Delete All Expenses

Clears stored records

Resets JSON file


🔹 Analytics & Queries --

View all expenses

Filter by category

Monthly spending summary

Show highest expense

Dynamic total calculation (computed, not stored)

🧱 Tech Stack

Python 3

uuid — unique identifiers

json — persistent storage

datetime — timestamps

os — file handling

No external dependencies.

🗃 Data Architecture

Expenses are stored as a dictionary using UUIDs as keys:

{
    "uuid1": {
        "amount": 50,
        "category": "Food",
        "description": "Lunch",
        "date": "02/26/2026"
    }
}
Why Dictionary-Based Storage?

O(1) lookup for edit/delete

Cleaner ID-based management

Closer to real backend/database design

🧠 Key Engineering Decisions

1️⃣ Dynamic Total Calculation

The total is computed dynamically:

sum(exp["amount"] for exp in self.expenses.values())

This prevents data inconsistency and ensures a single source of truth.

2️⃣ Centralized Persistence Logic

All file-writing operations are handled through a private method:

def _save(self):

This enforces DRY principles and keeps logic modular.

3️⃣ UUID-Based Identification

Each expense is assigned:

uuid.uuid4()

This ensures global uniqueness and mirrors production-grade systems.

▶️ Installation & Usage
Clone the Repository
git clone https://github.com/emmy-py/finance-manager.git
cd finance-manager
Run the Application
python finance_manager.py
📋 CLI Menu
1. Add Expense
2. Delete Expense by ID
3. Show All Expenses
4. Filter by Category
5. Monthly Summary
6. Show Highest Expense
7. Show Total
8. Exit
📈 What This Project Demonstrates

Clean object-oriented design

Dictionary vs list architectural tradeoffs

JSON lifecycle management

Safe state mutation

Backend-style CRUD implementation

Foundation building for AI/data engineering

🔜 Next Steps

Planned upgrades:

Convert JSON data into Pandas DataFrame

Add advanced analytics

Introduce logging system

Convert into REST API (FastAPI)

Add unit testing

📄 License

This project is for educational and portfolio purposes.