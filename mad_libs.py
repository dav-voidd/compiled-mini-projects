#MadLibs
print("=== MAD LIBS GAME ===")

print("\nMy name is 0.__________ and I am 1.________ years old. \nIf I were the president, I'd do a whole bunch of 2._______ things: "
      "\n1. I would drive the biggest 3.__________ car in the country. And that car would go faster than any other 4._______ in the world!"
      "\n2. Everyone would eat pepperoni 5.__________ for dinner. \n3. I would live in the Statue of 6.______ and build a 7.________ pool at her feet. "
      "\n4. I would wear a/an 8.__________ on my head, and everyone would said I look 9.______ like 10._______. "
      "\n5. School would be open only 11.________ days a year."
      "\n6. I would give my friends the best jobs. I would nominate 12.______ to be secretary of (the) 13._______, and 14._____ could be vice 15._______!")


answer = []
print("There will be 15 answers in total.")

for i in range(16):

    user_words = input(f"{i}. Answer for every blank: ")
    answer.append(user_words)

print(f"\nMy name is {answer[0]} and I am {answer[1]} years old. \nIf I were the president, I'd do a whole bunch of {answer[2]} things: "
      f"\n1. I would drive the biggest {answer[3]} car in the country. And that car would go faster than any other {answer[4]} in the world!"
      f"\n2. Everyone would eat pepperoni {answer[5]} for dinner. \n3. I would live in the Statue of {answer[6]} and build a {answer[7]} pool at her feet. "
      f"\n4. I would wear a/an {answer[8]} on my head, and everyone would said I look {answer[9]} like {answer[10]}. "
      f"\n5. School would be open only {answer[11]} days a year."
      f"\n6. I would give my friends the best jobs. I would nominate {answer[12]} to be secretary of (the) {answer[13]}, and {answer[14]} could be vice {answer[15]}!")