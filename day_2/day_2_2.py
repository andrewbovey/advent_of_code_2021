moves = [line.split() for line in open("2_input.txt", "r")]

x=0
y=0
aim=0 
for move in moves:
    match move[0]:
        case 'forward':
            x+=int(move[1])
            y+=aim*int(move[1])
        case 'up':
            aim-=int(move[1])
        case 'down':
            aim+=int(move[1])
            
print(x)
print(y)
print(x*y)