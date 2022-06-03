# Python program for Finite Automata
# Pattern searching Algorithm
 
NO_OF_CHARS = 256
 
def getNextState(pat, M, state, x):
    
    if state < M and x == ord(pat[state]):
        return state+1

    i=0
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns
    return 0
 
def computeTF(pat, M):

    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]
          for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
    return TF
 
def search(pat, txt):

    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)   
 
    state=0
    status=0

    for i in range(N):

        state = TF[state][ord(txt[i])]
        if state == M:
            status+=1
            print("Pattern found at index: {}".\
                   format(i-M+1))
            a=i-M+1
            b=i+1
            for i in range(i-M-14, i+16):
              if a <= i < b:
                print('\033[34m', txt[i], end = "")
              else:
                print( '\033[0m', txt[i], end = "")

            print("\n")

    if status == 0:
        print("Pattern not found")
        print("Status: Input Text Rejected.")
    else:
      print("\n")
      print("Total occurrences of pattern:", end = " ")
      print(status)
      print("Status: Input Text Accepted")
        
 
# Driver program to test above function           
def main():

    usertext = input("Enter the (filename).txt to be search: ")
    userpat = input("Enter pattern to be search: ")
    txt = open(usertext).read()
    pat = userpat

    print("\n")    
    print("******************** Program Input ********************")
    print("\n")
    print("Input Pattern: ", end = " ")
    print(pat)
    print("\n")
    print("Input Text: ", end = "\n\n")
    print(txt, end = "\n\n\n\n")
    print("******************** Program Output ********************")
    print("\n")

    search(pat, txt)
 
if __name__ == '__main__':
    main()
