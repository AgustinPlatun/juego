import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
failures = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

#Menu selector de niveles
print("¡Bienvenido al juego de adivinanzas!")
print("Ingresar que nivel desea jugar:")
print("Ingresar 1 para el nivel FACIL")
print("Ingresar 2 para el nivel INTERMEDIO")
print("Ingresar 3 para el nivel DIFICIL")
nivel = int(input("Ingresar nivel: "))

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
if nivel== 1:
    guessed_letters = ["a","e","i","o","u","á","é","í","ó","ú"]
    letters = []
    for i in secret_word:
        if i in guessed_letters:
            letters.append(i)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
elif nivel == 2:
    word_displayed =secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
elif nivel == 3:
    word_displayed ="_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while failures != 5:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word and letter != "":
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures += 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    if nivel == 2:
        letters.pop(0)
        letters.pop(-1)
        letters.insert(0,secret_word[0])
        letters.append(secret_word[-1])
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
    else:
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
    

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado los {failures} fallos.")
    print(f"La palabra secreta era: {secret_word}")