def has_33(a):
    for i in range(len(a)-1):
        if a[i]==3 and a[i+1]==3:
            return True
    return False

a=[1,3,3]
print(has_33(a))