#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void generateSubsequences(vector<int> &nums)
{
  int n = nums.size();
  int totalSubsequences = 1 << n;

  for (int i = 0; i < totalSubsequences; i++)
  {
    vector<int> subsequence;
    for (int j = 0; j < n; j++)
    {
      if (i & (1 << j))
      {
        subsequence.push_back(nums[j]);
      }
    }
    cout << "{ ";
    for (int num : subsequence)
    {
      cout << num << " ";
    }
    cout << "}" << endl;
  }
}

int main()
{
  vector<int> nums = {1, 2, 3};
  generateSubsequences(nums);
  return 0;
}