import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


def plot_distribuicao_categorica(df: pd.DataFrame, coluna: str):
    """Exibe gráfico de contagem de uma coluna categórica."""
    plt.figure(figsize=(8, 5))
    ordem = df[coluna].value_counts().index
    sns.countplot(data=df, x=coluna, order=ordem, hue='saiu')
    plt.title(f'Distribuição de {coluna} com status de saída')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()


def boxplot_com_saida(df: pd.DataFrame, coluna: str):
    """Boxplot de uma variável numérica segmentada por status de saída (com cor)."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='saiu', y=coluna, hue='saiu', palette='Set2')
    plt.title(f'Distribuição de {coluna} por saída')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def violinplot_idade_genero(df: pd.DataFrame):
    """Distribuição da idade por gênero com hue de saída."""
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df, x='genero', y='idade', hue='saiu', split=True)
    plt.title('Idade por gênero (com saída)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def histograma_coluna(df: pd.DataFrame, coluna: str, hue='saiu'):
    """Histograma com densidade de uma variável numérica."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=coluna, hue=hue, kde=True)
    plt.title(f'Distribuição de {coluna}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def heatmap_correlacoes(df: pd.DataFrame):
    """Mapa de calor da correlação entre variáveis numéricas (somente triângulo inferior)."""
    plt.figure(figsize=(10, 6))
    corr = df.select_dtypes(include='number').corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))  # Máscara para ocultar parte superior
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', mask=mask, linewidths=0.5)
    plt.title('Correlação entre variáveis numéricas')
    plt.tight_layout()
    plt.show()