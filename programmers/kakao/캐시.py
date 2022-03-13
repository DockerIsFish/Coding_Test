def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = []
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city.lower())
            else:
                cache.pop(0)
                cache.append(city.lower())
    return answer
