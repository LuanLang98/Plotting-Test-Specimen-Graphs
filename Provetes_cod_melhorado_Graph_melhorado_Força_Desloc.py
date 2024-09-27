#Código desenvolvido por Luan Matheus Capeletti Lang

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog

# Mapeamento de colunas para legendas
column_legends = {
    '%': 'Deformação (%)',
    'N/mm2': 'Tensão (N/mm²)',
    'seg': 'Tempo (s)',
    'N': 'Força (N)',
    'mm': 'Deslocamento (mm)'
}

# Função para ler múltiplos arquivos CSV e retornar uma lista de dataframes
def ler_multiplos_csv(caminhos_arquivos):
    dataframes = []
    for caminho in caminhos_arquivos:
        try:
            df = pd.read_csv(caminho, delimiter=',', decimal=',', skipinitialspace=True, encoding='utf-8', skiprows=2)
        except UnicodeDecodeError:
            # Tente uma codificação alternativa
            df = pd.read_csv(caminho, delimiter=',', decimal=',', skipinitialspace=True, encoding='latin1', skiprows=2)
        dataframes.append(df)
    return dataframes

# Função para remover manualmente pontos finais dos gráficos
def remover_pontos_finais(dataframes, x_col, y_col):
    pontos_remover = []
    for i in range(len(dataframes)):
        num_pontos = simpledialog.askinteger("Entrada", f"Quantos pontos finais deseja remover do Teste {i+1}?", minvalue=0, maxvalue=len(dataframes[i][x_col]))
        if num_pontos is None:
            num_pontos = 0
        pontos_remover.append(num_pontos)
    return pontos_remover

# Função para escolher as colunas, destacar o valor máximo e plotar múltiplos dataframes
def escolher_e_plotar_multiplos_colunas(dataframes, x_col_index, y_col_index, plot_choice, graph_title):
    # Selecionar as colunas escolhidas
    x_col = dataframes[0].columns[x_col_index]
    y_col = dataframes[0].columns[y_col_index]

    # Obter legendas das colunas
    x_col_legend = column_legends.get(x_col, x_col)
    y_col_legend = column_legends.get(y_col, y_col)

    # Inicializar uma lista para armazenar os valores x e y de cada dataframe
    x_values = []
    y_values = []
    max_values = []

    # Remover manualmente pontos finais
    pontos_remover = remover_pontos_finais(dataframes, x_col, y_col)

    # Definir limites máximos para padronizar a escala
    max_x_global = 0
    max_y_global = 0

    # Plotar as colunas selecionadas de todos os dataframes
    plt.figure(figsize=(10, 6))
    for i, df in enumerate(dataframes):
        # Verificar se as colunas são numéricas
        if not pd.api.types.is_numeric_dtype(df[x_col]) or not pd.api.types.is_numeric_dtype(df[y_col]):
            messagebox.showerror("Erro", f"Colunas {x_col} e/ou {y_col} não são numéricas.")
            return
        
        x = np.abs(df[x_col].values)
        y = np.abs(df[y_col].values)

        # Remover pontos finais especificados pelo usuário
        if pontos_remover[i] > 0:
            x = x[:-pontos_remover[i]]
            y = y[:-pontos_remover[i]]

        # Garantir que os comprimentos dos dados x e y sejam iguais
        min_length = min(len(x), len(y))
        x = x[:min_length]
        y = y[:min_length]

        # Remover pontos duplicados no eixo X
        unique_indices = np.unique(x, return_index=True)[1]
        x = x[unique_indices]
        y = y[unique_indices]

        # Destacar o valor máximo e imprimir no console
        max_index = y.argmax()
        max_value = y[max_index]
        max_x_value = x[max_index]
        max_values.append((i+1, max_value, max_x_value))
        
        if plot_choice in ['all', 'media_desvio_all']:
            plt.plot(x, y, linestyle='-', linewidth=1, label=f'Teste {i+1} (Ponto Máximo: {max_value:.2f} N/mm² em {max_x_value:.2f} mm)')
            plt.plot(x[max_index], y[max_index], marker='X', color='red', markersize=8)

        x_values.append(x)
        y_values.append(y)

        # Atualizar limites máximos globais
        max_x_global = max(max_x_global, np.max(x))
        max_y_global = max(max_y_global, np.max(y))

    if not x_values or not y_values:
        messagebox.showerror("Erro", "Não foram encontrados dados para plotar.")
        return

    # Garantir que todos os gráficos comecem em zero e usar os mesmos limites para todos
    plt.xlim(0, max_x_global * 1.05)  # Adicione um pequeno espaço extra no eixo X
    plt.ylim(0, max_y_global * 1.05)  # Ajustar limite do eixo Y com base no valor máximo

    # Definir intervalos fixos do eixo X e Y
    plt.yticks(np.arange(0, 70, step=5))  # Define o eixo y com intervalos de 5 a 5
    plt.xticks(np.arange(0, 500, step=100))  # Define o eixo x com intervalos de 100 a 100

    # Calcular a média dos valores y se necessário
    common_x = np.linspace(0, max_x_global, num=500)
    if plot_choice in ['media', 'media_desvio', 'media_desvio_all']:
        y_interpolated = [np.interp(common_x, np.insert(x, 0, 0), np.insert(y, 0, 0)) for x, y in zip(x_values, y_values)]
        y_values_mean = np.mean(y_interpolated, axis=0)
        
        # Encontrar a força máxima da média e seu deslocamento correspondente
        max_index_mean = y_values_mean.argmax()
        max_value_mean = y_values_mean[max_index_mean]
        max_x_value_mean = common_x[max_index_mean]
        
        # Atualizar a legenda com a força máxima e o deslocamento correspondente
        plt.plot(common_x, y_values_mean, linestyle='--', color='black', linewidth=1,
                 label=f'Média (Ponto Máximo: {max_value_mean:.2f} N em {max_x_value_mean:.2f} mm)')
        
        # Exibir o ponto máximo no gráfico
        plt.plot(max_x_value_mean, max_value_mean, marker='X', color='blue', markersize=8)

        # Solicitar ao usuário o nome do arquivo para salvar a média
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar Média como CSV")
        if save_path:
            media_df = pd.DataFrame({'Deslocamento (mm)': common_x, 'Força Média (N)': y_values_mean})
            media_df.to_csv(save_path, index=False)

    # Plotar o desvio padrão como área sombreada se necessário
    if plot_choice in ['desvio', 'media_desvio', 'media_desvio_all']:
        y_interpolated = [np.interp(common_x, np.insert(x, 0, 0), np.insert(y, 0, 0)) for x, y in zip(x_values, y_values)]
        y_values_mean = np.mean(y_interpolated, axis=0)
        y_values_std = np.std(y_interpolated, axis=0)
        plt.fill_between(common_x, y_values_mean - y_values_std, y_values_mean + y_values_std, color='gray', alpha=0.5, label='Desvio Padrão')

    plt.xlabel(x_col_legend)
    plt.ylabel(y_col_legend)
    
    # Ajuste para o título não ser cortado
    plt.title(graph_title if graph_title else f'{y_col_legend} vs {x_col_legend}', pad=20)
    
    plt.legend(loc='upper left')
    plt.grid(True)

    # Função para ajustar as margens e garantir que a legenda não corte
    plt.tight_layout()  # Ajusta automaticamente as margens para que nada seja cortado
    
    plt.show()

    # Exibir valores máximos em uma janela
    max_values_str = '\n'.join([f'Teste {mv[0]}: Máximo = {mv[1]:.2f} N/mm² em {mv[2]:.2f} mm' for mv in max_values])
    messagebox.showinfo("Valores Máximos", max_values_str)

# Função para abrir o diálogo de seleção de arquivos
def selecionar_arquivos():
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    return list(file_paths)

# Função para iniciar a plotagem com os arquivos selecionados
def iniciar_plotagem():
    global dataframes  # Declare dataframes como global para ser acessível em confirmar_selecao_colunas
    caminhos_arquivos = selecionar_arquivos()
    if not caminhos_arquivos:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
        return

    dataframes = ler_multiplos_csv(caminhos_arquivos)
    
    if not dataframes:
        messagebox.showwarning("Aviso", "Nenhum dado foi lido dos arquivos selecionados.")
        return

    # Atualizar as opções de colunas
    colunas = dataframes[0].columns.tolist()
    colunas_com_indices = [f"{i}: {col}" for i, col in enumerate(colunas)]
    combo_x_col['values'] = colunas_com_indices
    combo_y_col['values'] = colunas_com_indices

    # Mostrar as opções de seleção de colunas e plotagem
    frame_colunas.pack(pady=10)

# Função para confirmar a seleção das colunas e iniciar a plotagem
def confirmar_selecao_colunas():
    x_col_index = combo_x_col.current()
    y_col_index = combo_y_col.current()
    plot_choice = var_plot_choice.get()
    graph_title = entry_titulo.get()

    if x_col_index == -1 or y_col_index == -1:
        messagebox.showwarning("Aviso", "Por favor, selecione ambas as colunas X e Y.")
        return

    escolher_e_plotar_multiplos_colunas(dataframes, x_col_index, y_col_index, plot_choice, graph_title)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Plotagem de Arquivos CSV")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_selecionar = tk.Button(frame, text="Selecionar Arquivos CSV", command=iniciar_plotagem)
btn_selecionar.pack(pady=5)

frame_colunas = tk.Frame(root)

lbl_x_col = tk.Label(frame_colunas, text="Coluna para Eixo X:")
lbl_x_col.grid(row=0, column=0, padx=5, pady=5)

combo_x_col = ttk.Combobox(frame_colunas)
combo_x_col.grid(row=0, column=1, padx=5, pady=5)

lbl_y_col = tk.Label(frame_colunas, text="Coluna para Eixo Y:")
lbl_y_col.grid(row=1, column=0, padx=5, pady=5)

combo_y_col = ttk.Combobox(frame_colunas)
combo_y_col.grid(row=1, column=1, padx=5, pady=5)

lbl_titulo = tk.Label(frame_colunas, text="Título do Gráfico:")
lbl_titulo.grid(row=2, column=0, padx=5, pady=5)

entry_titulo = tk.Entry(frame_colunas)
entry_titulo.grid(row=2, column=1, padx=5, pady=5)

# Radio buttons para a seleção de opções de plotagem
var_plot_choice = tk.StringVar(value="all")
radio_all = tk.Radiobutton(frame_colunas, text="Todos os Testes", variable=var_plot_choice, value="all")
radio_all.grid(row=3, column=0, padx=5, pady=5)

radio_media = tk.Radiobutton(frame_colunas, text="Média", variable=var_plot_choice, value="media")
radio_media.grid(row=3, column=1, padx=5, pady=5)

radio_desvio = tk.Radiobutton(frame_colunas, text="Desvio Padrão", variable=var_plot_choice, value="desvio")
radio_desvio.grid(row=3, column=2, padx=5, pady=5)

radio_media_desvio_all = tk.Radiobutton(frame_colunas, text="Todos + Média + Desvio Padrão", variable=var_plot_choice, value="media_desvio_all")
radio_media_desvio_all.grid(row=3, column=3, padx=5, pady=5)

radio_media_desvio = tk.Radiobutton(frame_colunas, text="Média + Desvio Padrão", variable=var_plot_choice, value="media_desvio")
radio_media_desvio.grid(row=3, column=4, padx=5, pady=5)

btn_confirmar = tk.Button(frame_colunas, text="Confirmar Seleção e Plotar", command=confirmar_selecao_colunas)
btn_confirmar.grid(row=4, columnspan=5, pady=10)

root.mainloop()
