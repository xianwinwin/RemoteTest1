from utilities import MyUtilities

def playground1():
    n = [1,2,6,12,14,15,22,44,56,106, 78,100,105,17,0,30,22]
    n.sort()
    print (n)
    root = MyUtilities.build_bst(n)
    MyUtilities.print_tree(root)
    #l = MyUtilities.get_tree(r,req='inorder')
    #print (l)

def playground2():
    n = [1,9,14,36,72,66,12,54,7,0]
    r = MyUtilities.build_tree(n)
    MyUtilities.print_tree(r)

def playground3():
    n=[1,6,4,2,8,9,12,13,57,0,2]
    r = MyUtilities.build_linked_list(n)
    MyUtilities.print_linked_list(r)

def playground4(): 
    root = MyUtilities.build_tree( [1,6,2,3,3,None,None,4,5])
    MyUtilities.print_tree(root, init_space=5)

if __name__=='__main__':
    print ("Start...b")
    playground4()
    print ("END!")