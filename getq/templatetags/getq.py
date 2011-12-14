from django import template

register = template.Library()

class GetqUpdateNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return 'hello-world'

@register.tag
def getq_update(parser, token):
    return GetqUpdateNode()
