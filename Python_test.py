import time
import random

#note: there is something wrong with the books and vid games section dont try to run them

print("Loading...")
time.sleep(2)
print("Hello! I am Unnamed rn.")
time.sleep(0.7)
name = input("What should i call you?:")
time.sleep(0.4)
print("Hello", name, "! Nice to meet you.")
time.sleep(0.3)
print("Here are some commands you can choose from:")
time.sleep(0.4)
print("'movies' 'books' 'video games' 'random facts' 'more info' 'rename' 'music'.")

while True:
    reply = input("Lets talk about something!:")
    while True:
        if reply == "movies":
            print("horror, fantasy, sci-fi, adventure, comedy, thriller")
            reply1 = input("which genre? (Note:if you wanna exit the movie section type 'exit_movies'):")
            if reply1 == "horror":
                print(
                    "Im sorry, i havent watched many horror fims. But here are some of them: Nightmare on elm street and IT.")
                time.sleep(2.5)

            if reply1 == "fantasy":
                print(
                    "İ have watched a lot of them.(i generally hate movies especially series, they take a lot of time. So i dont watch much.) Avatar the last airbender(the movie one), the mask, Pixels ,jumanji 1&2 and all harry potter films. Spirited away also count as fantasy, but its an anime so")
                time.sleep(2.5)

            if reply1 == "sci-fi":
                print(
                    "I have watched lost in space, matrix, stranger things(idk if this counts), WALL-E, glitch and yakamoz s-245. I think i have watched more but i cant remember.. Anyways, i really liked WALL-E. I also reccomend lost in space. They were really good and you can watch them with your family!")
                time.sleep(2.5)

            if reply1 == "adventure":
                print(
                    "spirited away and drifting home also counts in this one, but they are all anime :,). Also, i really reccomend Drifting home. it was really good.")
                time.sleep(2.5)

            if reply1 == "comedy":
                print(
                    "I dont watch comedy. But my friend suggested Assasination classroom. Its also an anime. Im sorry :D")
                time.sleep(2.5)

            if reply1 == "thriller":
                print(
                    "Hmm... Breaking bad, and matrix(matrix mostly counts as action). i dont remember %80 of the movies i have watched. I only remember the ones that I have really liked.")
                time.sleep(2.5)

            if reply1 == "exit_movies":
                print("Update:you have exited the movies section.")
                print(
                    "Note: i will add more to this section, But i havent watched many movies. and i know that there is no mystery, romance, psychology and history. i will add them soon.")
                time.sleep(1.5)
                break

        if reply == "books":
            print("The books i like?")
            time.sleep(1.5)
            print("python gives an error so i will make it short.")
            time.sleep(0.7)
            print(
                "MOMO by micheal ende, the cat who saved books, animal farm by george orwell, fullmetal alchemist(manga), ")
            time.sleep(1.3)
            break

    while True:
        if reply == "video games":
            print("still working on it...")
            AB = input("type 'exit_vidgames'")
            if AB == "exit_vidgames":
                time.sleep(1.3)
                break