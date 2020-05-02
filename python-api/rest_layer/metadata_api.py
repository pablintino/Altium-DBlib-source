from flask_restful import Resource
from flask import Response
from services import metadata_service
from dtos import metadata_dtos


class MetadataResource(Resource):
    def get(self):
        metadata = metadata_service.get_component_metadata()
        json_dto = metadata_dtos.ModelDescriptorsDto.from_model_list(metadata).to_json()
        return Response(json_dto, mimetype="application/json", status=200)
