# DevOps Test Project

A Chainlit-based application with automated build and deployment capabilities.

## Project Structure

```
devops-test/
├── app/                    # Main application
│   ├── app.py             # Chainlit application entry point
│   └── maintenance_script.py  # Email notification script
├── backend/               # Backend package
│   ├── chainlit/         # Chainlit library source
│   ├── pyproject.toml    # Poetry configuration
│   └── poetry.lock       # Poetry lock file
├── frontend/             # Frontend React application
└── cypress/              # End-to-end tests
```

## Prerequisites

- Python 3.8+
- Poetry (Python dependency management)
- Node.js and pnpm (for frontend development)

## Installation & Setup

### 1. Build the Backend Package

Navigate to the backend directory and build the package using Poetry:

```bash
cd backend
poetry build
pip install dist/*.whl
```

This will:
- Build the Chainlit package from source
- Create a wheel distribution file
- Install the package locally

### 2. Start the Application

Run the Chainlit application:

```bash
cd app
chainlit run app.py -h --port $PORT --host 0.0.0.0
```

**Note**: Make sure to set the `PORT` environment variable before running:
```bash
export PORT=8000  # or your preferred port
```

## Environment Variables

- `PORT`: The port number for the application (default: 8000)

## Additional Scripts

### Maintenance Script

The project includes a maintenance script (`app/maintenance_script.py`) for sending email notifications. Configure your email settings in the script before using it for cron jobs.

## Development

### Frontend Development

```bash
cd frontend
pnpm install
pnpm dev
```

### Running Tests

```bash
# End-to-end tests
npx cypress open

# Frontend tests
cd frontend
pnpm test
```

### Backend Development

```bash
cd backend
poetry install
poetry shell
```

## Deployment

The application is configured to run on any host (`0.0.0.0`) and can be deployed to cloud platforms that support the `$PORT` environment variable.

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

Please refer to CONTRIBUTING.md for contribution guidelines.