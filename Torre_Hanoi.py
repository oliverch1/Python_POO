# Definir una función que recibe el número de discos y las varillas de origen, destino y auxiliar
def hanoi(n, origen, destino, auxiliar):
  # Si el número de discos es 1, mover el disco de origen a destino y mostrar el movimiento
  if n == 1:
    print(f"Mover el disco {n} de la varilla {origen} a la varilla {destino}")
  # Si el número de discos es mayor que 1, seguir los siguientes pasos:
  else:
    # Mover n-1 discos de origen a auxiliar, usando destino como varilla auxiliar
    hanoi(n-1, origen, auxiliar, destino)
    # Mover el disco n de origen a destino y mostrar el movimiento
    print(f"Mover el disco {n} de la varilla {origen} a la varilla {destino}")
    # Mover n-1 discos de auxiliar a destino, usando origen como varilla auxiliar
    hanoi(n-1, auxiliar, destino, origen)

# Pedir al usuario el número de discos
n = int(input("Ingrese el número de discos: "))
# Llamar a la función con el número de discos y las varillas A, B y C
hanoi(n, "A", "B", "C")
