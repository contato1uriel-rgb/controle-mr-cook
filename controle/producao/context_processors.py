"""Variáveis de template compartilhadas."""

import os

from django.contrib.staticfiles import finders

WALLPAPER_STATIC = "producao/wallpaper/background.jpg"


def wallpaper_version(_request):
    """Query string para cache-bust do papel de parede quando o arquivo é substituído."""
    path = finders.find(WALLPAPER_STATIC)
    v = 0
    if path and os.path.isfile(path):
        v = int(os.path.getmtime(path))
    return {"wallpaper_cache_bust": v}
