
def valid(DB, user, password):
    user_found = None
    for i in DB:
        if i["name"] == user:
            user_found = i
            break
        else:
            print("Username not found !")
            return False

    if user_found["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False