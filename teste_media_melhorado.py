#Código desenvolvido por Luan Matheus Capeletti Lang

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def plot_csv_files():
    # Inicializa a interface de seleção de arquivos
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    
    # Pede ao usuário para selecionar arquivos CSV
    file_paths = filedialog.askopenfilenames(title="Selecione arquivos CSV", filetypes=[("CSV files", "*.csv")])
    
    # Verifica se o usuário selecionou arquivos
    if not file_paths:
        print("Nenhum arquivo selecionado.")
        return
    
    # Pede ao usuário para inserir o título do gráfico
    title = input("Por favor, insira o título do gráfico: ")
    
    # Inicializa uma figura para o gráfico
    plt.figure(figsize=(10, 6))
    
    for file_path in file_paths:
        success = False
        for encoding in ['utf-8', 'latin1']:
            if success:
                break
            for delimiter in [',', ';', '\t']:
                try:
                    df = pd.read_csv(file_path, encoding=encoding, delimiter=delimiter, skiprows=1)
                    success = True
                    break
                except (UnicodeDecodeError, pd.errors.ParserError):
                    continue
        
        if not success:
            print(f"Não foi possível ler o arquivo {file_path} com as codificações 'utf-8' ou 'latin1' e delimitadores ',', ';' ou tabulação.")
            continue
        
        # Verifica se o DataFrame tem pelo menos duas colunas para plotar
        if df.shape[1] < 2:
            print(f"Arquivo {file_path} não tem colunas suficientes para plotar.")
            continue
        
        # Pega os nomes das colunas
        x_col = df.columns[0]
        y_col = df.columns[1]

        # Converte as colunas para float
        try:
            df[x_col] = pd.to_numeric(df[x_col], errors='coerce')
            df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
        except ValueError:
            print(f"Erro ao converter colunas para numérico no arquivo {file_path}.")
            continue

        # Remove linhas com dados inválidos
        df = df.dropna(subset=[x_col, y_col])

        if df.empty:
            print(f"Arquivo {file_path} não tem dados válidos para plotar após limpeza.")
            continue
        
        # Pede ao usuário para inserir o nome da legenda para o arquivo
        legend_name = input(f"Por favor, insira o nome da legenda para o arquivo {file_path}: ")
        
        # Plota os dados do arquivo
        plt.plot(df[x_col].astype(float), df[y_col].astype(float), label=legend_name)
    
    # Configurações do gráfico
    plt.xlabel('Deformação (%)')
    plt.ylabel('Tensão (N/mm²)')
    plt.title(title)
    plt.legend(loc='upper left')
    plt.grid(True)
    
    # Definindo os intervalos do eixo X e Y
    plt.xticks(range(0, 1100, 100))  # Intervalos de 100 em 100 no eixo X
    plt.yticks(range(0, 15, 1))     # Intervalos de 1 em 1 no eixo Y
    
    # Garantindo que os eixos comecem em 0
    plt.xlim(left=0)  # Eixo X começa em 0
    plt.ylim(bottom=0)  # Eixo Y começa em 0
    
    # Mostra o gráfico
    plt.show()

# Executa a função
plot_csv_files()
