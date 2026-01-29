temperatures = [32.5, 33.5, 67.5, 90,4]


total = 0
for temp in temperatures:
    total = total + temp


average = total/len(temperatures)
print(average)