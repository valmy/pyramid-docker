from pyramid.compat import escape

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home_view(request):
    return Response('<p>Visit <a href="/howdy/lisa">hello</a></p>')


# /howdy?name=alice which links to the next view
@view_config(route_name='hello', renderer='hello_world.jinja2')
def hello_view(request):
    return dict(name=request.matchdict['name'])

@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return [1, 2, 3]


# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")


# /problem which causes a site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()
