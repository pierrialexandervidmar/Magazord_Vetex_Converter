import pandas as pd

separador_csv = ';'
valor_peso_minimo = 301
valor_peso_maximo = 30001

caminho_arquivo = 'tabela.xlsx'
df = pd.read_excel(caminho_arquivo)

novo_df = pd.DataFrame(columns=['Localidade', 'Precos'])  # Novo DataFrame com a coluna 'Localidade'
linha_atual = []  # Lista para acumular os valores da coluna "preco"
local = None

for index, row in df.iterrows():
    if row['peso'] == valor_peso_minimo:
        local = str(row['localidade'])
        
    # Adiciona o valor da coluna 'preco' a linha_atual
    linha_atual.append(str(row['preco']))

    if row['peso'] == valor_peso_maximo:
        # Cria um novo dataframe com os valores acumulados na linha_atual separados por ; e concatena o 'novo_df'
        #novo_df = pd.concat([novo_df, pd.DataFrame({'Localidade': [row['localidade']], 'Precos': [';'.join(linha_atual[::1])]}, index=[0])], ignore_index=True)
        novo_df = pd.concat([novo_df, pd.DataFrame({'Localidade': [local], 'Precos': [';'.join(map(str, linha_atual))]})], ignore_index=True)

        linha_atual = []
        local = None

print(novo_df)

novo_caminho_arquivo = 'novo_arquivo.csv'
novo_df.to_csv(novo_caminho_arquivo, index=False, sep=separador_csv)