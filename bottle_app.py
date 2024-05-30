
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run

from distribute import distribute, Worker


@route('/')
def calculate():
    distribution = distribute(1800, Worker(name="Jonathan", effort=10, coefficient=600))
    return distribution

application = default_app()

if __name__ == "__main__":
    run()
