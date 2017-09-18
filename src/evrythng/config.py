__ENDPOINT_CONFIG = {
    'base_url': 'https://api.evrythng.com'
}

def set_endpoint_attribute(attribute_name, attribute_value):
    __ENDPOINT_CONFIG[attribute_name] = attribute_value

def get_endpoint_attribute(attribute_name):
    return __ENDPOINT_CONFIG[attribute_name]
