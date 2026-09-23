# ==============================================================================
# ATIVIDADE - PESQUISA DE OPINIÃO (TUDOWEB)
# Autor: Michael Silva
# Objetivo: Coletar a opinião de entrevistados e exibir a contagem de respostas.
# Nota para o teste: Alterado para 1 entrevistado para validação rápida do programa.
# ==============================================================================

# Boas-vindas ao sistema
print("=== PESQUISA DE SATISFAÇÃO DE ATENDIMENTO - TUDOWEB ===")

# Criamos os contadores para registrar a quantidade de respostas
quantidade_excelente = 0
quantidade_ruim = 0

# Definição do total de entrevistados (Ajustado para 1 entrevistado para teste)
TOTAL_ENTREVISTADOS = 1

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    # Solicita os dados do cliente
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade do entrevistado: "))
    
    # Exibe o menu de opções para a opinião
    print("Opções de opinião:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite o número correspondente à sua opinião (1, 2 ou 3): "))
    
    # Estruturas de decisão (if e elif) para verificar a resposta do cliente
    if opiniao == 1:
        quantidade_excelente = quantidade_excelente + 1
    elif opiniao == 3:
        quantidade_ruim = quantidade_ruim + 1

# Exibição do resultado final da pesquisa após a repetição terminar
print("\n" + "=" * 45)
print("          RESULTADO DA PESQUISA DE OPINIÃO          ")
print("=" * 45)
print(f"a) Quantidade de respostas 'EXCELENTE': {quantidade_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {quantidade_ruim}")
print("=" * 45)
