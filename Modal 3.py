import datetime
from time import sleep
from colorama import Style


def remover_caracteres_indesejados(entrada):
    entrada_sem_caracteres = entrada.replace(' ', '').replace('.', '').replace(',', '')
    return entrada_sem_caracteres


def print_cabecalho():
    print("*-*" * 25)
    print(f"{'SISTEMA DE EMPRÉSTIMO':^75}")
    print("*-*" * 25)


def obter_dados():
    nome = input('\nNome do colaborador: ')

    while True:
        dt_admissao_str = input('\nData da admissão (DD/MM/AAAA): ')
        try:
            datetime.datetime.strptime(dt_admissao_str, '%d/%m/%Y')
            break
        except ValueError:
            print("\nFormato de data incorreto. Por favor, insira a data no formato DD/MM/AAAA.")

    salario_atual = float(remover_caracteres_indesejados(input('\nSalário atual: ')))

    while True:
        emprestimo = float(remover_caracteres_indesejados(input('\nValor pretendido do empréstimo: ')))
        if emprestimo % 2 != 0:
            print('\nInsira um valor válido.')
        else:
            break

    limite_emprestimo = salario_atual * 2
    return nome, dt_admissao_str, salario_atual, emprestimo, limite_emprestimo


def manipulacao_data(dt_admissao_str):
    dt_admissao = datetime.datetime.strptime(dt_admissao_str, '%d/%m/%Y').date()
    data_atual = datetime.date.today()
    tempo_de_servico = data_atual - dt_admissao
    tempo_minimo = datetime.timedelta(days=365 * 2)
    return tempo_de_servico, tempo_minimo


def opcao_1(emprestimo):
    print('1- Notas de maior valor')
    qtd_notas_100 = emprestimo // 100
    if qtd_notas_100 > 0:
        print(f'{int(qtd_notas_100)} x 100 reais')
    qtd_notas_50 = (emprestimo % 100) // 50
    if qtd_notas_50 > 0:
        print(f'{int(qtd_notas_50)} x 50 reais')
    qtd_notas_20 = (emprestimo % 50) // 20
    if qtd_notas_20 > 0:
        print(f'{int(qtd_notas_20)} x 20 reais')
    qtd_notas_5 = (emprestimo % 20) // 5
    if qtd_notas_5 > 0:
        print(f'{int(qtd_notas_5)} x 5 reais')
    qtd_notas_2=(emprestimo % 5) // 2
    if qtd_notas_2>0:
        print(f'{int(qtd_notas_2)} x 2 reais')
    print('\n')


def opcao_2(emprestimo):
    print('2- Notas de menor valor')
    qtd_notas_20 = emprestimo // 20
    if qtd_notas_20 > 0:
        print(f'{int(qtd_notas_20)} x 20 reais')
    qtd_notas_10 = (emprestimo % 20) // 10
    if qtd_notas_10 > 0:
        print(f'{int(qtd_notas_10)} x 10 reais')
    qtd_notas_5 = (emprestimo % 10) // 5
    if qtd_notas_5 > 0:
        print(f'{int(qtd_notas_5)} x 5 reais')
    qtd_notas_2 = (emprestimo % 5) // 2
    if qtd_notas_2 > 0:
        print(f'{int(qtd_notas_2)} x 2 reais')
    print('\n')


def opcao_3(emprestimo):
    print('3- Notas meio a meio\n')
    print(f'{int(emprestimo / 2)} reais em notas de maior valor')
    qtd_notas_100 = emprestimo // 100
    if qtd_notas_100 > 0:
        print(f'{int(qtd_notas_100)} x 100 reais')
    qtd_notas_50 = (emprestimo % 100) // 50
    if qtd_notas_50 > 0:
        print(f'{int(qtd_notas_50)} x 50 reais')
    qtd_notas_20 = (emprestimo % 50) // 20
    if qtd_notas_20 > 0:
        print(f'{int(qtd_notas_20)} x 20 reais')
    qtd_notas_5 = (emprestimo % 20) // 5
    if qtd_notas_5 > 0:
        print(f'{int(qtd_notas_5)} x 5 reais')
    qtd_notas_2 = (emprestimo % 5) // 2
    if qtd_notas_2 > 0:
        print(f'{int(qtd_notas_2)} x 2 reais')
    print(f'\n{int(emprestimo / 2)} reais em notas de menor valor')
    qtd_notas_20 = emprestimo // 20
    if qtd_notas_20 > 0:
        print(f'{int(qtd_notas_20)} x 20 reais')
    qtd_notas_10 = (emprestimo % 20) // 10
    if qtd_notas_10 > 0:
        print(f'{int(qtd_notas_10)} x 10 reais')
    qtd_notas_5 = (emprestimo % 10) // 5
    if qtd_notas_5 > 0:
        print(f'{int(qtd_notas_5)} x 5 reais')
    qtd_notas_2 = (emprestimo % 5) // 2
    if qtd_notas_2 > 0:
        print(f'{int(qtd_notas_2)} x 2 reais')
    print('\n')


def saque(emprestimo, opcao):
    if opcao == 1:
        opcao_1(emprestimo)
    elif opcao == 2:
        opcao_2(emprestimo)
    elif opcao == 3:
        opcao_3(emprestimo)
    elif opcao == 4:
        print('\nOpcao inválida. Tente novamente.')


def main():

    print_cabecalho()
    nome, dt_admissao_str, salario_atual, emprestimo, limite_emprestimo = obter_dados()
    tempo_de_servico, tempo_minimo = manipulacao_data(dt_admissao_str)
    if tempo_de_servico < tempo_minimo or emprestimo > limite_emprestimo:
        print('\nAgradecemos seu interesse, mas você não atende os requisitos mínimos do programa.')
        exit()
    print('\nHá três opções para saque desse valor:\n')
    opcao_1(emprestimo)
    opcao_2(emprestimo)
    opcao_3(emprestimo)
    while True:
        opcao = int(input('Digite a opção escolhida (1, 2 ou 3): '))
        print(f'\nOpção escolhida: {opcao}')
        if opcao == 1:
            opcao_1(emprestimo)
            break
        elif opcao == 2:
            opcao_2(emprestimo)
            break
        elif opcao == 3:
            opcao_3(emprestimo)
            break
        else:
            print('Opção inválida. Tente novamente.')

    print('\nCalculando cédulas ...')
    sleep(1)
    print('\nOperação concluída com sucesso.\nRetire as cédulas no local indicado.\nVolte sempre!')

if __name__ == "__main__":
    main()
