# interable
# iterable
# generator

def makeList(n):
    return list(range(n))


res = makeList(100)
print(res)

# Every  generator is a interable, but every iterable is not a generator.
# Range is generator and iterable roo, wheras list is interable but not generator
