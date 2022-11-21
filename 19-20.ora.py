"""
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!, Hello, Hello,"
print(a)
uj_string = a.replace("Hello, World!, Hello, Hello,", "XXXX")
print("a régi sztring" +" " + a)
print("a régi sztring",a, sep = " ")
print("az uj " + uj_string)

a = "Hello"
b = "World"
space = " "
felkialtojel = "!"
c = a + space + b + felkialtojel + space + a + space + b + felkialtojel 
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1},"
print(myorder.format(quantity, itemno, price)) 

print("10.D osztály 1. csoport", end='\n')
print("10.D osztály 1. csoport", end='\t\t\t')
print("10.D osztály 1. csoport",)
"""
b = "Hello World!"

print(b[-5:-2]) #orl
print(b[-5:-1]) #orld
print(b[-1]) #!









