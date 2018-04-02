import re


def decode(url):
    url = re.sub('https://urldefense.proofpoint.com/v2/url\?u=', '', url)
    remove_list = re.findall('&d.*', url)
    remove = ''.join(remove_list)
    url = re.sub(remove, '', url)
    remove_list = re.findall('_7pt.*', url)
    remove = ''.join(remove_list)
    url = re.sub(remove, '', url)
    url = re.sub('__', '//', url)
    url = re.sub('_e_70492_', '/', url)
    url = re.sub('_', '/', url)
    url = re.sub('-26amp-3B', '&', url)

    url = re.sub('-21', '!', url)
    url = re.sub('-22', '%', url)
    url = re.sub('-23', '#', url)
    url = re.sub('-24', '$', url)
    url = re.sub('-25', '%', url)
    url = re.sub('-26', '&', url)
    url = re.sub('-27', '\'', url)
    url = re.sub('-28', '(', url)
    url = re.sub('-29', ')', url)
    url = re.sub('-2A', '*', url)
    url = re.sub('-2B', '+', url)
    url = re.sub('-2C', ',', url)
    url = re.sub('-2D', '', url)
    url = re.sub('-2E', '.', url)
    url = re.sub('-2F', '/', url)

    url = re.sub('-3A', ':', url)
    url = re.sub('-3B', ';', url)
    url = re.sub('-3C', '<', url)
    url = re.sub('-3D', '=', url)
    url = re.sub('-3E', '>', url)
    url = re.sub('-3F', '?', url)

    url = re.sub('-5B', '[', url)
    url = re.sub('-5C', r'\\', url)
    url = re.sub('-5D', ']', url)
    url = re.sub('-5E', '^', url)
    url = re.sub('-5F', '_', url)

    return url
