#Defining the Exceptions which could occur during the program
class notAcceptable(Exception): #Exeption to be raised if the entered credit value is not in the acceptable list
    pass
class incorrectTotal(Exception): #Exception to be raised if the total of the entered credits is not 120
    pass

#Funtions to be called during the determination process of the outcomes
def printProgress():
    print("Your progression outcome evaluates to: \"Progress\"\n")
def printTrailer():
    print("Your progression outcome evaluates to: \"Progress – module trailer\"\n")
def printRetriever():
    print("Your progression outcome evaluates to: \"Do not Progress – module retriever\"\n")
def printExclude():
    print("Your progression outcome evaluates to: \"Exclude\"\n")
    

#Section to read the credit values successfully
validForMain=False
while validForMain==False:
   try:    
         #Code to read pass credits until entered value is valid
         validFlag=False
         while validFlag==False:    
          try:
            passCredit=int(input("Enter pass credits\n"))
            #Checking whether the entered passCredit value is acceptable
            if (passCredit==0) or (passCredit==20) or (passCredit==40) or (passCredit==60) or (passCredit==80) or (passCredit==100) or (passCredit==120):
               validFlag=True
            else:
                raise notAcceptable()  #raise the notAcceptable exception if the if condition evaluates to false
                validFlag-False
          except ValueError:
               print("Please Enter a valid Intger\n")
          except notAcceptable:
               print("Please enter a valid integer from the list:0,20,40,60,80,100,120\n")

         #Code to read defer credits until entered value is valid
         validFlag=False
         while validFlag==False:    
          try:
            deferCredit=int(input("Enter defer credits\n"))
            #Checking whether the entered passCredit value is acceptable
            if (deferCredit==0) or (deferCredit==20) or (deferCredit==40) or (deferCredit==60) or (deferCredit==80) or (deferCredit==100) or (deferCredit==120):
                  validFlag=True
            else:
                raise notAcceptable()
                validFlag=False
          except ValueError:
               print("Please Enter a valid Intger\n")
          except notAcceptable:
               print("Please enter a valid integer from the list:0,20,40,60,80,100,120\n")

         #Code to read fail credits until entered value is valid
         validFlag=False
         while validFlag==False:    
          try:
            failCredit=int(input("Enter fail credits\n"))
            #Checking whether the entered passCredit value is acceptable
            if (failCredit==0) or (failCredit==20) or (failCredit==40) or (failCredit==60) or (failCredit==80) or (failCredit==100) or (failCredit==120):
               validFlag=True
            else:
                raise notAcceptable()
                validFlag=False
          except ValueError:
               print("Please Enter a valid Intger\n")
          except notAcceptable:
               print("Please enter a valid integer from the list:0,20,40,60,80,100,120\n")
         if (passCredit+deferCredit+failCredit)!=120 :
             raise incorrectTotal()
         validForMain=True #sets the loop control value to true if all the values are entered successfully so the loop can exit
   except incorrectTotal:
     print("The total of the credits you entered is not equal to 120. Please re-enter\n")

#Section to determine progression outcomes
if passCredit==120 and deferCredit==0 and failCredit==0:
    printProgress()
elif passCredit==100 and deferCredit==20 and failCredit==0:
    printTrailer()
elif passCredit==100 and deferCredit==0 and failCredit==20:
    printTrailer()
elif passCredit==80 and deferCredit==40 and failCredit==0:
    printRetriever()
elif passCredit==80 and deferCredit==20 and failCredit==20:
    printRetriever()
elif passCredit==80 and deferCredit==0 and failCredit==40:
    printRetriever()
elif passCredit==60 and deferCredit==60 and failCredit==0:
    printRetriever()
elif passCredit==60 and deferCredit==40 and failCredit==20:
    printRetriever()
elif passCredit==60 and deferCredit==20 and failCredit==40:
    printRetriever()
elif passCredit==60 and deferCredit==0 and failCredit==60:
    printRetriever()
elif passCredit==40 and deferCredit==80 and failCredit==0:
    printRetriever()
elif passCredit==40 and deferCredit==60 and failCredit==20:
    printRetriever()
elif passCredit==40 and deferCredit==40 and failCredit==40:
    printRetriever()
elif passCredit==40 and deferCredit==20 and failCredit==60:
    printRetriever()
elif passCredit==40 and deferCredit==0 and failCredit==80:
    printExclude()
elif passCredit==20 and deferCredit==100 and failCredit==0:
    printRetriever()
elif passCredit==20 and deferCredit==80 and failCredit==20:
    printRetriever()
elif passCredit==20 and deferCredit==60 and failCredit==40:
    printRetriever()
elif passCredit==20 and deferCredit==40 and failCredit==60:
    printRetriever()
elif passCredit==20 and deferCredit==20 and failCredit==80:
      printExclude()
elif passCredit==20 and deferCredit==0 and failCredit==100:
      printExclude()
elif passCredit==0 and deferCredit==120 and failCredit==0:
    printRetriever()
elif passCredit==0 and deferCredit==100 and failCredit==20:
    printRetriever()
elif passCredit==0 and deferCredit==80 and failCredit==40:
    printRetriever()
elif passCredit==0 and deferCredit==60 and failCredit==60:
    printRetriever()
elif passCredit==0 and deferCredit==40 and failCredit==80:
    printExclude()
elif passCredit==0 and deferCredit==20 and failCredit==100:
    printExclude()
elif passCredit==0 and deferCredit==0 and failCredit==120:
    printExclude()
terminate=input("Press \"q\" to terminate program\n")
if terminate=="q":
    quit()
          
