import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,70]
plt.boxplot(x)#,notch=True,widths=0.5,labels=['python'],patch_artist=True,showmeans=True,boxprops=dict(color='r'),capprops=dict(color='r'),whiskerprops=dict(color='r')
plt.show()