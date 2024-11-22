s = 'The dinner is not that bad!'

string = s.split()

for i in range(len(string)-1):
    if 'not' == string[i]:
        string[i] = 'good'
        string = string[0:i+1]
        break

print(string)
