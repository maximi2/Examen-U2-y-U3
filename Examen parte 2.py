import pandas as pd


def Limpieza_de_datos(df):
    df= df.dropna(subset = ["sales"]).copy()
    df["region"]= df["region"].fillna("DESCONOCIDO")

    return df

def Impuesto_iva(df):
    def Impuesto_iva(df):
        df["ventas_con_iva"] = df["sales"] + (df["sales"] * .16)


def resultados(df):
    total_region = df.groupby("region")["sales"].sum()
    print ("Total de ventas por region")
    print(total_region)
    promedio_producto = df.groupby("product")["sales"].mean()
    print("promedio ventas producto")
    print(promedio_producto)




if __name__ == "__main__":
    df = pd.read_csv("sales_data.csv")
    df= Limpieza_de_datos(df)
    Impuesto_iva(df)
    resultados(df)
    print(df.head())