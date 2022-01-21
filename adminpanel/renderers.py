import json

from rest_framework.renderers import JSONRenderer


class HouseJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(HouseJSONRenderer, self).render(data)

        return json.dumps({'house': data})