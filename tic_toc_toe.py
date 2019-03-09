import os

l=[0,1,2,3,4,5,6,7,8]


def board():

    os.system('clear')
    print(l[0],'|',l[1],'|',l[2])
    print('--  -- --')
    print(l[3],'|',l[4],'|',l[5])
    print('--  -- --')
    print(l[6],'|',l[7],'|',l[8])




def win_lose_check(pos):
    if pos==1 or pos==0 or pos==2 :
        if l[2]==l[0]==l[1]:
            win=l[pos]
            return win


    if pos==0 or pos==3 or pos==6:
        if l[0]==l[3]==l[6]:
            win=l[pos]
            return win


    if pos==3 or pos==4 or pos==5:
        if l[3]==l[4]==l[5]:
            win=l[pos]
            return win


    if pos==6 or pos==7 or pos==8:
        if l[6]==l[7]==l[8]:
            win=l[pos]
            return win


    if pos==1 or pos==4 or pos==7:
        if l[1]==l[4]==l[7]:
            win=l[pos]
            return win


    if pos==2 or pos==5 or pos==8:
        if l[2]==l[5]==l[8]:
            win=l[pos]
            return win


    if pos==0 or pos==4 or pos==8:
        if l[0]==l[4]==l[8]:
            win=l[pos]
            return win


    if pos==2 or pos==4 or pos==6 :
        if l[2]==l[4]==l[6]:
            win=l[pos]
            return win



def reset_board():
    for i in range(0,9):
        l[i]=i



def game():
    play='y'
    position=0
    while play=='y':
        p1=input("Enter your name Player1 : ")
        p2=input("Enter your name Player2 : ")
        reset_board()
        board()

        t=0
        while t<9 and position>=0 and position<9:

            print("{} ('X') enter your input : ".format(p1.upper()))

            position=int(input())
            while position>=9:
                print("""The position doesn't exist !!!
                        please enter another position""")
                position=int(input())
            while l[position]=='X' or l[position]=='O':
                print("The position is occupied please enter another location!!")
                position=int(input())
            t=t+1
            l[position]='X'
            board()
            ans=win_lose_check(position)
            if ans=='X' :
                print(f"{p1.upper()} is the winner")
                print("                 CONGRATULATIONS!!!              ")
                break
            elif ans=='O':
                print(f"{p2.upper()} is the winner")
                print("                 CONGRATULATIONS!!!              ")
                break


            if t==9:
                print("Nobody wins!!!")
                break

            print("{} ('O') enter your input : ".format(p2.upper()))
            position=int(input())
            while position>=9:
                print("""The position doesn't exist !!!
                        please enter another position""")
                position=int(input())
            while l[position]=='X' or l[position]=='O':
                print("The position is occupied please enter another location!!")
                position=int(input())
            t=t+1
            l[position]='O'
            board()
            ans=win_lose_check(position)
            if ans=='X' :
                print(f"{p1.upper()} is the winner")
                print("                 CONGRATULATIONS!!!              ")
                break
            elif ans=='O':
                print(f"{p2.upper()} is the winner")
                print("                 CONGRATULATIONS!!!              ")
                break



        print("Do you want to play again ? [y/n] :")
        play=input()


os.system('clear')
print(" Welcome to the Tic-Toc-Toe game!!!")
print("********Press 'Enter' to play*******")
if input()=="":
    game()
