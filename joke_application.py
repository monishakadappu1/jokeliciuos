import joke_of_the_day as jk

if __name__ == '__main__':
    joke = jk.Joke()
    print("Would you like to hear a new joke today??")
    ans = raw_input("yes/no")
    if ans == "yes":
        print(joke.getjoke())
    else:
        print("Thank you ,have a nice day")
