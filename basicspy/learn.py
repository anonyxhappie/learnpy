# Everything in python is object
# Variables, Functions, even Code
def main():
    x = 42
    print(x, "id(x):{},".format(id(x)), "type(x):{},".format(type(x)), "id(42):{},".format(id(42)), "type(42):{}".format(type(42)))
    x = 43
    print(x, "id(x):{},".format(id(x)), "type(x):{},".format(type(x)), "id(43):{},".format(id(43)), "type(43):{}".format(type(43)))
    x = 42
    print(x, "id(x):{},".format(id(x)), "type(x):{},".format(type(x)), "id(42):{},".format(id(42)), "type(42):{}".format(type(42)))
    # here variable x, only change reference to the object 

    num = 42 // 9
    print(type(num), num)
    
    num = round(42 / 9, 2)
    print(type(num), num)
    
    num = 42.9
    print(type(num), num)

    s = r"This is %s.{} a\nstring!".format(x) % (x+1)
    print(s)

    s = '''\
    this is a string
    line after line
    of text and more
    text.
    '''
    print(s)
    
    x = [1, 2, 3]
    x.append(5)
    x.insert(2, 7)
    print(type(x), x)

    x = "string"
    print(type(x), x[2:4])
    
    for i in x:
        print(i)

    d = { 'one': 1, 'two': 2, 'three': 3, 'four': 4,  'five': 5}
    for k in d:
        print(k, d[k])

    for k in sorted(d):
        print(k, d[k])

    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
        )
    for k in sorted(d):
        print(k, d[k])



if __name__ == "__main__": main()