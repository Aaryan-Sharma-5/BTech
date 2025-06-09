#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

struct Object
{
  double value, weight, ratio;
};

bool compare(Object a, Object b) { return a.ratio > b.ratio; }

double fractional_knapsnack(int capacity, vector<Object> &Objects)
{
  int n = Objects.size();
  for (int i = 0; i < n; i++)
  {
    Objects[i].ratio = Objects[i].value / Objects[i].weight;
  }
  sort(Objects.begin(), Objects.end(), compare);
  double total_value = 0.0;
  int cw = 0;
  for (int i = 0; i < n; i++)
  {
    if (cw + Objects[i].weight <= capacity)
    {
      cw += Objects[i].weight;
      total_value += Objects[i].value;
    }
    else
    {
      double fractional = (double)(capacity - cw) / Objects[i].weight;
      total_value += Objects[i].value * fractional;
      break;
    }
  }
  return total_value;
}

int main()
{
  int n, capacity;
  cout << "Enter number of Objects: ";
  cin >> n;
  cout << "Enter the capacity of knapsack: ";
  cin >> capacity;
  vector<Object> Objects(n);
  cout << "Enter value and weight of each Object respectively: " << endl;
  for (int i = 0; i < n; i++)
  {
    cin >> Objects[i].value >> Objects[i].weight;
  }
  double max_profit = fractional_knapsnack(capacity, Objects);
  cout << "Maximum profit: " << max_profit << endl;
}