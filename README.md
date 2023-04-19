# Simple Example

## Example description
In this simple example, `writer.py` periodically publishes data for a
*Square* topic, and `reader.py` subscribes to the topic and prints all the
data samples it receives.

## Running the example

Run the following commands in different shells:

    $ python reader.py
    $ python writer.py

You can run these commands in any order, and you can run multiple instances of
the writer and the reader. You can also run any other *DDS* application that
publishes or subscribes to the *Square* topic. For example, you can use
[RTI Shapes Demo](https://www.rti.com/free-trial/shapes-demo).


## Run in docker
build
    $ docker build -t rti-app .
    $ docker run --rm --network=bridge -it rti-app python3 sensor.py 1
    $ docker run --rm --network=bridge -it rti-app python3 central_server.py
    $ docker run --rm --network=bridge -it rti-app python3 healthcare_provider.py 1
    $ docker run --rm --network=bridge -it rti-app python3 select_records.py