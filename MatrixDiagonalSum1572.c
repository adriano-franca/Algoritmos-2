int diagonalSum(int** mat, int matSize, int* matColSize){
    int soma = 0, i, meio;
    for(i = 0; i < matSize ; i++){
        soma+=mat[i][i];
        soma+=mat[i][matSize-1-i];
    }
    if(matSize%2==0){
        return soma;
    }else{
        return soma - mat[matSize/2][matSize/2];
    }
}