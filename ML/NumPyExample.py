str = 'Snow White and the Seven Dwarfs'
arr = ['Snow', ' White', 'and', 'the', 'Seven', 'Dwarfs']

# print(str.__contains__("and"))
# print(arr.__contains__("and"))


for i in range(len(str)):
    df = str.split(" ")

print(df)

test = 'and'

var = input()

# Assuming df is your DataFrame
found = False
for i in range(len(df)):
    if df.loc[i, 'Tags'] == var:
        found = True
        break

if found:
    print("YES")
