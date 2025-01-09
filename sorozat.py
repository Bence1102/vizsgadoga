import random
def sor():
    print("II/A,B,C:")
    szamok=[]
    for _ in range(5):
        veletlenszam =random.randint(10,20)   
        szamok.append(veletlenszam)
    
    for i in range(5):
        if i > 0:
            print("-", end="")
        print(szamok[i], end="")
    print()  


def kisebb(szamok):
    print("II/D:")
    count = 0
    for i in range(1, len(szamok)):
        if szamok[i] > szamok[i-1]:  
            count += 1
    return count

def konzolba_ir(szamok):
    print("II/E:")
    eredmeny = kisebb(szamok)  
    print(f"A kisebb függvény eredménye: {eredmeny}")

def fajlba_ir(szamok):
    print("II/F:")
    eredmeny = kisebb(szamok)  
    with open("vegeredmeny.txt", "w") as file:
        file.write(f"A kisebb függvény eredménye: {eredmeny}\n")




    


    