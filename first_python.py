scores = [446,1684,1665164,164,6,46,46,464651,86,46,68481]

friends = ["列表","的用","表的用法","列表介紹","列表的用法"]

var1 = 20
var2 = 30
scores.append(var1)
print(scores)
scores.append(var2)
print(scores)

scores.insert(2,30)
print(scores)

print(scores.index(var2))

scores.remove(var1)
print(scores)
scores.remove(var2)

print(scores)

print(scores.index(var2))

scores.remove(var2)
print(scores)

scores.extend(friends)
print(scores)


