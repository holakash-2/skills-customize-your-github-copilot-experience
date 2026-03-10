# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create web services with automatic validation, documentation, and type hints to handle HTTP requests and responses efficiently.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application and Basic Routes

#### Description
Initialize a FastAPI application and create basic HTTP endpoints to handle GET and POST requests.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create a GET endpoint that returns a JSON response with a welcome message
- Create a POST endpoint that accepts request data and returns a confirmation response
- Run the application using uvicorn server

### 🛠️ Implement Data Models and Request Validation

#### Description
Define Pydantic models to validate incoming request data and ensure type safety across API endpoints.

#### Requirements
Completed program should:

- Create a Pydantic model for request data (e.g., a User or Item model)
- Use the model in endpoints to validate incoming JSON data
- Return appropriate error messages for invalid data
- Document expected data structure in API responses

### 🛠️ Build CRUD Operations and Path Parameters

#### Description
Develop endpoints that perform Create, Read, Update, and Delete operations with dynamic URL parameters.

#### Requirements
Completed program should:

- Create endpoints to retrieve, update, and delete items using path parameters (e.g., `/items/{item_id}`)
- Implement in-memory storage (e.g., using a list or dictionary) to persist data during runtime
- Validate that requested items exist before performing operations
- Return appropriate HTTP status codes for different scenarios (200, 201, 404, etc.)
