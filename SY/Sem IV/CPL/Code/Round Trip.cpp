#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

bool DFS(vector<int> graph[], int s, vector<bool> &visited, vector<int> &parent, vector<int> &cycle)
{
  visited[s] = true;
  for (int x : graph[s])
  {
    if (!visited[x])
    {
      parent[x] = s;
      if (DFS(graph, x, visited, parent, cycle))
      {
        return true;
      }
    }
    else if (x != parent[s])
    {
      cycle.push_back(s);
      int current = s;
      while (current != x)
      {
        current = parent[current];
        cycle.push_back(current);
      }
      reverse(cycle.begin(), cycle.end());
      cycle.push_back(x);
      return true;
    }
  }
  return false;
}

int main()
{
  int n, m;
  cin >> n >> m;
  vector<int> graph[n + 1];
  for (int i = 0; i < m; i++)
  {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  
  vector<bool> visited(n + 1, false);
  vector<int> parent(n + 1, -1);
  vector<int> cycle;
  for (int i = 1; i <= n; i++)
  {
    if (!visited[i])
    {
      if (DFS(graph, i, visited, parent, cycle))
      {
        cout << cycle.size() << endl;
        for (int city : cycle)
        {
          cout << city << " ";
        }
        cout << endl;
        return 0;
      }
    }
  }
  cout << "IMPOSSIBLE" << endl;
}