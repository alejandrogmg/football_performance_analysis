import pandas as pd
import os


# Leemos el csv con los datos.
cwd = os.getcwd()
df = pd.read_csv(cwd+'/football_performance.csv')


# Creamos una lista a partir del df con las columnas que únicamente tienen valores numéricos (float).
normalize_list = ['Indice InStat', 'Partidos jugados', 'Minutos jugados', 'Starting lineup appearances', 'Ocasiones claras falladas',
                  'Ocasiones falladas por partido', 'Goles', 'Goles por partido', 'Tiros a portería', 'Tiros a porteria por partido',
                  'xG', 'Regates', 'Regates por partido', ' % disputas ganadas', 'Faltas cometidas por partido', 'Taclkes por Partido',
                  'Perdidas en campo propio', 'Perdidas en campo propio por partido', 'Balones recuperados', 'Balones recuperados por partido',
                  ' % disputas por arriba ganadas', 'Interceptaciones', 'Interceptaciones por partido', 'Tarjetas amarillas', 'Asistencias',
                  'xA (Asistencias esperadas)', 'Asistencias por partido', '% de efectividad de pases', 'Pases de finalización',
                  'Pases de finalizacion por partido', ' % de efectividad de los centros', 'Balones perdidos', 'Balones perdidos por partido',
                  'Recuperaciones en campo rival', 'Recuperaciones en campo rival por partido', 'Tiros del rival', 'Remates del rival a puerta',
                  'Goles encajados', 'Goles encajados por partido', 'Tiros rechazados', 'Shots saved %', 'Pases', 'Pases efectivos', 'Pases completados por partido',
                  ' % de efectividad de pases', 'Salidas con exito por partido', '% Salidas con éxito', 'Pases largos completados', '% Pases largos completados',
                  'Cleansheets', 'PSxG']


# Normalizamos los valores para que tengan el mismo rango y lo podamos visualizar correctamente en el radar chart.

df[normalize_list] = df[normalize_list].apply(lambda x: (x - x.min()) / (x.max() - x.min()))



# Creamos las listas con los índices de las métricas de cada respectiva posición.
porteros_index = [44,46,50,51,54,55,56]
defensas_index = [20,21,23,25,26,28,29]
centrocampistas_index = [31,32,33,35,36,38,40]
delanteros_index = [11,13,15,16,18,19,35]


# Creamos una función que obtenga los KPIs target por posición.
def extract_position_kpi(position_index,position_list,kpi_list):
    for index in position_index:
        position_list.append(kpi_list[index])



# Creamos una lista con las columnas que necesitaremos en la barra lateral de filtrado.

target_columns = ["Liga", "Posicion", "Jugador"]


# MISCELLANEUS

def flat_list(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        for item in sublist:
            flat_list.append(item)
    return flat_list
