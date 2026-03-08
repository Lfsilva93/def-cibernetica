# (l+d) mod26

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto = input("Digite a mensagem secreta: ").upper()

d = int(input("Digite a chave de deslocamento: "))

resultado = ""

for caractere in texto:
    if caractere in alfabeto:

        l = alfabeto.index(caractere)

        nova_posicao = (l + d) % 26

        resultado += alfabeto[nova_posicao]

    else:
        resultado += caractere

print("Mensagem Criptografada:", resultado)

