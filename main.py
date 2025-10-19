# `main.py`: Exemplo do Padrão de Projeto State
# Intenção: Permitir que um objeto (Document) altere seu comportamento
# quando seu estado interno (Draft, InReview, Published) mudar.
# O objeto parecerá mudar de classe.

from __future__ import annotations
from abc import ABC, abstractmethod

# --- 1. O Contexto (Context) ---
# Define a interface de interesse dos clientes.
# Mantém uma instância de um subclasse de State que define o estado atual.

class Document:
    """
    O Contexto. Armazena o conteúdo do documento e uma referência
    para o seu estado atual. Ele delega o comportamento para o
    objeto de estado.
    """
    
    _state: State = None
    content: str = ""

    def __init__(self, content: str) -> None:
        self.content = content
        # O documento começa no estado Draft (Rascunho)
        self.transition_to(Draft())

    def transition_to(self, state: State) -> None:
        """
        Permite a mudança do objeto State em tempo de execução.
        """
        print(f"\nDocumento: Transicionando para o estado {type(state).__name__}")
        self._state = state
        self._state.context = self # Fornece ao estado o acesso ao contexto

    # Métodos de negócio. O comportamento é delegado ao estado.
    def write(self, text: str) -> None:
        """Adiciona texto ao conteúdo do documento."""
        self._state.write(text)

    def review_passed(self) -> None:
        """Chamado quando a revisão é aprovada."""
        self._state.review_passed()

    def review_failed(self) -> None:
        """Chamado quando a revisão é reprovada."""
        self._state.review_failed()

    def publish(self) -> None:
        """Tenta publicar o documento."""
        self._state.publish()

    def __str__(self) -> str:
        return f"Documento (Estado: {type(self._state).__name__}): '{self.content[:20]}...'"


# --- 2. A Interface do Estado (State) ---
# Declara métodos que todos os Estados Concretos devem implementar.

class State(ABC):
    """
    A interface base do Estado. Define métodos que todos os estados
    concretos devem implementar e fornece uma referência de volta
    ao objeto de Contexto (Document), se necessário, para a transição.
    """
    
    _context: Document

    @property
    def context(self) -> Document:
        return self._context

    @context.setter
    def context(self, context: Document) -> None:
        self._context = context

    @abstractmethod
    def write(self, text: str) -> None:
        """Comportamento de escrita."""
        pass

    @abstractmethod
    def review_passed(self) -> None:
        """Comportamento de aprovação de revisão."""
        pass

    @abstractmethod
    def review_failed(self) -> None:
        """Comportamento de reprovação de revisão."""
        pass

    @abstractmethod
    def publish(self) -> None:
        """Comportamento de publicação."""
        pass


# --- 3. Os Estados Concretos (Concrete States) ---
# Implementam os comportamentos associados a um estado do Contexto.

class Draft(State):
    """
    Estado Concreto: Rascunho.
    """
    def write(self, text: str) -> None:
        print("Draft: Adicionando texto ao rascunho...")
        self.context.content += text

    def review_passed(self) -> None:
        print("Draft: Não é possível aprovar. O documento deve ser enviado para revisão primeiro.")

    def review_failed(self) -> None:
        print("Draft: Não aplicável.")

    def publish(self) -> None:
        """
        No estado Draft, 'publicar' significa 'enviar para revisão'.
        """
        print("Draft: Enviando documento para revisão.")
        self.context.transition_to(InReview())


class InReview(State):
    """
    Estado Concreto: Em Revisão.
    """
    def write(self, text: str) -> None:
        print("InReview: Não é possível editar um documento em revisão.")

    def review_passed(self) -> None:
        print("InReview: Revisão aprovada!")
        self.context.transition_to(Published())

    def review_failed(self) -> None:
        print("InReview: Revisão reprovada. Voltando para rascunho.")
        self.context.transition_to(Draft())

    def publish(self) -> None:
        print("InReview: Documento já está em processo de revisão/publicação.")


class Published(State):
    """
    Estado Concreto: Publicado.
    """
    def write(self, text: str) -> None:
        print("Published: Não é possível editar um documento já publicado.")

    def review_passed(self) -> None:
        print("Published: Documento já foi aprovado e publicado.")

    def review_failed(self) -> None:
        print("Published: Não é possível reprovar um documento já publicado.")

    def publish(self) -> None:
        print("Published: Documento já está publicado.")


# --- 4. Código Cliente (Client) ---

if __name__ == "__main__":
    
    # 1. Cria um novo documento
    doc = Document("Este é o meu TCC...")
    print(doc)
    
    # 2. Escreve no rascunho
    doc.write(" Mais algum texto.")
    print(doc)
    
    # 3. Tenta aprovar (deve falhar, pois ainda é rascunho)
    doc.review_passed()
    print(doc)

    # 4. Envia para revisão (usa o método 'publish' do estado Draft)
    doc.publish()
    print(doc)
    
    # 5. Tenta escrever (deve falhar, pois está em revisão)
    doc.write(" Texto secreto.")
    print(doc)

    # 6. Revisão é reprovada
    doc.review_failed()
    print(doc)

    # 7. Escreve mais (agora pode, pois voltou a ser rascunho)
    doc.write(" Corrigindo o texto.")
    print(doc)

    # 8. Envia para revisão novamente
    doc.publish()
    print(doc)

    # 9. Revisão é aprovada!
    doc.review_passed()
    print(doc)

    # 10. Tenta publicar de novo (já está publicado)
    doc.publish()
    print(doc)
