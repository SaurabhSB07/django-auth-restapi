from rest_framework import renderers

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response') if renderer_context else None
        if response is not None and not (200 <= response.status_code < 300):
            data = {'errors': data}
        return super().render(data, accepted_media_type, renderer_context)
