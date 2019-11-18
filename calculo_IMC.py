import tkinter
from tkinter import messagebox


def imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 17:
        return "Muito abaixo do peso "
    elif 17 <= imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        return "Peso Normal"
    elif 25 <= imc < 30:
        return "Acima do Peso"
    elif 30 <= imc < 35:
        return "Obesidade I"
    elif 35 <= imc < 40:
        return "Obesidade II (severa)"
    else:
        return "Obesidade III (mórbida)"


def botaoCalcula():
    if not numero(valorPeso.get()) or not numero(valorAltura.get()):
        messagebox.showerror("ERRO", "Vírgula não suportada, troque por Ponto!")
    else:
        labelResultado.config(text=f"{imc(float(valorPeso.get()), float(valorAltura.get()))}")

def numero(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def resetar():
    valorPeso.delete(first=0,last=1000)
    valorAltura.delete(first=0,last=1000)

app = tkinter.Tk()
app.geometry("400x300")

labMass = tkinter.Label(app, text="Peso (em KG, Ex: 81.9)", font=("Lucida", 22))
labMass.place(x=5, y=0)

valorPeso = tkinter.Entry(app, width=20)
valorPeso.place(x=5, y=50)

labHeight = tkinter.Label(app, text="Tamanho(em m, Ex: 1.73)", font=("Lucida", 22))
labHeight.place(x=5, y=75)

valorAltura = tkinter.Entry(app, width=20)
valorAltura.place(x=5, y=125)

botaoCalc = tkinter.Button(app, text="Calcular", command=botaoCalcula, background="green",foreground="white",font=("Lucida", 16))
botaoCalc.place(x=5, y=160)

botaoReset = tkinter.Button(app, text="Reiniciar", command=resetar, background="Yellow",font=("Lucida", 16))
botaoReset.place(x=140, y=160)

botaoSair = tkinter.Button(app, text="Sair", command=app.destroy, background="Red",foreground="white",font=("Lucida", 16))
botaoSair.place(x=280, y=160)

labelResp = tkinter.Label(app, text="Resposta:", font=("Lucida", 20))
labelResp.place(x=5, y=210)

labelResultado = tkinter.Label(app, text="", background="cyan",font=("Lucida", 28))
labelResultado.place(x=5, y=250)

app.mainloop()
