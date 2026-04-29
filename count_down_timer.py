import time
my_time = int(input("Enter the time in seconds: "))


# for x in reversed (range(0, my_time)):
#     print(x)
#     time.sleep(1)

# print("Time's Up")

# range(start,stop,step)
# for i in range(my_time,0,-1):
#     print(i)
#     time.sleep(1)

# print("Time's Up!") 

while my_time > 0:
    print(my_time)
    my_time += -1
    time.sleep(1)
    
print("Time's Up!")     