def fun_account (account):
    print( "Sold disponibil", account )
    while account > 0:
        Ex = int(input("Ce suma scoti?"))
        # account = account - Ex (acelasi lucru)
        account -= Ex
        if account < 0: 
            print("Nu ai destui bani")
        elif account == 0:
            print("Ai ramas pe 0")
        else:
            print( "Sold disponibil", account )



# fun_account(2000)

def bancomat_limitat(suma_totala, limita):
    print("Suma ramasa:", suma_totala)
    sum_de_extras = int(input("Cat doresti sa scoti?"))
    for step in range(limita):
        if suma_totala - sum_de_extras > 0:
            suma_totala -= sum_de_extras
            print("Suma ramasa:", suma_totala)
            sum_de_extras = int(input("Cat doresti sa scoti?"))
        else:
            print("Ai ramas fara bani")
            break
# bancomat_limitat(4000,3)

# cuvant = "abcdef"

# for step in range(len(cuvant)):
#     print(step, cuvant[step])

# txt = "welcome to the jungle"
# x = txt.split()
# print(x,x[0])

#Lista de cumparaturi
QT_B = [10, 3, 6, 8, 2]
P_P = [10, 2, 4, 6, 4]
M_Q = [100, 20, 20, 50, 70]
def fun_list(QT_B, P_P, M_Q):
    assert len(QT_B) == len(P_P) == len(M_Q), "Nu putem procesa deoarece datele sunt invalide"



fun_list(QT_B, P_P, M_Q)


try: 
    a = 1
    print(a/0)
except Exception as err:  
    print(err)
finally:
    print("Executam de fiecare data")

print("SUNT VIU")