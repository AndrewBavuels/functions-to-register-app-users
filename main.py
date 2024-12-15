# Function to validate user input (name, email, and password)
def validate_user(name, email, password):
    # Validate the name: must be a string and at least 2 characters long
    if len(name) < 2 or not isinstance(name, str):
        raise ValueError("The name must be greater than two characters and in text format.")

    # Validate the email: must contain '@' and a valid domain ('.')
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("The email must contain a valid format and domain.")

    # Validate the password: it must be at least 8 characters and include certain characters
    if len(password) < 8:
        raise ValueError("The password must be greater than 8 characters and include at least one uppercase letter, one lowercase letter, one number, and one special character.")

    # Check if the password contains at least one uppercase letter
    if not any(p.isupper() for p in password):
        raise ValueError("The password must include at least one uppercase letter.")

    # Check if the password contains at least one lowercase letter
    if not any(p.islower() for p in password):
        raise ValueError("The password must include at least one lowercase letter.")

    # Check if the password contains at least one numeric character
    if not any(p.isdigit() for p in password):
        raise ValueError("The password must include at least one number.")

    # Check if the password contains at least one special character
    if not any(p in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for p in password):
        raise ValueError("The password must include at least one special character.")

    return True  # If all validations pass, return True

# Function to register the user if the input is valid
def register_user(name, email, password):
    try:
        # Call validate_user to check if the user details are valid
        if validate_user(name, email, password):
            # If validation passes, create the user dictionary
            user = {'name': name, 'email': email, 'password': password}
            return user  # Return the created user dictionary
    except ValueError as e:
        # If validation fails, return the error message raised by validate_user
        return str(e)  # Return the error message

# Example usage: Attempt to register a user with valid data
user = register_user('John', 'john@example.uk.es.com', 'securePassword123!')
print(user)  # Print the user dictionary if registration is successful