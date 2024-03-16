import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import math
col1, col2 = st.columns(2)
txt = 'Draw n-leaf clover '

with col1:
    st.subheader(txt)
# st.subheader('Draw n-leaf clover r = (sin(n1 * θ/2) + 0.2 * sin(n2 *4.5*θ/3))²')

with col2:    
    st.latex(r'''
            R = (sin(n_1 θ/2) + 0.2 * sin(4.5n_2 θ/3))^2
                ''')


with col1:
    n1 = st.slider("Number of petals1", min_value=1, max_value=12, value=1,  step=1)
with col2:    
    n2 = st.slider("Number of petals2", min_value=1, max_value=12, value=1,  step=1)
txt1 = ''    
if n1==3 and n2==3:
    txt1 = 'Happy St. Patrick\'s Day!'    

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


plt.show()
st.pyplot(fig)
st.subheader(txt1)