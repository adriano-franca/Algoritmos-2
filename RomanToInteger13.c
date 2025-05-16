//Resolvido em C

int romanToInt(char* s) {
    enum romanos {I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000}romanos;
    int valor = 0, contador = 0, aux1, aux2;
    while(contador < strlen(s)){
        switch(s[contador]){
            case 'I':
                aux1 = 1;
                break;
            case 'V':
                aux1 = 5;
                break;
            case 'X':
                aux1 = 10;
                break;
            case 'L':
                aux1 = 50;
                break;
            case 'C':
                aux1 = 100;
                break;
            case 'D':
                aux1 = 500;
                break;
            case 'M':
                aux1 = 1000;
                break;
        }
        switch(s[contador+1]){
            case 'I':
                aux2 = 1;
                break;
            case 'V':
                aux2 = 5;
                break;
            case 'X':
                aux2 = 10;
                break;
            case 'L':
                aux2 = 50;
                break;
            case 'C':
                aux2 = 100;
                break;
            case 'D':
                aux2 = 500;
                break;
            case 'M':
                aux2 = 1000;
                break;
        }
        if(aux1 < aux2){
            valor += aux2-aux1;
            contador+=2;
        }else{
            valor += aux1;
            contador+=1;
        }
        aux1 = 0;
        aux2 = 0;
    }
    return valor;
}

//Caso de teste
s = "III"
printf(romanToInt(s))