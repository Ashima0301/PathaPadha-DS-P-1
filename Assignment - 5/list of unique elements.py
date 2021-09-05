def unique_list(l1):
  l2 = []
  for i in l1:
    if i not in l2:
      l2.append(i)
  return l2
l1=[9,9,8,7,6,9,5]
print("Unique List: ",unique_list(l1))
