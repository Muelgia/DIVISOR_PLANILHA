import os
import pandas as pd


# CÓDIGO PARA DIVIDIR PLANILHAS
try:
    existe = False
    while existe == False:
        FONTE = input("Digite o caminho completo da planilha a ser dividida: \n>>>>>>")
        if os.path.exists(f"{FONTE}") == False:
            print("Planilha não encontrada, verifique o nome salvo..")
        else:
            print("Planilha localizada")
            existe = True
except Exception as e: 
    print(f"Erro na busca da fonte: {e}")

base = pd.read_excel(f"{FONTE}") 
print(base)

while True:   
    dividir = int(input("\nDividir a planilha em quantas fontes? [20 max]\n>>>>>> "))
    if dividir > 300:
        print("Valor inválido!")
        continue
    else:
        break

tam_total = len(base)
tam_fonte = round(tam_total/dividir)
print (f'Total de linhas: {tam_total}')
    
separados = {}

try:
    existe = False
    while existe == False:
        savepath = input('\nDigite o caminho completo da pasta onde deseja salvar o arquivo:\n>>>>>>')
        if os.path.exists(f"{FONTE}") == False:
            print("Caminho não encontrado, verifique o nome salvo..")
        else:
            print("Planilha localizada")
            existe = True
except Exception as e: 
    print(f"Erro na busca da fonte: {e}")

namepath = input('\nDigite o nome para fonte:\n>>>>>>')
SALVAR = os.path.join(savepath, namepath)

ext = 'none'
while ext != 'csv' and ext != 'xlsx':
    extpath = input('\nSalvar em formato CSV ou XLSX:\n>>>>>>')
    ext = extpath.lower()

for i in range(dividir):
    nome =  f"fonte{i+1}"  
    valor = base[tam_fonte*i:tam_fonte*(i+1)]
    separados[nome] = valor
    if ext == 'xlsx':
        valor.to_excel(SALVAR + f'_{i+1}' + '.xlsx', index=False)
    elif ext == 'csv':
        valor.to_csv(SALVAR + f'_{i+1}' + '.csv', index=False)
    print(f"\nplanilha {i+1}: {len(valor)} linhas")

