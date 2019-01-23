G = {}
G['a'] = ['b', 'c', 'd']
G['b'] = ['a', 'e', 'd']
G['c'] = ['f', 'h', 'a']
G['d'] = ['a', 'b']
G['e'] = ['b']
G['f'] = ['c', 'g']
G['g'] = ['f']
G['h'] = ['c']

for key, value in G.items():
    G[key] = set(value)

def bfs(G, start='a'):
    visited = set()
    q = [start]
    while len(q) > 0:
        curr = q.pop(0)
        if curr not in visited:
            print(curr)
            visited.add(curr)
            q.extend(G[curr] - visited)

# bfs(G)

def dfs(G, start = 'a'):
    visited = set()
    s = [start]
    while len(s) > 0:
        curr = s.pop()
        if curr not in visited:
            print(curr)
            visited.add(curr)
            s.extend(G[curr] - visited)
# dfs(G)
