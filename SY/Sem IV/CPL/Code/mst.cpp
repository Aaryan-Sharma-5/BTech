#include <bits/stdc++.h>
using namespace std;

struct Edge
{
  int u, v, w, idx;
  bool operator<(const Edge &other) const
  {
    return w < other.w;
  }
};

struct DSU
{
  vector<int> parent, rank;

  DSU(int size)
  {
    parent.resize(size + 1);
    rank.resize(size + 1, 1);
    for (int i = 0; i <= size; ++i)
      parent[i] = i;
  }

  int find(int x)
  {
    if (parent[x] != x)
      parent[x] = find(parent[x]);
    return parent[x];
  }

  bool unite(int x, int y)
  {
    x = find(x);
    y = find(y);
    if (x == y)
      return false;

    if (rank[x] < rank[y])
    {
      parent[x] = y;
    }
    else
    {
      parent[y] = x;
      if (rank[x] == rank[y])
        ++rank[x];
    }
    return true;
  }
};

int main()
{
  int n, m;
  scanf("%d %d", &n, &m);

  vector<Edge> edges(m);
  for (int i = 0; i < m; ++i)
  {
    scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w);
    edges[i].idx = i;
  }

  // Kruskal's algorithm to find MST
  vector<Edge> sorted_edges = edges;
  sort(sorted_edges.begin(), sorted_edges.end());

  DSU dsu(n);
  vector<bool> in_mst(m, false);
  long long mst_sum = 0;
  vector<vector<pair<int, int>>> adj(n + 1);

  for (const Edge &e : sorted_edges)
  {
    if (dsu.unite(e.u, e.v))
    {
      in_mst[e.idx] = true;
      mst_sum += e.w;
      adj[e.u].emplace_back(e.v, e.w);
      adj[e.v].emplace_back(e.u, e.w);
    }
  }

  // BFS to set up parent and depth for LCA
  vector<int> parent(n + 1, 0);
  vector<int> edge_weight(n + 1, 0);
  vector<int> depth(n + 1, 0);
  queue<int> q;

  q.push(1);
  parent[1] = 0;
  depth[1] = 0;

  while (!q.empty())
  {
    int u = q.front();
    q.pop();

    for (auto &p : adj[u])
    {
      int v = p.first;
      int w = p.second;
      if (parent[v] == 0 && v != 1)
      {
        parent[v] = u;
        edge_weight[v] = w;
        depth[v] = depth[u] + 1;
        q.push(v);
      }
    }
  }

  // Binary Lifting preprocessing
  const int LOG = 20;
  vector<vector<int>> up_ancestor(LOG, vector<int>(n + 1));
  vector<vector<int>> up_max_edge(LOG, vector<int>(n + 1));

  for (int v = 1; v <= n; ++v)
  {
    up_ancestor[0][v] = parent[v];
    up_max_edge[0][v] = edge_weight[v];
  }

  for (int j = 1; j < LOG; ++j)
  {
    for (int v = 1; v <= n; ++v)
    {
      up_ancestor[j][v] = up_ancestor[j - 1][up_ancestor[j - 1][v]];
      up_max_edge[j][v] = max(up_max_edge[j - 1][v], up_max_edge[j - 1][up_ancestor[j - 1][v]]);
    }
  }

  // Function to get maximum edge on path between u and v
  auto get_max_edge = [&](int u, int v) -> int
  {
    if (u == v)
      return 0;
    int max_e = 0;

    if (depth[u] < depth[v])
      swap(u, v);

    // Bring u up to depth of v
    for (int j = LOG - 1; j >= 0; --j)
    {
      if (depth[u] - (1 << j) >= depth[v])
      {
        max_e = max(max_e, up_max_edge[j][u]);
        u = up_ancestor[j][u];
      }
    }

    if (u == v)
      return max_e;

    // Now bring both up together
    for (int j = LOG - 1; j >= 0; --j)
    {
      if (up_ancestor[j][u] != up_ancestor[j][v])
      {
        max_e = max({max_e, up_max_edge[j][u], up_max_edge[j][v]});
        u = up_ancestor[j][u];
        v = up_ancestor[j][v];
      }
    }

    max_e = max({max_e, up_max_edge[0][u], up_max_edge[0][v]});
    return max_e;
  };

  // Process queries in original edge order
  for (int i = 0; i < m; ++i)
  {
    Edge &e = edges[i];
    if (in_mst[e.idx])
    {
      printf("%lld\n", mst_sum);
    }
    else
    {
      int max_e = get_max_edge(e.u, e.v);
      long long ans = mst_sum + e.w - max_e;
      printf("%lld\n", ans);
    }
  }

  return 0;
}