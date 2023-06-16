# from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
# from pyramid.response import Response
# import os

# def hello_world(request):
#    name = os.environ.get('NAME')
#    if name == None or len(name) == 0:
#        name = "world"
#    message = "Hello, " + name + "!\n"
#    return Response(message)

# if __name__ == '__main__':
#    port = int(os.environ.get("PORT"))
#    with Configurator() as config:
#        config.add_route('hello', '/')
#        config.add_view(hello_world, route_name='hello')
#        app = config.make_wsgi_app()
#    server = make_server('0.0.0.0', port, app)
#    server.serve_forever()
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
