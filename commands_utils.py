# def ninjarank(): #hace una función que de los beltpoints
#     info = open("stats.txt", "r")
#     playersdata = info.readlines() 
#     for beltdivision in playersdata:            
#         userdata = beltdivision.split(", ") #separa los datos
#         beltpoints = int(userdata[1]) #selecciona los datos y los vuelve un int
#         return(beltpoints) #regresa los beltpoints
#     close(stats.txt)

def current_ninjarank(ninjarank):
    if ninjarank < 25:           
        return None
    elif (ninjarank >= 25 and ninjarank <= 64):      
        return("White")         
    elif(ninjarank >= 65 and ninjarank <= 105):
        return("Yellow")
    elif(ninjarank >= 105 and ninjarank <= 149):
        return("Orange")
    elif (ninjarank >= 150 and ninjarank <= 199):
        return("Green")
    elif (ninjarank() >= 200 and ninjarank <= 259): 
        return("Blue")
    elif (ninjarank() >= 260 and ninjarank() <= 319):
        return("Red")
    elif (ninjarank() >= 320 and ninjarank() <= 379):
        return("Purple")
    elif (ninjarank() >= 380 and ninjarank() <= 439) :
        return("Brown")
    elif (ninjarank() >= 440): 
        return("Black")

# print(current_ninjarank())