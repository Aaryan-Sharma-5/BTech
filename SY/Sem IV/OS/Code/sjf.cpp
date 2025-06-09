#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

struct Process
{
  int pid;
  float arrival_time;
  float burst_time;
  float completion_time;
  float turnaround_time;
  float waiting_time;
};

bool compare(Process a, Process b)
{
  if (a.arrival_time == b.arrival_time)
  {
    return a.burst_time < b.burst_time;
  }
  return a.arrival_time < b.arrival_time;
}

void sjfScheduling(Process proc[], int n)
{
  sort(proc, proc + n, compare);
  int currentTime = 0;

  for (int i = 0; i < n; i++)
  {
    int minIndex = -1;
    int minburst_time = INT_MAX;
    for (int j = 0; j < n; j++)
    {
      if (proc[j].arrival_time <= currentTime && proc[j].completion_time == 0 && proc[j].burst_time < minburst_time)
      {
        minburst_time = proc[j].burst_time;
        minIndex = j;
      }
    }

    if (minIndex == -1)
    {
      currentTime++;
      i--;
      continue;
    }

    currentTime += proc[minIndex].burst_time;
    proc[minIndex].completion_time = currentTime;
    proc[minIndex].turnaround_time = proc[minIndex].completion_time - proc[minIndex].arrival_time;
    proc[minIndex].waiting_time = proc[minIndex].turnaround_time - proc[minIndex].burst_time;
  }
}

void findavgTime(Process proc[], int n)
{
  float avg_wt = 0, avg_tat = 0;
  for (int i = 0; i < n; i++)
  {
    avg_wt += proc[i].waiting_time;
    avg_tat += proc[i].turnaround_time;
  }

  cout << "Average waiting time = " << avg_wt / n << endl;
  cout << "Average turnaround time = " << avg_tat / n << endl;
}

int main()
{
  int n;
  cout << "Enter the number of processes: ";
  cin >> n;
  Process proc[n];

  for (int i = 0; i < n; i++)
  {
    cout << "Enter the arrival time of process " << i + 1 << ": ";
    cin >> proc[i].arrival_time;
    cout << "Enter the burst time of process " << i + 1 << ": ";
    cin >> proc[i].burst_time;
    proc[i].pid = i + 1;
  }

  sjfScheduling(proc, n);

  cout << "PN\tAT\tBT\tCT\tWT\tTAT" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << proc[i].pid << "\t" << proc[i].arrival_time << "\t" << proc[i].burst_time << "\t" << proc[i].completion_time << "\t" << proc[i].waiting_time << "\t" << proc[i].turnaround_time << endl;
  }

  findavgTime(proc, n);
}
