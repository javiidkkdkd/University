#javier fuentes

def resolver_ec(a,b,c):
    if a == 0:
        print("A tiene que ser distinto de 0")
        return None
    x = (c-b)/a
    return x

def main():
    a = int(input("Ingrese el valor a: "))
    b = int(input("ingrese el valor b: "))
    c = int(input("ingrese el valor c: "))
    x = resolver_ec(a,b,c)
    if x is not None:
        print("El valor de 'x' es:", x)
    
if __name__ == "__main__":
    main()
    