# Financial Analytics Dashboard

This project is a **personal finance control application** built with **Python, Flet, SQLite, and interactive charts**.

The application is inspired by a YouTube tutorial, but the goal of this project is to adapt the base structure to create a **personal financial management tool** focused on tracking **income, expenses, and investments**.

This repository is part of my **learning process while studying Python application development, databases, and data visualization**.

---

# Project Objective

Create a **financial dashboard application** that allows users to:

- Track money entering the system (income)
- Track money leaving the system (expenses)
- Organize transactions using categories
- Visualize financial data through charts and dashboards
- Analyze spending and financial distribution

---

# Technologies Used

- **Python**
- **Flet** (UI framework)
- **SQLite** (local database)
- **Charts / Data Visualization**

---

# Project Structure

```
.
├── src/                # Application source code
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
└── LICENSE
```

The structure may evolve as the project grows.

---

# Planned Features

## Income Management
- Add new income entries
- Categorize income sources
- Store income records in SQLite

## Expense Management
- Add new expenses
- Assign categories to expenses
- Track spending patterns

## Categories System
- Create custom categories
- Organize financial data by category

## Dashboard & Visualization
- Financial overview
- Charts for income vs expenses
- Category-based charts
- Trend visualization

## Future Improvements
- Investment tracking
- Monthly financial reports
- Budget limits per category
- Export financial data

---

# Setup (Initial)

Clone the repository

```bash
git clone https://github.com/GVelosa/financial-analytics-dashboard.git
```

Enter the project folder

```bash
cd your-repository
```

Install dependencies

```bash
uv sync
```

Run the application

```bash
python src/main.py
```

*(The entry point may change as the project evolves.)*

---

# Learning Purpose

This project is mainly intended for:

- Practicing Python project organization
- Learning how to build UIs with Flet
- Working with SQLite databases
- Implementing charts and dashboards
- Structuring real-world data applications
