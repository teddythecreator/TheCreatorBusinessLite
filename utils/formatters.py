import re
from urllib.parse import urlparse

def format_bytes(n, precision=2):
    for unit in ['B','KB','MB','GB','TB']:
        if n<1024.0 or unit=='TB':
            return f"{n:.{precision}f} {unit}"
        n /= 1024.0

def format_milliseconds(ms, precision=2):
    s = ms/1000.0
    return f"{s:.{precision}f} s"

def format_percentage(v, precision=0):
    if 0<=v<=1:
        v *= 100
    return f"{v:.{precision}f}%"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+','-', text)
    return re.sub(r'-{2,}','-', text).strip('-')

def is_valid_url(url):
    try:
        p = urlparse(url)
        return p.scheme in ('http','https') and bool(p.netloc)
    except:
        return False
