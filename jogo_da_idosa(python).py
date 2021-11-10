jogadorL = 0
jogadorC = 0
resp = 'S'


A = ['_','_','_']
B = ['_','_','_']
C = ['_','_','_']

esqueleto = [A,B,C]



print()
print('',A[0],"|",A[1],"|",A[2])
print("---|---|---")

print('',B[0],"|",B[1],"|",B[2])
print("---|---|---")
print('',C[0],"|",C[1],"|",C[2])
print()



    
def entrada():
     
    jogadas = 0
    while True:
            jogadas = jogadas + 1
            print("Jogador 1")
            jogador1L = int(input("digite uma linha [1][2][3]: "))
            jogador1C = int(input("digite uma coluna [1][2][3]: "))

            if(jogador1L == 1 and jogador1C == 1) and A[0] !="X" and A[0] !="O":
                A[0] = "X"
                ganhou()
                    
     
            if(jogador1L == 1 and jogador1C == 2) and A[1] !="X" and A[1] !="0":
                A[1] = "X"
                ganhou()
                

            if(jogador1L == 1 and jogador1C == 3) and A[2] !="X" and A[2] !="0":
                A[2] = "X"
                ganhou()
    #--------------
                    
            if(jogador1L == 2 and jogador1C == 1) and B[0] !="X" and B[0] !="O":
                B[0] = "X"
                ganhou()
                    

            if(jogador1L == 2 and jogador1C == 2) and B[1] !="X" and B[1] !="O":
                B[1] = "X"
                ganhou()
                     
            if(jogador1L == 2 and jogador1C == 3) and B[2] !="X" and B[2] !="O":
                B[2] = "X"
                ganhou()
     #--------------
                    
            if(jogador1L == 3 and jogador1C == 1) and C[0] !="x" and C[0] !="O":
                C[0] = "X"
                ganhou()
                     
            if(jogador1L == 3 and jogador1C == 2) and C[1] !="X" and C[1] !="O":
                C[1] = "X"
                ganhou()
                    
            if(jogador1L == 3 and jogador1C == 3) and C[2] !="X" and C[2] !="O":
                C[2] = "X"
                ganhou()


                    
            print()
            print('',A[0],"|",A[1],"|",A[2])
            print("---|---|---")
            print('',B[0],"|",B[1],"|",B[2])
            print("---|---|---")
            print('',C[0],"|",C[1],"|",C[2])
            print()

        
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
            jogadas = jogadas + 1
            print("jogador 2")
            jogador2L = int(input("digite uma linha [1][2][3]: "))
            jogador2C = int(input("digite uma coluna [1][2][3]: "))

            if(jogador2L == 1 and jogador2C == 1) and A[0] !="X" and A[0] !="O":
                A[0] = "O"
                ganhou1()

            if(jogador2L == 1 and jogador2C == 2) and A[1] !="X" and A[1] !="0":
                A[1] = "O"
                ganhou1()
                    
            if(jogador2L == 1 and jogador2C == 3) and A[2] !="X" and A[2] !="0":
                A[2] = "O"
                ganhou1()
    #--------------

            if(jogador2L == 2 and jogador2C == 1) and B[0] !="X" and B[0] !="O":
                B[0] = "O"
                ganhou1()

            if(jogador2L == 2 and jogador2C == 2) and B[1] !="X" and B[1] !="O":
                B[1] = "O"
                ganhou1()
                    
            if(jogador2L == 2 and jogador2C == 3) and B[2] !="X" and B[2] !="O":
                B[2] = "O"
                ganhou1()
    #--------------

            if(jogador2L == 3 and jogador2C == 1) and C[0] !="x" and C[0] !="O":
                C[0] = "O"
                ganhou1()
                

            if(jogador2L == 3 and jogador2C == 2) and C[1] !="X" and C[1] !="O":
                C[1] = "O"
                ganhou1()
                    
            if(jogador2L == 3 and jogador2C == 3) and C[2] !="X" and C[2] !="O":
                C[2] = "O"
                ganhou1()
        
            print()
            print('',A[0],"|",A[1],"|",A[2])
            print("---|---|---")
            print('',B[0],"|",B[1],"|",B[2])
            print("---|---|---")
            print('',C[0],"|",C[1],"|",C[2])
            print()

            if(jogadas > 9) or (ganhou1() != ''): 
                break
            
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def ganhou():
    vencedor = ''
    if(A[0] == 'X') and (A[1] == 'X') and (A[2] == 'X'):
        print(" O jogador 1 completou a primeira linha!")
        vencedor = 'X'
        
    if(B[0] == 'X') and (B[1] == 'X') and (B[2] == 'X'):
        print(" O jogador 1 completou a segunda linha!")
        vencedor = 'X'
            
    if(C[0] == 'X') and (C[1] == 'X') and (C[2] == 'X'):
        print(" O jogador 1 completou a terceira linha")
        vencedor = 'X'

    if(A[0] == 'X') and (B[0] == 'X') and (C[0] == 'X'):
        print("O jogador 1 completou a peimeira coluna!")
        vencedor = 'X'
        
    if(A[1] == 'X') and (B[1] == 'X') and (C[1] == 'X'):
        print(" O jogador 1 completou a peimeira coluna!")
        vencedor = 'X'
        
    if(A[2] == 'X') and (B[2] == 'X') and (C[2] == 'X'):
        print(" O jogador 1 completou a peimeira coluna!")
        vencedor = 'X'           

    if(A[0] == 'X') and (B[1] == 'X') and (C[2] == 'X'):
        print(" O jogador 1 completou a vertical direita")
        vencedor = 'X'
         
    if(A[2] == 'X') and (B[1] == 'X') and (C[0] == 'X'):
        print(" O jogador 1 completou a vertical direita")
        vencedor = 'X'

    return vencedor


            #-----------------------------------------------------#

def ganhou1():
    vencedor = ''
      
    if(A[0] == 'O') and (A[1] == 'O') and (A[2] == 'O'):
        print(" O jogador 2 completou a primeira linha!")
        vencedor = 'O'        
    if(B[0] == 'O') and (B[1] == 'O') and (B[2] == 'O'):
        print(" O jogador 2 completou a segunda linha!")
        vencedor = 'O'            
    if(C[0] == 'O') and (C[1] == 'O') and (C[2] == 'O'):
        print(" O jogador 2 completou a terceira linha")
        vencedor = 'O'

    if(A[0] == 'O') and (B[0] == 'O') and (C[0] == 'O'):
        print(" O jogador 2 completou a peimeira coluna!")
        vencedor = 'O'            
    if(A[1] == 'O') and (B[1] == 'O') and (C[1] == 'O'):
        print(" O jogador 2 completou a peimeira coluna!")
        vencedor = 'O'           
    if(A[2] == 'O') and (B[2] == 'O') and (C[2] == 'O'):
        print(" O jogador 2 completou a peimeira coluna!")
        vencedor = 'O'           

    if(A[0] == 'O') and (B[1] == 'O') and (C[2] == 'O'):
        print(" O jogador 2 completou a vertical direita")
        vencedor = 'O'            
    if(A[2] == 'O') and (B[1] == 'O') and (C[0] == 'O'):
        print(" O jogador 2 completou a vertical direita")
        vencedor = 'O'

    return vencedor
 
while True:
    jogadas = 0
    vencedor_check = ''
  
    vencedor_check = entrada()

        
    if(vencedor_check == ''):
        print("Velha")
    elif(vencedor_check == 'X') or (vencedor_check == 'O'):
        print("Jogador ", vencedor_check,"ganhou!!!")
             

    continuar = input('Deseja continuar o jogo [s] [n]?:')
    if(continuar == 's'):
        A = ['_','_','_']
        B = ['_','_','_']
        C = ['_','_','_']
        esqueleto = [A,B,C]
        
    elif(continuar == 'n'):
            break

         
