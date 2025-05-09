def valid(max_attempts=3):
    def entry(email):
        try:
            if "@" in email and "." in email:
                user, domain = email.split("@")
                if user and domain and "." in domain:
                    x, y = domain.split(".")
                    if x and y and "." not in y:
                        return True
            else: 
                return False
        except Exception as e:
            print("Error during email validation:", e)
            return False

    counter = max_attempts
    while counter > 0:
        try:
            email = input("Enter a valid email: ")
            if entry(email):
                print("Valid email entered:", email)
                return email  
            else:
                counter -= 1
                print(f"Invalid email. You have {counter} tries left.")
        except Exception as e:
            counter -= 1
            print(f"An error occurred: {e}. You have {counter} tries left.")
    
    print("Sorry, try again later.")
    return None  