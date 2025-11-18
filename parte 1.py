import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('consumo_semana.csv')

print("Dados carregados:")
print(df)

# Gerar gráfico de consumo total
plt.figure()
plt.plot(df['Dia'], df['Total_kWh'], marker='o')
plt.title('Consumo Total Semanal (kWh)')
plt.xlabel('Dia')
plt.ylabel('kWh')
plt.grid(True)

plt.show()               # EXIBE O GRÁFICO NA TELA
plt.savefig('grafico_consumo.png')  # SALVA O ARQUIVO
plt.close()

print("Gráfico salvo como grafico_consumo.png")

# Cálculo das médias semanais
media_ilum = df['Iluminacao'].mean()
media_comp = df['Computadores'].mean()
media_ar = df['Ar_Condicionado'].mean()

print("\nMédias semanais:")
print("Iluminação:", media_ilum)
print("Computadores:", media_comp)
print("Ar-condicionado:", media_ar)