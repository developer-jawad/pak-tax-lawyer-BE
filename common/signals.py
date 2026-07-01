"""
Cache invalidation signals.

Each page-level aggregator caches its full response. When any model that
contributes to a page is saved or deleted via admin, we bust that cache key
so the next request rebuilds fresh data.
"""

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Import keys lazily via strings to avoid circular imports at module load time.
_CACHE_KEY_MAP = {
    # (app_label, model_name) -> list of cache keys to bust
    "home": [
        "api:home:sections",
    ],
    "service": [
        "api:service:list",
        "api:home:sections",  # service section is embedded in home too
    ],
    "blog": [
        "api:blog:page",
        "api:home:sections",
    ],
    "videos": [
        "api:videos:page",
        "api:home:sections",
    ],
    "about": [
        "api:about:page",
    ],
    "contact": [
        "api:contact:page",
    ],
    "footer": [
        "api:footer:page",
    ],
}


def _bust_keys(keys):
    from django.core.cache import cache
    cache.delete_many(keys)


def _get_keys_for_instance(instance):
    app_label = instance._meta.app_label
    return _CACHE_KEY_MAP.get(app_label, [])


@receiver(post_save)
def invalidate_cache_on_save(sender, instance, **kwargs):
    keys = _get_keys_for_instance(instance)
    if keys:
        _bust_keys(keys)


@receiver(post_delete)
def invalidate_cache_on_delete(sender, instance, **kwargs):
    keys = _get_keys_for_instance(instance)
    if keys:
        _bust_keys(keys)
