"""
Módulo contendo o estado concreto: Verde.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from .base import EstadoSemaforo

if TYPE_CHECKING:
    from ..semaforo import Semaforo


class EstadoVerde(EstadoSemaforo):
    """
    Estado Concreto: Verde (Siga!)
    
    Representa o estado verde do semáforo, onde os veículos
    podem seguir. Ao avançar, transiciona para o estado amarelo.
    """
    
    def avancar(self) -> None:
        """
        Transiciona do estado Verde para o estado Amarelo.
        """
        print("Sinal VERDE... Siga em frente... Trocando para AMARELO.")
        
        # Import here to avoid circular dependency
        from .amarelo import EstadoAmarelo
        self.contexto.transicionar_para(EstadoAmarelo())

    def mostrar_cor(self) -> None:
        """
        Exibe a luz verde com a mensagem de SIGA.
        """
        print("🟢 LUZ: [VERDE] (SIGA!)")
