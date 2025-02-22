import sqlite3

def criar_tabela():
    #CRIAR BANCO
    conn = sqlite3.connect('banco.sqlite3')
    # cursor object
    cur = conn.cursor()
    # Deletar Tabela existente
    cur.execute(f"DROP TABLE IF EXISTS VIACEP")
    # Criar Tabela
    comando = f""" CREATE TABLE VIACEP (
                CEP VARCHAR(255),
                UNIDADE VARCHAR(255),
                UF VARCHAR(2),
                BAIRRO VARCHAR(255),
                LOCALIDADE VARCHAR(255),
                DDD INT,
                GIA INT,
                ESTADO VARCHAR(255),
                REGIAO VARCHAR(255),
                IBGE INT,
                COMPLEMENTO VARCHAR(255),
                LOGRADOURO VARCHAR(255),
                SIAFI INT
            ); """ 
    cur.execute(comando)
    # Fechar coenxão
    conn.close()

def ver_tabela():
#LER BANCO
    conn = sqlite3.connect('banco.sqlite3')
    # cursor object
    cur = conn.cursor()
    # Criar Tabela
    comando = f""" SELECT * FROM VIACEP """ 
    cur.execute(comando)
    #Retornar todas as linhas
    retorno = cur.fetchall()
    # Fechar coenxão
    conn.close()
    return retorno

def inserir_tabela(cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
    #INSERIR INFORMAÇÕES DO BANCO
    conn = sqlite3.connect('banco.sqlite3')
    # cursor object
    cur = conn.cursor()
    # Criar Tabela
    comando = f"""  INSERT INTO VIACEP (CEP, UNIDADE, UF, BAIRRO, LOCALIDADE, DDD, GIA, ESTADO, REGIAO, IBGE, COMPLEMENTO, LOGRADOURO, SIAFI)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""" 
    value = (cep, unidade, uf, bairro, localidade, ddd, gia, estado, regiao, ibge, complemento, logradouro, siafi)
    cur.execute(comando, value)
    conn.commit()
    # Fechar coenxão
    conn.close()

# criar_tabela()