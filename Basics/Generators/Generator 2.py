# interable vs generator

# def makeList(n):
#     result = []
#     for i in range(n):
#         result.append(i)
#     return result


# res = makeList(100)
# print(res)


def generatorFunc(n):
    for i in range(n):
        yield i


for item in generatorFunc(10000):
    print(item)
