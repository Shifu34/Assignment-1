# ML CI/CD Pipeline Project

This repository demonstrates a CI/CD pipeline for a machine learning project. The pipeline includes:
- **Repository Branching Strategy:** `dev` for development, `test` for integration testing, and `master` for production.
- **Code Quality Checks:** GitHub Actions with Flake8.
- **Automated Unit Testing:** GitHub Actions running tests on feature branches.
- **Deployment:** Jenkins job that containerizes the app with Docker and pushes it to Docker Hub.
- **Admin Notifications:** Email sent after successful deployment.

## Directory Structure
    ml-cicd-project/ ├── data/ │ └── unique_dataset.csv ├── models/ │ └── model.py ├── app/ │ ├── app.py │ └── requirements.txt ├── tests/ │ └── test_app.py ├── Dockerfile ├── Jenkinsfile ├── .github/ │ └── workflows/ │ ├── flake8.yml │ └── test.yml └── README.md

## How to Run

1. **Branching:**  
   - Develop new features on the `dev` branch.
   - Merge into `test` for integration testing.
   - Merge into `master` to trigger Jenkins for deployment.

2. **CI/CD Workflows:**  
   - GitHub Actions workflows will run Flake8 and unit tests on pull requests.
   - Jenkins will build and push a Docker image upon merge to `master`.

3. **Deployment:**  
   - Check Docker Hub for the new image.
   - An email will be sent to the admin confirming deployment.

Happy Coding!

