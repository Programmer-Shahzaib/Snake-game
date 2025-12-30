#Exercise 6:Snake and water gun game
name=input("Whats your name: ",)
print(f"Hello! {name} Welcome to our game (snake and water gun ):")
import random as r
game=["Snake","Water","Gun"]
print("game:","choose snake,gun,water")
while True:
    n=int(input("How many times you wnat to play the game:",))
    comp_points=0
    my_points=0
    for i in range(1,n+1):
        comp=r.choice(game).lower()
        print(f"Turn {i}:")
        user = input("Your Turn - select (snake / water / gun): ").lower()
        print(f"Opponent turn : {comp}")
        if comp=="snake"and user=="water":
            print("Snake swallows your water 🐍💧")
            print("computer wins")
            comp_points+=1
            print(f"computer points = {comp_points}")
        elif user=="snake"and comp=="water":
            print("snake swallows computer water 🐍💧")
            print("you win")
            my_points+=1
            print(f"your points = {my_points}")
        elif user=="gun"and comp=="water":
            print("gun is inside water 😅💧😅")
            print("computer wins")
            comp_points+=1
            print(f"computer points = {comp_points}")
        elif comp=="gun"and user=="water":
            print("gun is inside water 😅💧😅")
            print("you win")
            print(f"your points = {my_points}")
            my_points+=1
        elif comp=="snake"and user=="gun":
            print("Gun shot the snake🔫🐍")
            print("you win")
            my_points+=1
            print(f"your points = {my_points}")
        elif comp=="gun"and user=="snake":
            print("Gun shot the snake🔫🐍")
            print("computer win")
            comp_points+=1
            print(f"computer points = {comp_points}")
        elif user==comp:
            print("Draw,No point for both")
        else:
            print("invalid choice!")
    if my_points > comp_points:
        print(f"\n🎉 Congratulations! You win 🎉\nYou: {my_points} | Computer: {comp_points}")
    elif my_points < comp_points:
        print(f"\n😢 You lose, Computer wins!\nYou: {my_points} | Computer: {comp_points}")
    else:
        print(f"\n🤝 It's a Draw!\nYou: {my_points} | Computer: {comp_points}")
    choice=input("Do you want to play again (yes/no) : ",).lower()
    if choice=="yes":
        continue
    else:
        print("Thanks for playing game!")
        break
