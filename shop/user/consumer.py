from aiokafka import AIOKafkaConsumer
from json import loads
from config import settings, loop
from .schema import UserMutation

async def consume():
    consumer = AIOKafkaConsumer(settings.kafka_topic,
                                loop=loop,
                                bootstrap_servers=settings.kafka_bootstrap_server,
                                value_deserializer=loads)
    await consumer.start()
    try:
        async for msg in consumer:
            event = UserMutation(dictionary=msg.value)
            print(event)
    finally:
        await consumer.stop()
