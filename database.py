# database.py

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def conectar():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Erro de conexão: {e}")
        return None

def criar_tabela():
    conn = conectar()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS tb_produtos (
                id_produto         INT(9) AUTO_INCREMENT PRIMARY KEY,
                descricao_produto  VARCHAR(60) NOT NULL,
                categoria          VARCHAR(25) NOT NULL,
                valor_compra       DECIMAL(10,2) NOT NULL,
                lucro_obtido       DECIMAL(10,2) NOT NULL,
                valor_venda        DECIMAL(10,2) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cursor.execute(sql)
        conn.commit()
        return True
    except Error:
        return False
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def inserir_produto(descricao, categoria, valor_compra, valor_venda):
    lucro = round(valor_venda * 0.20, 2)
    conn = conectar()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO tb_produtos 
                 (descricao_produto, categoria, valor_compra, lucro_obtido, valor_venda)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (descricao, categoria, valor_compra, lucro, valor_venda))
        conn.commit()
        print(f"Produto cadastrado com sucesso! ID: {cursor.lastrowid}")
        return True
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def listar_produtos():
    conn = conectar()
    if not conn:
        return
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_produtos ORDER BY id_produto")
        produtos = cursor.fetchall()
        
        if not produtos:
            print("NENHUM PRODUTO CADASTRADO AINDA.")
            return

        print("\n  ID    PRODUTO                        CATEGORIA       COMPRA      VENDA      LUCRO")
        print("  _________________________________________________________________________________")

        for p in produtos:
            desc = p['descricao_produto'][:28]
            cat = p['categoria'][:14]
            print(f"  {p['id_produto']:<4}  {desc:<28}  {cat:<14}  "
                  f"R${float(p['valor_compra']):>7.2f}   "
                  f"R${float(p['valor_venda']):>7.2f}   "
                  f"R${float(p['lucro_obtido']):>6.2f}")

        print("  _________________________________________________________________________________")
        
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def alterar_produto():
    listar_produtos()
    try:
        idp = int(input("\nDigite o ID do produto que deseja alterar: "))
        print("Deixe em branco para manter o valor atual.")
        
        desc = input("Nova descrição: ").strip()
        cat = input("Nova categoria: ").strip()
        compra = input("Novo valor de compra: ").strip()
        venda = input("Novo valor de venda: ").strip()
        
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_produtos WHERE id_produto = %s", (idp,))
        prod = cursor.fetchone()
        
        if not prod:
            print("Produto não encontrado.")
            return
        
        desc = desc if desc else prod['descricao_produto']
        cat = cat if cat else prod['categoria']
        vcompra = float(compra) if compra else float(prod['valor_compra'])
        vvenda = float(venda) if venda else float(prod['valor_venda'])
        lucro = round(vvenda * 0.20, 2)
        
        sql = """UPDATE tb_produtos SET descricao_produto=%s, categoria=%s,
                 valor_compra=%s, lucro_obtido=%s, valor_venda=%s WHERE id_produto=%s"""
        cursor.execute(sql, (desc, cat, vcompra, lucro, vvenda, idp))
        conn.commit()
        print(f"Produto ID {idp} alterado com sucesso!")
    except:
        print("Erro ao alterar produto.")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def excluir_produto():
    listar_produtos()
    try:
        ids = input("\nDigite o(s) ID(s) que deseja excluir (separados por vírgula): ").strip()
        
        if not ids:
            print("Nenhum ID informado.")
            return
        
        id_list = [int(x.strip()) for x in ids.split(",") if x.strip().isdigit()]
        
        if not id_list:
            print("Nenhum ID válido informado.")
            return
        
        if len(id_list) == 1:
            confirmar = input(f"Confirmar exclusão do ID {id_list[0]}? (S/N): ").strip().upper()
        else:
            confirmar = input(f"Confirmar exclusão dos IDs {id_list}? (S/N): ").strip().upper()
        
        if confirmar != 'S':
            print("Exclusão cancelada.")
            return
        
        conn = conectar()
        if not conn:
            return
        
        cursor = conn.cursor()
        format_ids = ','.join(['%s'] * len(id_list))
        sql = f"DELETE FROM tb_produtos WHERE id_produto IN ({format_ids})"
        cursor.execute(sql, id_list)
        conn.commit()
        
        print(f"{cursor.rowcount} produto(s) excluído(s) com sucesso!")
        
    except ValueError:
        print("Por favor, digite apenas números separados por vírgula.")
    except Exception as e:
        print(f"Erro ao excluir: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()