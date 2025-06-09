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

void findCompletionTime(Process proc[], int n)
{
  float completion_time = 0;
  for (int i = 0; i < n; i++)
  {
    completion_time += proc[i].burst_time;
    proc[i].completion_time = completion_time;
  }
}

void findTurnAroundTime(Process proc[], int n)
{
  for (int i = 0; i < n; i++)
  {
    proc[i].turnaround_time = proc[i].completion_time - proc[i].arrival_time;
  }
}

void findWaitingTime(Process proc[], int n)
{
  for (int i = 0; i < n; i++)
  {
    proc[i].waiting_time = proc[i].turnaround_time - proc[i].burst_time;
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

  sort(proc, proc + n, [](Process a, Process b)
       { return a.arrival_time < b.arrival_time; });

  findCompletionTime(proc, n);
  findTurnAroundTime(proc, n);
  findWaitingTime(proc, n);

  cout << "PN\tAT\tBT\tCT\tWT\tTAT" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << proc[i].pid << "\t" << proc[i].arrival_time << "\t" << proc[i].burst_time << "\t" << proc[i].completion_time << "\t" << proc[i].waiting_time << "\t" << proc[i].turnaround_time << endl;
  }

  findavgTime(proc, n);
}