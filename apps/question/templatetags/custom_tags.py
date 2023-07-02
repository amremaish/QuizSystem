from django import template

register = template.Library()


@register.filter
def calculate_percent(correct, wrong):
    try:
        return f"{int((correct / (correct + wrong)) * 100)}%"
    except:
        pass
    return 0
