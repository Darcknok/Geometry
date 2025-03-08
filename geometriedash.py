import pyxel

class jeu():
    def __init__(self):
        # fenetre
        pyxel.init(128, 128, title="geometrie dash")

        #Init Joueur

        self.x_j=20
        self.y_j=104
        self.h_jump=8
        self.vie=True

        #init sprite
        pyxel.load("sprite/res.pyxres")

        #init block
        self.block_list = [[30,104],[40,104],[40,96]]


        pyxel.run(self.update, self.draw)

    #création map
    def creation_sol(self):
        x=0
        for i in range(16):
            pyxel.blt(x, 112, 0, 16, 0, 16, 16)
            x+=16




    #action du joueur
    def joueur_deplacement(self):

        if pyxel.btn(pyxel.KEY_D):
            if (self.x_j < 120) :
                self.x_j =self.x_j + 1
        if pyxel.btn(pyxel.KEY_Q):
            if (self.x_j > 0) :
                self.x_j = self.x_j - 1


    def jump(self):
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.h_jump==8 ) or self.h_jump!=8 :
            self.y_j-=self.h_jump
            self.h_jump-=1
            if self.h_jump<-8:
                self.h_jump=8





    #propiété block

    def colission_block(self):
        bloc_bas=False
        for block in self.block_list:
            if block[0] <= self.x_j+8 and block[1] == self.y_j+8 and block[0]+8 >= self.x_j: #colision cote haut
                self.h_jump=8
                self.y_j=block[1]-8
                bloc_bas=True
            elif self.x_j+8>block[0] and self.x_j<block[0] and self.y_j+8>block[1]:
                self.vie=False
        if bloc_bas==False and self.y_j<104 and self.h_jump==8: #tombe si pas de block
            self.y_j+=4









    #parametre jeu
    def gameover(self):
        pyxel.cls(0)
        pyxel.text(45,50, "GAME OVER", 7)
        pyxel.text(30,60, "PRESS R TO RESTART", 7)
    def Restart(self):

        if self.vie==False and pyxel.btn(pyxel.KEY_R):
            self.vie = True
            self.x_j=20
            self.y_j=104
            pyxel.cls(0)


##############################################################################################################################################
#UPDATE
##############################################################################################################################################


    def update(self):



        self.joueur_deplacement()

        self.jump()

        self.colission_block()

        self.Restart()

    ##############################################################################################################################################
    #DRAW
    ##############################################################################################################################################


    def draw(self):
        if self.vie==False:
            self.gameover()
        else:
            # vide la fenetre
            pyxel.cls(0)
            pyxel.blt(self.x_j, self.y_j, 0, 0, 0, 8, 8)
            self.creation_sol()

            #affichage block
            for block in self.block_list:
                pyxel.blt(block[0], block[1], 0, 32, 0, 8, 8)

jeu()
