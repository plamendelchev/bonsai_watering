from ucollections import namedtuple
from bonsai_watering import mqtt_client

from .devices import *
from .time import *
from .schedule import *
from .update import *

Route = namedtuple('Route', ['controller', 'topic'])
routes = []

def register_route(controller, topic):
    route = Route(controller, topic)
    routes.append(route)

def call(topic, message):
    route = next(route for route in routes if route.topic == topic)
    route.controller(message)
