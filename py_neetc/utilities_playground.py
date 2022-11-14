from utilities import MyUtilities

if __name__=='__main__':
    print ("Start...a")
 
    n = [1,2,6,12,14,15,22,44,56,106, 78,100,105,17,0,30,22]
    n.sort()
    print (n)
    r = MyUtilities.build_bst(n)
    l = MyUtilities.get_tree(r,req='inorder')
    MyUtilities.print_tree(r)

    print ("END!")
