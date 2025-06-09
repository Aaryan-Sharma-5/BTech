#include <bits/stdc++.h>
using namespace std;

int partition(int a[], int low, int high)
{
  int pivot = a[low];
  int i = low;

  for (int j = low + 1; j <= high; j++)
  {
    if (a[j] < pivot)
    {
      i++;
      swap(a[i], a[j]);
    }
  }
  swap(a[i], a[low]);
  return i;
}

void quickSort(int a[], int low, int high)
{
  if (low < high)
  {
    int q = partition(a, low, high);
    quickSort(a, low, q - 1);
    quickSort(a, q + 1, high);
  }
}

int main()
{
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  int a[n];
  cout << "Enter the elements: ";
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  
  quickSort(a, 0, n - 1);
  cout << "Sorted Array: ";
  for (int i = 0; i < n; i++)
  {
    cout << a[i] << " ";
  }
}