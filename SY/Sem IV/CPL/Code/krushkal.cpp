#include <bits/stdc++.h>
using namespace std;

vector<int> parent, dsuRank;
int find(int x)
{
  if (parent[x] != x)
  {
    parent[x] = find(parent[x]);
  }
  return parent[x];
}

// Union by rank
void unite(int x, int y)
{
  int rootX = find(x);
  int rootY = find(y);
  if (rootX != rootY)
  {
    if (dsuRank[rootX] > dsuRank[rootY])
    {
      parent[rootY] = rootX;
    }
    else if (dsuRank[rootX] < dsuRank[rootY])
    {
      parent[rootX] = rootY;
    }
    else
    {
      parent[rootY] = rootX;
      dsuRank[rootX]++;
    }
  }
}

typedef tuple<int, int, int> Edge;
vector<Edge> kruskalMST(int n, vector<Edge> &edges)
{
  sort(edges.begin(), edges.end());
  parent.resize(n + 1);
  dsuRank.resize(n + 1, 0);

  for (int i = 0; i <= n; i++)
  {
    parent[i] = i;
  }

  vector<Edge> mst;
  for (const Edge &edge : edges)
  {
    int weight, u, v;
    tie(weight, u, v) = edge;
    if (find(u) != find(v))
    {
      mst.push_back(edge);
      unite(u, v);
    }
  }

  if (mst.size() != n - 1)
  {
    cout << "Graph is disconnected, MST is incomplete!" << endl;
  }

  return mst;
}

int main()
{
  int n, m;
  cin >> n >> m;

  vector<Edge> edges;
  for (int i = 0; i < m; i++)
  {
    int u, v, weight;
    cin >> u >> v >> weight;
    edges.push_back({weight, u, v});
  }

  vector<Edge> mst = kruskalMST(n, edges);

  for (const Edge &edge : mst)
  {
    int weight, u, v;
    tie(weight, u, v) = edge;
    cout << u << " - " << v << " : " << weight << endl;
  }

  cout << "No. of edges in MST: " << mst.size() << endl;
}
