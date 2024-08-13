def funcao(data):
    dia, mes, ano = data.split("/")
    mes = str(mes)
    result = ""
    num = int(dia)
    if num < 10:
        dia = dia[1]
    if mes == "01":
        result = "janeiro"
    elif mes == "02":
        result = "fevereiro"
    elif mes == "03":
        result = "marco"
    elif mes == "04":
        result = "abril"
    elif mes == "05":
        result = "maio"
    elif mes == "06":
        result = "junho"
    elif mes == "07":
        result = "julho"
    elif mes == "08":
        result = "agosto"
    elif mes == "09":
        result = "setembro"
    elif mes == "10":
        result = "outubro"
    elif mes == "11":
        result = "novembro"
    elif mes == "12":
        result = "dezembro"
    return f"{dia} de {result} de {ano}"