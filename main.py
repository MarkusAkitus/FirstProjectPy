def parell(n):
    return n % 2 == 0

def primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# --- Programa principal ---
try:
    num = int(input("Escriu un nombre enter positiu: "))

    # Parell o imparell
    if parell(num):
        print(f"{num} És un nombre PARELL.")
    else:
        print(f"{num} És un nombre IMPARELL.")

    # Primer o no
    if primer(num):
        print(f"{num} És un nombre primer.")
    else:
        print(f"{num} NO és un nombre primer.")

    # Divisors
    divisors = divisors(num)
    print(f"Té {len(divisors)} divisors: {divisors}")

except ValueError:
    print("Has d'escriure un nombre enter vàlid.")