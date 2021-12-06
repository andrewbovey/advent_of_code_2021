moves = [line.split() for line in open("2_input.txt", "r")]

x=0
y=0

for move in moves:
    match move[0]:
        case 'forward':
            x+= int(move[1])
        case 'up':
            y-= int(move[1])
        case 'down':
            y+= int(move[1])

        
print(x)
print(y)
print(x*y)