import pickle
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection
import numpy as np

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
ext_data = conn.read(wroksheet="Sheet1", usecols=list(range(10)), ttl=5)
ext_data = ext_data.dropna(how="all")

st.line_chart(data=ext_data["Class"], columns=[ext_data["Female","Male"])
