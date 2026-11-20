"""A04 — complete as funções e teste as cinco notas no terminal."""
def calcular(campos, registro):
    # TODO: normalizar nome/turma e recusar texto vazio.
    nome = campos["nome"].strip()
    turma = campos["turma"].strip()

    if not nome or not turma: #identificação se eles estão vazios
        return "Preencha o que faltou."
    
    # TODO: conferir a presença de exatamente cinco notas.
    if len(campos["notas"]) != 5:
        return "Informe cinco notas."
    
    # TODO: converter cada texto, validar de 0 a 10 e criar uma nova lista.
    notas = []
    for texto in campos["notas"]:
        texto = texto.strip()

        if not texto:
            return "As cinco notas devem ser preenchidas."

        try:
            numero = float(texto.replace(",", ".")) #para o texto se transformar em número
        except ValueError:
            return "Preencha as notas corretamente."

        if numero < 0 or numero > 10:
            return "As notas precisam estar entre 0 e 10"

        notas.append(numero) #nota convertida indo para a lista nova

    # TODO: calcular a média com sum e len.
    media = sum(notas) / len(notas)

    # TODO: confirmar nome, turma, notas e média somente após validar tudo.
    registro.clear()
    registro.update({
        "nome": nome,
        "turma": turma,
        "notas": notas,
        "media": media
    })  #registro dos dados só pra depois das validações aqui

    return "Média calculada."


def exibir(registro):
    # TODO: tratar ausência; consultar apenas o último registro confirmado.
    if not registro:
        return "Nenhuma média calculada."

    # TODO: mostrar identificação e cinco notas usadas, com média em uma casa.
    notas_texto = ", ".join(str(nota) for nota in registro["notas"])
    return (
        f"Nome: {registro['nome']}\n"
        f"Turma: {registro['turma']}\n"
        f"Notas: {notas_texto}\n"
        f"Média: {registro['media']:.1f}"
    )


def limpar(campos):
    # TODO: esvaziar nome, turma e os cinco textos de notas.
    # O registro confirmado não é recebido por esta função.
    campos["nome"] = ""
    campos["turma"] = ""
    campos["notas"] = ["", "", "", "", ""] #a limpeza dos campos em ediçao


if __name__ == "__main__":
    campos = {"nome": "Lia", "turma": "T1", "notas": ["6", "7", "8", "9", "10"]}
    registro = {}
    print(exibir(registro))
    print(calcular(campos, registro))
    print(exibir(registro))
    # Acrescente as sequências da matriz, prevendo antes de executar.

    #campos["nome"] = "Rui"
    #campos["turma"] = "T2"
    #campos["notas"] = ["5", "5", "5", "5", "aaa"] #teste de erro depois de calcular
    #print(calcular(campos, registro))
    #print(exibir(registro))

    #campos["notas"][4] = "5"
    #print(calcular(campos, registro)) #correçao de nota
    #print(exibir(registro))

    #campos["notas"] = ["6", "7", "8", "9"]
    #print(calcular(campos, registro))
    #campos["notas"] = ["6", "7", "8", "9", "10", "10"] # Teste de lista com quantidade errada
    #print(calcular(campos, registro))

    #limpar(campos)
    #print("Campos depois de limpar:", campos) # Teste de limpeza sem apagar o registro confirmado
    #print(exibir(registro))
