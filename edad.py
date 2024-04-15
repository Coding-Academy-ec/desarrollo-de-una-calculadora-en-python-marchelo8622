import datetime

anio = int(input("Ingrese año:"))

anio_actual = datetime.datetime.now().year

anio_actual = anio_actual - anio

print("Edad:",anio_actual)

