from sklearn import datasets 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
iris = datasets.load_iris()
#print(iris.data)
#digits = datasets.load_digits()
#print(digits.data)
#file=open("C:/Users/navee/OneDrive/Desktop/independent study/independent study/data.txt", "r")
#print(file.read())
#file=open("C:/Users/navee/OneDrive/Desktop/independent study/independent study/data.txt", "w")
#file.write("hello")
#file=open("C:/Users/navee/OneDrive/Desktop/independent study/independent study/data.txt", "r")
#print(file.read())
file=open("C:/Users/navee/OneDrive/Desktop/independent study/independent study/iris.data")
#print(file.read())


#error bar
#x = np.linspace(0,10,19)
#data_ = np.tan(x)
#yerr = 0.5
#xerr = 0.5
#plt.errorbar(x,data_,yerr=yerr,fmt='o',color = 'red',ecolor='black',label = 'tan(x)')
#plt.xlabel('tan(x)')
#plt.title('Error bars - tan(x)')
#plt.legend(loc='lower right')
#plt.show()


#(historgram)
#data_ = np.random.randn(1000)
#lt.hist(data_,bins = 50,color='pink')
#plt.grid(True)
#plt.title("Histogram")
#plt.show()
#a= iris['variety'].value_counts()
#species = a.index
#count = a.values
#plt.bar(species,count,color = 'green')
#plt.xlabel('species')
#plt.ylabel('count')
#plt.show()

#scatter plot 
#file.plot(kind='scatter', x='petal.length', y='petal.width') 
#plt.show()

#colours = {'Setosa':'orange', 'Versicolor':'lightgreen', 'Virginica':'lightblue'}
#for i in range(len(iris['sepal.length'])):
#  plt.scatter(iris['petal.length'][i],iris['petal.width'][i], color = colours[iris['variety'][i]])
#plt.title('Iris')
#plt.xlabel('petal length')
#plt.ylabel('petal width')
#plt.grid(True)
#plt.show()


#(line plot)
#print(iris.data)
#plt.plot(iris.data) 
#plt.show()
#plt.hist(iris.data) (histogram)
#plt.show()
#x = np.linspace(0,20,30)
#y= x**2
#plt.plot(x, y)
#plt.show()
#x = np.linspace(0,20,30)
#y= x**2
#plt.plot(x, y)
#plt.xlabel('x-values')
#plt.ylabel('x^2-values')
#plt.title('line plot')
#plt.grid(True)
#plt.show()

# (sin and cos graph)
#plt.plot(np.sin(x),label='sin(x)',color='orange')     
#plt.plot(np.cos(x),label='cos(x)',color='green')
#plt.xlim(10,100)
#plt.legend()
#plt.title('math functions')
#plt.show()

#subgraphs 
#fig, axs = plt.subplots(2, 2 ,gridspec_kw={'hspace': 0.5, 'wspace': 0.4})
#x = np.linspace(0, 20, 400)
#y = np.tan(x)
#z=np.cot(x)
#m = (x**3)
#n=(x**2)
#axs[0, 0].plot(x, y)
#axs[0, 0].set_title('tan(x)')
#axs[0, 1].plot(x, z, 'tab:orange')
#axs[0, 1].set_title('cot(x)')
#axs[1, 0].plot(x, m, 'tab:green')
#axs[1, 0].set_title('x**3')
#axs[1, 1].plot(x,n, 'tab:red')
#axs[1, 1].set_title('x**2')
#plt.show()

#time = [0, 1, 2, 3]
#distance = [0, 100, 200, 300]

#plt.plot(time, distance)
#plt.xlabel('Time (hr)')
#plt.ylabel('distance (km)')