import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='sześcienna')
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
#
# plt.title('Prosty wykres')
#
# plt.legend()
#
# plt.show()

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, s, x, label='sin(x)')
#
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.title('Wykres sin(x)')
#
# plt.legend()
#
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 20, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# print(f"a={data['a'][0]}, b={data['b'][0]}, d={data['d'][0]}")
# plt.show()

# x1 =np.arange(0.0,2.0,0.02)
# x2 =np.arange(0.0,2.0,0.02)
#
# y1 =np.sin(2*np.pi *x1)
# y2 =np.cos(2*np.pi *x2)
#
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
#
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
#
# plt.show()

# x =np.random.randn(10000)
# plt.hist(x,bins=50,facecolor='g',alpha=0.75,density=True)
# plt.grid(True)
# plt.show()

# zawodnicy =['Messi','Suarez','Dembele','Coutinho']
# bramki =[48,25,13,11]
#
# wedges,texts,autotexts =plt.pie(bramki,labels=zawodnicy,autopct=lambda pct:"{:.1f}%".format(pct),textprops=dict(color="black"))
# plt.setp(autotexts,size=14,weight="bold")
# plt.title("Pierwsza wersja wykresu")
# plt.legend(title='Zawodnicy')
# plt.show()
#

x = np.arange(1, 20, 1)
y = 1/x

plt.plot(x, y, 'g>:', label='f(x)=1/x')
plt.legend()
plt.title('Wykres funkcji f(x) dla x[1, 20]')
plt.axis([0, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()