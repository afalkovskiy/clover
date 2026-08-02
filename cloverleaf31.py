import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import math

txt = 'Math of rose curves'

st.subheader(txt)
# st.subheader('Draw n-leaf clover: r = [sin(n1 * θ/2) + 0.2 * sin(n2 * 4.5*θ/3)]²')
st.latex(r'''
        r(φ) = cos(p φ)
        ''')

col1, col2, col3 = st.columns(3)
with col1:
    p = st.slider("p1 outer curve", min_value=1., max_value=24., value=3.,  step=1.)
with col2:    
    q = st.slider("p2 inner curve", min_value=3, max_value=24, value=6,  step=1)
with col3:
    r = st.slider("rnd", min_value=0., max_value=.5, value=0.05,  step=0.05)    
txt1 = ''    

i=200
pi = np.pi

# theta = np.arange(-4*pi/4., 4*pi, .01)    #[:]
theta = np.linspace(0, 2 * np.pi, 2000)
# theta = np.linspace(-1* np.pi, 1* np.pi, 2000)

rnd = r*np.random.rand(theta.size)


r = abs(np.cos(p*theta)) + rnd

r2 = abs(np.cos(q*theta)) + rnd
# r = np.linspace(2, 2, 2000)


r1 = 0.7 * r**2 
r2 = 0.4 * r2 
r3 = 0.1 * r2

fig = plt.figure()
# fig.set_facecolor('darkkhaki')
# fig.set_facecolor('olivedrab')
fig.set_facecolor('skyblue')
# fig.set_facecolor('darkgreen')
ax = fig.add_subplot(polar=True)
ax.axis('off')

# change negative r values to positive, rotating theta by 180º
# theta = np.where(r >= 0, theta, theta + np.pi)
# r = np.abs(r)

ax.plot(theta, r, color="yellow", linewidth=5)
# ax.plot(theta, r)
ax.plot(theta, r1)
ax.plot(theta, r1, color="sandybrown", linewidth=4)
ax.fill_between(theta, r1, r, where=r >= r1,
                facecolor='gold', interpolate=True)

ax.fill_between(theta, r1, r2, where=r2 < r1,
                facecolor='orange', interpolate=True)

ax.plot(theta, r2)
ax.plot(theta, r2, color="crimson", linewidth=3)
ax.fill_between(theta, r2, r3, where=r3 < r1,
                facecolor='orange', interpolate=True)

ax.plot(theta, r3, color="saddlebrown", linewidth=2)
ax.fill_between(theta, r3, r2, where=r3 < r2,
                facecolor='darkred', interpolate=True)

# plt.show()
st.pyplot(fig)

# r(φ) = (sin(\frac{n_1 φ}{2}) + 0.2 * sin(4.5n_2 φ/3))^2   

st.subheader(txt1)
url1 = "https://www.rmseismic.com/lasviewer.html"
st.write("Geo apps: [link](%s)" % url1)
st.write("A.F., Aug 2026")

