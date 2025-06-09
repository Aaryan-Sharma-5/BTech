#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int knapsack_01(int capacity, vector<int> &values, vector<int> &weights, int n)
{
  vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

  for (int i = 1; i <= n; i++)
  {
    for (int w = 0; w <= capacity; w++)
    {
      if (weights[i - 1] <= w)
      {
        dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
      }
      else
      {
        dp[i][w] = dp[i - 1][w];
      }
    }
  }
  return dp[n][capacity];
}

int main()
{
  int n, capacity;
  cout << "Enter number of objects: ";
  cin >> n;
  cout << "Enter the capacity of knapsack: ";
  cin >> capacity;

  vector<int> values(n), weights(n);
  cout << "Enter value and weight of each object respectively: " << endl;
  for (int i = 0; i < n; i++)
  {
    cin >> values[i] >> weights[i];
  }

  int max_profit = knapsack_01(capacity, values, weights, n);
  cout << "Maximum profit: " << max_profit << endl;
}
