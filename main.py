import inspect
from getpass import getpass

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
    # Check if the name is at least 2 characters long     
    if len(name) < 2 or not isinstance(name, str):
        raise ValueError("Please make sure your name is greater than 2 characters! And in text format!")

    # Check if the user email includes a '@' and a valid domain ('.')
    valid_domains = ['.org', '.net', '.edu', '.ac', '.uk', '.com']
    if email.count('@') != 1:
        raise ValueError("Email must contain exactly one '@' symbol.")
    
    domain_part = email.split('@')[1]  # Get the part after '@'
    if not any(domain_part.endswith(domain) for domain in valid_domains):
        raise ValueError(f"Your email domain must end with one of the following: {', '.join(valid_domains)}")

    # Check if the password is greater than 8 characters
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
# print(validate_user.__doc__)
# print(inspect.getdoc(validate_user))

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
    # Validate the user inputs
    if validate_user(name, email, password):

        # If validation passes, create the user dictionary
        return {'name': name, 'email': email, 'password': password}  # Return the created user dictionary
    
     # If validation fails, return False
    return False

if __name__ == "__main__":
    try:
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = getpass("Enter your password (input will be hidden): ").strip()

        user = register_user(name, email, password)
        if user:
            print("User registered successfully!")
            print(user)
    except ValueError as e:
        print(f"Error: {e}")