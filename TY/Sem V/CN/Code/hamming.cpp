#include <bits/stdc++.h>
using namespace std;

int Parity(int m)
{
  int r = 0;
  while ((1 << r) < (m + r + 1))
  {
    r++;
  }
  return r;
}

bool isPowerOfTwo(int x)
{
  return (x & (x - 1)) == 0;
}

int main()
{
  cout << "Enter the number of data bits: ";
  int m;
  cin >> m;

  vector<int> data(m);
  cout << "Enter the data bits (space separated): ";
  for (int i = 0; i < m; i++)
  {
    cin >> data[i];
  }

  cout << "\nUser input data bits: ";
  for (int i = 0; i < m; i++)
  {
    cout << data[i];
  }
  cout << endl;

  int r = Parity(m);
  int n = m + r;

  vector<int> encoded(n + 1, 0);
  for (int i = 1, j = 0; i <= n; i++)
  {
    if (isPowerOfTwo(i))
    {
      encoded[i] = 0;
    }
    else
    {
      encoded[i] = data[j++];
    }
  }

  vector<int> parityValues(r);
  for (int i = 0; i < r; i++)
  {
    int parityPos = 1 << i;
    int parity = 0;
    for (int j = parityPos; j <= n; j++)
    {
      if (j & parityPos)
      {
        parity ^= encoded[j];
      }
    }
    encoded[parityPos] = parity;
    parityValues[i] = parity;
  }

  cout << "\nParity bits and their values:\n";
  for (int i = 0; i < r; i++)
  {
    cout << "P" << (1 << i) << " = " << parityValues[i] << endl;
  }

  cout << "\nEncoded Hamming code (with parity bits): ";
  for (int i = n; i >= 1; i--)
  {
    cout << encoded[i];
  }
  cout << endl;

  int flipBit;
  cout << "\nEnter bit position to flip to simulate error (0 for no flip): ";
  cin >> flipBit;

  vector<int> received = encoded;
  if (flipBit != 0)
  {
    if (flipBit >= 1 && flipBit <= n)
    {
      received[flipBit] ^= 1;
      cout << "Bit " << flipBit << " flipped\n";
    }
    else
    {
      cout << "Invalid bit position to flip, No bit flipped\n";
    }
  }
  else
  {
    cout << "No bit flipped\n";
  }

  cout << "Received message: ";
  for (int i = n; i >= 1; i--)
  {
    cout << received[i];
  }
  cout << endl;

  int errorPos = 0;
  for (int i = 0; i < r; i++)
  {
    int parityPos = 1 << i;
    int parity = 0;
    for (int j = parityPos; j <= n; j++)
    {
      if (j & parityPos)
      {
        parity ^= received[j];
      }
    }
    if (parity != 0)
    {
      errorPos += parityPos;
    }
  }

  if (errorPos == 0)
  {
    cout << "\nNo error detected in the received message\n";
  }
  else
  {
    cout << "\nError detected at bit: P" << errorPos << endl;
    received[errorPos] ^= 1;

    cout << "Corrected message: ";
    for (int i = n; i >= 1; i--)
    {
      cout << received[i];
    }
    cout << endl;
  }

  return 0;
}