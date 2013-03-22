from django import template
from cache_tools.tools import get_group_key

register = template.Library()


class GetGroupKeyNode(template.Node):
    def __init__(self, group, var_name):
        self.group = group
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = get_group_key(self.group)
        return ''

@register.tag("get_group_key")
def do_get_group_key(parser, token):
    """
    This will store the group key for a specified group in the context.

    Usage::

        {% get_group_key group_name as group_key %}

    This will fetch the key for the selected group and
    put it's value into the ``group_key`` context
    variable.
    """
    # token.split_contents() isn't useful here because this tag doesn't accept variable as arguments
    args = token.contents.split()
    if len(args) != 4 or args[2] != 'as':
        raise TemplateSyntaxError("'get_group_key' requires 'as variable' (got %r)" % args)

    return GetGroupKeyNode(args[1], args[3])