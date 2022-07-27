
def test(str):
    counter = {}

    for word in str:
        counter[word] = counter.get(word, 0) + 1

    # for x, y in counter.items():
    #     print( x,y)
    return counter
print(test(['a','b','c','a']))


