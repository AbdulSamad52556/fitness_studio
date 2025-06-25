# 🏋️ Fitness Studio Booking API

A Django REST API for managing fitness class bookings with timezone support.

## 🌟 Features

- Class management (Yoga, Zumba, HIIT)
- Slot availability tracking
- Timezone-aware scheduling (IST with conversion support)
- RESTful API endpoints
- SQLite database (easy setup)

## 📌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/classes/` | GET | List all upcoming classes |
| `/api/bookings/book/` | POST | Create a new booking |
| `/api/bookings/` | GET | List bookings by client email |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbdulSamad52556/fitness_studio.git
   cd fitness_studio


2. Create and activate virtual environment:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Do Migrations

    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Seed sample data:

    ```bash
    python manage.py seed_data

5. Run development server:

    ```bash
    python manage.py runserver

## 🧪 Unit Testing

    python manage.py test

## 📚 API Documentation

### Get All Classes

    curl -X GET "http://localhost:8000/api/classes/?timezone=Asia/Kolkata"

### Create Booking

    curl -X POST "http://localhost:8000/api/bookings/book/" \
    -H "Content-Type: application/json" \
    -d '{
        "fitness_class": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }'

### Get Client Bookings

    curl -X GET "http://localhost:8000/api/bookings/?email=john@example.com"


