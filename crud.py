import sqlite3

conexao = sqlite3.connect('E:\\dbpessoas.db')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS 'pessoas'(codpessoa INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")

def cadastrar():
    nome = input('Nome: ')
    idade = input('Idade: ')
    cursor.execute("insert into pessoas(nome, idade) values('"+nome+"',"+idade+")")
    print(nome + ', '+ idade+' anos - Cadastrado Com Sucesso!\n')

def listarCadastros():
    print('\nTodos os cadastrados: ')
    cursor.execute('select * from pessoas')
    for row in cursor.fetchall():
        print('Cod: ' + str(row[0]) +', '+ row[1] + ' '+ str(row[2])+' anos')
    print()

def atualizarCadastro():
    listarCadastros()
    codigo = input('Informe o código da pessoa que deseja alterar: ')
    nome = input('Informe o novo nome: ')
    idade = input('Informe a nova idade: ')
    try:
        cursor.execute('update pessoas set nome = "'+nome+'", idade = '+idade+' where codpessoa = '+codigo+'')
        print('Cod: ' + str(codigo) +', '+ nome + ' '+ str(idade)+' anos - Atualizado Com Sucesso!\n')
    except:
        print('erro! ')
    
def apagarCadastro():
    listarCadastros()
    codigo = input('Informe o código da pessoa que deseja apagar: ')
    cursor.execute('select nome, idade from pessoas where codpessoa = '+codigo+'')
    for row in cursor.fetchall():
        nome = row[0]
        idade = row[1]
    confirmacao = input('tem certeza que deseja apagar '+ str(nome) + '? \n"s" ou "n"? ')
    if confirmacao == 's':
        cursor.execute('delete from pessoas where codpessoa = '+codigo+'')
        print('Cod: ' + str(codigo) +', '+ nome + ' '+str(idade)+' anos - Apagado Com Sucesso!\n')
    else:
        print('Operação cancelada!')


while True:
    cursor = conexao.cursor()

    option = input('O que deseja fazer:\n"c" --> Create\n"r" --> Read\n"u" --> Update\n"d" --> Delete\n"s" --> Sair\nOpção: ')
    if option == 'c':
        cadastrar()
    elif option == 'r':
        listarCadastros()
    elif option == 'u':
        atualizarCadastro()
    elif option == 'd':
        apagarCadastro()

    conexao.commit()
    cursor.close()   

    if option == 's' or option == 'S':
        break
    elif option not in ('c','r','u','d'):
        print('\nOpção invalida, tente novamente')

