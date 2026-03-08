# (l+d) mod26

import getpass

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto = getpass.getpass("Digite a mensagem secreta: ").upper()

d = int(getpass.getpass("Digite a chave de deslocamento: "))

resultado = ""

for caractere in texto:

    if caractere in alfabeto:

        l = alfabeto.index(caractere)

        nova_posicao = (l + d) % 26

        resultado += alfabeto[nova_posicao]

    else:

        resultado += caractere

arquivo_saida = open("segredo_criptografado.txt", "w")

arquivo_saida.write(resultado + "\n")

arquivo_saida.close()

print("Mensagem criptografada com sucesso e salva no arquivo 'segredo_criptografado.txt'.")
