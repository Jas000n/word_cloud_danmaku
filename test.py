import re
data = ""
with open('穷叉叉.xml') as f:
    while(f.readline()):
        data += f.readline()

# a = "">出不去了是怎么回事哈哈哈</d><d p=""
# b = "asdf[abc123]我们"
# g = re.search("\[.*\]", a)
result = re.findall("\">.*?</d><d p=\"",data)
print(data)
new_data = ""
for i in result:
    i = i[2:-10]
    new_data += i
print(new_data)