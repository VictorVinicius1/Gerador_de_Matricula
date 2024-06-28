import random
import string
def gerar_matricula(cpf_aluno):
    cod = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
    matricula = (cpf_aluno[:3]) + cod + (str(random.randint(0, 999)))


def cadastrar_aluno():
    while True:
        aluno = input('digite o nome do aluno ou 0 para retornar: ')
        if aluno == '0':
            break
        elif aluno.isalpha() == False:
            print('Nome invalido Tente Novamente')
        else:
            while True:
                cpf = input('digite o cpf do aluno sem caracteres especiais ou 0 para retornar: ')
                if cpf == '0':
                    break
                elif cpf.isnumeric() and len(cpf) == 11:
                    int(cpf)
                    # comando = ('INSERT INTO Alunos (nome,cpf))
                    gerar_matricula(cpf)
                    print("\n"*100)
                    print(f'{cpf} cadastrado')
                    break
                else:
                    print('cpf invalido')


def consultar_aluno():
    consulta = input('Informe o cpf do aluno: ')
    '''for aluno in alunos:
        if aluno[1] == consulta:
                print(f'aluno: {aluno[0]} possui o cpf: {aluno[1]} ')
        else:
            print('Aluno nao encontrado')'''

