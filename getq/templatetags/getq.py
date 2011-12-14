from django import template

register = template.Library()

class GetqUpdateNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        try:
            request = context['request']
        except KeyError:
            raise template.TemplateSyntaxError(
                "No request available in context (perhaps request context "
                "processor is disabled?)"
            )
        return 'hello-world'

@register.tag
def getq_update(parser, token):
    return GetqUpdateNode()
