
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, view, request

from distribute import distribute, Worker


@route("/")
@view("index")
def index():
    return { }


@route('/distribute', method="POST")
def distribute_controller():
    names = request.forms.getall('names')
    amounts = request.forms.getall('amounts')
    days = request.forms.getall('days')

    workers = [Worker(name=names[i], effort=int(days[i]), coefficient=int(amounts[i])) for i in range(len(names)) if names[i] != ""]
    distribution = distribute(int(request.POST.budget), *workers)
    return distribution

application = default_app()

if __name__ == "__main__":
    run(reloader=True)
