a_score = []
b_score = []
c_score = []
a_score.append('A')
b_score.append('B')
c_score.append('C')

print("輸入A學生成績")
for a in range(1,4):
    a_score.append(input())
    a_score[a]=int(a_score[a])
print(f"國文:{a_score[1]}")
print(f"數學:{a_score[2]}")
print(f"英文:{a_score[3]}")

print("輸入B學生成績")
for b in range(1,4):
    b_score.append(input())
    b_score[b]=int(b_score[b])
print(f"國文:{b_score[1]}")
print(f"數學:{b_score[2]}")
print(f"英文:{b_score[3]}")

print("輸入C學生成績")
for c in range(1,4):
    c_score.append(input())
    c_score[c]=int(c_score[c])
print(f"國文:{c_score[1]}")
print(f"數學:{c_score[2]}")
print(f"英文:{c_score[3]}")

a_score.append((a_score[1]+a_score[2]+a_score[3])/3)
b_score.append((b_score[1]+b_score[2]+b_score[3])/3)
c_score.append((c_score[1]+c_score[2]+c_score[3])/3)
a_score[4]=round(a_score[4],1)
b_score[4]=round(b_score[4],1)
c_score[4]=round(c_score[4],1)

print(a_score)
print(b_score)
print(c_score)