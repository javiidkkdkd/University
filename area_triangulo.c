#include <stdio.h>
//*realizar el cálculo del área de un triángulo, para ello se deben ingresar los valores para la base y altura.

int main() { 
    int num;
    int alt;
    int area;

    printf("Ingresa la base del triangulo: \n");
    scanf("%d", &num);
    printf("Muy bien, entonces la base del triangulo es: %d\n", num);

    printf("Ingresa la altura del triangulo: \n");
    scanf("%d", &alt);
    printf("Muy bien, entonces la altura del triangulo es: %d\n", alt);

    area = (num * alt) / 2;
    printf("El área del triángulo es: %d \n", area);
    
    return 0;
}