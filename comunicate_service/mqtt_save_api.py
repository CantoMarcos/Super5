import paho.mqtt.client as mqtt
import requests
import time
from utils.env import get_environment_config


config = get_environment_config()

URL = config.get('BACKEND_URL')

# Configurações MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "Marcos/sensor"

# Configuração do endpoint da API
API_URL = f'{URL}/sensores/create_sensor_data'  # Atualize com o URL correto da API

# Variável para armazenar o último valor
last_values = None

# Função para enviar dados para a API
def send_to_api(values):
    payload = {
        "sensor1": values[0],
        "sensor2": values[1],
        "sensor3": values[2],
        "sensor4": values[3],
        "sensor5": values[4]
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            print(f"Dados enviados com sucesso: {payload}")
        else:
            print(f"Erro ao enviar dados: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

# Callback de conexão
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker com código: {rc}")
    client.subscribe(TOPIC)

# Callback de mensagens
def on_message(client, userdata, msg):
    global last_values
    try:
        # Converte a mensagem para float
        current_values = list(map(float, msg.payload.decode().split(",")))

        # Verifica se os valores mudaram
        if last_values != current_values:
            print(f"Novos valores recebidos: {current_values}")
            send_to_api(current_values)  # Envia os dados para a API
            last_values = current_values
    except ValueError:
        print("Erro ao converter mensagem em float.")

# Configura o cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker
client.connect(BROKER, PORT, 60)

# Loop principal
try:
    client.loop_start()
    while True:
        time.sleep(120)  # Aguarda 2 minutos
except KeyboardInterrupt:
    print("Finalizando...")
    client.loop_stop()
    client.disconnect()
