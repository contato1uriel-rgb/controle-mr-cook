"""Variáveis de template compartilhadas."""

import os

from django.conf import settings
from django.contrib.staticfiles import finders

WALLPAPER_STATIC = "producao/wallpaper/background.jpg"


def wallpaper_version(_request):
    """Query string para cache-bust do papel de parede quando o arquivo é substituído."""
    path = finders.find(WALLPAPER_STATIC)
    v = 0
    if path and os.path.isfile(path):
        v = int(os.path.getmtime(path))
    return {"wallpaper_cache_bust": v}


def deploy_stamp(_request):
    """Mostra no rodapé um ID curto do deploy (Git ou variável do host)."""
    return {"app_deploy_id": getattr(settings, "APP_DEPLOY_ID", "")}
