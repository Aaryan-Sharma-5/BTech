#include <bits/stdc++.h>
using namespace std;

int main()
{
  const int packets = 9, windowSize = 3, K = 5;
  int base = 1, nextSeq = 1, expected = 1;
  int senderAttempt = 0, receiverReception = 0;

  cout << left
       << setw(10) << "ATTEMPT"
       << setw(10) << "SEND_PKT"
       << setw(10) << "EXPECTED"
       << setw(12) << "STATE" << "\n";

  while (expected <= packets)
  {
    if (nextSeq <= packets && nextSeq < base + windowSize)
    {
      senderAttempt++;
      int s = nextSeq++;
      int expectedBefore = expected;

      bool lost = (senderAttempt % K == 0);
      string outcome;

      if (lost)
      {
        outcome = "LOST";
      }
      else
      {
        receiverReception++;
        if (s == expected)
        {
          outcome = "ACCEPTED";
          expected++;
          base = expected;
        }
        else
        {
          outcome = "DISCARDED";
        }
      }

      cout << left
           << setw(10) << senderAttempt
           << setw(10) << s
           << setw(10) << expectedBefore
           << setw(12) << outcome << "\n";
    }
    else
    {
      nextSeq = base;
    }
  }

  cout << "\nFinal attempts (sender transmissions): " << senderAttempt << "\n";
  cout << "Final receptions (receiver actually saw): " << receiverReception;
}
