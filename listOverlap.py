# #List Overlap
# lst1 = [1,2,3,4]
# lst2 = [3,4,5,6]

# # overlap = []

# # for i in lst1:
# #     if i in lst2:
# #         overlap.append(i)
# # print(overlap)

# print(list(set(lst1) & set(lst2)))
lst = [1,2,3,4,5]
print(dir(lst))
lst.insert(4,4)
lst.append(6)
lst.pop()
lst.remove(4)
lst.reverse()
print(lst)