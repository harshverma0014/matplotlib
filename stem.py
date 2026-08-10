import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.stem(x,y,linefmt=':',markerfmt="r+",bottom=0)
plt.legend()
plt.plot(y)
plt.show()