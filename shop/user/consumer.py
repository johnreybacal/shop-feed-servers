from aiokafka import AIOKafkaConsumer
from json import loads
from config import settings, loop

async def consume():
    print(settings.kafka_topic)
    print(settings.kafka_bootstrap_server)
    consumer = AIOKafkaConsumer(settings.kafka_topic,
                                loop=loop,
                                bootstrap_servers=settings.kafka_bootstrap_server)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f'Consumer msg: {msg}')
    finally:
        await consumer.stop()
