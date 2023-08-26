import json
import logging


class Subject:
    def __init__(self, observers):
        self.observers = observers

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class SomeObserver:
    def update(self, data):
        print(data)


class DataExtractedNotify:
    def __init__(self, parser, publisher):
        self.publisher = publisher
        self.parser = parser

    def update(self, data):
        path = data['path']

        with open(path) as f:
            content = f.read()
            info = self.parser.parse(content)
            logging.info(f'Extracted info: {info}')

        self.publisher.publish(json.dumps(info))
        logging.info(f'Published data to broker')
