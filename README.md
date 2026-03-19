# TESTEST

A full-stack web application built with Next.js, Python (FastAPI), and PostgreSQL.

## Tech Stack

- **Frontend**: Next.js 14 (React, TypeScript)
- **Backend**: Python 3.11+ (FastAPI)
- **Database**: PostgreSQL 15+
- **ORM**: SQLAlchemy
- **API Documentation**: OpenAPI (Swagger)

## Project Structure

```
.
├── frontend/          # Next.js application
├── backend/           # Python FastAPI application
├── docker-compose.yml # Docker setup for local development
└── README.md
```

## Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Compose (optional, for containerized setup)

## Getting Started

### Option 1: Docker Setup (Recommended)

1. Start all services:
```bash
docker-compose up -d
```

2. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Option 2: Manual Setup

#### Database Setup

1. Create a PostgreSQL database:
```bash
createdb testest_db
```

2. Update environment variables (see Configuration section)

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the development server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

## Configuration

### Backend Environment Variables

Create a `.env` file in the `backend` directory:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/testest_db
SECRET_KEY=your-secret-key-here
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:3000
```

### Frontend Environment Variables

Create a `.env.local` file in the `frontend` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development

### Running Tests

Backend:
```bash
cd backend
pytest
```

Frontend:
```bash
cd frontend
npm test
```

### Code Formatting

Backend:
```bash
cd backend
black .
isort .
```

Frontend:
```bash
cd frontend
npm run lint
npm run format
```

## Production Build

### Frontend
```bash
cd frontend
npm run build
npm start
```

### Backend
```bash
cd backend
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT
