import pandas as pd

def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    
    tipos_de_casos = data["Tipo"].value_counts(dropna =False)
    resultado = tipos_de_casos[0]+tipos_de_casos[1]+tipos_de_casos[2]
    sum_edades_est = 0
    cant_edades_est = 0
    sum_edades_imp = 0
    cant_edades_imp = 0
    sum_edades_rel = 0
    cant_edades_rel = 0
    tipo = data["Tipo"]
    edad = data["Edad"]
    for tipo, edad in zip(tipo, edad):
        if tipo == "En estudio":
            sum_edades_est += edad
            cant_edades_est += 1
        elif tipo == "Importado":
            sum_edades_imp += edad
            cant_edades_imp += 1
        elif tipo == "Relacionado":
            sum_edades_rel += edad
            cant_edades_rel += 1
            
    dic = {
        "casos_en_estudio":tipos_de_casos[1],
        "prom_edades_casos_en_estudio":int(sum_edades_est/cant_edades_est),
        "casos_importados":tipos_de_casos[2],
        "prom_edades_casos_importados":int(sum_edades_imp/cant_edades_imp),
        "casos_relacionados":tipos_de_casos[0],
        "prom_edades_casos_relacionados":int(sum_edades_rel/cant_edades_rel),
        "total_casos":int(resultado)
        
    }
    
    return dic 

print(analisis_datos
      (pd.read_csv("https://bitbucket.org/ingluise2019/misiontic/downloads/Casos_positivos_de_COVID-19_en_Colombia.csv").sample(frac=0.25, random_state =123)))