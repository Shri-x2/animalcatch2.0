import pgzrun, time, random

WIDTH, HEIGHT = 1000, 800
TITLE = "Animal Connection 2.0"
# acti = Actor("giraffe", size=15)
# actii = Actor("kangaroo", size=15)
# actiii = Actor("koala", size=15)
# activ = Actor("lion", size=15)
# actv = Actor("panda", size=15)
actors = []
animals = ["giraffe", "kangaroo", "koala", "lion", "panda"]
lines = []
for i in animals:
    actors.append(Actor(i, size=15,pos=(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30))))
    
    

gamestage = "start"


timestart = time.time()
print(timestart)
nextanimal = 0

def draw():
    if gamestage == "start":
        screen.draw.text("Click on the animals in order to connect them!", (WIDTH//2, HEIGHT//2), color="white", fontsize=30, owidth=1, ocolor="black")
    elif gamestage == "playing":
        screen.blit("zoo2", (0, 0))
        for i,a in  enumerate(actors):
            a.draw()
            screen.draw.text(str(i+1), (a.x, a.y+40), color="blue", fontsize=30)
    
        for l in lines:
            print(l)
            screen.draw.line(l[0], l[1], color="red")
        
        if nextanimal < len(actors):
            screen.draw.text(f"Connect animal {nextanimal + 1}", (WIDTH//2, HEIGHT - 50), color="yellow", fontsize=24, owidth=1, ocolor="black")
            timetotal = time.time() - timestart
            screen.draw.text(f"Time: {timetotal:.2f} seconds", (10,40), fontsize=24, color="black")
        else:
            screen.draw.text("All animals connected!", (WIDTH//2, HEIGHT - 50), color="green", fontsize=30, owidth=1, ocolor="black")
            timetotal = time.time() - timestart
            screen.draw.text(f"Total time: {timetotal:.2f} seconds", (10,40), fontsize=67, color="black")

def on_mouse_down(pos):
    global gamestage, nextanimal, lines, timestart
    print(len(lines))
    if gamestage == "start":
        gamestage = "playing"
        timestart = time.time()
        print("Game started!")
        
    
        
    if nextanimal < len(actors):
        if actors[nextanimal].collidepoint(pos):
            if nextanimal:
                lines.append((actors[nextanimal-1].pos, actors[nextanimal].pos))
            nextanimal += 1
    else:
        print("Missed animal")
        lines = []
        nextanimal = 0


pgzrun.go()


