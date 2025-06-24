# Flask Late Show API

A comprehensive REST API for managing a Late Night TV show system built with Flask, PostgreSQL, and JWT authentication.

##  Features

- **MVC Architecture**: Clean separation of concerns with Models, Views, and Controllers
- **JWT Authentication**: Secure token-based authentication for protected routes
- **PostgreSQL Database**: Robust relational database with proper relationships
- **RESTful API**: Standard HTTP methods and status codes
- **Data Validation**: Input validation and error handling
- **Cascade Deletion**: Proper database relationships with cascade operations

##  Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-JWT-Extended
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Testing**: Postman
- **Version Control**: Git & GitHub

##  Prerequisites

- Python 3.8+
- PostgreSQL
- Pipenv
- Postman (for API testing)

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd late-show-api
```

### 2. Install Dependencies

```bash
pipenv install
pipenv shell
```

### 3. PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE late_show_db;
```

### 4. Environment Configuration

Update `server/config.py` with your database credentials:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/late_show_db"
```

For production, set environment variables:

```bash
export DATABASE_URL="postgresql://username:password@localhost:5432/late_show_db"
export JWT_SECRET_KEY="your-super-secret-key"
```

### 5. Database Setup

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6. Seed the Database

```bash
python server/seed.py
```

### 7. Run the Application

```bash
python server/app.py
```

The API will be available at `http://127.0.0.1:5000`

##  Authentication Flow

### 1. Register a New User

```bash
POST /register
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123"
}
```

### 2. Login to Get JWT Token

```bash
POST /login
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "admin"
  }
}
```

### 3. Use Token in Protected Routes

```bash
Authorization: Bearer <your-jwt-token>
```

##  API Routes

### Authentication Routes (No Auth Required)

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |

### Public Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/episodes` | Get all episodes |
| GET | `/episodes/<id>` | Get specific episode with appearances |
| GET | `/guests` | Get all guests |

### Protected Routes (JWT Required)

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/appearances` | Create new appearance |
| DELETE | `/episodes/<id>` | Delete episode (cascades to appearances) |

##  Sample Requests & Responses

### Get All Episodes

```bash
GET /episodes
```

**Response:**
```json
[
  {
    "id": 1,
    "date": "2024-01-15",
    "number": 1001
  },
  {
    "id": 2,
    "date": "2024-01-16",
    "number": 1002
  }
]
```

### Get Episode with Appearances

```bash
GET /episodes/1
```

**Response:**
```json
{
  "id": 1,
  "date": "2024-01-15",
  "number": 1001,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Jennifer Lawrence",
        "occupation": "Actress"
      }
    }
  ]
}
```

### Create New Appearance (Protected)

```bash
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
```

**Response:**
```json
{
  "id": 7,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2,
  "guest": {
    "id": 1,
    "name": "Jennifer Lawrence",
    "occupation": "Actress"
  }
}
```

##  Testing with Postman

### 1. Import Collection

1. Open Postman
2. Click "Import" 
3. Select `challenge-4-lateshow.postman_collection.json`
4. The collection will be imported with all endpoints

### 2. Environment Setup

The collection includes variables:
- `base_url`: `http://127.0.0.1:5000`
- `token`: Auto-populated after login

### 3. Testing Flow

1. **Register/Login**: Use "Authentication" → "Login User" to get token
2. **Test Public Routes**: Try "Episodes" → "Get All Episodes"
3. **Test Protected Routes**: Use "Appearances" → "Create Appearance"

### 4. Automatic Token Management

The login request automatically saves the JWT token to the collection variable, so protected requests will work immediately.

##  Database Schema

### Models Overview

```
User
├── id (Primary Key)
├── username (Unique)
└── password_hash

Guest
├── id (Primary Key)
├── name
└── occupation

Episode
├── id (Primary Key)
├── date
├── number
└── appearances (One-to-Many, Cascade Delete)

Appearance
├── id (Primary Key)
├── rating (1-5 validation)
├── guest_id (Foreign Key)
└── episode_id (Foreign Key)
```

### Relationships

- **Episode → Appearances**: One-to-Many with cascade delete
- **Guest → Appearances**: One-to-Many
- **Appearance**: Belongs to both Guest and Episode

##  Development

### Database Operations

```bash
# Create new migration
flask db migrate -m "description"

# Apply migrations
flask db upgrade

# Reset database
flask db downgrade
```

### Seeded Data

The seed script creates:
- 2 users (admin/password123, producer/producer123)
- 5 guests (Jennifer Lawrence, Elon Musk, etc.)
- 5 episodes with various appearances
- Sample appearances with ratings

##  Error Handling

The API includes comprehensive error handling:

- **400**: Bad Request (missing/invalid data)
- **401**: Unauthorized (invalid credentials/token)
- **404**: Not Found (resource doesn't exist)
- **409**: Conflict (duplicate username)
- **422**: Unprocessable Entity (validation errors)
- **500**: Internal Server Error

##  API Documentation

### Authentication

All protected routes require the `Authorization` header:

```
Authorization: Bearer <jwt_token>
```

### Validation Rules

- **Rating**: Must be integer between 1-5
- **Username**: Must be unique
- **Password**: Required for registration/login
- **Foreign Keys**: Must reference existing records

##  GitHub Repository

[Link to your GitHub repository]

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

##  License

This project is licensed under the MIT License.

---

**Built using Flask and PostgreSQL**
