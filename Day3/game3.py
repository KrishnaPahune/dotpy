seq1="FBLR"
seq2="FBRL"
seq3="FLBR"
seq4="FLRB"
seq5="FRBL"
seq6="FRLB"
seq7="BFLR"
seq8="BFRL"
seq9="BLFR"
seq10="BLRF"
seq11="BRFL"
seq12="BRLF"
seq13="LFRB"
seq14="LFBR"
seq15="LBFR"
seq16="LBRF"
seq17="LRFB"
seq18="LRBF"
seq19="RFLB"
seq20="RFBL"
seq21="RLFB"
seq22="RLBF"
seq23="RBFL"
seq24="RBLF"

print("Help little kris to find his christmas present!")
print("Kris's wonderful present is just 4 steps away!")
print("At a time kris can go only one step i.e left(L), right(R), forward(F), Backward(B)")
print("Steps should not be repeated")
print("Each unique sequence of steps unlocks unique and exciting present")
q=input("Are you ready to play?(yes/no) ")
if(q.lower()=="yes"):
    print("".center(100,"*"))
    while True:
        move=input("Enter your first move (L/R/F/B) :- ")
        seq=move
        move=input("Enter your second move:- ")
        seq+=move
        move=input("Enter your third move:- ")
        seq+=move
        move=input("Enter your last move:- ")
        seq+=move

        if seq == seq1:     
            print("Wow! Santa brought you a shiny new bicycle.")
        elif seq == seq2:       
            print("Amazing! Santa gave you a cute little puppy.")
        elif seq == seq3:       
            print("Fantastic! Santa brought you a set of colorful paints.")
        elif seq == seq4:       
            print("Great! Santa gave you a Lego building set.")
        elif seq == seq5:       
            print("Awesome! Santa brought you a remote-controlled car.")
        elif seq == seq6:       
            print("Impressive! Santa gave you a new soccer ball.")
        elif seq == seq7:       
            print("Cool! Santa brought you a giant teddy bear.")
        elif seq == seq8:       
            print("Amazing! Santa gave you a magic kit.")
        elif seq == seq9:       
            print("Splendid! Santa brought you a science experiment kit.")
        elif seq == seq10:      
            print("Outstanding! Santa gave you a skateboard.")
        elif seq == seq11:      
            print("Superb! Santa brought you a musical instrument.")
        elif seq == seq12:      
            print("Marvelous! Santa gave you a puzzle game.")
        elif seq == seq13:      
            print("Excellent! Santa brought you a storybook collection.")
        elif seq == seq14:
            print("Wonderful! Santa gave you a superhero costume.")
        elif seq == seq15:
            print("Fantastic! Santa brought you an art and craft set.")
        elif seq == seq16:
            print("Spectacular! Santa gave you a train set.")
        elif seq == seq17:
            print("Remarkable! Santa brought you a new backpack.")
        elif seq == seq18:
            print("Incredible! Santa gave you a pair of roller skates.")
        elif seq == seq19:
            print("Fabulous! Santa brought you a box of chocolates.")
        elif seq == seq20:
            print("Terrific! Santa gave you a dinosaur toy.")
        elif seq == seq21:
            print("Magnificent! Santa brought you a space exploration kit.")
        elif seq == seq22:
            print("Stunning! Santa gave you a fishing rod.")
        elif seq == seq23:
            print("Brilliant! Santa brought you a model airplane.")
        elif seq == seq24:
            print("Amazing! Santa gave you a new pair of sneakers.")

        play_again=input("do you want to play agin?(yes/no)")
        if play_again.lower()=="no":
         break