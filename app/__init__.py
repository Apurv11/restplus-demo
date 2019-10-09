from flask_restplus import Api
from flask import Blueprint

from .main.controller.nimbus_controller import api as nimbus_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS DEVOPS TOOLS REST API',
          version='1.0',
          description='flask restplus api for devops tools'
          )

api.add_namespace(nimbus_ns, path='/nimbus')
