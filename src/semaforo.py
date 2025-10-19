"""
Módulo contendo o Contexto (Context) do padrão State: a classe Semaforo.
"""

from __future__ import annotations
from typing import Optional

from .states import EstadoSemaforo, EstadoVermelho


class Semaforo:
    """
    O Contexto (Context) do padrão State.
    
    Este é o objeto principal (nosso Semáforo) cujo comportamento
    mudará dinamicamente com base no estado interno atual.
    
    O Semaforo mantém uma referência ao seu estado atual e delega
    todas as operações específicas de estado para o objeto de estado.
    
    Attributes:
        _estado: O estado atual do semáforo.
    """
    
    def __init__(self) -> None:
        """
        Inicializa o semáforo.
        
        O semáforo sempre começa no estado 'Vermelho' por questões
        de segurança no trânsito.
        """
        self._estado: Optional[EstadoSemaforo] = None
        # O semáforo começa no estado 'Vermelho'
        self.transicionar_para(EstadoVermelho())

    def transicionar_para(self, estado: EstadoSemaforo) -> None:
        """
        Permite a transição para um novo estado.
        
        Este método é chamado tanto internamente (durante a inicialização)
        quanto pelos próprios estados (quando decidem transicionar).
        
        Args:
            estado: O novo estado para o qual o semáforo deve transicionar.
        """
        print(f"\n🚦 SISTEMA: Trocando para o estado {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self  # Fornece ao estado acesso ao contexto

    def avancar(self) -> None:
        """
        Avança o semáforo para o próximo estado.
        
        A lógica específica de qual é o próximo estado é delegada
        ao objeto de estado atual através do método avancar().
        """
        if self._estado is None:
            raise RuntimeError("Estado do semáforo não foi inicializado!")
        
        self._estado.avancar()

    def mostrar_cor(self) -> None:
        """
        Exibe a cor atual do semáforo.
        
        O comportamento específico de como mostrar a cor é delegado
        ao objeto de estado atual através do método mostrar_cor().
        """
        if self._estado is None:
            raise RuntimeError("Estado do semáforo não foi inicializado!")
        
        self._estado.mostrar_cor()

    @property
    def estado_atual(self) -> str:
        """
        Retorna o nome do estado atual.
        
        Returns:
            String com o nome da classe do estado atual.
        """
        if self._estado is None:
            return "Não inicializado"
        return type(self._estado).__name__
