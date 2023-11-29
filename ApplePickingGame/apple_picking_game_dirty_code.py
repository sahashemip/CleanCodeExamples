from random import randint
import console, time

global gold
global apples
apples = 1
gold = 1

prompt = "> "

def main():
    global gold
    global apples
    console.clear()
    print "Gold: %r Apples: %r" % (gold, apples)
    print "Pick an apple?"
    choice = raw_input(prompt)
    if choice == "yes":
        pick()
    elif choice == "no":
        console.clear()
        global gold 
        global apples
        print "Apples: %r Gold: %r" % (apples, gold)
        print "Sell apples?"
        sell = raw_input(prompt)
        if sell == "yes" and apples >= 1:
            global gold
            global apples
            apple_sales = randint(1,5)
            gold = (gold * (apples / 2)) * apple_sales
            apples = apples - apples
            if gold >= 25 ** 25:
                console.clear()
                print "\t\t\tYou won!"
                print "Congrats on controlling the apple market!"
            else: 
                main()
        elif sell == "yes" and apples <= 0:
            print "\nNot enough apples!"
            time.sleep(0.7)
            main()
        elif sell == "no":
            main()
        else: 
            main()
    elif choice == "exit":
        console.clear()
        print "Bye..."
    else: 
        main()

def pick():
    console.clear()
    global gold
    global apples
    print "Type 0 to exit. How many?"
    print "Apples: %r Gold %r" % (apples, gold)
    try: 
        apple_num = int(raw_input(prompt))
        if apple_num == 3 or apple_num == 2 or apple_num == 1:
            global apples
            apples = apples + apple_num
            time.sleep(0.5)
            pick()
        elif apple_num >= 4:
            console.clear()
            print "You can't haul that many apples!"
            time.sleep(0.5)
            pick()
        elif apple_num == 0:
            main()
    except ValueError:
        pick()

main()
