def login(username, password):
    print("Authenticating user...")
    if username == "admin" and password == "1234":
        return "Authentication successful"
    return "Authentication failed"

print(login("admin", "1234"))