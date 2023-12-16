def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love NJU
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    num = num_attempts
    def get_secret(password_attempt):
        if(num == 0):
            return ("SECRET LOCKED")
        else:
            if(password_attempt == password):
                return secret
            else:
                num = num - 1
                return ("INCORRECT PASSWORD")  
    return get_secret


my_secret = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
my_secret = my_secret("hax0r_1") # 2 attempts left)