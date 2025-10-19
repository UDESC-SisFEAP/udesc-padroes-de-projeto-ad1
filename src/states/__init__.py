"""
Pacote contendo todos os estados concretos do semáforo.
"""

from .base import EstadoSemaforo
from .vermelho import EstadoVermelho
from .verde import EstadoVerde
from .amarelo import EstadoAmarelo

__all__ = [
    'EstadoSemaforo',
    'EstadoVermelho',
    'EstadoVerde',
    'EstadoAmarelo'
]
