import random
import os
from PIL import Image
from datetime import datetime
import qrandom
import time

def getBackground():
    ##chooses a random background
    backgroundPath = r"C:\Users\lolbo\Documents\GitHub\MoleMatchNFTProject"
    randomBackground = random.choice([
        x for x in os.listdir(backgroundPath)
        if os.path.isfile(os.path.join(backgroundPath, x))
    ])
    ##shows the background
    print(randomBackground)
    background = Image.open(randomBackground)
    #background.show()
    return background

def getFace():
    ##choose a random background
    facePath = r"C:\Users\lolbo\Documents\GitHub\Facial Expressions"
    randomFace = random.choice([
        y for y in os.listdir(facePath)
        if os.path.isfile(os.path.join(facePath, y))
    ])
    ##shows the face
    print(randomFace)
    Face = Image.open(randomFace)
    #Face.show()
    return Face

def getClothes():
    ##chooses a random clothing item
    clothesPath = r"C:\Users\lolbo\Documents\GitHub\Clothes"
    randomClothes = random.choice([
        z for z in os.listdir(clothesPath)
        if os.path.isfile(os.path.join(clothesPath, z))
    ])
    ##shows the clothes
    print(randomClothes)
    clothes = Image.open(randomClothes)
    #clothes.show()
    return clothes

def getHat():
    ##chooses a random hat
    hatPath = r"C:\Users\lolbo\Documents\GitHub\Hats"
    randomHat = random.choice([
        a for a in os.listdir(hatPath)
        if os.path.isfile(os.path.join(hatPath, a))
    ])
    ##shows the hat
    print(randomHat)
    hat = Image.open(randomHat)
    #hat.show()
    return hat

def rarity():
    rarityList = [1,1,1,1,1,2,2,2,2,3]
    rng = qrandom.randrange(9)
    print(rng)
    chosenRarity = rarityList[rng]
    if chosenRarity == 1:
        star = Image.open(r"C:\Users\lolbo\Documents\GitHub\OneStar.png")
        return star
    elif chosenRarity == 2:
        star = Image.open(r"C:\Users\lolbo\Documents\GitHub\TwoStar.png")
        return star
    elif chosenRarity == 3:
        star = Image.open(r"C:\Users\lolbo\Documents\GitHub\ThreeStar.png")
        return star
    

def seasonOfTheSplicer(generatedBackground, mole, generatedFace, generatedHat, rocks): ##generatedClothes, generatedHat, rocks, generatedStar):
    ##mole onto background
    generatedBackground.paste(mole,(0,0), mole)
    #generatedBackground.show()
    ##face onto mole
    generatedBackground.paste(generatedFace,(0,0), generatedFace)
    #generatedBackground.show()
    ##clothes onto mole
    ##generatedBackground.paste(generatedClothes,(0,0), generatedClothes)
    #generatedBackground.show()
    ##hat onto mole
    generatedBackground.paste(generatedHat,(0,0), generatedHat)
    #generatedBackground.show()
    ##rocks onto image
    generatedBackground.paste(rocks,(0,0), rocks)
    #generatedBackground.show()
    ##stars onto image
    ##generatedBackground.paste(generatedStar, (0,0), generatedStar)
    #generatedBackground.show()
    
    return generatedBackground

def saveTheImage(finalImage, savePath):
    ##gets the date and time for the filename
    currentDateTime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    splittedPath = os.path.splitext(savePath)
    modifiedPicturePath = splittedPath[0] + currentDateTime + splittedPath[1]

    finalImage.save(modifiedPicturePath + '.png')
    time.sleep(4)

    
##MAIN PROGRAM  
savePath = r"C:\Users\lolbo\Documents\GitHub\Output"
mole = Image.open(r"C:\Users\lolbo\Documents\GitHub\OriginalMole.png")
rocks = Image.open(r"C:\Users\lolbo\Documents\GitHub\Rocks.png")


for loop in range(100):  
    generatedBackground = getBackground()
    generatedFace = getFace()
    ##generatedClothes = getClothes()
    generatedHat = getHat()
    ##generatedStar = rarity()
    finalImage = seasonOfTheSplicer(generatedBackground, mole, generatedFace, generatedHat, rocks) ##generatedClothes, generatedHat, rocks, generatedStar)
    saving = saveTheImage(finalImage, savePath)
