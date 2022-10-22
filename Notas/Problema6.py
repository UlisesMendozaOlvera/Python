def repetido(lista1,lista2):
       
       
        
        lista3 = []
        lista4 = []
        
        for l1 in lista1:
            
            if l1 in lista2:
                lista3.append(l1)
            else:
                lista4.append(l1)
                
        for l2 in lista2:

            if l2 not in lista1:
                lista4.append(l2)
              
        print(lista3)
        print(lista4)      
listax = ['a','b',2,3]
listay = ['c','d',3,4]                 
repetido(listax,listay)