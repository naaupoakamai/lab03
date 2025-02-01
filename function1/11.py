def polindrom(st):
    cleaned_st = ""
    for char in st:
        if char != " ":
            cleaned_st += char.lower()
    a=0
    b=len(st)-1
    while a<b:
        if st[a]!=st[b]:
            return False
        a+=1
        b-=1
    return True
            
st=input()
print(polindrom(st))
