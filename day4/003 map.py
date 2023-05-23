row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position =input("Where do you want to put the treasure? ")

Hor=int(position[0])-1
Ver=int(position[1])-1

select_row=map[Ver]
select_row[Hor] = "X"

print(f"{row1}\n{row2}\n{row3}")
