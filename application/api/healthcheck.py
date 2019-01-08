from flask_restplus import Resource
from application.api import api
from application.common.types import Constants

ns = api.namespace(Constants.NS_HEALTH_CHECK, description='Service health check')


@ns.route('/')
class HealthCheck(Resource):
    from application.api.models import HealthCheckStatusModel

    @api.response(200, "Service is up")
    @api.marshal_with(HealthCheckStatusModel)
    def get(self):
        """
        Return status 200 if the service is alive.
        """
        from datetime import datetime
        return {
            'status': Constants.STATUS_OK,
            'timestamp': datetime.utcnow()
        }
