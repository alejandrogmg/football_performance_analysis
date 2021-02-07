import streamlit as st
import pandas as pd
import aux
import plotly.express as px
import plotly.graph_objects as go


df = aux.df

# LIST OF KPIS BY POSITION

kpi_list = list(df.head(0))

porteros_kpi_list = []
defensas_kpi_list = []
centrocampistas_kpi_list = []
delanteros_kpi_list = []

aux.extract_position_kpi(aux.porteros_index,porteros_kpi_list,kpi_list)
aux.extract_position_kpi(aux.defensas_index,defensas_kpi_list,kpi_list)
aux.extract_position_kpi(aux.centrocampistas_index,centrocampistas_kpi_list,kpi_list)
aux.extract_position_kpi(aux.delanteros_index,delanteros_kpi_list,kpi_list)


try:

   #  imagen_titulo = '''
   # <style>
   # body {
   # background-image: url("https://i.pinimg.com/originals/93/d4/35/93d435af7e2deeb62dcb2000399f75a9.jpg");
   # background-size: cover;
   # }
   # </style>
   # '''
   #  st.markdown(imagen_titulo, unsafe_allow_html=True)

   # TITLES
    st.header("COMPARATIVA ENTRE LOS TOP 5 POR POSICIÓN DE LAS 5 GRANDES LIGAS DE EUROPA")
    st.write("🔺️Es necesario seleccionar dos jugadores con la misma posición para completar la visualización🔻")
    st.text("Los datos están comprendidos desde el inicio de la temporada 20/21 hasta el día 04/12/2020")


   # FILTERING IN WEB

    df2 = df[aux.target_columns]

    st.sidebar.markdown('## ℹ️ Configuración')

    position_list = list(set(df["Posicion"].tolist()))
    st.sidebar.markdown('② ** Selecciona la posición **')
    POSITION_SELECTED = st.sidebar.selectbox('Posición', position_list)

    liga_list = list(set(df["Liga"].tolist()))
    liga_list.insert(0,'All')
    st.sidebar.markdown('① ** Selecciona la liga/s **')
    LEAGUE_SELECTED = st.sidebar.selectbox('Liga', liga_list)

    st.sidebar.markdown('③ ** Selecciona 2 jugadores para comparar **')
    if LEAGUE_SELECTED != 'All':
        PLAYERS_SELECTED = st.sidebar.multiselect('Jugadores', list(set(df2.loc[(df['Liga'] == LEAGUE_SELECTED) & (df2['Posicion'] == POSITION_SELECTED)]["Jugador"].tolist())))
    else:
        PLAYERS_SELECTED = st.sidebar.multiselect('Jugadores', list(set(df2.loc[(df['Posicion'] == POSITION_SELECTED)]["Jugador"].tolist())))





    def chart_kpis(POSITION_SELECTED):
        if POSITION_SELECTED == 'Portero':
            return porteros_kpi_list
        elif POSITION_SELECTED == 'Defensa':
            return defensas_kpi_list
        elif POSITION_SELECTED == 'Centrocampista':
            return centrocampistas_kpi_list
        else:
            return delanteros_kpi_list


    def player_position_list_kpi(position_selected, position_list):
        if position_selected == position_list[0]:
            return porteros_kpi_list
        if position_selected == position_list[1]:
            return defensas_kpi_list
        if position_selected == position_list[2]:
            return centrocampistas_kpi_list
        if position_selected == position_list[3]:
            return delanteros_kpi_list


    categories = chart_kpis(POSITION_SELECTED)

    player_one = PLAYERS_SELECTED[0]
    player_two = PLAYERS_SELECTED[1]

    df_player_one = df.loc[df['Jugador'] == player_one][player_position_list_kpi(POSITION_SELECTED, position_list)]
    df_player_two = df.loc[df['Jugador'] == player_two][player_position_list_kpi(POSITION_SELECTED, position_list)]

    player_one_list = aux.flat_list(df_player_one.values.tolist())
    player_two_list = aux.flat_list(df_player_two.values.tolist())

    fig = px.line_polar(df_player_one, r=player_one_list, theta=categories, line_close=True)

    fig.add_trace(go.Scatterpolar(
        r=player_one_list,
        theta=categories,
        fill='toself',
        name=player_one,
        visible=True
    ))
    fig.add_trace(go.Scatterpolar(
        r=player_two_list,
        theta=categories,
        fill='toself',
        name=player_two,
        visible=True
    ))

    st.write(fig)


except IndexError:
 pass


