import os
import pandas as pd

def buscar_dato_excel(base_path, year_month, dia, dni_buscado):
    """
    Busca un archivo Excel en una estructura de carpetas basada en año, mes y día, y extrae información de un DNI específico.

    :param base_path: Ruta base donde se encuentra la carpeta 'trabajo 1'.
    :param year_month: Año en formato 'YYYY' (por ejemplo, '2020').
    :param dia: El nombre del archivo, que corresponde al día (nombre del archivo de Excel).
    :param dni_buscado: DNI que se desea buscar en el archivo.
    """
    try:
        # Desglosar el año y mes
        year = year_month.split("-")[0]
        mes_nombre = year_month.split("-")[1].lower()

        # Lista de meses en español
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        
        # Verificar si el mes es válido
        if mes_nombre not in meses:
            print(f"Mes inválido: {mes_nombre}. Por favor ingrese un mes válido.")
            return

        # Ruta de la carpeta para el año y mes
        ruta_carpeta = os.path.join(base_path, year, mes_nombre)
        
        # Verificar si la ruta del año y mes existe
        if not os.path.exists(ruta_carpeta):
            print(f"No se encontró la carpeta para la fecha {year}-{mes_nombre}.")
            return
        
        # Buscar el archivo Excel dentro de la carpeta del mes con el nombre de día
        archivo_excel = f"{dia}.xlsx"
        ruta_archivo = os.path.join(ruta_carpeta, archivo_excel)
        
        # Verificar si el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"No se encontró el archivo {archivo_excel} en la carpeta {ruta_carpeta}.")
            return

        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo)
        
        # Limpiar los espacios y convertir los DNI en el archivo a texto
        df['DNI'] = df['DNI'].astype(str).str.strip()
        dni_buscado = str(dni_buscado).strip()

        # Buscar el DNI en el archivo
        fila = df[df['DNI'] == dni_buscado]

        if fila.empty:
            print(f"No se encontró el DNI {dni_buscado} en el archivo {archivo_excel}.")
        else:
            # Extraer los datos específicos
            nombres = fila.iloc[0].get('APELLIDOS Y NOMBRES', 'No disponible')
            telefono = fila.iloc[0].get('CELULAR', 'No disponible')
            direccion = fila.iloc[0].get('DIRECCIÓN', 'No disponible')
            fecha_nacimiento = fila.iloc[0].get('FECHA DE NACIMIENTO', 'No disponible')
            edad = fila.iloc[0].get('EDAD ACTUAL', 'No disponible')

            print(f"Resultados encontrados para el DNI {dni_buscado} en el archivo {archivo_excel}:")
            print(f"- Apellidos y Nombres: {nombres}")
            print(f"- Teléfono: {telefono}")
            print(f"- Dirección: {direccion}")
            print(f"- Fecha de Nacimiento: {fecha_nacimiento}")
            print(f"- Edad: {edad}")

    except Exception as e:
        print(f"Error: {e}")


# Datos de entrada
base_path = input("Ingrese la ruta base donde se encuentra la carpeta 'trabajo 1': ")
year_month = input("Ingrese el año y mes (AAAA-mes): ")  # Año y mes en formato 'YYYY-mes' (por ejemplo, '2020-enero')
dia = input("Ingrese el día: ")  # Día (nombre del archivo de Excel)
dni_buscado = input("Ingrese el DNI que desea buscar: ")  # DNI a buscar

# Ejecutar la función
buscar_dato_excel(base_path, year_month, dia, dni_buscado)
