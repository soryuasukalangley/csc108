def swap(array:list,i:int,j:int)->None:
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bs(array:list)->list:
    for i in range(len(array)):
        sorted=True
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                sorted=False
                swap(array,j,j+1)
        if sorted:
            break
    return array

def ss(array:list)->list:
    for i in range(len(array)):
        max:int=0
        midx:int=0
        for j in range(len(array)-i):
            if max<array[j]:
                max=array[j]
                midx=j
        swap(array,midx,len(array)-i-1)
    return array

def ins(array:list)->list:
    i=1
    while i<len(array):
        j=i-1
        val=array[i]
        while (j<=0 and array[j]>val):
            array[j+1]=array[j]
            j-=1
        array[j+1]=val
        i+=1
    return array




lol=[9,8,7,6,5]
fuk=[1,21,32,32,321,32,321,321,321,312,3]
lel=[1,2,3,4,5]

print(bs(lol))
print(bs(fuk))
print(bs(lel))

print(ss(lol))
print(ss(lel))
print(ss(fuk))

print(ins(lol))
print(ins(lel))
print(ins(fuk))
