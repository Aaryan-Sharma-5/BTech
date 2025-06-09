#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main()
{
  int n, head, size, move = 0;

  cout << "Enter the number of requests: ";
  cin >> n;

  vector<int> requests(n);

  cout << "Enter the requests:" << endl;
  for (int i = 0; i < n; ++i)
  {
    cin >> requests[i];
  }

  cout << "Enter the initial position of the disk: ";
  cin >> head;

  cout << "Enter the total disk size: ";
  cin >> size;

  requests.push_back(0);
  requests.push_back(size);
  n += 2;

  sort(requests.begin(), requests.end());

  int pos = 0;
  while (pos < n && requests[pos] < head)
  {
    pos++;
  }

  cout << "\nSequence of head movement:" << endl;
  cout << head;

  for (int i = pos; i < n; ++i)
  {
    move += abs(head - requests[i]);
    head = requests[i];
    cout << " -> " << head;
  }

  move += abs(head - requests[0]);
  head = requests[0];
  cout << " -> " << head;

  for (int i = 1; i < pos; ++i)
  {
    move += abs(head - requests[i]);
    head = requests[i];
    cout << " -> " << head;
  }

  cout << "\n\nSeek Time = " << move;

  return 0;
}