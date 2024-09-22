from aiokafka import AIOKafkaConsumer
from json import loads
from config import settings, loop
from user.schema import UserMutation
from user.event_handler import handle

async def consume():
    consumer = AIOKafkaConsumer(settings.kafka_topic,
                                loop=loop,
                                bootstrap_servers=settings.kafka_bootstrap_server,
                                value_deserializer=loads)
    await consumer.start()
    try:
        async for msg in consumer:
            msg.value["event_type"] = msg.value.pop("eventType")
            event = UserMutation.model_validate(msg.value)
            handle(event)
    finally:
        await consumer.stop()
