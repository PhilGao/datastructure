from datastructure import *

if __name__ =='__main__':
    singlelist = SingleLink()
    for i in range(1,5):
        singlelist.prepend(i)
    singlelist.printall()

    for i in range(6,10):
        singlelist.append(i)
    singlelist.printall()

    singlelist.pop()
    singlelist.printall()
    singlelist.pop_last()
    singlelist.printall()

    singlelist.for_each(lambda x: print(x))
    singlelist.for_each(lambda x: print(x.item+1,end=','))
    print('')
    results = singlelist.filter(lambda x: x == 5)
    print(results) # why not None ???????
    for result in results:
        print(result)