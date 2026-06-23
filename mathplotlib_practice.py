import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.plot([1,2,3],[2,4,6], label="Line 1", color='red', marker='o', linestyle='--')
plt.title("My First Plot", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20, 'color': 'blue'})

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xticks([1,2,3])
plt.yticks([2,4,6])
plt.legend()
plt.show()  

plt.figure(figsize=(10,5), dpi=100)
plt.savefig("my_first_plot.png")    

#mathplotlib documentation: https://matplotlib.org/stable/contents.html

x2=np.arange(0,10,1)
plt.plot(x2, x2**2, label="Line 2", color='green', marker='x', linestyle='-')
plt.legend()
plt.show()


labels = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]   
bar = plt.bar(labels, values, color=['red', 'blue', 'green', 'orange']) 
bar[0].set_hatch('/')
bar[1].set_hatch('\\')
bar[2].set_hatch('x')
bar[3].set_hatch('+')
   
plt.show()
