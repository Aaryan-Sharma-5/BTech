#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void merge(vector<int> &a, int l, int m, int r)
{
  int n1 = m - l + 1;
  int n2 = r - m;
  vector<int> L(n1), R(n2);
  for (int i = 0; i < n1; i++)
  {
    L[i] = a[l + i];
  }
  for (int j = 0; j < n2; j++)
  {
    R[j] = a[m + 1 + j];
  }

  int i = 0, j = 0, k = l;
  for (; i < n1 && j < n2; k++)
  {
    if (L[i] <= R[j])
    {
      a[k] = L[i];
      i++;
    }
    else
    {
      a[k] = R[j];
      j++;
    }
  }

  for (; i < n1; i++, k++)
  {
    a[k] = L[i];
  }
  for (; j < n2; j++, k++)
  {
    a[k] = R[j];
  }
}

void mergeSort(vector<int> &a, int l, int r)
{
  if (l >= r)
  {
    return;
  }
  int m = l + (r - l) / 2;
  mergeSort(a, l, m);
  mergeSort(a, m + 1, r);
  merge(a, l, m, r);
}

int main()
{
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  vector<int> v(n);
  for (int i = 0; i < n; i++)
  {
    cin >> v[i];
  }
  mergeSort(v, 0, n - 1);
  cout << "Sorted array: ";
  for (int i = 0; i < n; i++)
  {
    cout << v[i] << " ";
  }
  cout << endl;
}