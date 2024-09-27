from controllers.sayhello import SayHello
from controllers.server_version import ServerVersion 
from controllers.device_state import DeviceState


def InitRoutes(api):
        api.add_resource(SayHello, '/api/v1/hello')
        api.add_resource(ServerVersion, '/api/version')
        api.add_resource(DeviceState, '/api/v1/state')