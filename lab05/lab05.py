#creat dic0
dict0 = {
    "index":["國文", "英文", "數學", "自然", "社會"],
    "StuA":[50, 60, 70, 80, 90],
    "StuB":[57, 86, 73, 82, 43],
    "StuC":[97, 96, 86, 97, 83],
}
print(dict0)
#calculate average of student A,Ｂ and C
sum_a = 0
for a in dict0["StuA"]:
    sum_a+=a
avg_A = sum_a/5
sum_b = 0
for b in dict0["StuB"]:
    sum_b+=b
avg_B = sum_b/5
sum_c = 0
for c in dict0["StuC"]:
    sum_c+=c
avg_C = sum_c/5
print(f"""
A學生平均成績 : {avg_A}
B學生平均成績 : {avg_B}
C學生平均成績 : {avg_C}""")
#calculate averag of each subject
sum_list = [0,0,0,0,0]
avg_list = []
for subject in range(5):
    for score in dict0.values():
        if type(score[subject])==int:
            sum_list[subject]+=score[subject]
    avg_list.append(sum_list[subject]/3)
print(f"""
國文平均成績 : {avg_list[0]}
英文平均成績 : {avg_list[1]}
數學平均成績 : {avg_list[2]}
自然平均成績 : {avg_list[3]}
社會平均成績 : {avg_list[4]}
""")