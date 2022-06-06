import json

from rest_framework import renderers


class UserRender(renderers.JSONRenderer):
    charset = 'UTF8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # import pdb
        # pdb.set_trace()
        if 'ErrorDetail' in str(data):
            response = json.dumps({'error': data})
        else:
            response = json.dumps({'data': data})
        return response
        # return super().render(data, accepted_media_type, renderer_context)
