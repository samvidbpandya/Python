#parsing text file..

def main( ):
    #read file
    file = open( "JMD.txt","r" )
    lines = file.readlines()
    file.close()
    
    #Looking for Patterns in File
    countYes = 0
    countNo = 0
    countTrue = 0
    countFalse = 0

    for line in lines:
        line = line.strip().upper()

        if line.find("YES")!=-1:
            countYes = countYes + 1
        if line.find("NO")!=-1:
            countNo = countNo + 1
        if line.find("TRUE")!=-1:
            countTrue = countTrue + 1
        if line.find("FALSE")!=-1:
            countFalse = countFalse + 1

    print("Yes: ", countYes)
    print("No: ", countNo)
    print("True: ", countTrue)
    print("False: ", countFalse)
main()
