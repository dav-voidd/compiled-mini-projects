#Call Center Agent Round-Robin
#1st, create a class and initialize a list.
#2nd, create a pusher, If agents are queueing those who inputted or pressed queue first will be the one to take the call first.
#3rd, create a dequeuer, If agent 1 just got a call, pop agent 1 to the list, and append them at the end of the list, same to agent2.
#If the list is empty, print that the agents are busy and please call again.



class CallCenter:
    def __init__(self):
        self.queue = list()

    def add_agents(self, agents):
        self.queue.append(agents)

    def calls(self):
        if len(self.queue) == 0:
            print("The agents are busy. Please call again.")
        else:
            name_of_agent = self.queue.pop(0)
            print(f"{name_of_agent} just got a call.")
            self.queue.append(name_of_agent)


agency = CallCenter()
while True:
    user_input = input("Type (c) to call. QUEUE LIST | Add the agents name: ")
    if user_input == 'c':
        agency.calls()
    else:
        agency.add_agents(user_input)


