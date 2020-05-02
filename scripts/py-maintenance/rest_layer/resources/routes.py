from rest_layer.metadata_api import MetadataResource


def initialize_routes(api):
    api.add_resource(MetadataResource, '/metadata')
    # api.add_resource(MovieApi, '/movies/<id>')
