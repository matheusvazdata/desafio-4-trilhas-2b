import pandas as pd
import unidecode


def carregar_dados(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)


def renomear_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        unidecode.unidecode(col)
        .strip()
        .lower()
        .replace(' ', '_')
        .replace('-', '_')
        for col in df.columns
    ]
    return df


def corrigir_genero(df: pd.DataFrame) -> pd.DataFrame:
    df['genero'] = df['genero'].str.strip().str.lower()
    df['genero'] = df['genero'].replace({
        'mas': 'masculino', 'm': 'masculino',
        'fem': 'feminino', 'f': 'feminino'
    })
    df['genero'] = df['genero'].apply(lambda x: x if x in ['masculino', 'feminino'] else 'nao_informado')
    return df


def corrigir_estado(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza a coluna de estado. 
    Mantém CE, MA e PI. Agrupa outros estados válidos como 'outro_estado'. 
    Valores inválidos viram 'sem_estado'.
    """
    principais = {'PI', 'CE', 'MA'}

    siglas_validas = {
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
        'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
        'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    }

    df['estado'] = df['estado'].str.strip().str.upper()

    def categorizar_estado(sigla):
        if sigla in principais:
            return sigla
        elif sigla in siglas_validas:
            return 'outro_estado'
        else:
            return 'sem_estado'

    df['estado'] = df['estado'].apply(categorizar_estado)
    return df


def remover_duplicatas(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def tratar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna('nao_informado')
    return df


def tratar_outliers_iqr(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    for col in colunas:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        limite_inf = q1 - 1.5 * iqr
        limite_sup = q3 + 1.5 * iqr
        df[col] = df[col].clip(lower=limite_inf, upper=limite_sup)
    return df