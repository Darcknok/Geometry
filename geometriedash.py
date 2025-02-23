import pyxel

# fenetre
pyxel.init(128, 128, title="geometrie dash")


#co du joueur

x_j=20
y_j=100

h_jump=3




def joueur_deplacement(x,y):

    if pyxel.btn(pyxel.KEY_D):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x = x - 1
    return x, y

def jump(x,y):
    global h_jump
    if (pyxel.btnr(pyxel.KEY_SPACE) and h_jump==3 ) or h_jump!=3 :
        y-=3
        h_jump-=1
        if h_jump<-3:
            h_jump=3
    return x,y












##############################################################################################################################################
#UPDATE
##############################################################################################################################################


def update():
    global x_j , y_j , h_jump


    x_j,y_j = joueur_deplacement(x_j,y_j)

    x_j,y_j = jump(x_j,y_j)

##############################################################################################################################################
#DRAW
##############################################################################################################################################


def draw():
    # vide la fenetre
    pyxel.cls(0)
    pyxel.rect(0,100,128,30,3)
    pyxel.rect(x_j,y_j,8,8,1)




pyxel.run(update, draw)