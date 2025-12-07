# IT Support Ticket Helper using AI Agents

A Django-based web application that uses multi-agent AI to intelligently categorize and prioritize IT support tickets in real-time.

## Project Overview

This project demonstrates a practical implementation of a **multi-agent AI system** integrated with a Django web framework, SQL database, and analytics dashboard. The system reads incoming IT support requests, applies NLP-based classification, and automatically categorizes tickets by type and urgency.

## Key Features

- **Multi-Agent AI System**: Python agents that classify tickets and assign priorities
- **Django Web Interface**: User-friendly form and real-time ticket list
- **SQLite Database**: Persistent storage for all tickets
- **Data Export**: CSV export for Power BI analytics
- **GitHub Integration**: Full version control and collaboration support

## Tech Stack

- **Backend**: Django 4.x, Python 3.11
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **AI/ML**: NLP, Rule-based Classification
- **Data Analysis**: Pandas, NumPy
- **Version Control**: Git, GitHub

## Installation & Setup

### Prerequisites
- Python 3.11+
- Git
- VS Code (optional)

### Quick Start

```bash
# Clone repository
git clone https://github.com/nagarajumittapelli9344/ticket-helper-ai.git
cd ticket_helper_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Access at: http://127.0.0.1:8000/

## How AI Agents Work

The multi-agent system in `tickets/utils.py` contains two main agents:

**Category Agent:**
- Detects "network" → Network category
- Detects "password/login" → Access category
- Detects "error/bug" → Application category
- Default → General category

**Priority Agent:**
- Detects "urgent" or "not working" → High priority
- Detects "slow" → Medium priority
- Default → Low priority

## Testing Results

All 4 critical-path tests PASSED:

✅ Network issue → Network + High
✅ Login problem → Access + High
✅ Application error → Application + Medium
✅ General request → General + Low

## Skills Demonstrated

- Full-stack Django development
- Multi-agent AI architecture
- Database design & SQL
- Data analytics & visualization
- Git/GitHub version control
- Professional software engineering

## Author

**Mittapelli Nagaraju**
- GitHub: [@nagarajumittapelli9344](https://github.com/nagarajumittapelli9344)
- LinkedIn: [Mittapelli Nagaraju](https://www.linkedin.com/in/mittapelli-nagaraju-4b8623264/)

## License

MIT License - Open source project

---

**Status**: ✅ Production Ready | **Last Updated**: December 7, 2025
