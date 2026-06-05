def pass_check(p):
    has_digit = any(char.isdigit() for char in p)
    has_upper = any(char.isupper() for char in p)
    has_special = any(not char.isalnum() for char in p)
    has_letter = any(char.isalpha() for char in p)
    if len(p) >= 8 and has_digit and has_upper and has_special and has_letter:
        return "Strong Password"
    elif len(p) >= 8 and (has_digit or has_upper):
        return "Medium Password"
    else:
        return "Weak Password"
#=======================MAIN===========================
password = input("Enter your password: ")
print(pass_check(password))