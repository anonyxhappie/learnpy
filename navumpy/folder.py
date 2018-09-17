# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    s_photoArray = S
    s_photoArray = s_photoArray.split('\n')
    photoArray = S.split('\n')
    photoArray.sort(key=lambda x: x.split(', ')[-1])
   # print('PHOTOARRAY ASORT:::', photoArray)
    newSet = set()
    for photo in photoArray:
        pArray = photo.split(', ')
        newSet.add(pArray[1])
        # print(pArray)
    # print(photoArray)
    updatedPhotoArray = []
    for city in newSet:
        counter = 0
        c_len = sum(city in s for s in photoArray)
        c_len = len(str(c_len))
        # print(city, sum(city in s for s in photoArray), c_len)

        for x in (y for y in photoArray if y.split(', ')[1] == city):
            counter = counter + 1
            s_counter = str(counter).zfill(c_len)
            updatedPhotoArray.append(city + s_counter + '.' + x.split('.')[1])
    # print(updatedPhotoArray)
    output = [j.split(',')[0] for i in s_photoArray for j in updatedPhotoArray if i.split(',')[
        2] in j.split(',')[2]]
    # print()
    # print(output)
    output = "\n".join(str(x) for x in output)
    return output
S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\n\
john.png, London, 2015-06-20 15:13:22\n\
myFriends.png, Warsaw, 2013-09-05 14:07:13\n\
Eiffel.jpg, Paris, 2015-07-23 08:03:02\n\
pisatower.jpg, Paris, 2015-07-22 23:59:59\n\
BOB.jpg, London, 2015-08-05 00:02:03\n\
notredame.png, Paris, 2015-09-01 12:00:00\n\
me.jpg, Warsaw, 2013-09-06 15:40:22\n\
a.png, Warsaw, 2016-02-13 13:33:50\n\
b.jpg, Warsaw, 2016-01-02 15:12:22\n\
c.jpg, Warsaw, 2016-01-02 14:34:30\n\
d.jpg, Warsaw, 2016-01-02 15:15:01\n\
e.png, Warsaw, 2016-01-02 09:49:09\n\
f.png, Warsaw, 2016-01-02 10:55:32\n\
g.jpg, Warsaw, 2016-02-29 22:13:11'
print(solution(S))
