# ts-XternCoin
XternCoin Project Submission by Trenton Spice


XternCoin operates like this: The "server" (your code you are writing) stores a single random number. Clients have to guess what this number is. If they guess correctly, the app awards them 1 coin and chooses a new random number for the next guess.
There are three functions XternCoin's server will need.


func HandleGuess(userId string, guess int) bool {}
Function which takes a user's id and a user's guess, and returns whether or not their guess was correct.

func GetCoins(userId string) int {}
Function which takes a userid and returns how many coins they have.


Finally, one more function is required:
func StartGuessing() {}
A function which, when called, pretends to be a user of XternCoin and uses the other two functions you've written to accumulate coins by guessing random numbers in a loop (indefinite is fine).


Remember that users of XternCoin would only have access to the two functions you wrote above; they can't directly see what random number they are trying to guess, so this function will have to guess randomly as well.
It'd be a good idea to log every attempt you make, as well as a running count of how many coins you have. Here are some things you might consider:

- State to store the number of coins each user has
- State to store the current number clients are trying to guess
- Logic to generate a new random number when the correct one is guessed
 
While the above three functions are all that is required of this assessment a full implementation may require more. If you’d like to demonstrate more of your awesome skills feel free to write a complete program. 
