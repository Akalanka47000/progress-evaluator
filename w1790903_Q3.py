#Defining the Exceptions which could occur during the program
class notAcceptable(Exception): #Exeption to be raised if the entered credit value is not in the acceptable list
    pass
class incorrectTotal(Exception): #Exception to be raised if the total of the entered credits is not 120
    pass
class notDefinedCharacter(Exception): #Exception to be raised if the user enters any other character than p or q during the input section to termiante loop
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
    
#Code section to determine whether user wants to proceed or quit the program
runOrQuit="p"        #Initializing the counter control variable as to meet the loop entering requirement so that the loop can be entered during the first iteration
studentCounter=1     #variable to count the number of students for which credits were entered
progressCounter=0    #variable to count the number of students who progressed
trailingCounter=0    #variable to count the number of students who are trailing
retrieverCounter=0   #variable to count the number of students who have to repeat the module
excludedCounter=0    #variable to count the number of excluded students
row=100
column=4
histogramArray=[[1 for x in range(column+1)] for y in range(row+1)]
for x in range(row+1):
    for y in range(column+1):
        histogramArray[x][y]=" "
while runOrQuit=="p":
    runOrQuitFlag=False  #initialing a flag to handle an error where a user enters any other character than p or q during the input section to termiante loop
    errorOccurred=False   #initializing a flag tocontrol how the user input is asked for the 2 letters p or q when its entered for the first time or re-entering after errors
    #Section to read the credit values successfully
    validForMain=False
    while validForMain==False:
       try:    
             #Code to read pass credits until entered value is valid
             validFlag=False
             while validFlag==False:    
              try:
                print("Enter pass credits for student",studentCounter) 
                passCredit=int(input())
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
                print("Enter defer credits for student",studentCounter)  
                deferCredit=int(input())
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
                print("Enter fail credits for student",studentCounter)
                failCredit=int(input())
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
        rowCount=1
        rowFlag=False #Flag to control the while loop below so as to stop searching the array once the * is printed 
        while rowFlag==False:
            if  histogramArray[rowCount][1]!="*":                
               histogramArray[rowCount][1]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==100 and deferCredit==20 and failCredit==0:
        printTrailer()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][2]!="*":                
               histogramArray[rowCount][2]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==100 and deferCredit==0 and failCredit==20:
        printTrailer()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][2]!="*":                
               histogramArray[rowCount][2]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==80 and deferCredit==40 and failCredit==0:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==80 and deferCredit==20 and failCredit==20:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==80 and deferCredit==0 and failCredit==40:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==60 and deferCredit==60 and failCredit==0:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==60 and deferCredit==40 and failCredit==20:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==60 and deferCredit==20 and failCredit==40:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==60 and deferCredit==0 and failCredit==60:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==40 and deferCredit==80 and failCredit==0:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==40 and deferCredit==60 and failCredit==20:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==40 and deferCredit==40 and failCredit==40:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==40 and deferCredit==20 and failCredit==60:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==40 and deferCredit==0 and failCredit==80:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==100 and failCredit==0:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==80 and failCredit==20:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==60 and failCredit==40:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==40 and failCredit==60:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==20 and failCredit==80:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==20 and deferCredit==0 and failCredit==100:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==120 and failCredit==0:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==100 and failCredit==20:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==80 and failCredit==40:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==60 and failCredit==60:
        printRetriever()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][3]!="*":                
               histogramArray[rowCount][3]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==40 and failCredit==80:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==20 and failCredit==100:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    elif passCredit==0 and deferCredit==0 and failCredit==120:
        printExclude()
        rowCount=1
        rowFlag=False
        while rowFlag==False:
            if  histogramArray[rowCount][4]!="*":                
               histogramArray[rowCount][4]='*'
               rowFlag=True
            rowCount+=1
    #asks the user to re-nter a character until its p or a
    while runOrQuitFlag==False:
       try:
              if errorOccurred==False:
                 runOrQuit=input("Press \"p\" to proceed with next student, or \"q\" to quit\n")
              else:
                 runOrQuit=input("Please enter either \"p\" or \"q\"\n")
              if runOrQuit=="p" or runOrQuit=="q":
                 runOrQuitFlag=True
              else:
                 raise notDefinedCharacter()   #raises notDefinedCharacter exception if the entered character isnt either p or q
                 errorOccurred=True
       except notDefinedCharacter:
        print("Invalid character entered.")
        runOrQuitFlag=False
    studentCounter+=1

#Code section to print the histogram
if runOrQuit=="q":     
        print("Given below are the statistics for the entered student batch\n")
        print("Progress Trailing Retriever Excluded\n")
        #printing the histogram with alignment
        for printHistogram in range(1,studentCounter+1):
                print("  ",histogramArray[printHistogram][1],"       ",histogramArray[printHistogram][2],"      ",histogramArray[printHistogram][3],"      ",histogramArray[printHistogram][4], end="\n")  
        
