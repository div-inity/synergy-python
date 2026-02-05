n = list(map(int, input().split()))
for i in n :
    if n.count(i) > 1 : print(f'{i}: YES\n')
    else : print(f'{i}: NO\n')