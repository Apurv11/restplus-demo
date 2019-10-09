#from flask import
from flask_restplus import Resource, Namespace

from ..service.nimbus_service import get_namespaces, get_vservers

api = Namespace('nimbus', description='nimbus rest api operations')

@api.route('/')
class NimbusNamespaces(Resource):
    @api.doc('get list of nimbus namespaces')
    def get(self):
        """List all Nimbus Namespaces"""
        return get_namespaces()


@api.route('/<namespace>')
@api.param('namespace', 'Namespace to find vservers')
class NimbusVserver(Resource):
    @api.doc('Get list of vservers in a namespace')
    def get(self, namespace):
        """Get list of vservers in a namespace"""
        vserver_list = get_vservers(namespace)
        if not vserver_list:
            api.abort(404)
        else:
            return vserver_list
