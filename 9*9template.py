(1)for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,j*i),end='\t')

    print('\n')
    值得注意的是格式
    
（2）迭代大法
def f(i):
    if i>=1:
        f(i-1)
        print(['%d*%d=%d' %(j,i,j*i )for j in range(1,i+1)])

if __name__=='__main__':
    f(9)
   格式不一样，print（['']）
