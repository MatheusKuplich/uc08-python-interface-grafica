"""A03 — complete a lógica e os callbacks do conversor."""
import tkinter as tk
from tkinter import ttk


def calcular(campos, registro):
    # TODO: ler reais e as duas cotações; aceitar vírgula ou ponto decimal.
    reais_texto = campos["reais"].strip()
    dolar_texto = campos["cotacao_dolar"].strip()
    euro_texto = campos["cotacao_euro"].strip()

    if not reais_texto or not dolar_texto or not euro_texto:  #verificação dos campos que foram preenchidos novamente
        return "Preencha o que faltou."

    try:
        reais = float(reais_texto.replace(",", "."))
        cotacao_dolar = float(dolar_texto.replace(",", "."))  #textos para números novamente
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
        return "Nenhuma conversão confirmada."

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


def criar_janela():

    janela = tk.Tk()
    janela.title("Conversor com cotações fictícias.")
    janela.columnconfigure(1, weight=1)

    campos = {"reais": "", "cotacao_dolar": "", "cotacao_euro": ""}
    registro = {}

    ttk.Label(janela, text="Cotações.", wraplength=420).grid(row=0, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    ttk.Label(janela, text="Valor em reais (R$):").grid(row=1, column=0, padx=12, pady=6, sticky="w")
    entrada_reais = ttk.Entry(janela)
    entrada_reais.grid(row=1, column=1, padx=12, pady=6, sticky="ew")

    ttk.Label(janela, text="R$ por 1 USD:").grid(row=2, column=0, padx=12, pady=6, sticky="w")
    entrada_dolar = ttk.Entry(janela)
    entrada_dolar.grid(row=2, column=1, padx=12, pady=6, sticky="ew")

    ttk.Label(janela, text="R$ por 1 EUR:").grid(row=3, column=0, padx=12, pady=6, sticky="w")
    entrada_euro = ttk.Entry(janela)
    entrada_euro.grid(row=3, column=1, padx=12, pady=6, sticky="ew")

    def ao_calcular():
        # TODO: ler os três Entry, calcular e atualizar aviso/último confirmado.

        campos["reais"] = entrada_reais.get()   # copiando os textos digitados para os campos
        campos["cotacao_dolar"] = entrada_dolar.get()
        campos["cotacao_euro"] = entrada_euro.get()

        mensagem = calcular(campos, registro)

        aviso.configure(text=mensagem)
        resultado.configure(text=exibir(registro))  # mostrando o último cálculo confirmado

    def ao_exibir():
        # TODO: consultar somente registro, sem ler as entradas editáveis.
        resultado.configure(text=exibir(registro))
        aviso.configure(text="Consulta do último cálculo confirmado.")

    def ao_limpar():
        # TODO: esvaziar campos/Entry e devolver foco; conservar resultado.

        limpar(campos)

        entrada_reais.delete(0, tk.END)
        entrada_dolar.delete(0, tk.END)
        entrada_euro.delete(0, tk.END)

        aviso.configure(text="Limpeza dos campos editáveis feita.")
        entrada_reais.focus_set()  # devolvendo o foco para o primeiro campo

    ttk.Button(janela, text="Calcular", command=ao_calcular).grid(row=4, column=0, padx=12, pady=8)
    ttk.Button(janela, text="Exibir", command=ao_exibir).grid(row=4, column=1, padx=12, pady=8)
    ttk.Button(janela, text="Limpar campos", command=ao_limpar).grid(row=5, column=0, columnspan=2, pady=6)

    aviso = ttk.Label(janela, text="Use vírgula ou ponto decimal.", wraplength=420)
    aviso.grid(row=6, column=0, columnspan=2, padx=12, pady=8, sticky="w")

    resultado = ttk.Label(janela, text="Nenhuma conversão confirmada nesta sessão.", wraplength=420)
    resultado.grid(row=7, column=0, columnspan=2, padx=12, pady=8, sticky="w")

    entrada_reais.focus_set()
    return janela


if __name__ == "__main__":

    criar_janela().mainloop()