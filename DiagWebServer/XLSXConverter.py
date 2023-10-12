import pandas as pd

tabela = pd.read_excel("/OneDrive/08. Dev/00. Projetos/DiagWebServer/DiagEventList.xlsx")
file = open("DiagEventList.html", "w")
file.write(tabela.to_html())
