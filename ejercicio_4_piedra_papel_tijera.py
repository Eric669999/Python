import random

print("--- PIEDRA, PAPEL O TIJERA ---")

# 1. El ordenador elige al azar
opciones = ["piedra", "papel", "tijera"]
maquina = random.choice(opciones)

# 2. El jugador elige
jugador = input("Elige (piedra, papel, tijera): ").lower()


print(f"Tú: {jugador}")
print(f"Máquina: {maquina}")

# --- AQUÍ EMPIEZA TU RETO ---

# 1. if: Comprueba si hay empate
if jugador == maquina:
    print("¡Empate!")
elif jugador == 'papel' and maquina == 'piedra':
    print('Has ganado')
elif jugador == 'tijeras' and maquina == 'papel':
    print('Has ganado')
elif jugador == 'papel' and maquina == 'tijeras':
    print('Ha ganado la maquina')
elif jugador == 'piedra' and maquina == 'tijeras':
    print('Has ganado')
else:
    print('Ha ganado la maquina')

# 2. elifs: Escribe un elif para cada forma en la que tú (el jugador) puedes ganar.
# Pista 1: Usa 'and' para comprobar tu jugada y la de la máquina a la vez.
# Pista 2: Necesitarás 3 elif en total.
# ¡Escribe tus elifs debajo de esta línea!



# 3. else: Si no ha sido empate, y tampoco has ganado tú en los elifs... ¡es que gana la máquina!
# Escribe el else debajo de esta línea (recuerda que el else no lleva condición):