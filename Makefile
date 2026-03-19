.PHONY: help install dev-up dev-down clean test lint format

help:
	@echo "Available commands:"
	@echo "  make install    - Install all dependencies"
	@echo "  make dev-up     - Start development environment with Docker"
	@echo "  make dev-down   - Stop development environment"
	@echo "  make clean      - Clean all generated files"
	@echo "  make test       - Run all tests"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code"

install:
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "Dependencies installed!"

dev-up:
	@echo "Starting development environment..."
	docker-compose up -d
	@echo "Services started!"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

dev-down:
	@echo "Stopping development environment..."
	docker-compose down
	@echo "Services stopped!"

clean:
	@echo "Cleaning generated files..."
	rm -rf frontend/node_modules frontend/.next frontend/out
	rm -rf backend/venv backend/__pycache__ backend/**/__pycache__
	rm -rf backend/.pytest_cache backend/**/.pytest_cache
	rm -f backend/test.db
	@echo "Cleanup complete!"

test:
	@echo "Running backend tests..."
	cd backend && pytest
	@echo "Tests complete!"

lint:
	@echo "Linting backend..."
	cd backend && flake8 app
	@echo "Linting frontend..."
	cd frontend && npm run lint
	@echo "Linting complete!"

format:
	@echo "Formatting backend code..."
	cd backend && black . && isort .
	@echo "Formatting frontend code..."
	cd frontend && npm run format
	@echo "Formatting complete!"
