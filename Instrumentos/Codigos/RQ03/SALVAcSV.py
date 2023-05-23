import csv

def salvar_em_csv(valores, nome_arquivo, nomes_colunas):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(nomes_colunas)  # Escreve os nomes das colunas
        writer.writerow(valores)  # Escreve os valores


valores = [54.89, 54.63,54.20, 54.20, 54.50]
nomes_colunas = ['Rust', 'Python', 'Go', 'javascript', 'Java']
nome_arquivo = 'Percentual_perguntas_frequentes_2022.csv'

salvar_em_csv(valores, nome_arquivo, nomes_colunas)
