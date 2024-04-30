# Flask User Management System

This is a Flask web application for managing users. It provides basic CRUD (Create, Read, Update, Delete) functionality for users and utilizes Flask-Security for user authentication and authorization.

## Features

- **User Registration**: Registered users can add new users to the system.
- **User Listing**: Displays a paginated list of all users with sorting options.
- **User Details**: Allows users to view details of a specific user.
- **Navigation**: Provides a form to navigate to a specific user's page by entering their ID.
- **Responsive Design**: Responsive layout ensures optimal viewing experience across different devices.
- **CSS Styling**: Includes CSS styles for consistent and visually appealing user interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-user-management.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the root directory and add the following variables:

    ```plaintext
    DATABASE_URI_LOCAL=your_database_uri
    SECRET_KEY=your_secret_key
    SECURITY_PASSWORD_SALT=your_security_password_salt
    ```

4. Initialize the database and seed initial data:

    ```bash
    python app.py
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.


## Contact

For any questions or suggestions, please feel free to contact Sergeyhayrapetyan@hotmail.com .

---

Feel free to customize this README based on your specific project details and preferences!
