def valid(email):
    if len(email) < 5 or "@" not in email or "." not in email:
        return False
    a= email.split("@")
    if len(a) != 2:
        return False
    x,y= a
    if "." not in y or y.startswith(".") or y.endswith("."):
        return False
    y1 = y.split(".")
    if len(y1[-1]) < 2:
        return False
    return True
email = input("Enter a email:")
print( "email is valid ") if valid(email) else print ("email is not vaild")
