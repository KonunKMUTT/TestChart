import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection
import numpy as np
import seaborn as sns

# เชื่อมต่อกับ Google Sheets
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# อ่านข้อมูลจาก Google Sheets
ext_data = conn.read(wroksheet="Sheet1", usecols=list(range(10)), ttl=5)

# ลบข้อมูล NaN ทั้งหมด
ext_data = ext_data.dropna(how="all")

# เปลี่ยน 0 เป็น "Male" และ 1 เป็น "Female"
ext_data["female"] = ext_data["female"].replace({0: "Male", 1: "Female"})

# คำนวณเปอร์เซ็นไทล์
total_female = ext_data[ext_data["female"] == "Female"].shape[0]
total_male = ext_data[ext_data["female"] == "Male"].shape[0]
ext_data["Female %"] = (ext_data["female"] == "Female") * (100 / total_female)
ext_data["Male %"] = (ext_data["female"] == "Male") * (100 / total_male)

# สร้างกราฟ Count Plot
fig, ax = plt.subplots(figsize=(6, 6))
sns.countplot(x="female", hue="class", data=ext_data, palette="hls", ax=ax)

# เปลี่ยนชื่อแกน x
ax.set_xlabel("Gender")

# เปลี่ยนชื่อ label บนแท่ง
for p in ax.patches:
    percentage = f"{p.get_height():.1f}%"
    x = p.get_bbox().get_x() + p.get_width() / 2
    y = p.get_bbox().get_y() + p.get_height()
    ax.annotate(percentage, (x, y))

# แสดงกราฟ
st.pyplot(fig)
