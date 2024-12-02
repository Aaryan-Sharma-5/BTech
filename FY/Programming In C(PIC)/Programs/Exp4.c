#include  <stdio.h>
void main()
{
printf("Aaryan Sharma\n");
printf("16010123012\n");

  int s, i, j, n, new;
  printf("Enter the size of the arrays : ");
  scanf("%d", &s);

  int arr[s];
  printf("Enter the elements of the array :\n");
  for (i = 0; i < s; i++)
  {
      scanf("%d", &arr[i]);
  }
  printf("The array is : ");
  for (i = 0; i < s; i++)
  {
    printf("\t%d",arr[i]);
  }
     for (i = 0; i < s; ++i)
     {
        for (j = i + 1; j < s; ++j)
        {
           if (arr[i] > arr[j])
           {
              n = arr[i];
              arr[i] = arr[j];
              arr[j] = n;
           }
        }
     }
  printf("\nThe sorted array is: ");
  for (i = 0; i < s; ++i)
  {
    printf("%d\t",arr[i]);
  }
  printf("\nEnter element to be added in array:");
  scanf("%d",&new);
  arr[s]=new;
  s++;
    for (i = 0; i < s; ++i)
  {
    printf("%d\t",arr[i]);
  }
    for (i = 0; i < s; ++i)
     {
        for (j = i + 1; j < s; ++j)
        {
           if (arr[i] > arr[j])
           {
              n = arr[i];
              arr[i] = arr[j];
              arr[j] = n;
           }
        }
     }
  printf("\nThe sorted array is : ");
  for (i = 0; i < s; ++i)
  {
    printf("%d\t",arr[i]);
  }
}
