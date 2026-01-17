# Minimize URL - Flask URL Shortener

A Flask-based REST API for shortening URLs with user authentication and click tracking.

## Features

- User authentication with JWT tokens
- URL shortening with unique short codes
- Click tracking for shortened URLs
- SQLite database with Alembic migrations

## Project Structure

```
minimize-url-flask/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configuration settings
│   ├── extensions.py      # Flask extensions (SQLAlchemy, JWT)
│   ├── models/
│   │   ├── user.py        # User model with password hashing
│   │   └── short_url.py   # ShortUrl model
│   ├── routes/
│   │   ├── auth_routes.py # Authentication endpoints
│   │   └── url_routes.py  # URL shortening endpoints
│   └── utils/             # Utility functions
├── instance/              # Instance-specific files
├── migrations/            # Alembic database migrations
│   ├── alembic.ini
│   ├── env.py
│   └── versions/
└── __pycache__/
```

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd minimize-url-flask
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

The application will start on `http://localhost:5000` in debug mode.

## API Endpoints

### Authentication

#### Sign Up
```
POST /auth/signup
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password"
}
```

**Response (201):**
```json
{
  "message": "User registered successfully",
  "access_token": "eyJhbGc..."
}
```

#### Login
```
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "secure_password"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGc..."
}
```

### URL Shortening

#### Shorten URL
```
POST /url/shorten
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "original_url": "https://www.example.com/very/long/url"
}
```

**Response (200):**
```json
{
  "short_url": "http://localhost:5000/url/a1b2c3"
}
```

#### Redirect Short URL
```
GET /url/{short_code}
```

Redirects to the original URL and increments the click count.

## Database Migrations

### Create Initial Database
```bash
python main.py
```

This creates the SQLite database automatically on first run.

### Generate New Migration
```bash
flask db migrate -m "Description of changes"
```

### Apply Migrations
```bash
flask db upgrade
```

### Downgrade Database
```bash
flask db downgrade
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.2 | Web framework |
| Flask-SQLAlchemy | 3.1.1 | ORM & database |
| Flask-JWT-Extended | - | JWT authentication |
| Flask-Migrate | 4.1.0 | Database migrations |
| SQLAlchemy | 2.0.45 | Database toolkit |
| Werkzeug | 3.1.5 | WSGI utilities |
| Alembic | 1.18.1 | Database migrations |

See [requirements.txt](requirements.txt) for the complete list.

## Configuration

Edit [app/config.py](app/config.py) to modify:

- `SECRET_KEY` - Flask secret key (⚠️ change in production)
- `SQLALCHEMY_DATABASE_URI` - Database connection string
- `JWT_SECRET_KEY` - JWT signing key (⚠️ change in production)

## Security Notes

⚠️ **Before deploying to production:**

1. Change `SECRET_KEY` in [app/config.py](app/config.py)
2. Change `JWT_SECRET_KEY` in [app/config.py](app/config.py)
3. Use environment variables for sensitive data
4. Configure proper CORS settings
5. Use HTTPS instead of HTTP
6. Set `debug=False` in production

## Future Enhancements

- Custom short codes
- URL expiration
- Analytics dashboard
- Rate limiting
- Email verification
- Password reset functionality

## License

MIT License