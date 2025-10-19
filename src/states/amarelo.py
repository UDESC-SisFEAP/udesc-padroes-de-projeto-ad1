"""
Módulo contendo o estado concreto: Amarelo.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from .base import EstadoSemaforo

if TYPE_CHECKING:
    from ..semaforo import Semaforo


class EstadoAmarelo(EstadoSemaforo):
    """
    Estado Concreto: Amarelo (Atenção!)
    
    Representa o estado amarelo do semáforo, onde os veículos
    devem ter atenção e preparar para parar. Ao avançar, 
    transiciona para o estado vermelho.
    """
    
    def avancar(self) -> None:
        """
        Transiciona do estado Amarelo para o estado Vermelho.
        """
        print("Sinal AMARELO... Atenção... Trocando para VERMELHO.")
        
        # Import here to avoid circular dependency
        from .vermelho import EstadoVermelho
        self.contexto.transicionar_para(EstadoVermelho())

    def mostrar_cor(self) -> None:
        """
        Exibe a luz amarela com a mensagem de ATENÇÃO.
        """
        print("🟡 LUZ: [AMARELA] (ATENÇÃO!)")
