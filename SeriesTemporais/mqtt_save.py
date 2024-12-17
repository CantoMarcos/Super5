import paho.mqtt.client as mqtt
import csv
import time

# Configurações MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "Marcos/sensor"

# Variável para armazenar o último valor
last_values = None

# Nome do arquivo CSV
CSV_FILE = "dados_mqtt.csv"

# Função para salvar no CSV
def save_to_csv(values):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S")] + values)

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
            save_to_csv(current_values)
            last_values = current_values
    except ValueError:
        print("Erro ao converter mensagem em float.")

# Configura o cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker
client.connect(BROKER, PORT, 60)

# Inicializa o arquivo CSV com cabeçalhos, se ainda não existir
try:
    with open(CSV_FILE, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Sensor1", "Sensor2", "Sensor3", "Sensor4", "Sensor5"])
except FileExistsError:
    pass

# Loop principal
try:
    client.loop_start()
    while True:
        time.sleep(120)  # Aguarda 2 minutos
except KeyboardInterrupt:
    print("Finalizando...")
    client.loop_stop()
    client.disconnect()
