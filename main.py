from funciones.triangulo import leer_base_altura, calcular_area, mostrar_area
from funciones.pago_semanal import leer_horas_tarifa, calcular_pago, mostrar_pago
from funciones.conversion_tiempo import leer_segundos, convertir_tiempo, mostrar_tiempo

def main():
    # Llamar a las funciones del módulo triangulo
    leer_base_altura()
    calcular_area()
    mostrar_area()

    # Llamar a las funciones del módulo pago_semanal
    leer_horas_tarifa()
    calcular_pago()
    mostrar_pago()

    # Llamar a las funciones del módulo conversion_tiempo
    leer_segundos()
    convertir_tiempo()
    mostrar_tiempo()

def main():
    pass

if __name__ == "__main__":
    main()