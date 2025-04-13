# Blog Site - Django + PostgreSQL + Docker

This project is a blog site built with **Django** as the backend framework and **PostgreSQL** as the database. It is **dockerized** for easy local development and deployment.

## Features

- User authentication (register, login, logout)
- Create, edit, and delete blog posts
- View posts by all users
- Responsive UI (can be improved)
- PostgreSQL database integration

## Technologies Used

- **Django** - Backend framework
- **PostgreSQL** - Database
- **Docker** - Containerization
- **Docker Compose** - Multi-container management
- **HTML/CSS** - Frontend (basic)

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose
- Python (for local testing, if you want to run it without Docker)
- PostgreSQL (if not using Docker)

### Running with Docker

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/blog-site.git
   cd blog-site

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build

3. The site will be available at http://localhost:8000.

**Docker Commands**
To start the containers:
```bash
  docker-compose up
```
This will start the following services:

  **Django app (backend)**
  
  **PostgreSQL database**


To stop the Docker containers:
  ```bash
  docker-compose down
```
To view the logs of the Docker containers

```bash
  docker-compose logs
```

Apply migrations: After the containers are up and running, apply the database migrations:

```bash
docker-compose exec web python manage.py migrate
```

Access the application:

Visit the site at: http://localhost:8000.

