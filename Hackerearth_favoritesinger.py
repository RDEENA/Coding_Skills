#HackerEarth Favorite singer problem
def favorite_singers(n, playlist):
    count = {}
    max_count = 0

    if not playlist:
        return 0

    for singer in playlist:
        count[singer] = count.get(singer, 0) + 1
        max_count = max(max_count, count[singer])

    favorite_singers_count = 0
    for i in count.values():
        if i==max_count:
            favorite_singers_count+=1
    return favorite_singers_count

n = int(input())
playlist = list(map(int, input().split()))
res = favorite_singers(n, playlist)
print(res)
