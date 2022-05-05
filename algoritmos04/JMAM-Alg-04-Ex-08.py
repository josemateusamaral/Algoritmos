mensagem = input('Digite uma mensagem para ser codificada: ')
deslocamento = int(input('Deslocamento da codificação: '))
mensagemCodificada = ''
for caractere in mensagem:
    mensagemCodificada += chr(( ord(caractere) + deslocamento ))
print('A mensagem decodificada ficou: ',mensagemCodificada)
