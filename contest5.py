def count_states_cities(n, roads):
    cities_graph = [set() for _ in range(n + 1)]
    cities = set()
    m = len(roads)
    for i in range(m):
        v, u, _ = roads[i]
        cities.update({v, u})

        cities_graph[v].add(u)
        cities_graph[u].add(v)
       
    for i in range(n + 1):
        for j in range(1, n+1):
            if i == 0 or i == j:
                continue
            elif j in cities_graph[i]:
                cities_graph[i].update(cities_graph[j])
                cities_graph[j] = []
            elif len(cities_graph[j]) > 0:
                for city in cities_graph[j]:
                    if city in cities_graph[i]:
                        cities_graph[i].update(cities_graph[j])
                        cities_graph[j] = []
                        break

    cities_graph[0] = []
    states_count = 0

    for city in cities_graph:
        if len(city) != 0:
            states_count += 1
    return states_count, len(cities)


n, m = map(int, input().split())
roads = []
for _ in range(m):
    v, u, w = map(int, input().split())
    roads.append((v, u, w))

roads.sort(key=lambda x: x[2])
states_count, cities_count = count_states_cities(n, roads)

res = 0
temp_res = 0
while roads:
    _, _, res = roads.pop(0)
    temp_states_count, temp_cities_count = count_states_cities(n, roads)
    if states_count != temp_states_count or cities_count != temp_cities_count:
        break
print(res - 1)