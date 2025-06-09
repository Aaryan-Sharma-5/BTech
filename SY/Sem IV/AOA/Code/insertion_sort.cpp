#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;

void insertionSort(long arr[], int n)
{
  for (int i = 1; i < n; i++)
  {
    int select = arr[i];
    int j = i -  1;
    while (j >= 0 && arr[j] > select)
    {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = select;
  }
}

int main()
{
  long n = 100;
  long arr[n];
  srand(time(0));
  int i;
  for (i = 0; i < n; i++)
  {
    arr[i] = rand() % 10000;
  }
  auto start = high_resolution_clock::now();
  insertionSort(arr, n);
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << "\n";
  cout << "Time taken by function: " << duration.count() << " microseconds" << endl;
}