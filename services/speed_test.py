import requests
from config import PAGE_SPEED_API_KEY
from utils.formatters import format_bytes, format_milliseconds, format_percentage

def run_speed_test(url: str, strategy: str = "mobile") -> dict:
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {"url":url, "strategy":strategy, "key":PAGE_SPEED_API_KEY}
    res = requests.get(endpoint, params=params, timeout=10)
    res.raise_for_status()
    d = res.json().get("lighthouseResult", {})
    audits = d.get("audits", {})
    score = d.get("categories",{}).get("performance",{}).get("score",0)
    m = {"performance_score": format_percentage(score,0)}
    def G(k, fn=None):
        v = audits.get(k,{}).get("numericValue",0)
        return fn(v) if fn else v
    m.update({
        "FCP": G("first-contentful-paint", format_milliseconds),
        "SI":  G("speed-index", format_milliseconds),
        "LCP": G("largest-contentful-paint", format_milliseconds),
        "TBT": G("total-blocking-time", format_milliseconds),
        "TTI": G("interactive", format_milliseconds),
        "Size":G("total-byte-weight",   format_bytes),
    })
    return m
