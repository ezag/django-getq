from django import template

register = template.Library()

class GetqUpdateNode(template.Node):
    def __init__(self, params):
        self.new_params = params

    def render(self, context):
        try:
            request = context['request']
        except KeyError:
            raise template.TemplateSyntaxError(
                "No request available in context (perhaps request context "
                "processor is disabled?)"
            )
        params = request.GET.copy()
        # Not using QueryDict.update() because it does append updated
        # values to existing ones rather then replace them.
        for param, value in self.new_params.iteritems():
            params[param] = value
        return '%s?%s' % (request.path, params.urlencode())

@register.tag
def getq_update(parser, token):
    contents = token.split_contents()
    tag_name = contents[0]
    statements = contents[1:]
    if not statements:
        raise template.TemplateSyntaxError(
            "'%s' tag requires 1 or more arguments" % tag_name
        )
    params = dict(s.split('=', 1) for s in statements)
    return GetqUpdateNode(params)
