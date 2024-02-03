console.log ("hi there")

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const n = [1,5,6,9,12,16,20,21,22,23,24,40,50,55,56]

function array2bst()
{
    function dfs(array)
    {
        if (array==undefined || array.length==0)
        {
            return 
        }

        const mid = Math.floor((array.length-1)/2)
        const midv = array[mid]
        let n = new Node(midv)
        n.left = dfs(array.slice(0,mid))
        n.right = dfs(array.slice(mid+1,array.length))
        return n
    }

    return dfs(n)
}

let r = array2bst()
console.log(r)