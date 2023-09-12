import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Dealer import Dealer
from Player import Player
from sixdeck import SixDeck

def BlackJackGame():
    root = tk.Tk()
    
    icomp = Image.open('cartas/icono.png')
    iconPhoto = ImageTk.PhotoImage(icomp)
    root.title(string= "BlackJack")
    root.iconpPhoto(False, iconPhoto)
    
    p = Player()
    d = Dealer()
    deck = SixDeck()
    deck.shuffle()
    
    global betSize
    betSize = 0
    
    global frameCount
    frameCount = 0
    
    global playerCardTracker
    playerCardTracker = 0
    
    global dealerCardTracker
    dealerCardTracker= 0
    
    global imageCount
    imageCount = 0
    
    global bjBool
    bjBool = False
    
    global downCardIndex
    downCardIndex = 0
    
    global startChips
    startChips = 0
    
    global doubleBool
    doubleBool = False
    
    def clearFrame():
        for widgets in frame_List [globals()['frameCount']].winfo_children():
            widgets.destroy()
        frame_List[globals()['frameCount']].destroy()
        
    def drawAdds(s,v):
        getCardString(s,v)
        
    def getCardString(s,v):
        if (v == 1):
            valString = "ace"
        elif (v == 11):
            valString = "jack"
        elif (v == 12):
            valString = "queen"
        elif (v == 13):
            valString = "king"
        else:
            valString = str(v)
        fileName = "cards/" +s.lower()+"_"+valString+".png"
        addImage(fileName)
        
    def addImage(fileName):
        card = Image.open(fileName)
        cim = card.resize((95,145), Image.ANTIALIAS)
        im_card = ImageTk.PhotoImage(cim)
        image_List.append (im_card)
    
    def hitandStandDestroy():
        hitButton_List[globals()['frameCount']].destroy()
        standButton_List[globals()['frameCount']].destroy()
            
    def start():
        p.addChips(float(buyInEntry.get()))
        globals()['betSize'] = float(betEntry.get())
        globals()['startChips'] = float(buyInEntry.get())
        deal()
    
    def deal():
        clearFrame()
        if(globals()['doubleBool']== True):
            globals()['betSize'] = globals()['betSize']/2
            globals()['doubleBool'] = False
        
        p.reset()
        d.reset()
        globals()['playerCardTracker'] = 0
        globals()['dealerCardTracker'] = 0
        
        globals()['frameCount'] += 1
        frame_List [globals()['frameCount']].pack(padx = 1, pady = 1)
        p.loseChips(globals()['betSize'])
        
        p.draw(deck)
        drawAdds(p.getSuit(),p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount']+= 100
        globals()['playerCardTracker'] +=100
        
        d.draw(deck)
        drawAdds(p.getSuit(),p.getVal())
        globals()['downCardIndex'] = globals()['imageCount']
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['playerCardTracker'], y=100)
        globals()['imageCount']+= 100
        globals()['playerCardTracker'] +=100
        
        p.draw(deck)
        drawAdds(p.getSuit(),p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount']+= 100
        globals()['playerCardTracker'] +=100
        
        d.draw(deck)
        drawAdds(p.getSuit(),p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['playerCardTracker'], y=100)
        globals()['imageCount']+= 100
        globals()['playerCardTracker'] +=100
        
        Label(frame_List[globals()['frameCount']], text = str (p.score()),width= 7, font= ("Arial",25)).place(x=330, y= 680)
        hitButton_List[globals()['frameCount']].place(x=300, y=400)
        standButton_List[globals()['frameCount']].place(x=375, y=400)
        
        Label(frame_List[globals()['frameCount']], width = 15, text = "Chips $" + str(p.chipCount()), font = ("Arial",22)).place(x=280, y= 750)
        Label(frame_List[globals()['frameCount']], image = idpc).place(x = 50, y = 400)
        Label(frame_List[globals()['frameCount']], text = str(globals()['betSize']), width = 7, font = ("Arial", 20)).place(x = 100, y = 400)
        
        playerBJCheck()
        dealerBJCheck()
        
    def playerBJCheck():
        globals()['bjBool'] = True
        if(p.score() == 21):
            hitandStandDestroy()
            doubleButton_List[globals()['frameCount']].destroy()
            Label(frame_List[globals()['frameCount']], Text = "BLACKJACK", width = 12, font = ("Arial",25)).place(x = 330, y = 680)
            playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
            colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
            if(d.score()==21):
                p.addChips(globals()['betSize'])
                Label(frame_List[globals()['frameCount']], Text = "Dealer and player BlackJack pushed", width=15, font= ("Arial",25)).place(x=310, y=680)
                Label(frame_List[globals()['frameCount']], Text = "+", width= 6, fg = 'black', font= ("Arial",25 )).place(x=150,y=550)
            else:
                Label(frame_List[globals()['frameCount']], Text = "BLACKJACK!", width= 12, font= ("Arial",25 )).place(x=330,y=680)
                p.addChips(globals()['betSize']*2,5)
                Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']*1,5), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y =550 )
            
    def dealerBJCheck():
       if(d.score()==21):
           Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x=300, y=100)
           hitandStandDestroy()
           doubleButton_List[globals()['frameCount']].destroy()
           playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
           colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
           Label(frame_List[globals()['frameCount']], text = "dealerBlackJack", width= 15, font=("Arial", 25)).place(x=300,y=680)
           Label(frame_List[globals()['frameCount']],text= "-" +str(globals()['betSize']), width=6, fg= 'red', font= ("Arial", 25)).place(x=150, y=550)
    
    def hit():
        p.draw(deck)
        getCardString(p.getSuit(),p.getVal())
        doubleButton_List[globals()['frameCount']].destroy()
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500 )
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width = 7, font = ("Arial", 25)).place(x = 330, y = 680)
        if(p.score() > 21):
            Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
            hitandStandDestroy()
            playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
            colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
            Label(frame_List[globals()['frameCount']], text = "Player Busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
            Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
            
        
    def dealersTurn():
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
        doubleButton_List[globals()['frameCount']].destroy()
        while(d.score() < 17):
            d.draw(deck)
            getCardString(d.getSuit(),d.getval())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['dealerCardTracker'], y = 100)
            globals()['imageCount'] += 1
            globals()['frameCount'] += 100
            
        Label(frame_List[globals()['frameCount']], text = str(d.score()), width = 7, font = ("Arial", 25)).place(x = 330, y = 50)
        if (d.score() > 21):
            hitandStandDestroy()
            playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
            colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
            p.addChips(globals()['betSize']*2)
            Label(frame_List[globals()['frameCount']], text =  "Deale Busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
            Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y = 550)
        else:
            checkWin()
            
    def checkWin():
        hitandStandDestroy()
        playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
        colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
        if(p.score() > d.score()):
            p.addChips(globals()['betSize']*2)
            Label(frame_List[globals()['frameCount']], text = "Player Wins", width = 12, font = ("Arial", 25)).place(x = 300, y = 680)
            Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y = 550)
        elif (p.score() == d.score()):
            p.addChips(globals()['betSize'])
            Label(frame_List[globals()['frameCount']], text = "Bets Pushed", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
            Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
        else:
            Label(frame_List[globals()['frameCount']], text = "Dealer Wins", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
            Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
    
    def endGame():
        finalChips = p.chipCount() - globals()['startChips']
        if(finalChips >= 0):
            Label(root, text = "You Won" + str(finalChips) + "Chips", width = 25, font = ("Arial", 24), fg = 'green').place(x = 400, y =400)
        else:
            finalChips = finalChips * -1
            Label(root, text = "You Lost" + str(finalChips) + "Chips", width = 25, font = ("Arial", 24), fg = 'red').place(x = 400, y =400)
        clearFrame()
        
    def double():
        globals()['doubleBol'] = True
        globals()['betSize'] = globals()['betSize'] * 2
        p.loseChips(globals()['betSize'])
        Label(frame_List[globals()['frameCount']], width= 15, text= "Chips $" + str(p.chipCount()), font= ("Arial", 22)).place(x=280, y= 750)
        p.draw(deck)
        getCardString(p.getSuit(), p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x= 300 + globals()['playerCardTracker'], y= 500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        Label(frame_List[globals()['frameCount']], text= str(p.score()), width=7, font= ("Arial", 25)).place(x=330, y= 680)
        if(p.score() > 21):
             Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x=300, y=100)
             hitandStandDestroy()
             playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
             colorUpButton_List[globals()['frameCount']].place (x = 420, y = 400)
             Label(frame_List[globals()['frameCount']], text = "Player busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
             Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
        else:
            dealersTurn()
            
    def split():
         p.loseChips(globals()['betSize'])
         globals()['playerCardTracker'] = 0
         getCardString(p.getSuit(), p.getVal())
         Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500 )
        
    frame_List = []
    image_List = []
    hitButton_List = []
    standButton_List = []
    playAgainButton_List = []
    colorUpButton_List = []
    doubleButton_List = []
    splitButton_List =  []
    
    
    for i in range (0,2000):
        frame_List.append(LabelFrame(root, width= 2000, height= 2000, background= 'darkgray'))
        hitButton_List.append(Button(frame_List[i], text= "Hit", command = hit, height= 2, width= 5, background="salmon", font = ("Arial", 15)))
        standButton_List.append(Button(frame_List[i], text=" Stand", command = dealersTurn, height=2, width=5, background="turquoise", font = ("Arial", 15)))
        playAgainButton_List.append(Button(frame_List[i], text = "Play Again", command = deal,height = 2, width= 8,background = "agua", font = ("Arial", 15)))
        colorUpButton_List.append(Button(frame_List[i], text = "Color up", command = endGame,height = 2, width= 8,background = "coral", font = ("Arial", 15)))
        doubleButton_List.append(Button(frame_List[i],Text = "double", command = double, height= 2, width = 5, background = 'fuchsia', font = ("Arial", 15)))
        splitButton_List.append(Button(frame_List[i],Text = "Split", command = split, height= 2, width = 5, background = 'gold', font = ("Arial", 15)))
        
        
        
    frame_List[0].pack()
    
    Button(frame_List[0], text = "Play Black Jack", command= start, height= 10, width= 25, background= 'salmon', font= ("Arial", 25)).place(x=700, y=100)
    buyInEntry = Entry (frame_List[0], font =("Arial", 15))
    buyInEntry.place(x = 870, y = 550)
    buyInLabel = Label(frame_List[0], font = ("Arial", 15), text = "Chips Buy in $").place(x=700, y=550)
    betEntry = Entry (frame_List[0], font =("Arial", 15))
    betEntry.place(x = 870, y = 650)
    betLabel = Label(frame_List[0], font = ("Arial", 15), text = "Intial Bet Size $: ").place(x=700, y=650)
    
    pc = Image.open('cards/chip.png')
    dpc = pc.resize((40,40), Image.ANTIALIAS)
    idpc = ImageTk.PhotoImage(dpc)
    bc = Image.open('cards/blue.png')
    dbc = bc.resize((95, 145), Image.ANIALIAS)
    imbc = ImageTk.PhotoImage(dbc)
    
    root.mainloop()
    
    
BlackJackGame()    