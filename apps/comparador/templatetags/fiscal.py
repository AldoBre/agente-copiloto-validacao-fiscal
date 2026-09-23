"""Filtros de template do comparador."""
import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

_RE_NEGRITO = re.compile(r"\*\*(.+?)\*\*")


@register.filter
def negrito(valor):
    """
    ``"**75** notas"`` → ``"<strong>75</strong> notas"``.

    Escapa primeiro e só depois converte, então nada do conteúdo vira HTML por
    acidente.
    """
    return mark_safe(_RE_NEGRITO.sub(r"<strong>\1</strong>", escape(valor or "")))
