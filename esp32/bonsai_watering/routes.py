from ucollections import namedtuple

Route = namedtuple('Route', ['controller', 'topic', 'response_topic'])
routes = []

def register_route(controller, topic, response_topic=None):
    route = Route(controller, topic, response_topic)
    routes.append(route)

def run_controller(topic, message):
    route = next(route for route in routes if route.topic == topic)
    route.controller(topic, message, route.response_topic)

def topics():
    return [route.topic for route in routes]
