import functions

import mysql.connector as conector

cnx = conector.connect(user='root',password='',host='127.0.0.1',database='Curso')
cnx.cursor()

cnx.close()

print('Bem vindo ao banco de cadastro e consulta de alunos, digite o numero equivalente a opção desejada:' )
while True:
    escolha = input('1 para cadastrar, 2 para consultar, 3 para consultar todos ou 0 para sair: ')
    if escolha == '0':
        break
    elif escolha == '1':
        functions.cadastrar_aluno()
    elif escolha == '2':
        print('em breve')
    elif escolha == '3':
        print('em breve')
    else:
        print('Esse sistema e aprova de idiotas nao seja um e tente novamente')




                    


