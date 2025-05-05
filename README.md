# REST Hit

A Django REST API for managing music artists and their hits.

## Features

- Hit management (create, read, update, delete)
- RESTful API endpoints
- Automatic slug generation for hit titles
- Database population command for testing

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Szampan/zadanie_rest_hits.git
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. The API will be available at `http://localhost:8000/api/`

### API Endpoints

- Hits:
  - GET /api/v1/hits/ - List all hits
  - POST /api/v1/hits/ - Create a new hit
  - GET /api/v1/hits/{title_url}/ - Get hit details
  - PUT /ap/v1i/hits/{title_url}/ - Update hit
  - DELETE /api/v1/hits/{title_url}/ - Delete hit

### Populating the Database

To populate the database with sample data:
```bash
python manage.py populate_db
```

## Development

### Code Style

This project uses:
- Black for code formatting
- isort for import sorting

### Running Tests

```bash
python manage.py test
```

## Project Structure

```
rest-hits-api/
├── rest_hits_project/    # Project settings
├── rest_hits_app/        # Main application
│   ├── management/       # Custom management commands
│   ├── models.py         # Database models
│   ├── serializers.py    # API serializers
│   ├── urls.py          # URL routing
│   └── views.py         # API views
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```
