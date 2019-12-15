def allCircular(l):
    
    def circular(m):
        for i in range(len(m) - 1):
            m[i], m[i+1] = m[i+1], m[i]

        return m

    permute = []
    permute.append(l)
    p = circular(l[:])
    while True:
        if p in permute:
            break
        permute.append(p)
        p = circular(p[:])
        
    return permute
    
print(allCircular( [1, 2, 3, 4, 5] ) )