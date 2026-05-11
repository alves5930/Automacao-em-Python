# main.py

from database import criar_tabela, inserir_produto, listar_produtos, alterar_produto, excluir_produto

def cadastrar():
    print("\n" + "═"*70)
    print("                    CADASTRO DE PRODUTO")
    print("═"*70)
    
    desc = input("Descrição do produto: ").strip()
    while not desc:
        desc = input("Descrição obrigatória: ").strip()
    
    cat = input("Categoria: ").strip()
    while not cat:
        cat = input("Categoria obrigatória: ").strip()
    
    while True:
        try:
            compra = float(input("Valor de compra (R$): "))
            venda = float(input("Valor de venda (R$): "))
            if venda > 0:
                break
            print("Valor de venda deve ser maior que zero.")
        except:
            print("Digite valores numéricos válidos.")
    
    inserir_produto(desc, cat, compra, venda)

def menu():
    while True:
        print("\n" + "═"*70)
        print("          SISTEMA DE GERENCIAMENTO DE PRODUTOS")
        print("═"*70)
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Alterar produto")
        print("4. Excluir produto")
        print("5. Sair")
        print("═"*70)
        
        op = input("\nEscolha uma opção (1-5): ").strip()
        
        if op == "1":
            cadastrar()
        elif op == "2":
            listar_produtos()
        elif op == "3":
            alterar_produto()
        elif op == "4":
            excluir_produto()
        elif op == "5":
            print("\nSistema encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    print("Iniciando system.alves")
    if criar_tabela():
        menu()
    else:
        print("Erro ao conectar ao banco de dados. Verifique o XAMPP.")