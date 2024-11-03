# Technical Test Instructions for Python Developer

## Objective

Your task is to extend an existing Python web application by adding new features that simulate a real-world scenario. You will:

- Add a new endpoint that allows users to receive personalized recommendations based on their interests.
- Save these recommendations in an in memory cache.
- Add another endpoint to retrieve saved recommendations for each user.
- Integrate with a mock Large Language Model (LLM) agent using a provided Docker Compose setup.

This task assesses your ability to integrate external services, handle HTTP requests/responses, and write clean, maintainable code following best practices.

### Note: you can change any file on this project, as long as you provide a working code OR enough code that can you can explain you choices.

## Project Overview

You are provided with a basic project structure of a web application built using FastAPI. The application currently has a few endpoints set up. Your job is to:


1. **Add a new endpoint `/recommendations`** that generates and saves personalized recommendations.
    - Integrate with a mock LLM agent, accessible via Docker Compose, to generate recommendations.
    - Save recommendations in a database (you'll need to add a in memory cache).
  
2. **Add another endpoint `/users/:user_id/recommendations`** to retrieve saved recommendations.
    - Ensure proper error handling and input validation.

3. **Create a frontend using React that uses those two endpoints**
   - there is no restriction on component library or tools you use
   - create is based on the mockup provided

4. **Write unit tests** for your new code.
  
5. **Document your work** and provide instructions on how to run the application.

## Task Details

### 1. create the FrontEnd based on the muckup provided
- **Create Add a React app that will be based on the mockup provided**:
  - it is recommended to use NextJS and shadcn, but any component library will work.
  - this can be served using the existing server, or you can create another server to serve the new FE app.
  - if you decide to add a new app, make sure to add it to the docker compose file.
  - the frontend should be mobile compatible and look good both and dsektop and on mobile.

### 2. Start the Mock LLM Agent Docker Compose

- Use the provided `docker-compose.yml` file to start the mock LLM agent.
- **LLM Agent URL:** The mock LLM agent will be accessible at `http://localhost:1080`.

### 3. Create a New Endpoint `/recommendations`

- **Method:** POST
- **Description:** Accepts a JSON payload containing user preferences, generates personalized recommendations using the mock LLM agent, saves them in the cache, and returns them in the response.
- **Request Body Example:**
  ```json
  {
    "user_id": "12345",
    "preferences": ["science fiction", "artificial intelligence", "space exploration"]
  }
  ```
- **Response Body Example:**
  ```json
  {
    "user_id": "12345",
    "recommendations": [
      "Book: 'Dune' by Frank Herbert",
      "Article: 'The Future of AI in Space Travel'",
      "Movie: 'Interstellar'"
    ]
  }
  ```
- **Real-World Scenario:** This endpoint simulates a feature in a content platform where users receive content recommendations based on their interests.

### 4. Save Recommendations in an in memory cache

- **Data Persistence**:
  - Save each user's recommendations in an in memory cache

bonus:
- **Database Setup**:
  - Add a MongoDB database service to the `docker-compose.yml` file.
  - Configure the database connection in your application.
  - Define models/schemas using Mongoose.
- **Data Persistence**:
  - Save each user's recommendations in the database with the `user_id` as a reference.
  - Ensure that data is stored securely and efficiently.

### 5. Create Another Endpoint `/users/{user_id}/recommendations`

- **Method:** GET
- **Description:** Retrieves saved recommendations for a given `user_id`. If the user hasn't requested any recommendations yet, return a 404 error.
- **Response Body Example (Success):**
  ```json
  {
    "user_id": "12345",
    "recommendations": [
      "Book: 'Dune' by Frank Herbert",
      "Article: 'The Future of AI in Space Travel'",
      "Movie: 'Interstellar'"
    ]
  }
  ```
- **Error Response Example (User Not Found):**
  ```json
  {
    "error": "No recommendations found for user_id 12345."
  }
  ```

### 6. Integrate with the Mock LLM Agent

- **LLM Agent Interaction:** Send a POST request to `http://localhost:8080/llm/generate` with the user's preferences.
- The mock LLM agent will return a list of recommendations based on the provided preferences.
- **LLM Agent Request Example:**
  ```json
  {
    "preferences": ["science fiction", "artificial intelligence", "space exploration"]
  }
  ```
- **LLM Agent Response Example:**
  ```json
  {
    "recommendations": [
      "Book: 'Dune' by Frank Herbert",
      "Article: 'The Future of AI in Space Travel'",
      "Movie: 'Interstellar'"
    ]
  }
  ```

### 7. Error Handling and Input Validation

- **Input Validation:**
  - Ensure that `user_id` is provided and is a non-empty string.
  - Ensure that `preferences` is a non-empty list of strings.
- **Error Handling:**
  - Handle scenarios where the LLM agent returns an error or is unreachable.
  - Handle database errors (e.g., connection issues, query failures).
  - Return appropriate HTTP status codes and error messages.
- **Error Response Example:**
  ```json
  {
    "error": "Unable to fetch recommendations at this time. Please try again later."
  }
  ```

### 8. Documentation

- **Update `README.md`:**
  - Provide instructions on how to set up and run the application, including starting the services via Docker Compose.
  - Explain how to run the tests.
  - Document any assumptions or decisions made during development.

## Requirements

- **Programming Language:** Python 3.8 or higher
- **Web Framework:** FastAPI
- **Testing Framework:** `pytest` or `unittest`
- **External Tools:** MockServer: Accessible at `http://localhost:8080` via Docker Compose.
- **Code Style:** Adhere to PEP 8 guidelines.
- **Version Control:** Provide your solution in a Git repository format.

## Submission Guidelines

- **Source Code:** Submit all source code files, including the updated project structure.
- **Documentation:** Ensure the `README.md` is clear and provides all necessary instructions.
- **Dependencies:** Include a `requirements.txt` file listing all Python dependencies.
- **Testing:** All tests should be runnable using a single command (e.g., `pytest`).
- **Docker Compose:** Include your updated `docker-compose.yml` file with the database service added. Ensure that all services can be started with `docker-compose up`.
- **Git Commits:** Make meaningful commit messages that reflect the changes made.

## Evaluation Criteria

- **Functionality:**
  - The endpoints work as specified.
  - Correct integration with the mock LLM agent.

- **Code Quality:**
  - Clean, readable, and well-organized code following best practices.
  - Proper use of comments and docstrings where appropriate.

- **Error Handling:** 
  - Robust input validation and error management.
  - Appropriate HTTP status codes are returned.

- **Testing:**
  - Comprehensive unit tests covering various scenarios.
  - Tests run successfully without errors.

- **Documentation:**
  - Clear instructions and explanations in the `README.md`.
  - Any assumptions or design decisions are well-documented.

- **Integration:**
  - Effective use of the provided MockServer to simulate the LLM agent.
  - Bonus: Successful addition of a database service to Docker Compose.

## Notes

- **Additional Libraries:** You may use additional Python libraries if necessary (e.g., SQLAlchemy for database interactions), but please justify their use in your documentation.
- **Assumptions:** If any part of the task is unclear, make reasonable assumptions and note them in the `README.md`.
- **Focus Areas:** Demonstrate your understanding of API development, external service integration, and testing.
- **Time Management:** While quality is important, this task is also an opportunity to show how you manage your time to deliver a working solution efficiently.

We look forward to reviewing your submission. If you have any questions, feel free to reach out. Good luck!

## Getting Started (For Your Reference)

Below is a brief guide to help you set up the project environment.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up the Environment

- **Python Dependencies:**

  ```bash
  pip install -r requirements.txt
  ```

- **Docker Services:**

  Start all services (including the mock LLM agent) using Docker Compose:

  ```bash
  docker-compose up
  ```

### 3. Run the Application

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

### 4. Test the Endpoints

- **Generate Recommendations:**

  ```bash
  curl -X POST "http://localhost:8000/recommendations" \
  -H "Content-Type: application/json" \
  -d '{ "user_id": "12345", "preferences": ["science fiction", "artificial intelligence", "space exploration"] }'
  ```

- **Retrieve Recommendations:**

  ```bash
  curl -X GET "http://localhost:8000/users/12345/recommendations"
  ```

### 5. Run Tests

```bash
pytest
```

**Note:** Replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name of your Git repository.

### Additional Information

**Mock LLM Agent Endpoint:** `http://localhost:8080/llm/generate`

- **Database Service:** If applicable, ensure the database is correctly configured in both `docker-compose.yml` and your application settings.

Feel free to enhance the project structure and configuration as you see fit, as long as the core requirements are met.
- **it is recommended to look at the different options for the LLM Agent Endpoints!**


**Good luck!**