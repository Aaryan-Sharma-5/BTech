#include <bits/stdc++.h>

using namespace std;

int main()
{
  vector<int> v;
  for (int i = 0; i < 5; i++)
  {
    int x;
    cin >> x;
    v.push_back(x);
  }
  sort(v.begin(), v.end());
  long long minSum = static_cast<long long>(v[0]) + v[1] + v[2] + v[3];
  long long maxSum = static_cast<long long>(v[1]) + v[2] + v[3] + v[4];
  cout << minSum << " " << maxSum << endl;
  return 0;
}