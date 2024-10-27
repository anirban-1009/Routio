
# **Contributing to Routio**

Thank you for considering contributing to **Routio**! This project aims to optimize waste management routes using modern web technologies. Whether you're fixing bugs, adding new features, or improving documentation, your contributions are welcome.

## **Table of Contents**
1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Branching Strategy](#branching-strategy)
5. [Issue Tracking](#issue-tracking)
6. [Commit Message Guidelines](#commit-message-guidelines)
7. [Pull Requests](#pull-requests)



## **Code of Conduct**

By contributing to Routio, you agree to follow our [Code of Conduct](#), which outlines the standards of behavior expected from the community.



## **Getting Started**

### **1. Fork the Repository**
Start by forking the main Routio repository to your GitLab or GitHub account.

### **2. Clone the Repository**
```bash
git clone https://gitlab.com/your-username/routio-turborepo.git
cd routio-turborepo
```

### **3. Install Dependencies**

Routio uses a monorepo structure with both frontend and backend components.

- **Frontend (Next.js with Tailwind CSS)**
  ```bash
  cd apps/frontend
  npm install
  ```

- **Backend (Django Rest Framework)**
  ```bash
  cd apps/backend
  poetry install
  ```

### **4. Environment Variables**

You'll need to set up the required environment variables. Copy the example environment files and update them with your credentials:
- **Frontend**: `apps/frontend/.env.local`
- **Backend**: `apps/backend/.env`

If using Auth0, set up the following:
```bash
AUTH0_DOMAIN=<your-auth0-domain>
AUTH0_CLIENT_ID=<your-auth0-client-id>
AUTH0_CLIENT_SECRET=<your-auth0-client-secret>
```

### **5. Running the Application**

- **Frontend (Next.js)**:
  ```bash
  cd apps/frontend
  npm run dev
  ```

- **Backend (Django)**:
  ```bash
  cd apps/backend
  python manage.py runserver
  ```



## **Development Workflow**

1. Create a new **issue** or comment on an existing one in the GitLab repository. Label it as either `frontend` or `backend` depending on the work you're doing.
   
2. Once assigned to an issue, create a new branch:
   ```bash
   git checkout -b feature/issue-<issue-number>-<short-description>
   ```

3. Make your changes, and be sure to **commit frequently**. Use clear and descriptive commit messages following the guidelines below.

4. Push your branch to your forked repository and create a **Merge Request (MR)** targeting either the `main` branch for frontend changes or the `_backend` branch for backend changes.



## **Branching Strategy**

Routio follows a two-branch production strategy:

- **`main`**: Contains the latest stable code for both frontend and backend. This branch is deployed on Vercel for frontend.
- **`_backend`**: Contains the latest backend code, hosted on PythonAnywhere for the API.



## **Issue Tracking**

- Issues are tracked using GitLab. Make sure to describe the issue in detail and label it appropriately (e.g., `frontend`, `backend`, `bug`, `feature`).
- When working on an issue, assign yourself and move it to the "In Progress" section on the GitLab issue board.



## **Commit Message Guidelines**

- Use descriptive commit messages that clearly explain **what** and **why** you made the changes.
- Commit message format:
  ```
  <type>(<scope>): <subject>
  ```
  Example:
  ```
  feat(frontend): Add route plotting on the map
  fix(backend): Resolve database issue with driver roles
  ```

- **Types**:
  - `feat`: New feature
  - `fix`: Bug fix
  - `docs`: Documentation updates
  - `refactor`: Code refactoring without adding new features or fixing bugs



## **Pull Requests**

1. Ensure that your branch is up to date with the target branch (`main` or `_backend`) before creating a Merge Request.
2. Submit a **Merge Request (MR)** on GitLab:
   - Include a link to the issue you worked on.
   - Add a clear title and description of what your MR achieves.
   - If applicable, include screenshots or additional documentation.

3. Ensure that **tests pass** and the code is reviewed by at least one maintainer.



## **Contact**

For any further questions or help, feel free to reach out via GitLab or open an issue. We're here to help you contribute!
