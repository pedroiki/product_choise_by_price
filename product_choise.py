
a = int(input("Digite o valor do produto 1: ")) 
b = int(input("Digite o valor do produto 2: "))
c = int(input("Digite o valor do produto 3: "))

#Sei que está correto, pois cada variável apareceu 2x

if a>b and a>c and b>c:
    print("Compre o produto de valor {}".format(c))
elif a>b and a>c and c>b:
    print("Compre o produto de valor {}".format(b))
elif b>a and b>c and c>a:
    print("Compre o produto de valor {}".format(a))
elif b>a and b>c and a>c:
    print("Compre o produto de valor {}".format(c))
elif c>a and c>b and b>a:
    print("Compre o produto de valor {}".format(a))
else:
    print("Compre o produto de valor {}".format(b))
