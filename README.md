# 🏋️ Fitness Studio Booking API

A Django REST API for managing fitness class bookings with timezone support.

## 🌟 Features

- Class management (Yoga, Zumba, HIIT)
- Real-time slot availability tracking
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
   cd fitness_studio/fitness_api


2. Create and activate virtual environment:

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. Install dependencies:

    pip install -r requirements.txt

4. Seed sample data:

    python manage.py seed_data

5. Run development server:

    python manage.py runserver


📚 API Documentation

Get All Classes

    curl -X GET "http://localhost:8000/api/classes/?timezone=Asia/Kolkata"

    Response:
        [
            {
                "id": 1,
                "name": "YOGA",
                "datetime": "2023-12-25T03:30:00Z",
                "local_datetime": "2023-12-25T09:00:00+05:30",
                "instructor": "Yoga Master",
                "max_slots": 15,
                "available_slots": 10
            }
        ]

Create Booking

    curl -X POST "http://localhost:8000/api/bookings/book/" \
    -H "Content-Type: application/json" \
    -d '{
        "fitness_class": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }'

Get Client Bookings

    curl -X GET "http://localhost:8000/api/bookings/?email=john@example.com"