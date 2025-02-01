def spy_game(nums):
    list=[0,0,7]
    index=0
    for num in nums:
        if num==list[index]:
            index+=1
        if index==len(list):
            return True
    return False

print(spy_game([1,7,2,0,4,5,0]))
