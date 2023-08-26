import logging

import pika
from pbroker import rabbitmq as proxies

import config
import event
import utils


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():

    # RabbitMQ connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=config.AREPORT_BROKER_HOST,
            port=config.AREPORT_BROKER_PORT
        )
    )
    channel = utils.get_channel(connection)

    # Rabbitmq subscriber for new report file events
    new_file_subscriber = proxies.RabbitMQTopicSubscriber(
        channel,
        config.AREPORT_BROKER_EXCHANGE,
        proxies.RabbitMQTopicQueue(channel, exclusive=True),
        config.AREPORT_BROKER_TOPIC_NEW_DATA,
        auto_ack=True
    )

    # Listen new report file events, extract and pusblish data to rabbitmq
    subject = event.Subject([
        event.SomeObserver()
    ])
    new_file_subscriber.consume(
        callback=utils.notify(utils.rabbitmq_data, subject),
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    main()
