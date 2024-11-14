"""

Questão 5 - Peça ao usuário para inserir uma frase e conte quantas vezes uma letra específica aparece na frase usando o método `.count()`.

"""

# Solicita ao usuário que insira uma frase
frase = input("Insira uma frase: ")

# Solicita ao usuário que insira uma letra
letra = input("Insira uma letra: ")

# Conta quantas vezes a letra aparece na frase
contagem = frase.count(letra)

# Exibe a contagem
print(f"A letra '{letra}' aparece {contagem} vezes na frase.")
