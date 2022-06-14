import pandas as pd

df_faturamento = pd.read_json (r'D:\UPE\python\Target Sistemas\dados.json')
mask = df_faturamento['valor'] == 0
df_fat_limpo = df_faturamento.loc[~mask]
min = df_fat_limpo["valor"].min()
max = df_fat_limpo["valor"].max()
print("O menor valor de faturamento ocorrido em um dia do mês foi :R$", min)
print ("O maior valor de faturamento ocorrido em um dia do mês foi :R$",max)
media = df_fat_limpo['valor'].mean()
mask_dia = df_faturamento['valor'] > media
df_fat_maior = df_fat_limpo.loc[mask_dia]
#print(df_fat_maior)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ",len(df_fat_maior))
