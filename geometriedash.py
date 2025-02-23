import pyxel

# fenetre
pyxel.init(128, 128, title="geometrie dash")


#co du joueur

x_j=20
y_j=100

h_jump=7

#init sprite
pyxel.load("./sprite/res.pyxres")


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
    if (pyxel.btnr(pyxel.KEY_SPACE) and h_jump==7 ) or h_jump!=7 :
        y-=h_jump
        h_jump-=1
        if h_jump<-7:
            h_jump=7
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
    pyxel.blt(x_j, y_j, 0, 0, 0, 8, 8)
    pyxel.blt(0, 112, 0, 16, 0, 16, 16)
    pyxel.blt(16, 112, 0, 16, 0, 16, 16)



pyxel.run(update, draw)
