# criptografa texto grandes
a = 5
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
        'X','Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', '!', '?', ';', 'õ', 'á', 'Á', 'ô', 'ó','é', 'í', 'ã', 'à',
       'ç', ':', 'ú', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  # abcdário/acentos/ pontuação que o programa lê


print("Tecle enter para continuar :")
input()# iniciar o programa

while a != 0:    # repetição do programa
    Textofinal = ""
    print("Digite uma opção")
    print("1- Criptografar")
    print("2- Descriptografar") # mostrando as opções para o usuário
    opcao = int(input("Sua escolha:"))
    texto = ''.join(input("Digite o texto: "))  # pedinho a frase/ texto para o usuário
    key = str(input('Digite a key: ')).upper()  # pedindo a key

    keyFinal = ""  # criação da váriavel para ser utilizada no final
    if len(key) > len(texto):
        print("A key é maior que a frase !") # caso o usuário adicione uma palavra chave maior que a frase aparece esta mensagem
    else:
        i = int(0)
        while len(keyFinal) < len(texto):  # deixando a key do tamanho da frase/palavra a ser criptografada
            keyFinal += key[i]
            i += 1
            if i == len(key):
                i = 0
        for i in range(len(texto)):  # criptografia/ descriptografia de acordo com viginere com alterações
            if texto[i] != ' ':
                posicao_letra_frase = int(abc.index(texto[i]))
                posicao_letra_chave = int(abc.index(keyFinal[i]))
                if opcao == 1:
                    Textofinal += str(abc[(posicao_letra_frase + posicao_letra_chave) % len(abc)])
                else:
                    Textofinal += str(abc[(posicao_letra_frase - posicao_letra_chave) % len(abc)])
            else:
                Textofinal += ' '

        print("Frase final: {}".format(Textofinal)) # entregando a criptografia/ descriptografia
        input()
pass
