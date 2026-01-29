import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
# import math

txt = 'Draw your n-leaf clover'

st.subheader(txt)
# st.subheader('Draw n-leaf clover r = (sin(n1 * θ/2) + 0.2 * sin(n2 *4.5*θ/3))²')

col1, col2 = st.columns(2)
with col1:
    n1 = st.slider("n1", min_value=1, max_value=12, value=3,  step=1)
with col2:    
    n2 = st.slider("n2", min_value=1, max_value=12, value=3,  step=1)
txt1 = ''    
if n1==3 and n2==3:
    txt1 = 'Happy St. Patrick\'s Day!'    

if n1==4 and n2==4:
    txt1 = 'A lucky four-leaf clover!' 

i=200
pi = np.pi

theta = np.arange(0, 2 * np.pi, .01)[1:]
# r = 2 * np.cos(theta) + 2 * np.sin(theta)
# theta = np.arange(0, 0.01*math.pi*i, 0.01)[1:]

r = (np.sin(3*theta/2) + 0.2 * np.sin(4.5*theta))**2
r = (np.sin(4*theta/2) + 0.2 * np.sin(4*4.5*theta/3))**2
r = (np.sin(5*theta/2) + 0.2 * np.sin(5*4.5*theta/3))**2

r = (np.sin(n1*theta/2) + 0.2 * np.sin(n2*4.5*theta/3))**2
r1 = 0.7 * r
r2 = 0.05 * r

fig = plt.figure()
ax = fig.add_subplot(polar=True)

# change negative r values to positive, rotating theta by 180º
theta = np.where(r >= 0, theta, theta + np.pi)
r = np.abs(r)

ax.plot(theta, r, color="green", linewidth=5)
ax.plot(theta, r)
# ax.plot(theta, r1)
ax.plot(theta, r1, color="green", linewidth=5)
ax.fill_between(theta, r1, r, where=r >= r1,
                facecolor='limegreen', interpolate=True)

ax.plot(theta, r2, color="darkgreen", linewidth=5)
ax.fill_between(theta, r2, r1, where=r1 >= r2,
                facecolor='darkgreen', interpolate=True)

# plt.show()
st.pyplot(fig)

# r(φ) = (sin(\frac{n_1 φ}{2}) + 0.2 * sin(4.5n_2 φ/3))^2   
st.latex(r'''
        r(φ) = (sin(\frac{n_1 φ}{2}) + 0.2 * sin(\frac{3 n_2 φ}{2}))^2
        ''')
st.subheader(txt1)
url1 = "https://www.rmseismic.com/lasviewer.html"
st.write("More geo apps: [link](%s)" % url1)
st.write("A.F., Mar 2024")

