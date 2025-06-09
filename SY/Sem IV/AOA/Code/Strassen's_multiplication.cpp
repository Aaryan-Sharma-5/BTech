#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void addMatrix(vector<vector<int>> &A, vector<vector<int>> &B, vector<vector<int>> &C, int size)
{
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      C[i][j] = A[i][j] + B[i][j];
    }
  }
}

void subtractMatrix(vector<vector<int>> &A, vector<vector<int>> &B, vector<vector<int>> &C, int size)
{
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      C[i][j] = A[i][j] - B[i][j];
    }
  }
}

void strassenMatrixMultiplication(vector<vector<int>> &A, vector<vector<int>> &B, vector<vector<int>> &C, int size)
{
  if (size == 2)
  {
    int m1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1]);
    int m2 = (A[1][0] + A[1][1]) * B[0][0];
    int m3 = A[0][0] * (B[0][1] - B[1][1]);
    int m4 = A[1][1] * (B[1][0] - B[0][0]);
    int m5 = (A[0][0] + A[0][1]) * B[1][1];
    int m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1]);
    int m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1]);
    C[0][0] = m1 + m4 - m5 + m7;
    C[0][1] = m3 + m5;
    C[1][0] = m2 + m4;
    C[1][1] = m1 - m2 + m3 + m6;
  }
  else
  {
    int newSize = size / 2;
    vector<int> inner(newSize);
    vector<vector<int>>
        A11(newSize, inner), A12(newSize, inner), A21(newSize, inner), A22(newSize, inner),
        B11(newSize, inner), B12(newSize, inner), B21(newSize, inner), B22(newSize, inner),
        C11(newSize, inner), C12(newSize, inner), C21(newSize, inner), C22(newSize, inner),
        M1(newSize, inner), M2(newSize, inner), M3(newSize, inner), M4(newSize, inner),
        M5(newSize, inner), M6(newSize, inner), M7(newSize, inner),
        AResult(newSize, inner), BResult(newSize, inner);

    for (int i = 0; i < newSize; i++)
    {
      for (int j = 0; j < newSize; j++)
      {
        A11[i][j] = A[i][j];
        A12[i][j] = A[i][j + newSize];
        A21[i][j] = A[i + newSize][j];
        A22[i][j] = A[i + newSize][j + newSize];

        B11[i][j] = B[i][j];
        B12[i][j] = B[i][j + newSize];
        B21[i][j] = B[i + newSize][j];
        B22[i][j] = B[i + newSize][j + newSize];
      }
    }
    addMatrix(A11, A22, AResult, newSize);
    addMatrix(B11, B22, BResult, newSize);
    strassenMatrixMultiplication(AResult, BResult, M1, newSize);

    addMatrix(A21, A22, AResult, newSize);
    strassenMatrixMultiplication(AResult, B11, M2, newSize);

    subtractMatrix(B12, B22, BResult, newSize);
    strassenMatrixMultiplication(A11, BResult, M3, newSize);

    subtractMatrix(B21, B11, BResult, newSize);
    strassenMatrixMultiplication(A22, BResult, M4, newSize);

    addMatrix(A11, A12, AResult, newSize);
    strassenMatrixMultiplication(AResult, B22, M5, newSize);

    subtractMatrix(A21, A11, AResult, newSize);
    addMatrix(B11, B12, BResult, newSize);
    strassenMatrixMultiplication(AResult, BResult, M6, newSize);

    subtractMatrix(A12, A22, AResult, newSize);
    addMatrix(B21, B22, BResult, newSize);
    strassenMatrixMultiplication(AResult, BResult, M7, newSize);

    addMatrix(M1, M4, AResult, newSize);
    subtractMatrix(AResult, M5, BResult, newSize);
    addMatrix(BResult, M7, C11, newSize);

    addMatrix(M3, M5, C12, newSize);
    addMatrix(M2, M4, C21, newSize);

    addMatrix(M1, M3, AResult, newSize);
    subtractMatrix(AResult, M2, BResult, newSize);
    addMatrix(BResult, M6, C22, newSize);

    for (int i = 0; i < newSize; i++)
    {
      for (int j = 0; j < newSize; j++)
      {
        C[i][j] = C11[i][j];
        C[i][j + newSize] = C12[i][j];
        C[i + newSize][j] = C21[i][j];
        C[i + newSize][j + newSize] = C22[i][j];
      }
    }
  }
}

int main()
{
  int n;
  cout << "Enter the size of the matrices (must be a power of 2): ";
  cin >> n;
  vector<vector<int>> A(n, vector<int>(n));
  vector<vector<int>> B(n, vector<int>(n));
  vector<vector<int>> C(n, vector<int>(n, 0));
  cout << "Enter the elements of the first matrix: ";
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cin >> A[i][j];
    }
  }
  cout << "Enter the elements of the second matrix: ";
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cin >> B[i][j];
    }
  }

  strassenMatrixMultiplication(A, B, C, n);
  cout << "Resultant matrix: " << endl;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cout << C[i][j] << " ";
    }
    cout << endl;
  }
}