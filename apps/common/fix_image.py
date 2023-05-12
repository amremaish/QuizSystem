from QuizSystem.settings import AWS_ENDPOINT_URI


def fix_underscore(obj, key: str):
    if not isinstance(obj, dict):
        obj = obj.__dict__
    obj[key[1:]] = obj.pop(key)
    return obj, key[1:]


def add_prefix_image(obj, key: str):
    obj[key] = AWS_ENDPOINT_URI + obj[key]
    return obj


def fix_image_admin(obj, key: str):
    if not isinstance(obj, dict):
        obj = obj.__dict__
    if key not in obj:
        return obj
    obj, key = fix_underscore(obj, key)
    add_prefix_image(obj, key)
    return obj
