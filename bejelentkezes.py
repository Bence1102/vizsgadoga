def fel1():
    print("I/A,B,C:")
    email:str=str(input("Add meg az email címed:"))
    emailujra:str=str(input("Add meg az email címed újra:"))
    jelszo:str=str(input("Add meg a jelszavad:"))
    if email==emailujra and len(jelszo)>= 6:
        print(f"Sikeres bejelntkezés: {email}!")
    elif len(jelszo)<6:
        print("Sikertelen bejelntkezés(üres jelszó!)")
    else:
        print("Sikertelen bejelntkezés, email címek nem egyeznek!")