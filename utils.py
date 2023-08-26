import json
import logging
from typing import Any

import config


logging.basicConfig(level=logging.INFO)


def get_channel(connection):
    channel = connection.channel()
    channel.exchange_declare(
        exchange=config.AREPORT_BROKER_EXCHANGE,
        exchange_type='topic'
    )

    return channel


def notify(fn, subject):
    def inner(*args, **kwargs):
        data = fn(*args, **kwargs)
        logging.info(f'New data: {data}')
        subject.notify(data)

    return inner


def rabbitmq_data(ch, method, properties, body):
    return json.loads(body)
