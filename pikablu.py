import pika

def callback(ch, method, properties, body):
    data = json.loads(body)
    if 'location' in data:
        print(f"Data enriched with location: {data['location']}")
        # Trigger next task based on enriched data
        trigger_next_task(data)

def trigger_next_task(data):
    # Example: Triggering another automated task based on enriched data
    print(f"Triggering task for {data['location']}")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-service'))
channel = connection.channel()

channel.queue_declare(queue='data_enriched')

channel.basic_consume(queue='data_enriched', on_message_callback=callback, auto_ack=True)

print('Waiting for data. To exit press CTRL+C')
channel.start_consuming()