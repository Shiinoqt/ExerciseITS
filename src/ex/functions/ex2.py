def check_lenght(smthing: str):
    if len(smthing) > 10:
        print(f"The {smthing} is longer than 10 characters.")
    elif len(smthing) < 10:
        print(f"The {smthing} is shorter than 10 characters.")
    else:
        print(f"The {smthing} is equal to 10 characters.")

check_lenght("Hello World")
check_lenght("Hello")
check_lenght("Hello Worl")