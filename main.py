#
#    Escreva um programa que receba um endereço virtual (em decimal) na linha de comando
#    ou leitura do arquivo addresses.txt faça com que ele produza o número da página e o deslocamento do endereço
#    fornecido, sendo que essa posição indica qual a posição que será lido do arquivo data_memory.txt.
#

# Menu
def menu():

    # Variável de controle
    flag = False

    # Enquanto a opção for inválida, repete:
    while not flag:

        print("Escolha o tamanho de memória desejado: ")
        print("1 - 16 Bits ")
        print("2 - 32 Bits ")
        menu = input("Opção: ")

        # Se menu for diferente de 1 e 2 a entrada é inválida
        if menu != '1' and menu != '2':
            print("Entrada Inválida!")

        # Senão retorna o valor escolhido
        else:
            flag = True
            return menu


# 16-Bits
def dezesseis_bits():

    with open("addresses_16b.txt", "r") as arquivo_16b:

        # Lê o conteúdo do arquivo
        conteudo = arquivo_16b.readlines()

        # Para cada linha do arquivo
        for linha in conteudo:

            # Converte o conteúdo da linha para inteiro
            int_linha = int(linha)

            # Converte o inteiro para binário
            aux = bin(int_linha)

            # remove o '0b' da frente do número
            binario = aux[2::]

            # Adiciona 0's na frente até ter 16 bits
            # Captura quantos bits faltam para completar 16
            tam = (len(binario) - 16) * -1

            # Adiciona os 0's faltantes
            for x in range(tam):
                binario = "0"+binario

            # exibe os valores
            calcula_posicao_16_bits(binario)


# Calcula a posição e deslocamento para endereços 16-Bits
def calcula_posicao_16_bits(binario):

    # Captura os 4 primeiros bits do endereço
    pagina = binario[0:3]

    # Converte para inteiro
    pagina = int(pagina, 2)

    # Captura os bits restantes
    deslocamento = binario[4:15]

    # Converte para decimal
    deslocamento = int(deslocamento, 2)

    # Exibe os valores
    print("Pagina: " + str(pagina))
    print("Deslocamento: " + str(deslocamento))


# 32-Bits
def trinta_e_dois_bits():

    with open("addresses_32b.txt", "r") as arquivo_32b:

        # Lê o conteúdo do arquivo
        conteudo = arquivo_32b.readlines()

        # Para cada linha do arquivo
        for linha in conteudo:

            # Converte o conteúdo da linha para inteiro
            int_linha = int(linha)

            # Converte o conteúdo da linha para binário
            aux = bin(int_linha)

            # remove o '0b' da frente do número
            binario = aux[2::]

            # Adiciona 0's na frente até ter 32 bits
            # Captura quantos bits faltam para completar 32
            tam = (len(binario) - 32) * -1

            # Adiciona os 0's faltantes
            for x in range(tam):
                binario = "0" + binario

            # exibe os valores
            calcula_posicao_32_bits(binario)


# Calcula a posição e deslocamento para endereços 32-Bits
def calcula_posicao_32_bits(binario):

    # Captura os 20 primeiros bits do endereço
    pagina = binario[0:19]

    # Converte para decimal
    pagina = int(pagina, 2)

    # Captura os bits restantes
    deslocamento = binario[4:31]

    # Converte para inteiro
    deslocamento = int(deslocamento, 2)

    # Exibe os valores
    print("Pagina: " + str(pagina))
    print("Deslocamento: " + str(deslocamento))


# Função Main
if __name__ == '__main__':

    # Chama o Menu e atribui a opção à variável menu
    menu = menu()

    # 16-Bits
    if menu == '1':

        # Chama a função para 16 bits
        dezesseis_bits()

    # 32-Bits
    else:

        # Chama a função para 32 bits
        trinta_e_dois_bits()

