import pyxel

# fenetre
pyxel.init(128, 128, title="geometrie dash")

#Init Joueur 

x_j=20
y_j=104
h_jump=8
vie=True

#init sprite
pyxel.load("sprite/res.pyxres")

#init block
block_list = [[30,104],[40,104],[40,96]]

def creation_sol():
    x=0
    for i in range(16):
        pyxel.blt(x, 112, 0, 16, 0, 16, 16)
        x+=16

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
    if (pyxel.btnp(pyxel.KEY_SPACE) and h_jump==8 ) or h_jump!=8 :
        y-=h_jump
        h_jump-=1
        if h_jump<-8:
            h_jump=8

    return x,y

def collision():
    global x_j,y_j
    for block in block_list:
        if block[0] <= x_j+8 and block[0]+8 >= x_j and block[1]+8 >= y_j:
            vie = False

def gameover():
    pyxel.cls(0)
    pyxel.text(50,50, "GAME OVER", 7)

def colision_haut_block(x,y):
    global h_jump
    bloc_bas=False
    for block in block_list:
        if block[0] <= x_j+8 and block[1] == y_j+8 and block[0]+8 >= x_j:
            h_jump=8
            y=block[1]-8
            bloc_bas=True
    if bloc_bas==False and y<104 and h_jump==8:
        y+=4
    return y



##############################################################################################################################################
#UPDATE
##############################################################################################################################################


def update():
    global x_j , y_j , h_jump,vie ,block_list


    x_j,y_j = joueur_deplacement(x_j,y_j)

    x_j,y_j = jump(x_j,y_j)

    y_j= colision_haut_block(x_j,y_j)

    collision()

##############################################################################################################################################
#DRAW
##############################################################################################################################################


def draw():
    if vie==False:
        gameover()
    else:
        # vide la fenetre
        pyxel.cls(0)
        pyxel.blt(x_j, y_j, 0, 0, 0, 8, 8)
        creation_sol()



        for block in block_list:
            pyxel.rect(block[0], block[1], 8, 8, 8)

pyxel.run(update, draw)
