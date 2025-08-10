# Stock Portfolio Service CI/CD Pipeline (Cloud Computing Assignment #4)

This repository contains the source code and CI/CD pipeline configuration for the stock portfolio application using GitHub Actions. This is the final assignment migrating the finance application from Docker Compose to a fully automated CI/CD pipeline with testing and deployment orchestration.

---

## Overview

Assignment #4 implements a GitHub Actions workflow that builds, tests, and validates the stock portfolio application comprising three services:

- **Stocks Service:** A single instance managing stock portfolio data, connected to a MySQL database.  
- **Capital Gains Service:** Communicates with the stocks service to calculate capital gains; stateless and non-persistent.  
- **MySQL Database:** Holds persistent stock portfolio data for the stocks service.  

This assignment simplifies the architecture from assignment #2 by removing load balancing and NGINX reverse proxy, focusing on CI/CD automation and robustness.

---

## Architecture

- **Stocks Service** listens on host port **5001** forwarding to container port **8000**.  
- **Capital Gains Service** listens on host port **5003** forwarding to container port **8080**.  
- **MySQL** serves as the persistent data store with a single database/schema used by the stocks service.  
- The services communicate internally via Docker Compose networking.

---

## CI/CD Pipeline (GitHub Actions)

The pipeline, defined in `.github/workflows/assignment4.yml`, consists of three sequential jobs triggered manually (`workflow_dispatch` event):

1. **Build Job:**  
   Builds Docker images for the stocks and capital gains services (Java-based). If successful, proceeds to testing.

2. **Test Job:**  
   Uses the built images and a MySQL container to run the full application via `docker compose up`.  
   Executes **pytest** tests located in the `tests/` directory (`assn4_tests.py`) to validate API functionality and correctness.

3. **Query Job:**  
   Runs the application again and reads query instructions from a `query.txt` file.  
   Issues HTTP GET requests with query strings against the services, capturing responses into a `response.txt` file.  
   Uploads this file as an artifact for review.

---

## Testing

- Tests are implemented with **pytest** in the `tests/assn4_tests.py` file.  
- Tests cover:  
  - Adding multiple stocks with POST requests and validating unique IDs and correct status codes.  
  - Retrieving individual stocks and portfolios.  
  - Checking stock values and portfolio valuation with allowable price fluctuation margin.  
  - Handling invalid requests with expected error codes.  
  - Deleting stocks and verifying proper deletion.  

---

## Artifacts

Upon workflow completion, the following artifacts are uploaded and available in the GitHub Actions UI:

- **log.txt:** Contains timestamps, submitter info, image build status, container startup status, and test results summary.  
- **assn4_test_results.txt:** Detailed pytest test output with pass/fail results.  
- **response.txt:** Outputs from query job with request-response logs for queries specified in `query.txt`.

---

## Running Locally

To run the application locally with Docker Compose:

```bash
docker compose up --build
```
---

Ensure MongoDB is running or available as per the docker-compose.yml configuration. Access the services on ports 5001 (stocks) and 5003 (capital gains).

## Repository Structure
- /stocks-service/ — Stocks service Java source code and Dockerfile

- /capital-gains-service/ — Capital gains service Java source code and Dockerfile

- docker-compose.yml — Defines multi-container application setup with MySQL

- /tests/assn4_tests.py — Pytest test cases for automated API testing

- .github/workflows/assignment4.yml — GitHub Actions workflow file

- query.txt — Sample query file used by the query job

---

## Notes

- The capital gains service is updated to communicate with only a single stocks service instance.

- The CI/CD pipeline uses manual triggers to control deployment cycles.

- MySQL is used as the persistent backend for this assignment, differing from previous assignments that used MongoDB or in-memory storage.

- All Docker images and containers are built and run within the workflow to ensure reproducible and isolated testing environments.

- Although the services are implemented in Java, tests are run using pytest (Python) for API-level validation.

---
