#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
const int MOD = 1e9 + 7;

int sumSubseqWidths(vector<int> &nums)
{
    int n = nums.size();
    sort(nums.begin(), nums.end());
    vector<ll> twos(n, 1);
    for (int i = 1; i < n; i++)
    {
        twos[i] = (twos[i - 1] * 2) % MOD;
    }

    ll out = 0;
    for (int i = 0; i < n; i++)
    {
        ll s = (twos[i] - twos[n - i - 1]) % MOD;
        s = (s * nums[i]) % MOD;
        out = (out + s) % MOD;
    }
    return (out + MOD) % MOD;
}

int main()
{
    vector<int> nums = {2, 1, 3};
    cout << sumSubseqWidths(nums) << endl;
}