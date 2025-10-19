"""
Módulo contendo o estado concreto: Vermelho.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from .base import EstadoSemaforo

if TYPE_CHECKING:
    from ..semaforo import Semaforo


class EstadoVermelho(EstadoSemaforo):
    """
    Estado Concreto: Vermelho (Pare!)
    
    Representa o estado vermelho do semáforo, onde os veículos
    devem parar. Ao avançar, transiciona para o estado verde.
    """
    
    def avancar(self) -> None:
        """
        Transiciona do estado Vermelho para o estado Verde.
        """
        print("Sinal VERMELHO... Aguardando... Trocando para VERDE.")
        
        # Import here to avoid circular dependency
        from .verde import EstadoVerde
        self.contexto.transicionar_para(EstadoVerde())

    def mostrar_cor(self) -> None:
        """
        Exibe a luz vermelha com a mensagem de PARE.
        """
        print("🔴 LUZ: [VERMELHA] (PARE!)")
