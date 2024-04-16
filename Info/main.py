from ast import Return


print("hello word")
a=1
b=7
print("a+b=", a+b)
print("A=",a, "B=",b)


a="1"
b="7"
print("a+b=", a+b)
print("A=",a, "B=",b)

print(type(a))
print(type(a).__name__)

#verifica tipul de date
if type(a).__name__=="int" and type(b).__name__=="int":
    print("a+b=", a+b)
else:
    print("a+b=", int(a) + int(b))


#print(int("a"))

def check_type(a,b):
    if type(a).__name__=="int" and type(b).__name__=="int":
        return True
    else:
        return False
    
print(check_type(a,b))
#a=1
#b=7
print(check_type(a,b))
if check_type(a,b):
    print("a+b=", a+b)
else:
    print("nu sunt numere")

