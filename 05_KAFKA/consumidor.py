from kafka import KafkaConsumer

# Consumidor suscrito al tópico 'tema1'
consumer = KafkaConsumer(
    'tema1',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: m.decode('utf-8')
)

print("[Consumidor] Esperando mensajes en el tópico 'tema1'...")
for mensaje in consumer:
    print(f"[Consumidor] Mensaje recibido: {mensaje.value}")
