import hashlib

from django.core.cache import cache

DEFAULT_TTL = 60 * 15  # 15 minutes


def make_cache_key(prefix: str, *parts) -> str:
    raw = ":".join(str(p) for p in parts)
    digest = hashlib.md5(raw.encode(), usedforsecurity=False).hexdigest()[:12]
    return f"{prefix}:{digest}"


def get_or_set(key: str, callable, timeout: int = DEFAULT_TTL):
    try:
        value = cache.get(key)
    except Exception:
        value = None
    if value is None:
        value = callable()
        try:
            cache.set(key, value, timeout)
        except Exception:
            pass
    return value
