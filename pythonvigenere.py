abecedario = "abcdefghijklmnopqrstuvwxyz"

print("\nMenu")
print("1. Cifrar")
print("2. Descifrar")
opcion = input("Opcion: (1 o 2): ")

texto = input("\nIngresa tu texto: ").lower()
clave = input("Ingresa la clave: ").lower()

resultado = ""
indice_clave = 0

for letra in texto:

    if letra in abecedario:
        pos_texto = abecedario.index(letra)
        pos_clave = abecedario.index(clave[indice_clave % len(clave)])

        if opcion == "1":
            nueva_pos = (pos_texto + pos_clave) % len(abecedario)
        else:
            nueva_pos = (pos_texto - pos_clave) % len(abecedario)

        resultado += abecedario[nueva_pos]
        indice_clave += 1

    else:
        resultado += letra

print("\nResultado final:", resultado)