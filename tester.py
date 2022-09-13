
def test(a):
    comp = []
    
    l,r = 1, len(a)-1
    while l != r or l != r-1:
        comp.append(a[l])
        comp.append(a[r])
        l-=1
        r-=1
    
    if a.sort() == comp:
        return True
    else: 
        return False    

print(test([1, 3, 5, 6, 4, 2]))