#WeightConverter.py
#Scripted By: Samvid Pandya (samvidbpandya/sammy_boy)
#Description: Converts lbs into kgs and vice versa


# 1 lb = 0.453592 kgs
# 1 kg = 2.20462 lbs

def weightConverter():
        
    #Find out what user wants to convert... 1) lbs ---> kgs or 2) kgs ---> lbs
    #store in a variable
    MyChoice = input ("Mass Type?? \n 1) lbs > kgs \n 2) kgs > lbs \n")


    #check what user typed...

    #if the user has type 1
    if MyChoice == "1":
        

            #mass to be convert in kgs
            print ("Choice = 1")

            #store in a variable
            LBS = int(input ("Enter the weight in lbs to convert \n"))
            KGS = LBS * 0.453592
            print (LBS, "lbs" , "=", KGS, "kgs")
            print("------------------------------")
            TryAgain()
            #Output Mass




    #if the user has type 2
    elif MyChoice == "2":
             #mass to be convert in kgs
             print("Choice = 2")

             #store in a variable
             KGS = int(input ("Enter the weight in kgs to convert \n"))
             LBS = KGS * 2.20462
             print (KGS, "kgs","=", LBS, "lbs" )
             print("------------------------------")
             TryAgain()
             #lbs = kgs*2.20462
             #Output Mass


    #if the user has type other thing 
    else:
            #something went wrong please check again
            print ("ERROR You entered wrong information PLEASE TRY AGAIN ")
            print("------------------------------")
            weightConverter()
           #Run Again

#weightConverter()

def TryAgain():
        
    #Find out what user wants to convert... 1) lbs ---> kgs or 2) kgs ---> lbs
    #store in a variable
    Again = input ("Want to try again?? \n 1) Yes \n 2) No \n")


    #check what user typed...

    #if the user has type 1
    if Again == "1":
        weightConverter()
    #if the user has type 2
    elif Again == "2":
             print("Thank You for Using this script")
    else:
            #something went wrong please check again
            print ("ERROR You entered wrong information PLEASE TRY AGAIN ")
            weightConverter()
           #Run Again

#TryAgain()
weightConverter()
