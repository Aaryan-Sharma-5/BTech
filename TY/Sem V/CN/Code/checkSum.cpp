#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  unsigned int sum = 0, wrapsum, checksum, recvsum;
  cout << "Enter number of 16-bit hexadecimal values: ";
  cin >> n;

  vector<unsigned int> data(n);
  cout << "Enter " << n << " hexadecimal values (0x0000 to 0xFFFF): ";
  for (int i = 0; i < n; i++)
  {
    cin >> hex >> data[i];
    sum += data[i];
    sum = (sum & 0xFFFF) + (sum >> 16);
    sum = (sum & 0xFFFF) + (sum >> 16);
  }

  wrapsum = sum;
  checksum = ~wrapsum & 0xFFFF;
  cout << "Wrapsum (before sending): 0x" << hex << setw(4) << setfill('0') << wrapsum << endl;
  cout << "Checksum (before sending): 0x" << hex << setw(4) << setfill('0') << checksum << endl;

  recvsum = 0;
  cout << "Enter received " << n << " hexadecimal values: ";
  for (int i = 0; i < n; i++)
  {
    unsigned int val;
    cin >> hex >> val;
    recvsum += val;
    recvsum = (recvsum & 0xFFFF) + (recvsum >> 16);
    recvsum = (recvsum & 0xFFFF) + (recvsum >> 16);
  }
  recvsum += checksum;
  recvsum = (recvsum & 0xFFFF) + (recvsum >> 16);
  recvsum = (recvsum & 0xFFFF) + (recvsum >> 16);

  cout << "Checksum after receiving: 0x" << hex << setw(4) << setfill('0') << recvsum << endl;
  if (recvsum == 0xFFFF)
  {
    cout << "No Error" << endl;
  }
  else
  {
    cout << "Error Detected" << endl;
  }
}
