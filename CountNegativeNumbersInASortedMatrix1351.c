int countNegatives(int** grid, int gridSize, int* gridColSize){
    int quant=0;
    for(int i = 0; i < gridSize; i++)
        for(int j = 0; j < (*gridColSize); j++)
            if(grid[i][j]<0)
                quant++;
    return quant;
}

//Caso de teste
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
printf(countNegatives(grid))