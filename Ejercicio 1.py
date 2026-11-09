#Ejercicio 1 - Trabajo Práctico Final


# Punto A: Normalización de lecturas
def limpiar_registro_sensor(registro_raw):

    # Limpiar el identificador eliminando espacios
    sensor_id = registro_raw.get("sensor_id", "DESCONOCIDO")
    sensor_id = str(sensor_id).strip()

    # Obtener la temperatura y eliminar la unidad de medida
    temperatura_raw = registro_raw.get("temperatura", "0")
    temperatura_raw = str(temperatura_raw).strip()
    temperatura = float(
        temperatura_raw.replace("°C", "").replace("C", "").strip()
    )

    # Asignar una ubicación por defecto si no existe
    ubicacion = registro_raw.get("ubicacion") or "Ubicación no registrada"
    ubicacion = str(ubicacion).strip()

    # Retornar un nuevo diccionario estandarizado
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


# Punto B: Monitoreo y resumen estadístico
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []

    # Buscar sensores que superen el umbral
    for sensor in lista_sensores_limpios:
        if sensor["temperatura"] > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    # Calcular el promedio de temperatura
    if len(lista_sensores_limpios) > 0:
        suma_temperaturas = sum(
            sensor["temperatura"] for sensor in lista_sensores_limpios
        )
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0.0

    # Retornar una tupla con las alertas y el promedio
    return lista_sensores_alerta, promedio_temperatura


# BLOQUE PRINCIPAL DE EJECUCIÓN

# Registros crudos recibidos de los sensores
registros_crudos = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": " SENSOR-002 ",
        "temperatura": "38.7°C",
        "ubicacion": "Planta Sur"
    },
    {
        "sensor_id": " SENSOR-003 ",
        "temperatura": "29.2C",
        "ubicacion": "Planta Este"
    },
    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "42.5°C",
        "ubicacion": ""
    }
]

# Limpiar los registros
sensores_limpios = []

for registro in registros_crudos:
    sensor_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(sensor_limpio)

# Definir el umbral máximo permitido
umbral = 35.0

# Generar el reporte estadístico
alertas, promedio = generar_resumen_sensores(
    sensores_limpios,
    umbral
)

# IMPRESIÓN DEL REPORTE FINAL

print("\nLECTURAS NORMALIZADAS:")

for sensor in sensores_limpios:
    print(
        f"ID: {sensor['sensor_id']} | "
        f"Temperatura: {sensor['temperatura']:.2f} °C | "
        f"Ubicación: {sensor['ubicacion']}"
    )

print("\n--------------------------------------")
print(f"Umbral de temperatura: {umbral:.2f} °C")
print(f"Promedio térmico global: {promedio:.2f} °C")

print("\nSENSORES EN ALERTA:")

if alertas:
    for sensor_id in alertas:
        print(f"¡ALERTA! El sensor {sensor_id} superó el umbral.")
else:
    print("No se detectaron temperaturas fuera del límite.")

print("FIN DEL REPORTE")


