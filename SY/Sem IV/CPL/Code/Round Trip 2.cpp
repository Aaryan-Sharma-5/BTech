#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

bool found = false;
vector<int> cycle;

bool dfs(int u, vector<vector<int>> &graph, vector<bool> &visited, vector<bool> &in_stack, vector<int> &path)
{
  visited[u] = true;
  in_stack[u] = true;
  path.push_back(u);

  for (int v : graph[u])
  {
    if (!visited[v])
    {
      if (dfs(v, graph, visited, in_stack, path))
      {
        return true;
      }
    }
    else if (in_stack[v])
    {
      auto it = find(path.begin(), path.end(), v);
      if (it != path.end())
      {
        cycle = vector<int>(it, path.end());
        cycle.push_back(v);
        found = true;
        return true;
      }
    }
  }

  in_stack[u] = false;
  path.pop_back();
  return false;
}

int main()
{
  int n, m;
  cin >> n >> m;

  vector<vector<int>> graph(n + 1);
  for (int i = 0; i < m; ++i)
  {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
  }

  vector<bool> visited(n + 1, false);
  vector<bool> in_stack(n + 1, false);
  vector<int> path;

  for (int u = 1; u <= n && !found; ++u)
  {
    if (!visited[u])
    {
      if (dfs(u, graph, visited, in_stack, path))
      {
        break;
      }
    }
  }

  if (found)
  {
    cout << cycle.size() << endl;
    for (size_t i = 0; i < cycle.size(); ++i)
    {
      if (i > 0)
        cout << " ";
      cout << cycle[i];
    }
    cout << endl;
  }
  else
  {
    cout << "IMPOSSIBLE" << endl;
  }
}