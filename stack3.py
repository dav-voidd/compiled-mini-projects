#How did this work? - First, I created a type class then initialized the 2 list.
#Then, I made 4 functions. The first function was to append the user input to the undo list. Second function was to check if there's items inside
#the list. there we created a temporary variable to put the popped value and transferred the popped value to the redo list.
#For the 3rd function (redo), the same function was used from the undo function.
#4th function was to check the current status of the text. I used the .join function to join each text from the list.
#Then I declared a variable as the Class so that we can work or access what's inside of it.
#After that, we used the while loop to loop the if/elif statements to append and call the functions.
#What was the problems you encountered? I encountered alot, I forgot to rename the list because the name of the functions and the list are the same!
#It took me a long time what was wrong T_T But I figured it out.




class Type:
    def __init__(self):
        self.my_undo = list()
        self.my_redo = list()

    def type(self, word):
        self.my_undo.append(word)

    def undo(self):
        if len(self.my_undo) > 0:
            save_list = self.my_undo.pop()
            self.my_redo.append(save_list)
        return "no more words"

    def redo(self):
        if len(self.my_redo) > 0:
            save_list = self.my_redo.pop()
            self.my_undo.append(save_list)
        return "no more words"

    def get_current_text(self):
        return " ".join(self.my_undo)


editor = Type()

while True:
    print(f"\nYour Current Document: [ {editor.get_current_text()} ]")

    action = input("Type a word, or enter 'undo' / 'redo': ").strip()

    if action.lower() == "undo":
        editor.undo()
    elif action.lower() == "redo":
        editor.redo()
    else:
        editor.type(action)

