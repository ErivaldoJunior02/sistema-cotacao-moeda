import requests

def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"http://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f"{codigo_moeda}BRL"]['bid']
        return cotacao
    except:
        print("Codigo de Moeda Inválido")
        return None