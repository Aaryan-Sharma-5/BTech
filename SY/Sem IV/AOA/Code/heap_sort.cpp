#include <bits/stdc++.h>
using namespace std;

void heapify(vector<int> &a, int n, int i)
{
  int largest = i, left = 2 * i + 1, right = 2 * i + 2;
  if (left < n && a[left] > a[largest])
  {
    largest = left;
  }
  if (right < n && a[right] > a[largest])
  {
    largest = right;
  }
  if (largest != i)
  {
    swap(a[i], a[largest]);
    heapify(a, n, largest);
  }
}

void heapSort(vector<int> &a, int n)
{
  // Build max heap
  for (int i = n / 2 - 1; i >= 0; i--)
  {
    heapify(a, n, i);
  }

  // Extract elements from the heap one by one
  for (int i = n - 1; i > 0; i--)
  {
    swap(a[0], a[i]);  // Move current root to the end
    heapify(a, i, 0);   // Call heapify on the reduced heap
  }
}

int main()
{
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  vector<int> v(n);

  cout << "Enter the elements: ";
  for (int i = 0; i < n; i++)
  {
    cin >> v[i];
  }

  heapSort(v, n);
  cout << "Sorted array: ";
  for (int i = 0; i < n; i++)
  {
    cout << v[i] << " ";
  }

  return 0;
}
