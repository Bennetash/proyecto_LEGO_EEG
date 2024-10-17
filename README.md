🚀 Proyecto LEGO EEG Control 🎮🧠

¡Bienvenido/a al Proyecto LEGO EEG Control! 🎉 Este proyecto utiliza señales cerebrales capturadas por ArduEEG para controlar un vehículo LEGO Technic a través de comandos enviados por Bluetooth. ¡Increíble, verdad? 🤯
🧠 ¿Qué hace este proyecto?

El proyecto usa un modelo de Red Neuronal Profunda (DNN) 🧑‍💻 entrenado con datos EEG para predecir acciones. Dependiendo de los datos cerebrales recibidos, el sistema puede controlar el vehículo LEGO, realizando acciones como:

    Avanzar 🚗
    Retroceder 🔙
    Parar 🛑
    Girar a la izquierda ⬅️
    Girar a la derecha ➡️

🛠️ Estructura del Proyecto

Este es un vistazo a los archivos y directorios del proyecto:

graphql

proyecto_LEGO_EEG/
│
├── captura_eeg.py          # Captura y procesa las señales EEG en tiempo real
├── control_bluetooth.py    # Controla el LEGO Technic via Bluetooth
├── main.py                 # Script principal que integra todo
├── modelo_dnn_eeg.h5       # Modelo de Red Neuronal entrenado
├── requisitos.txt          # Dependencias necesarias para ejecutar el proyecto

🧑‍💻 Cómo Ejecutar el Proyecto
1. 🧱 Clona el Repositorio

Primero, clona el repositorio en tu máquina:

bash

git clone https://github.com/tu-usuario/proyecto_LEGO_EEG.git
cd proyecto_LEGO_EEG

2. 🛠️ Instala las Dependencias

Instala las dependencias necesarias (usa un entorno virtual para aislar el proyecto):

bash

pip install -r requisitos.txt

3. 🎮 Conecta el LEGO Technic

Asegúrate de tener encendido tu LEGO Technic Hub y de que está visible vía Bluetooth. Luego, corre el archivo main.py:

bash

python main.py

¡Y listo! 🎉 El sistema comenzará a recibir tus señales cerebrales y controlará el LEGO según tus pensamientos.
📦 Dependencias

    TensorFlow 🧠: Para el modelo de red neuronal.
    Bleak 📡: Para la conexión Bluetooth.
    NumPy ➗: Para el manejo de los datos.
    SciPy 🧪: Para el filtrado de señales EEG.
    Socket 📡: Para la conexión con el ArduEEG vía UDP.

🔮 Futuras Mejoras

    🚀 Optimizar el modelo DNN para un tiempo de respuesta más rápido.
    🤖 Añadir más comandos para movimientos avanzados del LEGO.
    🌐 Crear una interfaz web para monitorear en tiempo real los comandos enviados al LEGO.

🧑‍🏫 Contribuciones

¡Las contribuciones son siempre bienvenidas! Si tienes alguna mejora, idea o corrección, por favor crea un pull request o abre un issue.
✨ Créditos

Este proyecto fue inspirado en la unión de Inteligencia Artificial y Control Mental 🤯 con un toque de creatividad para hacer del control de un LEGO Technic algo totalmente revolucionario 🚀.

Espero que disfrutes tanto este proyecto como nosotros disfrutamos desarrollarlo. ¡Vamos a construir el futuro, un pensamiento a la vez! 🧠✨
