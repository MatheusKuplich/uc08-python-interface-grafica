"""A03 — complete as funções antes de conectá-las à janela."""
def calcular(campos, registro):
    # TODO: ler reais e as duas cotações; aceitar vírgula ou ponto decimal.
    reais_texto = campos["reais"].strip()
    dolar_texto = campos["cotacao_dolar"].strip()    
    euro_texto = campos["cotacao_euro"].strip()

    
    if not reais_texto or not dolar_texto or not euro_texto: # só pra ver se tem campo vazio
        return "Preencha o que faltou."
    
    try:
        reais = float(reais_texto.replace(",", "."))    # textos para número
        cotacao_dolar = float(dolar_texto.replace(",", "."))
        cotacao_euro = float(euro_texto.replace(",", "."))

    except ValueError:
        return "Preencha os valores corretamente."

    # TODO: tratar conversão inválida, reais negativos e cotações <= 0.
    if reais < 0:
        return "O valor em reais não pode ser negativo."

    if cotacao_dolar <= 0 or cotacao_euro <= 0:
        return "As cotações precisam ser maiores que zero."

    # TODO: dividir reais por cada cotação.
    dolar = reais / cotacao_dolar
    euro = reais / cotacao_euro

    # TODO: confirmar entradas e os dois resultados somente após validar tudo.
    registro.clear()
    registro.update({
        "reais": reais,
        "cotacao_dolar": cotacao_dolar,
        "cotacao_euro": cotacao_euro,
        "dolar": dolar,
        "euro": euro
    })  #registro dos dados só pra depois das validações aqui
    return "Conversão feita."

def exibir(registro):
    # TODO: tratar ausência de conversão; consultar somente registro.
    if not registro:
        return "Nenhuma conversão veio a ser confirmada."

    # TODO: mostrar entradas usadas e resultados, estes com duas casas.
    return (
        f"Valor em reais: R$ {registro['reais']:.2f}\n"
        f"Cotação do dólar: R$ {registro['cotacao_dolar']:.2f}\n"
        f"Cotação do euro: R$ {registro['cotacao_euro']:.2f}\n"
        f"Resultado em dólares: USD {registro['dolar']:.2f}\n"
        f"Resultado em euros: EUR {registro['euro']:.2f}"
    )


def limpar(campos):
    # TODO: esvaziar os três campos; preservar registro e resultados.
    campos["reais"] = ""
    campos["cotacao_dolar"] = ""
    campos["cotacao_euro"] = ""  #limpando os campos em edição


if __name__ == "__main__":
    campos = {"reais": "100", "cotacao_dolar": "5", "cotacao_euro": "4"}
    registro = {}
    print(exibir(registro))
    print(calcular(campos, registro))
    print(exibir(registro))
    # Acrescente as outras sequências da matriz, prevendo antes de executar.
    
    campos["reais"] = "200" # testando uma tentativa inválida para ver se mantém o cálculo anterior
    campos["cotacao_dolar"] = "10"
    campos["cotacao_euro"] = "aaa"

    print(calcular(campos, registro))
    print(exibir(registro))

    limpar(campos)
    print(campos)   # testando a limpeza sem apagar o último cálculo confirmado
    print(exibir(registro))
