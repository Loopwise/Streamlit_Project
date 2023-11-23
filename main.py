import streamlit as st
import pandas as pd
import numpy as np
import datetime
from utilities import *

import os
os.system('cls')

import warnings
warnings.filterwarnings('ignore')

st.set_page_config(     
    page_title="Dashboard Programación Avanzada",
    layout="wide",
)


url = 'https://www.datosabiertos.gob.pe/sites/default/files/D.%20Composici%C3%B3n%20Anual%20de%20residuos%20domiciliarios_Distrital_2019_2022.csv'

data = get_data(url, sep = ';', encoding='latin-1')

sel = 'QRESIDUOS_TEREFLATO_POLIETILENO'

st.bar_chart(data, x = 'DEPARTAMENTO', y = 'QRESIDUOS_TEREFLATO_POLIETILENO')

st.dataframe(filter_dataframe(data))

print(data.dtypes)