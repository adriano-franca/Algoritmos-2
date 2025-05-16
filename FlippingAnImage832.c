//Feita em C

int** flipAndInvertImage(int** image, int imageSize, int* imageColSize, int* returnSize, int** returnColumnSizes){
    int i, j;

    *returnSize = imageSize;
    int colSize = *imageColSize;
    *returnColumnSizes = (int *)malloc(sizeof(int)*colSize);

    int **out = malloc(sizeof(int *)*imageSize);
    for(i = 0;i < imageSize; i++){
        out[i] = malloc(sizeof(int)*colSize);
        (*returnColumnSizes)[i] = colSize;
    }
    for(i=0 ; i< imageSize; i++){
        for(j = 0;j < colSize; j++){
            out[i][j] = image[i][colSize-1-j];
            }
        }

    for(i=0 ; i< imageSize; i++){
        for(j = 0;j < colSize; j++){
            if(out[i][j]==0){
                out[i][j]=1;
            }else{
                out[i][j]=0;
            }
        }
    }
    return out;
}

//Caso de teste
image = [[1,1,0],[1,0,1],[0,0,0]]
printf(flipAndInvertImage(image))