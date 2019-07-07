import matplotlib.pyplot as plt
xs=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
ys=[10,12,20,22,21,25,30,21,32,34,35,30,50,45,55,60,66,64,67,72,74,80,79,84]
print(len(xs),len(ys))
import numpy as np
def slope_intercept(x_val,y_val):
    x=np.array(x_val)
    y=np.array(y_val)
    m=(((np.mean(x)*np.mean(y))-np.mean(x*y))/
       (np.mean(x)**2-np.mean(x**2)))
    m=round(m,2)
    b=(np.mean(y)-np.mean(x)*m)
    return m,b
m,b=slope_intercept(xs,ys)
reg_line=[(m*x)+b for x in xs]
plt.scatter(xs,ys,color="red")
plt.plot(xs,reg_line)
plt.ylabel("dependent variable")
plt.xlabel("Independent variable")
plt.title("making regression line")
plt.show()
