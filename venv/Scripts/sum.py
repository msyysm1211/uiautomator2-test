

a=[1,2,3]
b=4
def sum(all,str):
    for i in range(len(all)):
        if all[i]==str:
            return False
        else:
            all.append(str)
            return True


print (sum(a,b))