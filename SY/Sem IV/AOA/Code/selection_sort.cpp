#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;

void selectionSort(long arr[], int n)
{
  for (int i = 0; i < n - 1; i++)
  {
    int min = i;
    for (int j = i + 1; j < n; j++)
    {
      if (arr[j] < arr[min])
      {
        min = j;
      }
    }
    swap(arr[i], arr[min]);
  }
}

int main()
{
  long n = 10000;
  long arr[n];
  srand(time(0));
  int i;
  for (i = 0; i < n; i++)
  {
    arr[i] = rand() % 10000;
  }
  auto start = high_resolution_clock::now();
  selectionSort(arr, n);
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << "\n";
  cout << "Time taken by function: " << duration.count() << " microseconds" << endl;
}