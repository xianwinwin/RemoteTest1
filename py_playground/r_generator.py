
def get_itr():
    for i in range(0,5):
        yield i

def foo():
    print ("foo")
    itr = get_itr()
    print ('itr:=',itr)
    for i in itr:
        print (i)

if __name__=='__main__':
    print ("Start...")
    foo()
    print ('END')