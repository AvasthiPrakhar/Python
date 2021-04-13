#!/usr/bin/env python
# coding: utf-8

# In[5]:


class ShuffledDeck():

    def __init__(self,):
        
        self.J=10
        self.Q=10
        self.K=10
        #self.A=1
        self.A='A'
        #self.deck=[2,3,4,5,6,7,8,9,10,self.J,self.Q,self.K,self.A]*4    # K in capital
        self.deck=['A',7,10]*20
        pass
    
    def sh_deck(self):
        from random import shuffle
        shuffle(self.deck)
        return self.deck


# In[6]:



# Onject asking to 'hit' or 'stop' and automated hit ad stop based on "Logic"

class HitOrStop():
    
    
    
    
    def __init__(self):
    
        pass

    def ask(self):
        i=input("Enter H to hit , press anyother key to stop\n").lower()
        return i
        
    def hit(self,arg1,arg2,add,auto=0,n=100):                   #arg1 = popped list , arg2 = appended list , add = list sum
        
                                                                # n compared with add
                                                                #put auto = 1 to select cards automatically
        if auto == 0 :
 
                        
            CheckA().manual_check(arg2)
            
                        
            if Logic().adding(arg2,add,n)[0] == 0 :
                print("---------------------END 0 -------------------------------")
                return Logic().adding(arg2,add,n)        
                        
        
            
            
            while self.ask() == 'h' :  
                            

                arg2.append(arg1.pop())
                CheckA().manual_check(arg2)
                


                    
                
                if Logic().adding(arg2,add,n)[0] == 0 :
                    print("------------------------END ---------------------------")
                    
                            
                    return Logic().adding(arg2,add,n)
            
            print(arg2)
            CheckA().manual_check(arg2)

            return Logic().adding(arg2,add,n)
            
        else :
                
            
         
            CheckA().check(arg2)

          
            
           
            
            while  Logic().adding(arg2,add,n)[0] == 1 :
                
                CheckA().check(arg2)
                print(arg2)
                print("testing hit automated ")
                arg2.append(arg1.pop())
                print("------------------arg 2-----------------------------------------")
                print(arg2)
                CheckA().check(arg2)
                print("------------------arg 2 after checking ----------------------------------------")
                print(arg2)
 
            if Logic().adding(arg2,add,n)[1] == 0 :
                print("Dealer lost")
                
            else :
                print("Dealer Won !")
                print("------------------------END 2  ---------------------------")
                
          


# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


class Logic():
    
  
    def __init__(self):
        pass
    
    def adding(self,lis,add,add2=89): 
        
        # lis = the hand to be summed
                                          # add = list's elements' sum 
                                          # add2 = no. to be compared with "add"
            
        print(lis)
        for item in lis :
            add=add+item
      
                

            
        print("-----------------------------")
        print("deck {} ".format(lis))
        print("Total Sum Of Hand is : {}".format(add)) 
        print("-----------------------------")
                
                
        print(add)
        print("was compared with")
        print(add2)    

        if add>21 :
           
            return [0,0]
            
            
        elif add>add2 :

            
            return [0,1]
                  
            
        elif add==21 :
            
            return [0,1]
        
        else :
            return [1,2]


# In[8]:


class Game():

    
    def __init__(self):
            
        self.deck_one = ShuffledDeck().sh_deck() 
        
            # assigning non-static values to deck_one , any change in deck_one would not
            # affect any static variables of ShuffledDeck and only affect varibles for "deck_one" instance .
     
        self.mh=[] #my hand
        self.h=[]  #varable to hold a shuffled deck
        self.dh=[] #dealer's hand
        self.sum_mh=0
        self.sum_dh=0
        pass
    
    def Play(self):
        self.dh.append(self.deck_one.pop())        #popping and appending cards
        self.dh.append(self.deck_one.pop())
        print("Dealer's cards :")
        arg2 = CheckA().check(self.dh)
        print("Dealer's cards :")
        print(self.dh)
        print("-------------------1--------------------")
        
        self.mh.append(self.deck_one.pop())                #popping and appending cards
        self.mh.append(self.deck_one.pop())  
        print("your cards")
        print(self.mh)

        print("Your cards :")
        print(self.mh)
        print("-------------------2--------------------")

        
  
        
        #         hit(self,arg1,arg2,add,auto=0,n=100):          
        #         arg1 = popped list , 
        #         arg2 = appended list , 
        #         add = list sum
        #         put auto = 1 to select cards automatically, default = 0
        #         n is compared with add, default = 89
        #                                                        
        
        fun=HitOrStop().hit(self.deck_one,self.mh,self.sum_mh,0)
        print(self.mh)

        print("____________________________________________________________________________________________________")
        print(fun)
        print("____________________________________________________________________________________________________")

        if fun[1] == 0 :
            print("Player Lost")
            
        elif fun[1] == 1:
            print("Player won !")
            
        else :
            print("____________________Dealer's Turn_________________________")
            add_2=0

            for _ in self.mh :
                add_2 = _ + add_2

            
            HitOrStop().hit(self.deck_one,self.dh,self.sum_dh,1,add_2)


# In[ ]:





# In[9]:



class CheckA():
    
    def __init__(self):
        pass
    
    
    
    
    def check(self,arg):
        storage=[]
        E=11
        O=1
        
        if 11 in arg :
            while (11 in arg ) :
                arg.pop(arg.index(11))
                arg.append('A')
                
        if 1 in arg :
            while (1 in arg ) :
                arg.pop(arg.index(1))
                arg.append('A')
        
        if 'A' in arg :
            while ('A' in arg) :
                storage.append(arg.pop(arg.index('A')))
                
        add_val=0
  
        i=storage.count('A')
        #print(i)
        
        while i != 0  :
            
            
            
            for _ in arg :  
                
                add_val= _ + add_val
            
            
            
            if (add_val + 11 <= 21) :
                
                arg.append(E)
                add_val = add_val + E
                storage.pop()
                
                
               
            
            else :
                
                arg.append(O)
                add_val = add_val + O
                storage.pop()
                
                
            i = i-1  
              
            
        
        s=0
        for _ in arg :
            s=s + _
              
        return arg
        #print(s) 
         
        
        
    def manual_check(self,arg):
        
        storage=[]

        if 11 in arg :
            while (11 in arg ) :
                storage.append(arg.pop(arg.index(11)))
                arg.append('A')
             
                
        if 1 in arg :
            while (1 in arg ) :
                storage.append(arg.pop(arg.index(1)))
                arg.append('A')

                
        
   
        print(arg)
        if 'A' in arg :

            b=input("Press A to change value of A in your deck, any other key to ignore \n ").upper()
            
            if b == 'A' :

                while 'A' in arg :

                    arg.insert(arg.index("A"),int(input("enter value for A")))
                    arg.pop(arg.index("A"))
                    print(f"your cards are : {arg}" )

            else :
                while 'A' in arg :
                    
                    
                    arg.append(storage.pop())
                    arg.pop(arg.index('A'))
                    print(f"your cards are : {arg}" )



        
        
        



  


# In[10]:


#Testing CheckA :
m=[11,7]
CheckA().manual_check(m)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[57]:


Game().Play()


# In[ ]:





# In[ ]:





# In[ ]:




