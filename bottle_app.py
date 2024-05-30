
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, view, request

from distribute import distribute, Worker


@route("/")
@view("index")
def index():
    return { }


@route('/distribute', method="POST")
def distribute_controller():
    names = [request.POST.name1, request.POST.name2, request.POST.name3, request.POST.name4, request.POST.name5,]
    workers = [Worker(name=name, effort=10, coefficient=600) for name in names if name != ""]
    distribution = distribute(int(request.POST.budget), *workers)
    return distribution

application = default_app()

if __name__ == "__main__":
    run(reloader=True)
