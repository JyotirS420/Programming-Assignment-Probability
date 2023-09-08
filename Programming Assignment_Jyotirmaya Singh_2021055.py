import matplotlib.pyplot as pl
import statistics as stats
import numpy as np
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import truncnorm
from math import sqrt
from random import randint

#L_data=[,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,]
L_data=[4,0,12,0,0,23,0,0,3,1,1,4,13,11,14,56,0,10,0,0,2,1,2,11,32,29,1,15,27,11]

#print(len(L_data))
#print("\n\n\n")

"""
L_data=[]

for i in range(0,30):
    num=randint(0,30)
    L_data.append(num)
"""

dict_freq={}
L_mean=[]
L_variance=[0]

def print_list(L):
    for i in L:
        print(i,end=" ")
    print()


#for creating a sorted array and then plotting values in line graph
L_data_copy=sorted(L_data)


#finding the frequency of all the observations
for i in L_data_copy:
    if i not in dict_freq:
        dict_freq[i]=1
    else:
        dict_freq[i]+=1


#dividing each of the observed frequencies by 30 to obtain the relative frequency
for i in dict_freq:
    dict_freq[i]/=30


#creating variables to calculate the mean and the variance
sum_val=0
var_val=0


for i in range(0,len(L_data)):

    #calculating the mean and the variance
    sum_val=(sum(L_data[0:i+1]))/(i+1)
    var_val=stats.variance(L_data[0:i+2])

    #rounding off to 3 decimal places
    sum_val=round(sum_val,3)
    var_val=round(var_val,3)

    #adding the result to the list of means and variances
    L_mean.append(sum_val)
    L_variance.append(var_val)

    """
    for j in range(0,i):
        cal+=L_data[j]
        cal_square+=(L_data[j])**2
    """

#print("LENGTH 1: ",len(L_mean))
#print()
L_variance.pop()
#print("LENGTH 2: ",len(L_variance))
print()
print("Printing data:\n")
print(L_data)
print()

#printing the means and variances

print("Printing the list of mean values:\n",L_mean)
print()
print("Printing the list of variance values (assuming variance of first observation to be 0):\n",L_variance)



#x=np.arange(0,60,0.001) 
x=np.linspace(0,70,1000)#defining a numpy array to plot Guassian and Exponential PDFs
#x=list(dict_freq.keys())
#x.sort()


#finding the final mean and variance of all 30 obersvations with maximum precision
final_mean=(sum(L_data[0:30]))/30
final_variance=stats.variance(L_data[0:30])

"""
print()
print(round(final_variance,3))
print()
"""

"""
axis[0].plot(list(dict_freq.keys()),list(dict_freq.values()),'b')
axis[0].set_title("Line Frequency Distribution")

axis[1].plot(list(dict_freq.keys()),expon.pdf(list(dict_freq.keys()),1/final_mean),'g')
axis[1].set_title("Exponential Distribution")

axis[2].plot(list(dict_freq.keys()),norm.pdf(list(sorted(dict_freq.keys())),final_mean,sqrt(final_variance)),'r')
axis[2].set_title("Gaussian Distribution")
"""


def plot_line():
    """For only line frequency graph"""
    
    pl.xlabel("Time Interval (in min)")
    pl.ylabel("Relative Frequency")
    pl.plot(list(dict_freq.keys()),list(dict_freq.values()),marker='o',markersize=4,color='b')
    #pl.plot(list(dict_freq.keys()),list(dict_freq.values()),'b',linewidth=2)
    #pl.plot(L,L2)
    pl.show()
    
def plot_exp():
    """For only exponential curve"""

    x=np.linspace(0,70,1000)
    pl.xlabel("Time Interval (in min)")
    pl.ylabel("fx")
    pl.plot(x,expon.pdf(x,loc=0,scale=final_mean),color='g')
    pl.show()


def plot_normal_full():
    """For only Gaussian curve"""

    x=np.linspace(-60,60,1000)
    pl.xlabel("Time Interval (in min)")
    pl.ylabel("fx")
    pl.title("Normal Distribution")
    pl.plot(x,norm.pdf(x,final_mean,sqrt(final_variance)),color='r')
    pl.show()

def plot_normal_half():
    """For only Gaussian curve in + X-axis region"""

    x=np.linspace(0,60,1000)
    pl.xlabel("Time Interval (in min)")
    pl.ylabel("fx")
    pl.title("Normal Distribution in +X Axis")
    pl.plot(x,norm.pdf(x,final_mean,sqrt(final_variance)),color='r')
    pl.show()
    
def plot_truncated_normal():
    """For Truncated Normal Curve"""
    myclip_a = 0
    myclip_b = 56
    my_mean = final_mean
    my_std = sqrt(final_variance)

    a, b = (myclip_a - my_mean) / my_std, (myclip_b - my_mean) / my_std
    x_range = np.linspace(0,60,1000)
    pl.xlabel("Time Interval (in min)")
    pl.ylabel("fx")
    pl.title("Truncated Normal Distribution")
    pl.plot(x_range, truncnorm.pdf(x_range, a, b, loc = my_mean, scale = my_std),color='r')
    pl.show()
    
print("""\n1. Line Frequency
2. Exponential PDF
3. Normal PDF
4. Normal PDF in +X axis region
5. Truncated Normal PDF
""")
option=0
while option!=6:
    option=int(input("Enter option number: "))
    if option==1:
        plot_line()
    elif option==2:
        plot_exp()
    elif option==3:
        plot_normal_full()
    elif option==4:
        plot_normal_half()
    elif option==5:
        plot_truncated_normal()
    else:
        break




def plot_all():

    
    """Plotting all the graphs on the same figure"""
   
    fig,axis=pl.subplots(3)
    fig.suptitle("Comparing distributions")
    
    axis[0].plot(list(dict_freq.keys()),list(dict_freq.values()),'b')
    axis[0].set_title("Line Frequency Distribution")
    pl.ylabel("fx")

    axis[1].plot(x,expon.pdf(x,loc=0,scale=final_mean),'g')
    axis[1].set_title("Exponential Distribution")
    pl.ylabel("fx")

    axis[2].plot(x,norm.pdf(x,final_mean,sqrt(final_variance)),'r')
    axis[2].set_title("Gaussian Distribution")
    pl.ylabel("fx")

    fig.tight_layout()
    pl.subplots_adjust(wspace=0.5)
    pl.show()



#To plot on the same figure
"""
pl.xlabel("Time Interval (in min)")
pl.ylabel("Relative Frequency")
pl.plot(list(dict_freq.keys()),norm.pdf(list(dict_freq.keys()),final_mean,final_variance))
pl.plot(list(dict_freq.keys()),expon.pdf(list(dict_freq.keys()),1/final_mean))
pl.plot(list(dict_freq.keys()),list(dict_freq.values()),marker='o',markersize=4)
pl.show()
"""

"""
print("Here: \n" )
print(list(sorted(dict_freq.keys())))
print()

"""









