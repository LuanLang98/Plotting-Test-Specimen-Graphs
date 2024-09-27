Plotagem de Gráficos de Testes de Provetes
Este repositório contém scripts em Python que permitem a plotagem de gráficos a partir de dados experimentais de testes de provetes. Os dados são carregados de arquivos CSV e os gráficos são gerados para análise de força, deformação, tensão, deslocamento e outros parâmetros relacionados aos testes mecânicos. Este README descreve o funcionamento de cada código, bem como as instruções de uso.

Funcionalidade Geral
Os scripts neste repositório são projetados para:

Carregar múltiplos arquivos CSV.
Processar e limpar os dados, removendo valores duplicados e permitindo ao usuário excluir pontos finais indesejados.
Plotar gráficos de múltiplos testes, destacando valores máximos e calculando a média e o desvio padrão quando aplicável.
Exportar a média dos dados para arquivos CSV.
Ajustar as escalas dos eixos e personalizar os títulos e legendas dos gráficos.

Scripts

1. Provetes_cod_melhorado_Graph_melhorado.py
Esse script carrega múltiplos arquivos CSV e gera gráficos comparativos de dados de deformação e tensão ou outros parâmetros de medição. O usuário pode:

Selecionar colunas para o eixo X e Y.
Remover manualmente pontos finais dos gráficos.
Destacar o valor máximo de cada teste.
Plotar a média e o desvio padrão dos valores em gráficos adicionais.
Como usar:
Execute o script e selecione os arquivos CSV que contêm os dados de interesse.
Escolha as colunas a serem plotadas nos eixos X e Y.
Ajuste o título do gráfico, e se necessário, remova os pontos finais.
O gráfico será exibido com as opções selecionadas, incluindo a média e desvio padrão (se habilitado).
O usuário pode salvar os resultados como arquivos CSV contendo a média.

2. Provetes_cod_melhorado_Graph_melhorado_Força_Desloc.py
Semelhante ao código anterior, esse script é específico para plotagem de gráficos de força vs deslocamento. Ele também permite:

Plotagem dos testes selecionados.
Cálculo e exibição da média e desvio padrão.
Ajuste das escalas dos eixos para força e deslocamento com intervalos predefinidos.
Como usar:
O procedimento de uso é semelhante ao primeiro código, mas este script é otimizado para plotagens de força e deslocamento, com intervalos e ajustes específicos para esses parâmetros.

3. teste_media_melhorado.py
Este script foca em gerar a média de diferentes testes e visualizá-la em um gráfico. O código:

Permite ao usuário selecionar múltiplos arquivos CSV.
Gera um gráfico de média de força e deformação para os testes selecionados.
Como usar:
O usuário seleciona os arquivos CSV e define o título do gráfico.
O script processa os arquivos e plota a média dos testes selecionados.
A média pode ser salva em um arquivo CSV.
4. testes_praticos_melhorado.py
Este script é voltado para a análise prática de testes mecânicos, permitindo a comparação de vários testes e a exibição de resultados de força e deslocamento. Inclui funções para destacar o valor máximo de cada teste e calcular médias e desvios padrão.

Como usar:
O usuário seleciona os arquivos CSV contendo os dados dos testes.
O script permite a seleção de colunas para plotagem, remoção de pontos finais e visualização dos resultados.
Inclui opções para exibir a média e o desvio padrão em gráficos.
5. Cod_Provetes_2x_Graph_melhorado.py
Este código permite a plotagem de gráficos de testes agrupados. Cada par de testes é agrupado e plotado em uma única linha, permitindo comparar dois testes por vez. Isso é útil para comparar séries de testes semelhantes.

Como usar:
O script agrupa os testes de dois em dois, comparando-os lado a lado.
Permite salvar a média dos resultados agrupados.
6. medias_garras_testes_praticos_melhorado.py
Esse código é dedicado à comparação de diferentes formatos de garras em testes mecânicos. Ele permite plotar e comparar os dados de testes realizados com diferentes configurações de garras.

Como usar:
O usuário seleciona os arquivos CSV correspondentes aos testes de cada tipo de garra.
O script plota os resultados para comparação e calcula a média dos testes para cada tipo de garra.

Dependências
Os scripts utilizam as seguintes bibliotecas Python:

pandas: Para manipulação e análise de dados em arquivos CSV.
matplotlib: Para gerar gráficos.
numpy: Para cálculos matemáticos, como a interpolação e cálculo da média e desvio padrão.
tkinter: Para interfaces gráficas que permitem ao usuário selecionar arquivos e ajustar configurações de plotagem.
Para instalar as dependências, execute:

pip install pandas matplotlib numpy

Como Executar os Scripts
Clone este repositório para a sua máquina local.
Instale as dependências listadas acima.

Execute o script desejado usando Python:

cd localização_da_pasta_do_código
python nome_do_script.py
Siga as instruções da interface gráfica para carregar os arquivos CSV e gerar os gráficos.

Feito por Luan Matheus Capeletti Lang