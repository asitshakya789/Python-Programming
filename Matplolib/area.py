import matplotlib.pyplot as plt 
x =[1,2,3,4,5,6]
y1,y2=[10,20,30,40,50],[4,5,6,5,34]
plt.fill_between(x,y1,y2,alpha=0.4,label ='area 1-2')
plt.plot(x,y1,label='line1',maker ='o')
plt.plot(x,y2,label='line2',maker ='o')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('are chare')
plt.legend()
plt.show()