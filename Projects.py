# 🚀 Project 1: My coding Hours Tracking

import matplotlib.pyplot as plt

days = list(map(int,input("Enter The Days(1 - 7): ").split()))
hours = list(map(int,input("Enter The Number Of hours Per Day: ").split()))

max_studied = max(hours)
max_index = hours.index(max_studied)
max_position = days[max_index]

least_studied = min(hours)
least_index = hours.index(least_studied)
least_position = days[least_index]

# Making Graph understandable
plt.title("My 7-Days Coding Progress")
plt.xlabel("Days")
plt.ylabel("Hours Studied")

# plotting Graph
plt.plot(days,hours,linestyle = "-",linewidth = 3,marker = 'o',color = 'green',label = "Coding Hours")

# Pinning Highest and lowest Studied Day
plt.plot(max_position,max_studied,marker = 'o',color = 'red',markersize = 10,label = "Max Study")
plt.plot(least_position,least_studied,marker = 'o',color = 'Blue',markersize = 10,label = "Least Study")

# Adding text to the labels
plt.text(max_position,max_studied + 0.2,"Highest",color = 'red')
plt.text(least_position,least_studied - 0.3, "Lowest ",color = 'blue')

print(f"Max studied Hours: {max_studied}")
print(f"Max studied Day: {max_position}")
print(f"Least studied Hours: {least_studied}")
print(f"Least studied Day: {least_position}")

plt.legend()
plt.grid()
plt.show()





