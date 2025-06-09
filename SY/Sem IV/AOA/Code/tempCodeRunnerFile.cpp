#include <bits/stdc++.h>
using namespace std;

void printDPMatrix(const vector<vector<int>> &dp, const string &X, const string &Y)
{
  cout << "\nDP Matrix (LCS lengths):\n";
  cout << "    ";
  for (int j = 0; j < Y.length(); j++)
  {
    cout << Y[j] << " ";
  }
  cout << endl;

  for (int i = 0; i <= X.length(); i++)
  {
    if (i == 0)
    {
      cout << "  ";
    }
    else
    {
      cout << X[i - 1] << " ";
    }

    for (int j = 0; j <= Y.length(); j++)
    {
      cout << dp[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

pair<string, vector<vector<int>>> lcs(const string &X, const string &Y)
{
  int m = X.length();
  int n = Y.length();

  vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
  vector<vector<char>> direction(m + 1, vector<char>(n + 1));
  for (int i = 1; i <= m; ++i)
  {
    for (int j = 1; j <= n; ++j)
    {
      if (X[i - 1] == Y[j - 1])
      {
        dp[i][j] = dp[i - 1][j - 1] + 1;
        direction[i][j] = 'D';
      }
      else if (dp[i - 1][j] >= dp[i][j - 1])
      {
        dp[i][j] = dp[i - 1][j];
        direction[i][j] = 'U';
      }
      else
      {
        dp[i][j] = dp[i][j - 1];
        direction[i][j] = 'L';
      }
    }
  }

  string lcs_str;
  lcs_str.reserve(dp[m][n]);

  int i = m, j = n;
  while (i > 0 && j > 0)
  {
    if (direction[i][j] == 'D')
    {
      lcs_str.push_back(X[i - 1]);
      i--;
      j--;
    }
    else if (direction[i][j] == 'U')
    {
      i--;
    }
    else
    {
      j--;
    }
  }

  reverse(lcs_str.begin(), lcs_str.end());
  return {lcs_str, dp};
}

int main()
{
  string X, Y;

  cout << "Enter the first string: ";
  cin >> X;
  cout << "Enter the second string: ";
  cin >> Y;

  auto [result, dp] = lcs(X, Y);

  cout << "LCS of \"" << X << "\" and \"" << Y << "\" is \"" << result << "\"" << endl;

  printDPMatrix(dp, X, Y);
}