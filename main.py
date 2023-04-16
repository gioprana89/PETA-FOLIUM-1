import streamlit as st
import folium as folium 
import pandas as pd
from streamlit_folium import st_folium
import pandas
import os
from folium import IFrame
#import base64 as base64

import pybase64

st.set_page_config(layout="wide")





st.markdown("<h5 style='text-align: justify; color: blue;'>Membuat Peta dengan Python (Library: STREAMLIT & FOLIUM)<br><br></h5>", unsafe_allow_html=True)

st.image("ugi.png", caption='', width = 350)

file1 =  'jam_gadang.jpg'
dir_base1 = 'D:/PYTHON/STREAMLIT/PETA/FOLIUM'
Filename1 = dir_base1 + "/" + file1

encoded1 = pybase64.b64encode(open(Filename1, 'rb').read())

svg1 = """<center>
  <object data="data:image/jpg;base64,{}" width="{}" height="{} type="image/svg+xml">
  </object></center>""".format



file2 =  'masjid.jpg'
dir_base2 = 'D:/PYTHON/STREAMLIT/PETA/FOLIUM'
Filename2 = dir_base2 + "/" + file2

encoded2 = pybase64.b64encode(open(Filename2, 'rb').read())

svg2 = """<center>
  <object data="data:image/jpg;base64,{}" width="{}" height="{} type="image/svg+xml">
  </object></center>""".format


width, height, fat_wh = 150, 150, 1.3


iframe1 = IFrame(svg1(encoded1.decode('UTF-8'), width, height) , width=width, height=height)

popup1  = folium.Popup(iframe1, parse_html = True, max_width=150)



iframe2 = IFrame(svg2(encoded2.decode('UTF-8'), width, height) , width=width, height=height)

popup2  = folium.Popup(iframe2, parse_html = True, max_width=150)


 
m = folium.Map(location = [-0.789275, 113.921327],
               zoom_start = 5,
              )


folium.Marker([4.695135, 96.749397],  icon=folium.Icon(color='red', icon='anchor', prefix='fa'), 
                popup=popup2).add_to(m)

folium.Marker([-0.94708, 100.41718],  icon=folium.Icon(color='blue', icon='anchor', prefix='fa'), 
                popup=popup1).add_to(m)


st_data = st_folium(m, width = "100%")