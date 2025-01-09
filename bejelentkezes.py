def elso():
    print("I/A, B:")
    email:str=str(input("Email cím: "))
    megegyszere:str=str(input("Email cím mégegyszer: "))
    jelszo:str=str(input("Jelszó: "))

    print("I/C:")
    if email == megegyszere and jelszo !="":
        print(f"Sikeres bejelentkezés {email}!")
    elif jelszo == "":
        print("Sikertelen bejelentkezés (üres jelszó).")
    else:
        print("Sikertelen bejelentkezés (email címek nem egyeznek).")
        