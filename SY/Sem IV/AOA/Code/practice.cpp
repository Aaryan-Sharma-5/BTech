#include <bits/stdc++.h>
using namespace std;

void allPair(vector<vector<int>> &A){
  int n = A.size();
  for(int k = 0; k < n; k++){
    for(int i = 0; i <n; i++){
      for(int j = 0;j <n;j++){
        if(A[i][k] == INT_MAX || A[k][j] == INT_MAX){
          continue;
        }
        if(A[i][j] == INT_MAX ||A[i][j] > A[i][k] + A[k][j]){
          A[i][j] = A[i][k] + A[k][j];
        }
      }
    }
  }
}

int main(){
  int n;
  cout << "Enter the number of vertices: ";
  cin >> n;

  vector<vector<int>> W(n, vector<int>(n));
  cout << "Enter the adjacency matrix: " << endl;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      cin >> W[i][j];
      if(i != j && W[i][j] == 0)
        W[i][j] = INT_MAX;
    }
  }
}