    # ============================================================
    # SISTEMA DE CONTROL DE CALIFICACIONES
    # Archivo: sistema_estudiantes.py
    # Requisito: Python 3
    # ============================================================

import math


    # ============================================================
    # FASE 1. DEFINICIÓN DE LA CLASE ESTUDIANTE
    # ============================================================

class Estudiante:
        """
        Almacena los datos de un estudiante, valida sus
        calificaciones y calcula su promedio académico.
        """

        def __init__(self, nombre, matricula, calificaciones):

            # Validar el nombre.
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre no puede estar vacío.")

            # Validar la matrícula.
            if not isinstance(matricula, str) or not matricula.strip():
                raise ValueError("La matrícula no puede estar vacía.")

            # Validar que existan calificaciones.
            if not isinstance(calificaciones, (list, tuple)):
                raise ValueError("Las calificaciones deben ser una lista.")

            if len(calificaciones) == 0:
                raise ValueError(
                    "Debe registrar al menos una calificación."
                )

            # Validar todas las calificaciones.
            for nota in calificaciones:

                # Evitar valores booleanos y datos no numéricos.
                if isinstance(nota, bool) or not isinstance(
                    nota, (int, float)
                ):
                    raise ValueError(
                        "Las calificaciones deben ser numéricas."
                    )

                # Verificar que la nota sea finita y esté entre 0 y 100.
                if not math.isfinite(nota) or not 0 <= nota <= 100:
                    raise ValueError(
                        "Cada calificación debe estar entre 0 y 100."
                    )

            # Guardar los datos validados.
            self.__nombre = nombre.strip()
            self.__matricula = matricula.strip()
            self.__calificaciones = list(calificaciones)

        # ========================================================
        # FASE 2. MÉTODOS DE CONSULTA
        # ========================================================

        @property
        def nombre(self):
            return self.__nombre

        @property
        def matricula(self):
            return self.__matricula

        @property
        def calificaciones(self):
            # Devolver una copia para proteger los datos internos.
            return self.__calificaciones.copy()

        # ========================================================
        # FASE 3. CÁLCULO DEL PROMEDIO
        # ========================================================

        def calcular_promedio(self):
            return sum(self.__calificaciones) / len(
                self.__calificaciones
            )

        # ========================================================
        # FASE 4. DETERMINACIÓN DEL ESTADO ACADÉMICO
        # ========================================================

        def esta_aprobado(self):
            return self.calcular_promedio() >= 70

        # ========================================================
        # FASE 5. PRESENTACIÓN DEL REPORTE INDIVIDUAL
        # ========================================================

        def mostrar_datos(self):

            promedio = self.calcular_promedio()

            print("\n" + "=" * 45)
            print("          REPORTE DEL ESTUDIANTE")
            print("=" * 45)
            print(f"Nombre:         {self.nombre}")
            print(f"Matrícula:      {self.matricula}")
            print(f"Calificaciones: {self.calificaciones}")
            print(f"Promedio:       {promedio:.2f}")

            if self.esta_aprobado():
                print("Estado:         APROBADO")
            else:
                print("Estado:         REPROBADO")

            print("=" * 45)


    # ============================================================
    # FASE 6. FUNCIONES PARA CAPTURAR Y VALIDAR DATOS
    # ============================================================

def solicitar_texto(mensaje):
        """
        Solicita un texto no vacío.
        Repite la pregunta si el usuario no introduce información.
        """

        while True:
            valor = input(mensaje).strip()

            if valor:
                return valor

            print("Error: este campo no puede estar vacío.")


def solicitar_entero_positivo(mensaje):
        """
        Solicita un número entero mayor que cero.
        Controla entradas vacías, letras y números inválidos.
        """

        while True:
            entrada = input(mensaje).strip()

            try:
                numero = int(entrada)

                if numero > 0:
                    return numero

                print("Error: debe introducir un número mayor que cero.")

            except ValueError:
                print("Error: introduzca un número entero válido.")


def solicitar_calificacion(numero_nota):
        """
        Solicita una calificación numérica entre 0 y 100.
        Rechaza letras, valores fuera de rango, NaN e infinitos.
        """

        while True:
            entrada = input(
                f"Introduzca la calificación {numero_nota} (0-100): "
            ).strip()

            try:
                nota = float(entrada)

                if not math.isfinite(nota):
                    print("Error: introduzca un número finito.")
                    continue

                if 0 <= nota <= 100:
                    return nota

                print("Error: la calificación debe estar entre 0 y 100.")

            except ValueError:
                print("Error: introduzca una calificación numérica válida.")


def solicitar_confirmacion(mensaje):
        """
        Acepta únicamente las respuestas S o N.
        """

        while True:
            respuesta = input(mensaje).strip().casefold()

            if respuesta in ("s", "si", "sí"):
                return True

            if respuesta in ("n", "no"):
                return False

            print("Respuesta inválida. Escriba S para sí o N para no.")


    # ============================================================
    # FASE 7. REGISTRO DE VARIOS ESTUDIANTES
    # ============================================================

def registrar_estudiante(estudiantes):
        """
        Captura los datos de un estudiante.
        Comprueba que su matrícula no esté registrada.
        Añade el estudiante a la lista solo cuando los datos
        se han capturado y validado correctamente.
        """

        print("\n--- REGISTRO DE ESTUDIANTE ---")

        nombre = solicitar_texto("Nombre completo: ")

        # Validar que la matrícula no esté duplicada.
        while True:
            matricula = solicitar_texto("Matrícula: ")

            duplicada = any(
                estudiante.matricula.casefold() == matricula.casefold()
                for estudiante in estudiantes
            )

            if not duplicada:
                break

            print(
                "Error: esa matrícula ya está registrada. "
                "Introduzca otra."
            )

        # Preguntar cuántas calificaciones se registrarán.
        cantidad = solicitar_entero_positivo(
            "¿Cuántas calificaciones desea registrar? "
        )

        calificaciones = []

        # Capturar y validar cada calificación.
        for numero in range(1, cantidad + 1):
            nota = solicitar_calificacion(numero)
            calificaciones.append(nota)

        # Crear el objeto y añadirlo a la lista.
        estudiante = Estudiante(
            nombre,
            matricula,
            calificaciones
        )

        estudiantes.append(estudiante)

        print("\nEstudiante registrado correctamente.")

        # Mostrar el reporte inmediatamente.
        estudiante.mostrar_datos()


    # ============================================================
    # FASE 8. REPORTE GENERAL
    # ============================================================

def mostrar_reporte_general(estudiantes):
        """
        Presenta todos los estudiantes registrados y calcula
        las estadísticas generales del grupo.
        """

        print("\n" + "=" * 55)
        print("              REPORTE GENERAL")
        print("=" * 55)

        if not estudiantes:
            print("No hay estudiantes registrados.")
            print("=" * 55)
            return

        aprobados = 0
        reprobados = 0
        suma_promedios = 0.0

        # Recorrer a todos los estudiantes.
        for numero, estudiante in enumerate(estudiantes, start=1):

            promedio = estudiante.calcular_promedio()
            estado = (
                "APROBADO"
                if estudiante.esta_aprobado()
                else "REPROBADO"
            )

            print(f"\nEstudiante #{numero}")
            print(f"Nombre:    {estudiante.nombre}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Promedio:  {promedio:.2f}")
            print(f"Estado:    {estado}")

            suma_promedios += promedio

            if estudiante.esta_aprobado():
                aprobados += 1
            else:
                reprobados += 1

        # Calcular el promedio de los promedios individuales.
        promedio_grupal = suma_promedios / len(estudiantes)

        print("\n" + "-" * 55)
        print(f"Total de estudiantes: {len(estudiantes)}")
        print(f"Estudiantes aprobados: {aprobados}")
        print(f"Estudiantes reprobados: {reprobados}")
        print(f"Promedio de los promedios: {promedio_grupal:.2f}")
        print("=" * 55)


    # ============================================================
    # FASE 9. MENÚ PRINCIPAL
    # ============================================================

def main():
        """
        Controla el flujo de la aplicación y permite registrar
        varios estudiantes antes de finalizar.
        """

        estudiantes = []

        print("=" * 55)
        print(" SISTEMA DE CONTROL DE CALIFICACIONES")
        print("=" * 55)

        while True:

            print("\nMENÚ PRINCIPAL")
            print("1. Registrar estudiante")
            print("2. Mostrar reporte general")
            print("3. Salir")

            opcion = input("Seleccione una opción (1-3): ").strip()

            if opcion == "1":

                registrar_estudiante(estudiantes)

            elif opcion == "2":

                mostrar_reporte_general(estudiantes)

            elif opcion == "3":

                print("\nReporte final:")
                mostrar_reporte_general(estudiantes)
                print("\nPrograma finalizado correctamente.")
                break

            else:
                print(
                    "Opción inválida. Seleccione 1, 2 o 3."
                )


    # ============================================================
    # FASE 10. INICIO Y MANEJO DE INTERRUPCIONES
    # ============================================================

if __name__ == "__main__":

        try:
            main()

        except (KeyboardInterrupt, EOFError):
            # Permitir una salida controlada si se interrumpe
            # la entrada de datos desde el teclado.
            print("\n\nPrograma interrumpido por el usuario.")