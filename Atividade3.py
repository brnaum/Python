# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_MB = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_Mbps = float(input("Informe a velocidade da internet (em Mbps): "))
#Converter o arquivo de Megabytes para Megabits
arquivo_Mb = arquivo_MB / 8
#Calcular o tempo em segundos
tempo_segundos = arquivo_Mb / velocidade_Mbps
#Transformar para minutos
tempo_minutos = tempo_segundos / 60
#Valor aproximado
tempo_aproximado = round(tempo_minutos)
print(f"O tempo de download do arquivo informado é de, aproximadamente: {tempo_aproximado} minutos")