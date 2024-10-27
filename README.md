

# **Routio: Waste Management Route Optimization**

![Routio Logo](Banner.png) <!-- Add a logo or banner if available -->

**Routio** is an innovative platform designed to optimize urban waste management routes in real-time. It enhances efficiency, reduces operational costs, and contributes to environmental sustainability by dynamically adjusting collection routes based on data.


## **Table of Contents**
1. [About](#about)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Getting Started](#getting-started)
5. [Development Workflow](#development-workflow)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## **About**

In modern cities, waste management involves complex logistics, such as fluctuating waste volumes and dynamic traffic conditions. Routio tackles these challenges by integrating real-time data, optimizing routes, and providing key insights to enhance waste collection efficiency.

The project is built on a **monorepo** structure using modern web development technologies for both the frontend and backend, ensuring ease of development, collaboration, and deployment.


## **Features**
- **Real-Time Route Optimization**: Automatically adjusts waste collection routes based on dynamic factors like traffic and waste volume.
- **Role-Based Access Control**: Different views for regular users and drivers, managed through **Auth0**.
- **Map Integration**: Routes and collection points are visualized on an interactive map using **Next.js**.
- **Green Impact Metrics**: Display vehicle vitals, CO2 emissions, and other key metrics in real-time.
- **User-Friendly Interface**: Designed with a focus on easy navigation and accessibility for all users.


## **Technology Stack**

- **Frontend**: 
  - [Next.js](https://nextjs.org) for server-side rendering and a fast user interface.
  - [Tailwind CSS](https://tailwindcss.com) for responsive and modern UI components.
  
- **Backend**: 
  - [Django Rest Framework (DRF)](https://www.django-rest-framework.org) for handling APIs and data models.

- **Monorepo Management**: 
  - [TurboRepo](https://turborepo.org) for efficient monorepo handling.

- **Authentication**: 
  - [Auth0](https://auth0.com) for managing user login, logout, and roles.

- **Hosting**:
  - **Frontend**: Deployed on [Vercel](https://vercel.com).
  - **Backend**: Hosted on [PythonAnywhere](https://www.pythonanywhere.com) for API management.


## **Getting Started**

Follow the steps below to set up the project on your local machine for development or testing.

### **1. Clone the Repository**
```bash
git clone https://gitlab.com/your-username/routio-turborepo.git
cd routio-turborepo
```

### **2. Install Dependencies**

- **Frontend (Next.js)**:
  ```bash
  cd apps/frontend
  npm install
  ```

- **Backend (Django)**:
  ```bash
  cd apps/backend
  poetry install
  ```

### **3. Setup Environment Variables**

- Create an `.env.local` file for the **frontend**:
  ```bash
  cd apps/frontend
  cp .env.local\ example .env.local
  ```

- Setup environment variables for the **backend** in `.env`.
    ```bash
    cd apps/backend
    cp .env.example .env
    ```

### **4. Run the Application**

- **Frontend (Next.js)**:
  ```bash
  cd apps/frontend
  npm run dev
  ```

- **Backend (Django)**:
  ```bash
  cd apps/backend
  poetry shell
  python manage.py runserver
  ```

- **Unified server**:
    ```bash
    cd apps/backend
    poetry shell
    cd ../..
    npm run dev
    ```

## **Development Workflow**

Routio uses a monorepo structure, allowing both frontend and backend code to exist within the same repository. The workflow is managed using GitLab for issues and merge requests.

- **Branch Strategy**: 
  - `main` for both frontend and backend.
  - `_backend` for backend development and API hosting.

For detailed contribution steps, see the [Contributing Guide](CONTRIBUTING.md).



## **Contributing**

Contributions are welcome! Please follow our [Contributing Guidelines](CONTRIBUTING.md) for details on the code of conduct, development process, and how to submit your changes.



## **License**

This project is licensed under the GNU AGPLv3 License. See the [LICENSE](LICENSE) file for more information.


## **Contact**

For questions, feedback, or issues, feel free to reach out:

- **Project Lead**: Anirban Sikdar
- **Email**: anirbansikdar1009@gmail.com
- **GitLab Repository**: [Routio on GitLab](https://gitlab.com/anirban-sikdar/routio-turborepo)
