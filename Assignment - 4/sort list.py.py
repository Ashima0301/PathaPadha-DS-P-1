l1=[-38,5231,0,49,-65,234]
sort_l1 = []
while l1:
    min=l1[0]
    for i in l1:
        if i<min:
            min=i
    sort_l1.append(min)
    l1.remove(min)
print("sorted list: ",sort_l1)
