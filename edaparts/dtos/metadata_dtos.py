from dtos.encoders.dto_json_encoder import JsonizableBaseClass


class FieldDto(JsonizableBaseClass):
    def __init__(self, name, is_mandatory, data_type):
        self.name = name
        self.is_mandatory = is_mandatory
        self.data_type = data_type if type(data_type) is str else data_type.__name__

    @staticmethod
    def from_model(field_model):
        return FieldDto(field_model.name, field_model.is_mandatory, field_model.data_type)


class ModelDescriptorDto(JsonizableBaseClass):

    def __init__(self, model_name, fields=[]):
        self.model_name = model_name
        self.fields = fields

    @staticmethod
    def from_model(component_model):
        field_dtos = []
        for f_id, fm in component_model.fields.items():
            field_dtos.append(FieldDto.from_model(fm))
        return ModelDescriptorDto(component_model.model_name, field_dtos)


class ModelDescriptorsDto(JsonizableBaseClass):

    def __init__(self, models=[]):
        self.models = models

    @staticmethod
    def from_model_list(models):
        model_list = []
        for model in models:
            model_list.append(ModelDescriptorDto.from_model(model))
        return ModelDescriptorsDto(model_list)
