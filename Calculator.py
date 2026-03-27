def add(x, y):
    return x + y

def subtrack(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sqrt(x):
    return x ** 0.5

print("Επιλεξε την πραξη που θελεις να εκτελεσεις:")
print("1. Πρόσθεση")
print("2. Αφαίρεση")
print("3. Πολλαπλασιασμός")
print("4. Διαίρεση")
print("5. Τετραγωνική ρίζα")

choise = input("Επίλεξε την πράξη (1/2/3/4/5):")

num1 = float(input("Εισαγωγή πρώτου αριθμού : "))
num2 = float(input("Εισαγωγή δεύτερου αριθμού : "))

if choise == "1":
    print("Το αποτέλεσμα είναι:", add(num1, num2))
elif choise == "2":
    print("Το αποτέλεσμα είναι:", subtrack(num1, num2))
elif choise == "3":
    print("Το αποτέλεσμα είναι:", multiply(num1, num2))
elif choise == "4":
    print("Το αποτέλεσμα είναι:", divide(num1,num2))        
elif choise == "5":
    print("Το αποτέλεσμα είναι:", sqrt(num1))
else:
    print("Mή έγκυρη επιλογή")                 