import numpy as np
import socket
from scipy import signal

# Configuración de la conexión UDP
UDP_IP = "192.168.1.30"  # Dirección IP del ArduEEG
UDP_PORT = 13900         # Puerto configurado en el ArduEEG
data_length = 1350
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Parámetros del procesamiento de la señal
sample_lens = 50
fps = 250  # Frecuencia de muestreo
highcut = 8
lowcut = 12
data_test = 0x7FFFFF
data_check = 0xFFFFFF

# Filtrado de señales
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

# Función principal para capturar datos EEG
def capturar_datos_eeg():
    result = data_length * [0]
    channels = [[] for _ in range(8)]  # Ocho canales EEG
    data_before = [[0]*sample_lens for _ in range(8)]  # Datos previos para suavizado

    # Recepción de datos desde el ArduEEG
    data, addr = sock.recvfrom(data_length)
    data_list = [byte for byte in data]
    output = data_list

    for c in range(0, data_length, 27):
        for a in range(0, 24, 3):
            voltage_1 = (output[a+c] << 8) | output[a+1+c]
            voltage_1 = (voltage_1 << 8) | output[a+2+c]

            convert_voltage = voltage_1 | data_test

            if convert_voltage == data_check:
                voltage_1_after_convert = (16777214 - voltage_1)
            else:
                voltage_1_after_convert = voltage_1
            channel_num = int(a / 3)
            result[channel_num] = round(1000000 * 4.5 * (voltage_1_after_convert / 16777215), 2)

        # Añadir los datos al canal correspondiente
        for i in range(8):
            channels[i].append(result[i])

        # Filtrar los datos cuando haya suficientes muestras
        if len(channels[0]) == sample_lens:
            data_filt_high = butter_highpass_filter(channels[0], highcut, fps)
            data_filt_low = butter_lowpass_filter(data_filt_high, lowcut, fps)
            
            # Retornar solo los últimos datos procesados para predicción
            return np.array([data_filt_low[-sample_lens:]])  # Última ventana filtrada
