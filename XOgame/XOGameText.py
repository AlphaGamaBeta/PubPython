Over = False
cl = [[" ", " ", " "], [" ", " ", ""], [" ", " ", " "]]
check = (
    (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (0, 0), (1, 1), (2, 2), (0, 2), (1, 1),
    (2, 0), (0, 0), (1, 0), (2, 0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2))
starter = f"""
   {cl[0][0]}  | {cl[0][1]} | {cl[0][2]}
-----------------
   {cl[1][0]}  | {cl[1][1]} | {cl[1][2]}
-----------------
   {cl[2][0]}  | {cl[2][1]} | {cl[2][2]}"""


def update():
    starter = f"""
       {cl[0][0]}  | {cl[0][1]} | {cl[0][2]}
    -----------------
       {cl[1][0]}  | {cl[1][1]} | {cl[1][2]}
    -----------------
       {cl[2][0]}  | {cl[2][1]} | {cl[2][2]}"""
    print(starter)
    print("\n")


print(starter)
print("\n")
while not Over:
    xloc = input("Location of choice for player X:row,column: ")
    xloc = xloc.split(',')
    cl[int(xloc[0])][int(xloc[1])] = "X"
    update()
    for n in range (0,21,3):
        if cl[check[n][0]][check[n][1]] == cl[check[n+1][0]][check[n+1][1]] == cl[check[n+2][0]][check[n+2][1]] and cl[check[n][0]][check[n][1]] != " ":
            if cl[check[n][0]][check[n][1]]=="X":
                print("\n\n\n\nPlayer X won Congrats\n\n\n\n")
                Over=True
                break
            else:
                print("\n\n\n\nPlayer O won Congrats\n\n\n\n")
                Over=True
                break
    if Over:
        break
    oloc = input("Location of choice for player O:row,column: ")
    oloc = oloc.split(',')
    cl[int(oloc[0])][int(oloc[1])] = "O"
    update()
    for n in range (0,21,3):
        if cl[check[n][0]][check[n][1]] == cl[check[n+1][0]][check[n+1][1]] == cl[check[n+2][0]][check[n+2][1]] and cl[check[n][0]][check[n][1]] != " ":
            if cl[check[n][0]][check[n][1]]=="X":
                print("\n\n\n\nPlayer X won Congrats\n\n\n\n")
                Over = True
                break
            else:
                print("\n\n\n\nPlayer O won Congrats\n\n\n\n")
                Over = True
                break
    if Over:
        break