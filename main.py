# `main.py`: Exemplo Didático do Padrão de Projeto State
# Intenção: Demonstrar como um objeto (Semaforo) muda seu
# comportamento (o que `avancar()` faz) com base em seu
# estado interno (Vermelho, Verde, Amarelo).

from __future__ import annotations
from abc import ABC, abstractmethod
import time

# --- 1. O Contexto (Context) ---
# Mantém uma referência ao seu estado atual e delega
# o comportamento para esse estado.

class Semaforo:
    """
    O Contexto (Context). Este é o objeto (nosso Semáforo)
    cujo comportamento mudará com base no estado.
    """
    
    _estado: EstadoSemaforo = None

    def __init__(self) -> None:
        # O semáforo começa no estado 'Vermelho'
        self.transicionar_para(EstadoVermelho())

    def transicionar_para(self, estado: EstadoSemaforo) -> None:
        """
        O Contexto permite mudar seu objeto de Estado.
        """
        print(f"\nSISTEMA: Trocando para o estado {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self # Dá ao estado acesso ao contexto

    def avancar(self) -> None:
        """
        A ação de avançar no tempo. O comportamento é
        delegado ao objeto de estado atual.
        """
        self._estado.avancar()

    def mostrar_cor(self) -> None:
        """
        A ação de mostrar a cor. O comportamento também é
        delegado ao objeto de estado atual.
        """
        self._estado.mostrar_cor()


# --- 2. A Interface do Estado (State) ---
# Declara os métodos que todos os estados concretos devem ter.

class EstadoSemaforo(ABC):
    """
    A interface abstrata do Estado.
    """
    
    _contexto: Semaforo

    @property
    def contexto(self) -> Semaforo:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Semaforo) -> None:
        self._contexto = contexto

    @abstractmethod
    def avancar(self) -> None:
        """
        Define a lógica de transição para o próximo estado.
        """
        pass
    
    @abstractmethod
    def mostrar_cor(self) -> None:
        """
        Define o comportamento (mostrar cor) deste estado.
        """
        pass


# --- 3. Os Estados Concretos (Concrete States) ---
# Implementam o comportamento específico de cada estado.

class EstadoVermelho(EstadoSemaforo):
    """
    Estado Concreto: Vermelho (Pare!)
    """
    def avancar(self) -> None:
        print("Sinal VERMELHO... Aguardando... Trocando para VERDE.")
        # Ao avançar, o Vermelho transiciona para o Verde
        self.contexto.transicionar_para(EstadoVerde())

    def mostrar_cor(self) -> None:
        print("LUZ: [VERMELHA] (PARE!)")


class EstadoVerde(EstadoSemaforo):
    """
    Estado Concreto: Verde (Siga!)
    """
    def avancar(self) -> None:
        print("Sinal VERDE... Siga em frente... Trocando para AMARELO.")
        # Ao avançar, o Verde transiciona para o Amarelo
        self.contexto.transicionar_para(EstadoAmarelo())

    def mostrar_cor(self) -> None:
        print("LUZ: [VERDE] (SIGA!)")


class EstadoAmarelo(EstadoSemaforo):
    """
    Estado Concreto: Amarelo (Atenção!)
    """
    def avancar(self) -> None:
        print("Sinal AMARELO... Atenção... Trocando para VERMELHO.")
        # Ao avançar, o Amarelo transiciona para o Vermelho
        self.contexto.transicionar_para(EstadoVermelho())

    def mostrar_cor(self) -> None:
        print("LUZ: [AMARELA] (ATENÇÃO!)")


# --- 4. Código Cliente (Client) ---

if __name__ == "__main__":
    
    # Cria o contexto
    semaforo = Semaforo()
    
    # Executa o ciclo do semáforo várias vezes
    for _ in range(6):
        semaforo.mostrar_cor()  # Mostra a cor atual
        semaforo.avancar()      # Avança para o próximo estado
        time.sleep(1)           # Pausa para visualização

    # Mostra o estado final do ciclo
    semaforo.mostrar_cor()
