import pandas as pd

df = pd.read_excel("transacoes.xlsx")

duplicados = df[df.duplicated()]

suspeitos = df[df["Valor"] > 50000]

print("Duplicados:")
print(duplicados)

#Encontrar valores suspeitos
print("\nValores altos:")
print(suspeitos)

#Contar riscos
print(f"Total de registros: {len(df)}")
print(f"Duplicados: {len(duplicados)}")
print(f"Valores acima do limite: {len(suspeitos)}")


#fornecedores com mais gastos
fornecedores = (
    df.groupby("Fornecedor")["Valor"]
      .sum()
      .sort_values(ascending=False)
)

print(fornecedores.head())

#exportar
import pandas as pd

df = pd.read_excel("transacoes.xlsx")

duplicados = df[df.duplicated(subset=["Fornecedor", "Valor", "Data"], keep=False)]

suspeitos = df[df["Valor"] > 50000]

print("Duplicados:")
print(duplicados)

#Encontrar valores suspeitos
print("\nValores altos:")
print(suspeitos)

#Contar riscos
print(f"Total de registros: {len(df)}")
print(f"Duplicados: {len(duplicados)}")
print(f"Valores acima do limite: {len(suspeitos)}")


#fornecedores com mais gastos
fornecedores = (
    df.groupby("Fornecedor")["Valor"]
      .sum()
      .sort_values(ascending=False)
)

print(fornecedores.head())

#exportar
# exportar relatório
with pd.ExcelWriter("Relatorio_Auditoria.xlsx") as writer:

    # Base completa
    df.to_excel(
        writer,
        sheet_name="Base_Completa",
        index=False
    )

    # Duplicados
    duplicados.to_excel(
        writer,
        sheet_name="Duplicados",
        index=False
    )

    # Valores suspeitos
    suspeitos.to_excel(
        writer,
        sheet_name="Valores_Altos",
        index=False
    )

print("\nRelatório gerado com sucesso!")