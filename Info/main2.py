#par si impar

#impartire cu cat si rest
# // -> cat
# % -> rest
# / -> impartire cu float - nr cu virgula

#functie de verificare par si impar

def check_even(a):
    if(a%2 == 0):
        return True
    else:
        return False
print(check_even(3))


#print nr 1
global nr
nr=50
def mod_nr():
    
    nr=2
mod_nr()
print(nr)


#print nr 2
global nr2
nr2=50
def mod_nr_global():
    global nr2
    nr2=2
mod_nr_global()
print(nr2)

#nr de incercari
global pinok
pinok = 1234
def check_pin():
    global pinok
    print(type(pinok))
    while int(input("introdu pin")) != pinok:
          print("PIN GRESIT")
check_pin()

x = "1234567"
x[6]
x_len = len(x)
print(x_len)