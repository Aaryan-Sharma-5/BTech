#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int minDistance(vector<int> &dist, vector<bool> &S, int n)
{
  int min = INT_MAX, minIndex = -1;
  for (int i = 0; i < n; i++)
  {
    if (!S[i] && dist[i] < min)
    {
      min = dist[i];
      minIndex = i;
    }
  }
  return minIndex;
}

void dijkstra(vector<vector<int>> &W, int source, int n, vector<int> &dist)
{
  vector<bool> S(n, false);
  dist[source] = 0;

  for (int i = 0; i < n - 1; i++)
  {
    int u = minDistance(dist, S, n);
    if (u == -1)
    {
      break;
    }

    S[u] = true;
    for (int v = 0; v < n; v++)
    {
      if (!S[v] && W[u][v] != INT_MAX && dist[u] != INT_MAX &&
          dist[u] + W[u][v] < dist[v])
      {
        dist[v] = dist[u] + W[u][v];
      }
    }
  }
}

int main()
{
  int n;
  cout << "Enter the number of vertices: ";
  cin >> n;

  vector<vector<int>> W(n, vector<int>(n));
  cout << "Enter the adjacency matrix: " << endl;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cin >> W[i][j];
      if (i != j && W[i][j] == 0)
        W[i][j] = INT_MAX;
    }
  }

  int source;
  cout << "Enter the source vertex: ";
  cin >> source;
  if (source < 0 || source >= n)
  {
    cout << "Invalid source vertex. Exiting...\n";
    return 1;
  }

  vector<int> dist(n, INT_MAX);
  dijkstra(W, source, n, dist);

  cout << "\nVertex\tDistance from Source" << endl;
  for (int i = 0; i < n; i++)
  {
    if (dist[i] == INT_MAX)
      cout << i << "\tNo Path" << endl;
    else
      cout << i << "\t" << dist[i] << endl;
  }
}
