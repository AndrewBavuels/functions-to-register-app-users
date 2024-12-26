# Creating Functions to Register App Users

## Description

This project implements a simple Python-based system to validate and register users for an application. It includes functionalities to verify user inputs (name, email, and password) and to create a structured user record upon successful validation.

The project structure is as follows:

```sh
└── register_user
    ├── README.md
    └── main.py
```

## Features

- **Input Validation**:
  - Ensures the user name is at least 2 characters long and is a string.
  - Validates the email contains "@" and a proper domain.
  - Enforces password strength with the following rules:
    - Minimum 8 characters.
    - At least one uppercase letter.
    - At least one lowercase letter.
    - At least one numeric character.
    - At least one special character.

- **User Registration**:
  - Creates a dictionary containing validated user information.

## Requirements

- Python 3.8 or higher.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/register_user.git
   cd register_user

2. (Optional) Set up a virtual environment:

    ```bash
    conda create --name register_user

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py

2. Example:

    - Input:

    ```bash
    register_user('John', 'john@example.com', 'securePassword123!')

    - Output:

    ```bash
    {'name': 'John', 'email': 'john@example.com', 'password': 'securePassword123!'}

