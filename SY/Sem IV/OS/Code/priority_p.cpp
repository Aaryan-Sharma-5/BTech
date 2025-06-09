#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

struct Process
{
  int pid;
  float arrivalTime;
  float burstTime;
  float remainingTime;
  float completionTime;
  float turnaroundTime;
  float waitingTime;
  int priority;
};

struct comparePriority
{
  bool operator()(Process &a, Process &b)
  {
    if (a.priority == b.priority)
      return a.arrivalTime > b.arrivalTime; // If priorities are equal, then compare arrival times
    return a.priority < b.priority;         // Higher priority first
  }
};

void findCompletionTime(Process proc[], int n)
{
  float current_time = 0;
  int completed = 0;
  int i = 0;
  priority_queue<Process, vector<Process>, comparePriority> pq;

  // Sort processes by Arrival Time (AT)
  sort(proc, proc + n, [](const Process &a, const Process &b)
       { return a.arrivalTime < b.arrivalTime; });

  while (completed < n)
  {
    while (i < n && proc[i].arrivalTime <= current_time)
    {
      pq.push(proc[i]);
      i++;
    }

    if (pq.empty())
    {
      current_time++;
      continue;
    }

    Process currProc = pq.top();
    pq.pop();

    currProc.remainingTime--;
    current_time++;

    if (currProc.remainingTime == 0)
    {
      completed++;
      currProc.completionTime = current_time;
      currProc.turnaroundTime = currProc.completionTime - currProc.arrivalTime;
      currProc.waitingTime = currProc.turnaroundTime - currProc.burstTime;
    }
    if (currProc.remainingTime > 0)
    {
      pq.push(currProc);
    }
    else
    {
      proc[currProc.pid - 1] = currProc; // Update the process in the original array
    }
  }
}

void printAvgTime(Process proc[], int n)
{
  float total_wt = 0, total_tat = 0;
  for (int i = 0; i < n; i++)
  {
    total_wt += proc[i].waitingTime;
    total_tat += proc[i].turnaroundTime;
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

  // Input process details
  for (int i = 0; i < n; i++)
  {
    cout << "Enter the arrival time of process " << i + 1 << ": ";
    cin >> proc[i].arrivalTime;
    cout << "Enter the burst time of process " << i + 1 << ": ";
    cin >> proc[i].burstTime;
    cout << "Enter the priority of process " << i + 1 << ": ";
    cin >> proc[i].priority;

    proc[i].pid = i + 1;
    proc[i].remainingTime = proc[i].burstTime;
  }
  findCompletionTime(proc, n);
  cout << endl;
  cout << "PN\tAT\tBT\tPriority\tCT\tTAT\tWT" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << proc[i].pid << "\t" << proc[i].arrivalTime << "\t" << proc[i].burstTime << "\t"
         << proc[i].priority << "\t\t" << proc[i].completionTime << "\t"
         << proc[i].turnaroundTime << "\t" << proc[i].waitingTime << endl;
  }
  printAvgTime(proc, n);

  return 0;
}