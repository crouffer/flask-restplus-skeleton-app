from flask_restplus import Api

api = Api(
    version='0.1',
    title='Example Flask Restplus Application',
    description='API For the Example Flask Restplus Application',
    catch_all_404s=True,
    default_mediatype='application/json'
    )
