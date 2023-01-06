def solution(cacheSize, cities):
    answer = 0
    usecache = 0
    cache = ["" for i in range(cacheSize)]
    if cacheSize == 0:
        answer = (len(cities))*5
    else:
        for city in cities:
            for temp in cache:
                if city.lower() == temp.lower():
                    usecache = usecache + 1
                    cache.remove(temp)
                    cache.append(city)
                    break
                    
            if not city.lower() == cache[-1].lower():
                del cache[0]
                answer = answer + 5
                cache.append(city)
        answer = answer + usecache
    
    return answer