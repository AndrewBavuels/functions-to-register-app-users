import inspect
def validate_user(name, email, password):
    """
    Validate each one of the user inputs to register for an App.
    
    Parameters
    ----------
    
    Args:
        name (str): text the user name as a string type and at least 2 characters long.
        email (str): text the user email and include a '@' and a valid domain ('.').
        password: create a strong password with at least 8 characters and include certain characters.
    
    Returns
    -------
        bool: returns True if all validations inputs pass.

    """
    
    if len(name) < 2 or not isinstance(name, str):
        raise ValueError("The name must be greater than two characters and in text format.")

    
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("The email must contain a valid format and domain.")

    
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

    return True
print(validate_user.__doc__)
print(inspect.getdoc(validate_user))

# Function to register the user if the input is valid
def register_user(name, email, password):
    """
    Register the previous validated user inputs to register for an App.
    
    Parameters
    ----------
    
    Args:
        name (str): text the user name as a string type and at least 2 characters long.
        email (str): text the user email and include a '@' and a valid domain ('.').
        password: create a strong password with at least 8 characters and include certain characters.
    
    Returns
    -------
        Dict.

    """    
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
print(register_user.__doc__)
print(inspect.getdoc(register_user))
user = register_user('John', 'john@example.uk.es.com', 'securePassword123!')
print(user)  # Print the user dictionary if registration is successful