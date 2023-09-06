# interable
# iterable
# generator

def makeList(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


res = makeList(100)
print(res)

# Every  generator is a interable, but every iterable is not a generator.
# Range is generator and iterable roo, wheras list is interable but not generator
