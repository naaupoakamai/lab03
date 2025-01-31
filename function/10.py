def unique_elements(lst):
    new_list=[]
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list

old_list=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6]
print(unique_elements(old_list))