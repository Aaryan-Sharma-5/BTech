#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

struct Job
{
  int id, deadline, profit;
};

bool compare(Job a, Job b) { return a.profit > b.profit; }

int job_scheduling(vector<Job> &jobs, int max_deadline)
{
  sort(jobs.begin(), jobs.end(), compare);
  vector<int> schedule(max_deadline, -1);
  int total_profit = 0, jobs_over = 0;

  for (Job &job : jobs)
  {
    for (int i = min(max_deadline, job.deadline) - 1; i >= 0; i--)
    {
      if (schedule[i] == -1)
      {
        schedule[i] = job.id; 
        total_profit += job.profit;
        jobs_over++;
        break;
      }
    }
  }

  cout << "Scheduled Jobs: ";
  for (int i = 0; i < max_deadline; i++)
  {
    if (schedule[i] != -1)
    {
      cout << schedule[i] << " ";
    }
  }
  cout << endl;

  return total_profit;
}

int main()
{
  int n;
  cout << "Enter number of jobs: ";
  cin >> n;
  vector<Job> jobs(n);
  int max_deadline = 0;

  cout << "Enter Job ID, Deadline, and Profit for each job: " << endl;
  for (int i = 0; i < n; i++)
  {
    cin >> jobs[i].id >> jobs[i].deadline >> jobs[i].profit;
    max_deadline = max(max_deadline, jobs[i].deadline);
  }

  int max_profit = job_scheduling(jobs, max_deadline);
  cout << "Maximum Profit: " << max_profit << endl;
}
