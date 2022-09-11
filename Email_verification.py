import re
email=input("Enter the email :\n")
#password=input("Enter the password :")
pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

if re.search(pattern,email):
    print(email,'is a correct email')
else:
    print(email,"is a wrong email")