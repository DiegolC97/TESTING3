# TESTEST

A full-stack application built with Next.js, Python (FastAPI), and PostgreSQL.

## Tech Stack

- **Frontend**: Next.js 14 (React, TypeScript)
- **Backend**: Python 3.11+ with FastAPI
- **Database**: PostgreSQL
- **Styling**: Tailwind CSS
- **API Communication**: Axios
- **ORM**: SQLAlchemy

## Project Structure

```
.
├── frontend/          # Next.js frontend application
│   ├── src/
│   │   ├── app/      # App router pages
│   │   ├── components/
│   │   └── lib/      # Utilities and API client
│   └── public/
├── backend/          # Python FastAPI backend
│   ├── app/
│   │   ├── api/      # API routes
│   │   ├── core/     # Configuration
│   │   ├── db/       # Database models and connection
│   │   └── schemas/  # Pydantic schemas
│   └── tests/
└── docker/           # Docker configuration
```

## Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Python 3.11+
- PostgreSQL 14+
- Docker and Docker Compose (optional)

## Setup Instructions

### 1. Database Setup

Create a PostgreSQL database:

```bash
createdb testest_db
```

Or use Docker:

```bash
docker-compose up -d postgres
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at http://localhost:8000
API documentation at http://localhost:8000/docs

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env.local file
cp .env.example .env.local

# Start development server
npm run dev
```

Frontend will be available at http://localhost:3000

## Development

### Running with Docker

```bash
docker-compose up
```

This will start all services (frontend, backend, and database).

### Database Migrations

```bash
cd backend

# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Running Tests

Backend tests:
```bash
cd backend
pytest
```

Frontend tests:
```bash
cd frontend
npm test
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `ENVIRONMENT`: development/production

### Frontend (.env.local)
- `NEXT_PUBLIC_API_URL`: Backend API URL

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/v1/items` - List items
- `POST /api/v1/items` - Create item
- `GET /api/v1/items/{id}` - Get item by ID
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

## License

MIT
