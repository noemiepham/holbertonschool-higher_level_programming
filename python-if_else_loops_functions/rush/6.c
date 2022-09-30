#include <stdio.h>
int main(void)
{
     int i = 0;
     int j;
     while ( i < 9)
     {
          j = i + 1;
               while (j < 10)
               {
                    printf("%d", i);
                    printf("%d\n", j);
                    j++;
               }      
     i++;
     }
}