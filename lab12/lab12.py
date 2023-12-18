import matplotlib.pyplot as plt

with open ("Temperature.txt") as file:
    data_list = []
    year_list = []
    for line in file:
        row_data = line.strip().split(', ')
        if(row_data[0]!="Tainan:"):
            year_list.append(int(row_data[0]))
        data_list.append([float(value) for value in row_data[1:]])
    data_list=data_list[1:]


fig = plt.figure(figsize=(12,5))
fig.add_subplot(1, 2, 1)

for i in range(len(data_list)):
    plt.plot(range(1, 13), data_list[i], label=year_list[i])  

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc=8)
#plt.show()


plt.subplot(1, 2, 2)
avg_list=[]
for m in range(0, 12):
    total=0
    for a in range(0, 9):
        total+=data_list[a][m]
    avg_list.append(round(total/9, 2))

plt.plot(range(1, 13), avg_list, '-o', 8, markerfacecolor='red', markeredgecolor='red', color='blue')

for x, y in zip(range(1, 13), avg_list):
    plt.text(x, y, f'{y}', ha='left', va='bottom')

avg=0
for i in range(0, 12):
    avg+=avg_list[i]
avg=round(round(avg/12, 2)-0.01, 2)
plt.axhline(y=avg, color='red', linestyle='--', label='Mean of 9 Years')
plt.text(0.3, 25, f'{avg}', color='black', ha='left', va='bottom')

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
plt.yticks(range(16, 33, 2))
plt.ylim(16, 32)
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc=1)


fig.suptitle('', fontsize=16)
plt.tight_layout() #讓子圖之間適當排列不重疊
plt.show()
fig.savefig('lab12_03.png')

