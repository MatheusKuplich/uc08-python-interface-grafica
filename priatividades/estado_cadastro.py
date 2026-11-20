"""A02 — prática 1: campos em edição e registro confirmado."""

def registrar(campos, registro):
    nome = campos["nome"].strip()
    sobrenome = campos["sobrenome"].strip() #removendo os vazios das extremidades
    idade = campos["idade"].strip()

    # TODO: ler e normalizar nome e sobrenome; recusar texto vazio.
    if not nome or not sobrenome:
        return "Preencha nome e sobrenome."

    # TODO: converter idade e validar inteiro maior que zero.

    
    try:
        idade = int(idade)  #fazendo a idade passar a ser um inteiro
    except ValueError:  #impedindo que idades com letras passem pelo sistema
        return "Preencha a idade corretamente, parceiro."

    if idade <= 0:
        return "Novo demais... suspeito."

    # TODO: atualizar registro somente depois de todas as validações.
    registro.clear()
    registro.update({   #atualizando o dicionario depois das validações
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade
    })
    return "Registro completo."


def exibir(registro):
    # TODO: tratar a ausência de registro e consultar o último válido.
    if not registro:
        return "Nada foi confirmado."

    return (
        f"Nome: {registro['nome']}\n"
        f"Sobrenome: {registro['sobrenome']}\n"
        f"Idade: {registro['idade']}"
    )

def limpar(campos):
    # TODO: esvaziar os três textos editáveis.
    # O registro confirmado é separado e não é recebido por esta função.
    campos["nome"] = ""
    campos["sobrenome"] = ""
    campos["idade"] = ""

if __name__ == "__main__":
    # campos = {"nome": "Lia", "sobrenome": "Costa", "idade": "18"}
    campos = {"nome": "Lia", "sobrenome": "Costa", "idade": "18"}
    registro = {}

   # Exibindo sem registro, informando ausência:
    #print(exibir(registro))


    # Um válido sendo consultado:
    #print(registrar(campos, registro))
    #print(exibir(registro))

    # Limpeza de campos: 
    #limpar(campos)
    #print("Campos após limpar:", campos)
    #print(exibir(registro))

    # Dados invalidos:
    #campos = {"nome": "Rui", "sobrenome": "Lima", "idade": "aaa"}
    #print(registrar(campos, registro))
    #print(exibir(registro))

    # Novo válido e substituindo:
    #campos = {"nome": "Rui", "sobrenome": "Lima", "idade": "25"}
    #print(registrar(campos, registro))
    #print(exibir(registro))
    # Acrescente os outros cenários da matriz, um de cada vez.