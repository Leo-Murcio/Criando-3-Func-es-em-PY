# 1ª FUNÇÃO - essa função simplesmente imprime o BemVindo
def BemVindo():
    print("Bem Vindo a turma de ADS <3")
# chamando a função para exibir as Boas-Vindas
BemVindo()

#----------------------------------------------------

# 2ª FUNÇÃO - essa função recebe o nome de uma pessoa como parâmetro e imprime uma Boas-Vindas DIFERENCIADA
def BemVindoDiferenciado(nome):
    print(f"Bem Vindo! {nome} Já estudou hoje?")
# chamando a função e contendo um nome como parâmetro
nome_da_pessoa = "Leo"
BemVindoDiferenciado(nome_da_pessoa)

#----------------------------------------------------

# 3º FUNÇÃO - essa função calcula a área de um retângulo com base em sua largura e altura e retorna o resultado
def calculo_retangulo(largura, altura):
    area = largura * altura
    return area
# chamando a função para calcular a área do retângulo
largura_do_retangulo = 5
altura_do_retangulo = 3
area_calculada = calculo_retangulo(largura_do_retangulo, altura_do_retangulo)
print(f"A área do retângulo é: {area_calculada} unidades quadradas.")