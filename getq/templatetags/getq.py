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
            literal = value.to_literal(context)
            if literal is None:
                if param in params:
                    del params[param]
            else:
                params[param] = literal
        if params:
            return '%s?%s' % (request.path, params.urlencode())
        else:
            return request.path


class Value(object):
    def __init__(self, raw):
        self.raw = raw

    def to_literal(self, context):
        # TODO: Use smarter parsing with escaping support, etc.
        if not self.raw:
            # Empty string means that param sould be removed
            return None
        if self.raw[0] == self.raw[-1] and self.raw[0] in ('"', "'"):
            # Got literal - unquote the value
            return self.raw[1:-1]
        else:
            # Got variable name name - resolve it
            return template.Variable(self.raw).resolve(context)


@register.tag
def getq_update(parser, token):
    contents = token.split_contents()
    tag_name = contents[0]
    statements = contents[1:]
    if not statements:
        raise template.TemplateSyntaxError(
            "'%s' tag requires 1 or more arguments" % tag_name
        )
    params = dict((p, Value(v)) for p, v
                                in (s.split('=', 1) for s in statements))
    return GetqUpdateNode(params)
