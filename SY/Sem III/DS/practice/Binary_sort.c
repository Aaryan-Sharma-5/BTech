#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

void bubbleSort(int arr[], int n){
  bool swapped;
  for(int i = 0; i < n - 1; i++){
    swapped = false;
    for(int j = 0; j < n - i - 1; j++){
      if(arr[j] > arr[j + 1]){
        swap(&arr[j], &arr[j + 1]);
        swapped = true;
      }
    }
    if(!swapped){
      break;
    }
  }
}

void printArray(int arr[], int n){
  for(int i = 0; i < n; i++){
    printf("%d\t", arr[i]);
  }
  printf("\n");
}

int main(){
  int n;
  printf("Enter the number of elements: ");
  scanf("%d", &n);
  
  int arr[n];
  for(int i = 0; i < n; i++){
    printf("Enter integer %d: ", i + 1);
    scanf("%d", &arr[i]);
  }
  bubbleSort(arr, n);
  printf("Sorted array: ");
  printArray(arr, n);
  
  return 0;
}