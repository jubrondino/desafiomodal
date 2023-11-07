from datetime import datetime

def extrair_mes(data):
    return int(data.split('-')[1])

mes_atual = datetime.today().month

arquivo_geral = 'dados.txt'
arquivo_mes = 'aniversariantes_do_mes.txt'

with open(arquivo_geral, 'r') as arquivo:
    with open(arquivo_mes, 'w') as mes:
        for linha in arquivo:
            dados = linha.strip().split('|')
            if len(dados) >= 3:
                nome_completo, email, data_nascimento = dados
                mes_aniversario = extrair_mes(data_nascimento)
                if mes_aniversario == mes_atual:
                    mes.write(f"{nome_completo} | {email} | {data_nascimento}\n")

print(f"Aniversariantes do mês {mes_atual} foram salvos em '{arquivo_mes}'.")



