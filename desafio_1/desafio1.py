'''
Descrição
Você está desenvolvendo um sistema de geração de sugestões de tópicos para um blog de tecnologia. O objetivo 
é associar características específicas dos modelos Claude 3 da Anthropic às palavras-chave fornecidas e 
fornecer o nome do modelo correspondente como saída.

Entrada
Uma descrição correspondente a um dos modelos Claude 3 da Anthropic, como "automatizar tarefas" ou "equilíbrio
 ideal entre inteligência e velocidade".

Saída
O nome do modelo Claude 3 que melhor corresponde à característica fornecida na entrada, como "Claude 3 Opus",
 "Claude 3 Sonnet" e "Claude 3 Haiku". Caso a entrada não possua características dos modelos citados acima, 
 o programa deve retornar uma mensagem: Modelo não encontrado.
'''

# Dicionário associando características aos modelos Claude 3
caracteristicas_modelos = {
    "automatizar tarefas": "Claude 3 Opus",
    "pesquisa e desenvolvimento": "Claude 3 Opus",
    "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",
    "motores de chatbots de lojas": "Claude 3 Haiku",
    "moderação de conteúdo": "Claude 3 Haiku",
    "processamento de tarefas mais básicas": "Claude 3 Haiku",
    "raciocínio cuidadoso": "Claude 3 Sonnet",
    "processamento de dados": "Claude 3 Sonnet",
    "aplicações de vendas": "Claude 3 Sonnet",
    "extração de texto de imagens": "Claude 3 Sonnet",
    "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
   
}

# Crie uma função 'encontrar_modelo' para encontrar o modelo correspondente à característica fornecida: 
def encontrar_modelo(caracteristica_fornecida, caracteristicas_modelos):
# Itere sobre cada chave e valor no dicionário caracteristicas_modelos:
    for caracteristica, modelo in caracteristicas_modelos.items():
# Verifique se a palavra-chave (característica) está contida na característica fornecida (ignorando maiúsculas/minúsculas):
        if caracteristica.lower() in caracteristica_fornecida.lower():
# Se encontrada, retorne o modelo correspondente:
            return modelo
# Se não encontrada, retorne uma mensagem indicando que o modelo não foi encontrado
    return "Modelo não encontrado."

# Entrada do usuário
caracteristica_fornecida = input("Descreva as caracteristicas do modelo: ")

# Encontrar e imprimir o modelo correspondente
modelo_correspondente = encontrar_modelo(caracteristica_fornecida, caracteristicas_modelos)
print(modelo_correspondente)