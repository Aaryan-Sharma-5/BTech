#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int removeDuplicates(vector<int> &nums)
{
  if (nums.empty())
  {
    return 0;
  }

  int unique = 0;
  for (int i = 1; i < nums.size(); i++)
  {
    if (nums[i] != nums[unique])
    {
      unique++;
      nums[unique] = nums[i];
    }
  }
  return unique + 1;
}

int main()
{
  vector<int> nums = {1, 1, 2};
  cout << removeDuplicates(nums) << endl;
}
