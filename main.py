"""
Fichero principal del programa con la ejecución
"""
# Incluimos las funciones necesarias para los calculos, del archivo de lógica
from irpf_logic import calcular_retencion, generar_informe


def ejecutar_calculadora():
    """
    Función principal del programa para ejectura la calculadora IRPF
    """
    # Bucle para menú
    while True:
        # Mostramos menú
        print("+------------------------------+")
        print("| 💵 Calculadora de IRPF       |")
        print("+------------------------------+")
        print("| 1 - Realizar nuevo calculo   |")
        print("| 2 - Salir del programa       |")
        print("+------------------------------+\n")
        # Solictamos opción al usuario
        opcion = int(input("Seleccione una opción: "))
        print("")
        match opcion:
            case 1:
                bruto = float(input("Introduce tu sueldo bruto: "))
                retencion = calcular_retencion(bruto)
                informe = generar_informe(bruto, retencion)
                # Mostramos los datos formateados
                print("Resultados.")
                print(f" - Sueldo bruto: {bruto} €")
                print(f" - Impuesto a abonar: {retencion} €")
                print(f" - Sueldo Neto: {informe['sueldo_neto']} €")
                print(
                    f" - Porcentaje apliado: {informe['porcentaje_retencion']}%")
            case 2:
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("🛑 Opción no válida....")


if __name__ == "__main__":
    ejecutar_calculadora()
