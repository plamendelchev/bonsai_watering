from ucollections import namedtuple

from .devices import *
from .time import *
from .schedule import *
from .update import *

Route = namedtuple('Route', ['controller', 'topic', 'response_topic'])
routes = []

def register_route(controller, topic, response_topic):
    route = Route(controller, topic, response_topic)
    routes.append(route)

def call(topic, message):
    route = next(route for route in routes if route.topic == topic)
    route.controller(topic, message, route.response_topic)
