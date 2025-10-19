"""
Módulo contendo a interface abstrata base para todos os estados do semáforo.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..semaforo import Semaforo


class EstadoSemaforo(ABC):
    """
    A interface abstrata do Estado.
    
    Define os métodos que todos os estados concretos devem implementar.
    Fornece uma referência de volta ao objeto de Contexto (Semaforo).
    """
    
    _contexto: Semaforo

    @property
    def contexto(self) -> Semaforo:
        """Retorna a referência ao contexto (Semaforo)."""
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Semaforo) -> None:
        """Define a referência ao contexto (Semaforo)."""
        self._contexto = contexto

    @abstractmethod
    def avancar(self) -> None:
        """
        Define a lógica de transição para o próximo estado.
        
        Este método deve ser implementado por cada estado concreto
        para definir qual é o próximo estado na sequência.
        """
        pass
    
    @abstractmethod
    def mostrar_cor(self) -> None:
        """
        Define o comportamento de exibição da cor deste estado.
        
        Este método deve ser implementado por cada estado concreto
        para mostrar sua cor e mensagem específica.
        """
        pass
