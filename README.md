# Report scraping

Observe new report files notified from a message broker,
read the file, extract useful data and publish it to a message broker.

## Setup
### Python dependecies

Create a virtual environment and install python dependencies.

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements/base.txt
```

### Environment variables
Set the following environment variables

**AREPORT_BROKER_HOST** default to *localhost*

**AREPORT_BROKER_PORT** default to *5672*

**AREPORT_BROKER_EXCHANGE** default to *scraping*

**AREPORT_BROKER_TOPIC_NEW_FILE** default to *file.new*

**AREPORT_BROKER_TOPIC_NEW_DATA** defult to *data.new*
