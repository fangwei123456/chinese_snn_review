results = []
T = 8
for t in range(1, T + 1):
    for tau in range(t + 1, T + 1):
        results.append(f'{t}-{tau}')

results.sort()
print(results)
results.clear()
for tau in range(2, T + 1):
    for t in range(1, tau):
        results.append(f'{t}-{tau}')
results.sort()
print(results)