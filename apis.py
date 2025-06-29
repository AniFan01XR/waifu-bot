import requests
import random

APIS = [
    lambda tag: requests.get('https://konachan.com/post.json', params={'tags': tag}).json(),
    lambda tag: requests.get('https://yande.re/post.json', params={'tags': tag}).json(),
    lambda tag: requests.get('https://danbooru.donmai.us/posts.json', params={'tags': tag, 'limit': 100}).json(),
]

def search_any(tag):
    for api in APIS:
        try:
            res = api(tag)
            if isinstance(res, list) and res:
                sel = random.choice(res)
                return sel.get('file_url') or sel.get('large_file_url')
        except Exception:
            continue
    return None
