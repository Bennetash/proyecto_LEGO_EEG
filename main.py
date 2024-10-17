import asyncio
import numpy as np
from tensorflow.keras.models import load_model
from captura_eeg import captura_datos_eeg
from control_bluetooth import conectar_lego, enviar_comando_lego

# Cargar el modelo entrenado
modelo = load_model('modelo_dnn_eeg.h5')

# Funcion para hacer la prediccion de EEG
def predecir_accion(datos_eeg):
    prediccion = modelo.predict(datos_eeg)
    cluster = np.argmax(prediccion)
    return cluster

# Funcion para mapear el cluster a una accion
def mapear_accion(cluster):
    acciones = {0: "Avanzar", 1: "Retroceder", 2: "parar", 3: "doblar izquierda", 4: "doblar derecha"}
    return acciones.get(cluster, "Estado desconocido")

# Funcion principal para controlar el LEGO basado en EEG
async def controlar_lego():
    client = await conectar_lego()

    while True:
        # Captura los datos del EEG
        datos_eeg = captura_datos_eeg()
        # Predecir la accion con el modelo DNN
        cluster = predecir_accion(datos_eeg)
        accion = mapear_accion(cluster)
        # Enviar el comando al LEGO
        await enviar_comando_lego(client, accion)
        #Pausar antes de la siguiente captura
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(controlar_lego())