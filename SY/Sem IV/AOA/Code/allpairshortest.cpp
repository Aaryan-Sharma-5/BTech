#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void allPair(vector<vector<int>> &A)
{
  int n = A.size();

  for (int k = 0; k < n; k++)
  {
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        if (A[i][k] == -1 || A[k][j] == -1)
        {
          continue;
        }

        if (A[i][j] == -1 || A[i][j] > A[i][k] + A[k][j])
        {
          A[i][j] = A[i][k] + A[k][j];
        }
      }
    }
  }
}

void printMatrix(const vector<vector<int>> &A)
{
  int n = A.size();
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      if (A[i][j] == -1)
      {
        cout << "INF ";
      }
      else
      {
        cout << A[i][j] << "   ";
      }
    }
    cout << endl;
  }
}

int main()
{
  vector<vector<int>> A = {
      {0, 3, -1, 7},
      {8, 0, 2, -1},
      {5, -1, 0, 1},
      {2, -1, -1, 0}};

  cout << "Initial Adjacency Matrix:" << endl;
  printMatrix(A);

  allPair(A);

  cout << "\nAll-Pairs Shortest Path Matrix:" << endl;
  printMatrix(A);

  return 0;
}
