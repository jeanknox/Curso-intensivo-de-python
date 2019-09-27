with open("pi_digits.txt","r") as pi:
    texto = (i for i in pi)
    print(pi.read())
    print(texto)
