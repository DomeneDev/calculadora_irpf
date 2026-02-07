"""
Fichero principal del programa con la ejecución
"""
# Incluimos las funciones necesarias para los calculos, del archivo de lógica
from irpf_logic import calcular_retencion, generar_informe
from utils import mostrar_menu, validacion_dato_opcion, validacion_dato, mostrar_resultados

# ---- CONTSTANTES DE INPUTS ----
INPUT_OPCION = "Seleccione una opción: "
INPUT_SALARIO = "Introduce tu sueldo bruto: "

# ---- CONSTANTES DE ERROR ----
ERROR_OPCION = "🛑 Opción no válida, debe ser un número entero"
ERROR_SALARIO_NEG = "🛑 El suelo no puede ser negativo"
ERROR_SALARIO_DATO = "🛑 Error debe introducir un valor válido.."


def ejecutar_calculadora():
    """
    Función principal del programa para ejectura la calculadora IRPF
    """
    # Bucle para menú
    while True:
        # Mostramos menú
        mostrar_menu()
        # Solictamos opción al usuario
        opcion = validacion_dato_opcion(INPUT_OPCION, ERROR_OPCION)
        match opcion:
            case 1:
                bruto = validacion_dato(
                    INPUT_SALARIO, ERROR_SALARIO_NEG, ERROR_SALARIO_DATO)
                retencion = calcular_retencion(bruto)
                informe = generar_informe(bruto, retencion)
                # Mostramos los datos formateados
                mostrar_resultados(bruto, retencion, informe)
            case 2:
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("🛑 Opción no válida....")


if __name__ == "__main__":
    ejecutar_calculadora()
