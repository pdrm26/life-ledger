# Life Ledger App 📖

## 📋 Project Overview

A comprehensive life management application built with Django to streamline personal and professional productivity across multiple domains.

## 🚀 Features

### Core Modules

#### 1. Todo Management

- Three-stage management system
  - `Backlog`
  - `In Progress`
  - `Done`
- 24-hour advance deadline alerts
- Automatic archiving of overdue tasks

#### 3. Finance Tracker

- Income and expense management
- Financial overview
- Spending category tracking
- Budget planning

## 🛠 Technical Stack

### Backend

- `Django`
- `PostgreSQL`
- `Celery` for background tasks

### Frontend

- `Next.js`

### Additional Technologies

- `Docker`
- `Celery`
- `Redis`

## 📂 Project Structure

```
life_ledger/
|
├── core/             # Common things in the apps
│   ├── models.py
│   ├── views.py
|   └── ...│
|
│
├── finance/           # Finance tracking module
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── todo/              # Todo management module
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── templates/         # HTML templates
│   ├── base.html
│   └── home.html
│
├── Makefile
├── manage.py
├── requirements.txt
└── config/            # Project configuration
    ├── settings.py
    └── celery.py
```

## 💻 Project Setup

### Prerequisites

- `Python 3.9+`
- `Django 4.2+`
- `PostgreSQL`
- `Node.js`

### Installation Steps

1. Clone the repository

```bash
git clone git@github.com:pdrm26/life-ledger.git
cd life-ledger
```

2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install Python dependencies

```bash
pip install -r requirements.txt
```

4. Database setup

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run development server

```bash
python manage.py runserver
```

## 🔐 Key Features Details

### Finance Module

- Track income sources
- Record expenses
- Categorize financial transactions
- Generate financial reports
- Budget alerts

### Todo Module

- Create multiple todo lists
- Set priorities
- Track completion status
- Deadline management

## 🔜 Upcoming Improvements

- [ ] Implement responsive frontend
- [ ] Add comprehensive test coverage
- [ ] Create Docker configuration
- [ ] Develop continuous integration pipeline
- [ ] Advanced data visualization
- [ ] Machine learning-powered insights

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License.
