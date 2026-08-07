import matplotlib.pyplot as plt
import numpy as np

x=[20,50,40,60,90,10]
y=[10,100,120,80,130,200]
plt.scatter(x,y,s=[10,20,30,40,40,50],color="green",marker="*",cmap="viridis")
plt.show()