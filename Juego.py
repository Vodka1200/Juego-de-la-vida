'''
Reglas del juego de la vida

1. Si una célula que se encuentra viva tiene 0 o 1 vecino, muere por soledad para la siguiente generación. Donde los vecinos son las 8 células que lo rodean inmediatamente.
2. Una célula viva que tiene 2 o 3 vecinos sobrevive para la siguiente generación.
3. Una célula viva que tiene 4 o más vecinos muere por sobrepoblación para la siguiente generación.
4. Una célula muerta con exáctamente 3 vecinos vivos resulta en un nacimiento cuya vida empieza en la siguiente generación. Todas las demás células muertas permanecen muertas para la siguiente generación.

----------------------------------------------------------------
ADT Juego de la vida

JuegoDeLaVida(rows,cols,generaciones,poblacion_inicial)
get_num_rows()
get_num_cols()
configure_next_gen(nueva_poblacion)
set_cell_death(row,col)
set_cell_alive(row,col)
is_live_cell(row,col) => boolean
get_num_live_neighbors(row,col)
'''
from Array2D import Array2D

class JuegoDeLaVida:
    def _init_(self,rows,cols,generaciones,poblacion_inicial):
        self.__cuadro = Array2D(rows,cols)
        self.__filas = rows
        self.__columnas = cols
        self.__generaciones = generaciones
        #poblacion_inicial = [[1,3],[2,2],[2,3],[2,4]]
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def get_num_rows(self):
        return self.__filas

    def get_num_rows(self):
        return self.__columnas
        
    def to_string(self):
        self.__cuadro.to_string()

    def configure_next_generation(self,nueva_generacion): #nueva_generacion = [[1,3],[2,2],[2,3],[2,4]]
        self.__cuadro.clearing(0)
        for cell in nueva_generacion:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def set_cell_death(self,row,col):
        self.__cuadro.set_item(row,col,0)

    def set_cell_alive(self,row,col):
        self.__cuadro.set_item(row,col,1)

    def is_live_cell(self,row,col):
        return self.__cuadro.get_item(row,col)==1

    def get_num_live_neighbors(self,row,col):
        limites = self.calcula_vecinos(row,col)
        cont = 0
        for fila in range(limites[0],limites[2]+1):
            for cols in range(limites[1],limites[3]+1):
                if fila == row and cols == col:
                    pass
                else:
                    if self.is_live_cell(fila,cols):
                        cont = cont+1
        return cont

    def calcula_vecinos(self,y,x):
        #[y_ini, x_ini, y_fin, x_fin]
        vecinos=[y-1,x-1,y+1,x+1]
        if vecinos[0] == -1:
            vecinos[0] = 0
        if vecinos[1] == -1:
            vecinos[1] = 0
        if vecinos[2] == self.__filas:
            vecinos[2] == self.__filas - 1
        if vecinos[3] == self.__columnas:
            vecinos[3] == self.__columnas - 1
        return vecinos
    
def main():
    pass
    #inicial = [[1,3],[2,2],[2,3],[3,4]]
    #juego = JuegoDeLaVida(7,7,4,inicial)
    #juego.to_string()
    #vivos = juego.get_num_live_neighbors(2,3)
    #print(f"vivos = {vivos}")

main()
