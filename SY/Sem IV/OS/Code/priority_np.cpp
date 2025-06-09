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
  int priority;
};

void findCompletionTime(Process proc[], int n)
{
  float current_time = 0;
  vector<bool> is_completed(n, false);

  for (int count = 0; count < n; count++)
  {
    int idx = -1;
    float max_priority = -1;

    for (int i = 0; i < n; i++)
    {
      if (!is_completed[i] && proc[i].arrival_time <= current_time)
      {
        if (proc[i].priority > max_priority)
        {
          max_priority = proc[i].priority;
          idx = i;
        }
      }
    }

    if (idx == -1)
    {
      current_time++;
      continue;
    }

    current_time += proc[idx].burst_time;
    proc[idx].completion_time = current_time;
    is_completed[idx] = true;
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

void findAvgTime(Process proc[], int n)
{
  float total_wt = 0, total_tat = 0;
  for (int i = 0; i < n; i++)
  {
    total_wt += proc[i].waiting_time;
    total_tat += proc[i].turnaround_time;
  }
  cout << "Average turnaround time = " << total_tat / n << endl;
  cout << "Average waiting time = " << total_wt / n << endl;
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
    cout << "Enter the priority of process " << i + 1 << "(higher value means higher priority): ";
    cin >> proc[i].priority;
    proc[i].pid = i + 1;
  }

  sort(proc, proc + n, [](Process a, Process b)
       { return a.arrival_time < b.arrival_time; });

  findCompletionTime(proc, n);
  findTurnAroundTime(proc, n);
  findWaitingTime(proc, n);

  cout << "PN\tAT\tBT\tPriority\tCT\tTAT\tWT" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << proc[i].pid << "\t" << proc[i].arrival_time << "\t" << proc[i].burst_time
         << "\t" << proc[i].priority << "\t\t" << proc[i].completion_time << "\t"
         << proc[i].turnaround_time << "\t" << proc[i].waiting_time << endl;
  }

  findAvgTime(proc, n);
  return 0;
}