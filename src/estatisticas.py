import pandas as pd


def media_mediana_por_idade(df: pd.DataFrame, idade_limite: int = 40) -> pd.DataFrame:
    menores = df[df['idade'] < idade_limite]
    maiores = df[df['idade'] >= idade_limite]

    return pd.DataFrame([
        {'faixa_etaria': '< 40', 'media_saldo': round(menores['saldo_na_conta'].mean(), 2), 'mediana_saldo': round(menores['saldo_na_conta'].median(), 2)},
        {'faixa_etaria': '>= 40', 'media_saldo': round(maiores['saldo_na_conta'].mean(), 2), 'mediana_saldo': round(maiores['saldo_na_conta'].median(), 2)}
    ])


def media_mediana_por_saida(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([
        {'situacao': 'saiu', 'media_saldo': round(df[df['saiu'] == 1]['saldo_na_conta'].mean(), 2),
         'mediana_saldo': round(df[df['saiu'] == 1]['saldo_na_conta'].median(), 2)},
        {'situacao': 'ficou', 'media_saldo': round(df[df['saiu'] == 0]['saldo_na_conta'].mean(), 2),
         'mediana_saldo': round(df[df['saiu'] == 0]['saldo_na_conta'].median(), 2)},
    ])


def perfil_clientes_que_saem(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    saiu = df[df['saiu'] == 1]
    agrupado = saiu.groupby(['genero', 'estado']).agg({
        'idade': 'median',
        'saldo_na_conta': 'mean',
        'bens': 'mean',
        'saiu': 'count'
    }).rename(columns={
        'idade': 'idade_mediana',
        'saldo_na_conta': 'saldo_medio',
        'bens': 'bens_medio',
        'saiu': 'quantidade'
    }).sort_values(by='quantidade', ascending=False).reset_index()

    agrupado['saldo_medio'] = agrupado['saldo_medio'].round(2)
    agrupado['bens_medio'] = agrupado['bens_medio'].round(2)

    return agrupado.head(top_n)