## The Humanitarian App (Logistics Management System)

### Overview
The **Humanitarian App (Logistics Management System)** is a robust, scalable, and modular platform designed to handle logistics, supply chain, and distribution operations. Built using Django, this system offers a comprehensive solution for managing users, inventory, orders, and shipments. It incorporates advanced features such as role-based access control, shipment tracking, and efficient order management, while maintaining high standards of security and performance.

### Key Features

- **User Authentication & Authorization**: 
  - **JWT Authentication** for secure and stateless user authentication.
  - **Role-Based Access Control (RBAC)** ensuring that users have access only to resources relevant to their role (admin, manager, user).
  - **Admin Dashboard** for managing users, shipments, and orders.

- **Inventory Management**: 
  - Seamlessly manage product listings, including item details, stock levels, and pricing.
  - **Real-time stock updates** upon order placement and shipment processing.

- **Order Management**: 
  - Efficient management of customer orders, including itemized details, pricing, and status updates.
  - **Order Itemization** to track specific items in each order, with support for multiple items per order.

- **Shipment Tracking**: 
  - Comprehensive shipment management, including **real-time tracking**, shipment status updates, and **estimated delivery times**.
  - **Notifications** to keep users informed about shipment status, order progress, and updates.

- **Comprehensive Testing**:
  - **Unit tests** and **integration tests** to ensure reliability, stability, and high performance.
  - **Performance testing** for handling large datasets, ensuring optimal response times even under heavy load.

- **CI/CD Integration**:
  - **Automated testing** and **continuous integration** using popular CI/CD tools.
  - **Dockerized** environment for consistent deployments and containerized applications.

- **Frontend**: 
  - A **React.js** frontend for an intuitive user interface, providing a seamless experience for users, admins, and managers.
  - Features include login, order management, shipment tracking, and a comprehensive admin dashboard.

### Tech Stack

- **Backend**: Django, Django Rest Framework (DRF), PostgreSQL
- **Frontend**: React.js
- **Authentication**: JWT (JSON Web Tokens)
- **Task Queue**: Celery with Redis for asynchronous processing
- **Caching**: Redis for caching frequently accessed data
- **Testing**: Pytest, Django’s TestCase
- **CI/CD**: GitHub Actions, Docker
- **Containerization**: Docker Compose for multi-container setups

### Architecture

- **Modular Design**: The project is split into four main apps:
  - **User**: Handles user authentication, role management, and user-specific data.
  - **Inventory**: Manages items, their details, and stock levels.
  - **Orders**: Manages customer orders, order items, and order status.
  - **Shipment**: Manages the logistics of shipment, including tracking and status updates.

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Festorah/Humanitarian-inventory.git
   cd inventory_management
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for sensitive data like database credentials, secret keys, etc.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. For Dockerized environment, run:
   ```bash
   docker-compose up --build
   ```

### Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests to cover your changes.
4. Submit a pull request with a detailed description of your changes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
