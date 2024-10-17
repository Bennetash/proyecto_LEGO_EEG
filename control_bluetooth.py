import asyncio
from bleak import BleakClient

# Actualiza con la dirección MAC del Technic Hub
LEGO_MAC_ADDRESS = "90:84:2B:70:69:6D"

# UUID del servicio principal y de las características
LEGO_SERVICE_UUID = "00001623-1212-efde-1623-785feabcd123"
LEGO_CHARACTERISTIC_UUID = "00001624-1212-efde-1623-785feabcd123"  # Característica para enviar comandos

# Función para conectar al LEGO Technic via Bluetooth
async def conectar_lego():
    client = BleakClient(LEGO_MAC_ADDRESS)
    await client.connect()
    print("Conectado a LEGO Technic Hub!")
    return client

# Función para enviar comandos al LEGO
async def enviar_comando_lego(client, comando):
    comandos_bytes = {
        "avanzar": b'\x01\x02\x03',  # Comando para avanzar (ajústalo según la especificación del Technic Hub)
        "retroceder": b'\x04\x05\x06',  # Comando para retroceder
        "parar": b'\x07\x08\x09',  # Comando para parar
        "doblar izquierda": b'\x0A\x0B\x0C',  # Comando para doblar a la izquierda
        "doblar derecha": b'\x0D\x0E\x0F'  # Comando para doblar a la derecha
    }

    if comando in comandos_bytes:
        await client.write_gatt_char(LEGO_CHARACTERISTIC_UUID, comandos_bytes[comando])
        print(f"Comando enviado: {comando}")
    else:
        print(f"Comando desconocido: {comando}")

# Función para desconectar
async def desconectar_lego(client):
    await client.disconnect()
    print("Desconectado del LEGO Technic Hub")