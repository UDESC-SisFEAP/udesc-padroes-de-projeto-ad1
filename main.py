"""
main.py - Exemplo Didático do Padrão de Projeto State

Demonstra o uso do padrão State através de um Semáforo que muda
seu comportamento dinamicamente com base no estado interno 
(Vermelho, Verde, Amarelo).

Autor: Equipe de Padrões de Projeto - UDESC
Data: Outubro 2025
"""

import time
from src import Semaforo


def main() -> None:
    """
    Função principal que demonstra o funcionamento do padrão State.
    
    Cria um semáforo e executa vários ciclos de transições entre
    os estados, mostrando como o comportamento muda dinamicamente.
    """
    print("=" * 60)
    print("DEMONSTRAÇÃO DO PADRÃO STATE - SEMÁFORO")
    print("=" * 60)
    
    # Cria o contexto (Semáforo)
    semaforo = Semaforo()
    
    # Define o número de ciclos a executar
    numero_de_ciclos = 2
    transicoes_por_ciclo = 3  # Vermelho -> Verde -> Amarelo
    total_transicoes = numero_de_ciclos * transicoes_por_ciclo
    
    print(f"\nExecutando {numero_de_ciclos} ciclos completos do semáforo...")
    print(f"Total de {total_transicoes} transições de estado.\n")
    
    # Executa o ciclo do semáforo
    for i in range(total_transicoes):
        print(f"\n--- Transição {i + 1}/{total_transicoes} ---")
        semaforo.mostrar_cor()      # Mostra a cor atual
        semaforo.avancar()          # Avança para o próximo estado
        time.sleep(1)               # Pausa de 1 segundo para visualização
    
    # Mostra o estado final após todos os ciclos
    print(f"\n--- Estado Final ---")
    semaforo.mostrar_cor()
    print(f"\nEstado atual do semáforo: {semaforo.estado_atual}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 60)


if __name__ == "__main__":
    main()
