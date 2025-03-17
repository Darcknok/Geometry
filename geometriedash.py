import pyxel

class jeu():
    def __init__(self):
        # fenetre
        pyxel.init(128, 128, title="geometrie dash")

        self.x_cam=0
        self.y_cam=0

        #Init Joueur

        self.x_j=20
        self.y_j=104
        self.h_jump=8
        self.bloc_bas=False
        self.vie=True
        self.scor=0
        pyxel.camera(self.x_j - 8,0)
        #init sprite
        pyxel.load("sprite\\res.pyxres")

        #init block
        self.block_list = [[150,104],[166,104],[166,96],[204,104],[204,40]]


        pyxel.run(self.update, self.draw)

    #création map
    def creation_sol(self):
        x=0
        for i in range(100):
            pyxel.blt(x, 112, 0, 16, 0, 16, 16)
            x+=16




    #action du joueur
    def joueur_deplacement(self):
        if self.vie:
            self.x_j =self.x_j + 1.5
            pyxel.camera(self.x_j - 8,0)


    def jump(self):
        if self.vie:
            if (pyxel.btn(pyxel.KEY_SPACE) and self.h_jump==8 and(self.y_j==104 or self.bloc_bas) ) or self.h_jump!=8 :
                self.y_j-=self.h_jump
                self.h_jump-=(8/6)
                if self.h_jump<-8:
                    self.h_jump=8

    def score(self):
        if self.vie:
            self.scor=int((self.x_j-20)/1.5)

    def score_draw(self):
        if self.vie:
            pyxel.text(self.x_j - 4,0, "SCORE :", 5)
            pyxel.text(self.x_j,10, str(self.scor), 5)








    #propiété block

    def colission_block(self):
        if self.vie:
            self.bloc_bas=False
            for block in self.block_list:
                if block[0] <= self.x_j+8 and block[1] == self.y_j+8 and block[0]+8 >= self.x_j: #colision cote haut
                    self.h_jump=8
                    self.y_j=block[1]-8
                    self.bloc_bas=True
                elif self.x_j+8>block[0] and self.x_j<block[0] and self.y_j+8>block[1] and self.y_j<block[1]+8:
                    self.vie=False
            if self.bloc_bas==False and self.y_j<104 and self.h_jump==8: #tombe si pas de block
                self.y_j+=4
            if self.y_j>104:
                self.y_j=104










    #parametre jeu
    def gameover(self):
        pyxel.cls(0)
        pyxel.text(45,50, "GAME OVER", 7)
        pyxel.text(30,60, "PRESS R TO RESTART", 7)
        pyxel.text(52,70, "SCORE :", 5)
        pyxel.text(59,80, str(self.scor), 5)
        pyxel.camera(0,0)
    def Restart(self):

        if self.vie==False and pyxel.btn(pyxel.KEY_R):
            self.vie = True
            self.x_j=20
            self.y_j=104
            self.h_jump=8
            pyxel.cls(0)

    def debug(self):
        if pyxel.btnp(pyxel.KEY_K):
            self.vie=False

##############################################################################################################################################
#UPDATE
##############################################################################################################################################


    def update(self):



        self.joueur_deplacement()

        self.jump()

        self.colission_block()

        self.Restart()

        self.debug()

        self.score()


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
                self.score_draw()

jeu()
