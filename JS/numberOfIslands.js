

let grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","1","1","0","1"]
  ]


  function countIslands()
  {
    let visited = new Set();
    const ROWS = grid[0].length
    const COLS = grid.length

    function dfs(c,r)
    {
        //in bound?
        const str = String(c)+'-'+String(r)
        if (c>=COLS || r>=ROWS || c<0 || r<0 || visited.has(str))
        {
            return
        }
        
        if (grid[c][r]==1)
        {
            visited.add(str);
            console.log(visited)
            dfs(c,r+1) //go right
            dfs(c,r-1) //go left
            dfs(c+1,r) //go down
            dfs(c-1,r) //go up
        }
        return
    }
    
    let counter = 0;
    //iterate the column
    for (let c=0;c<grid.length; c++)
    {
        //on each colum iterate the row
        for (let r=0; r<grid[0].length; r++)
        {
            const str = String(c)+'-'+String(r)
            const isVisited = visited.has(str)
            const value = grid[c][r]
            if (value==1 && !isVisited)
            {
                counter+=1;
                dfs(c,r)
            }
        }
    }

    return counter;
  }


  const i = countIslands()
  console.log('I found '+i+' islands in the grid')