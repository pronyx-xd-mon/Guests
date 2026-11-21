def geo_series(N):
    terms=[]
    for n in range (0, N+1):
        a=(3+2*n)/2**n
        terms.append(a)

    return terms

print(geo_series(5))


def sum_of_series(N):
    return sum(geo_series(N))

print(sum_of_series(5))

