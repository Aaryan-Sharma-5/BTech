#include <bits/stdc++.h>
#define endl '\n';
using namespace std;

int main()
{
  int n, head, move = 0;
  cout << "Enter the number of requests: ";
  cin >> n;
  vector<int> requests(n);
  cout << "Enter the requests: " << endl;
  for (int i = 0; i < n; ++i)
  {
    cin >> requests[i];
  }

  cout << "Enter the initial position of the disk: ";
  cin >> head;
  cout << "\nSequence of movement:" << endl;
  cout << head;
  for (int i = 0; i < n; ++i)
  {
    move += abs(requests[i] - head);
    head = requests[i];
    cout << " -> " << head;
  }
  cout << "\n\nSeek Time = " << move << endl;
  return 0;
}
