'''
Each week you are meeting with your friends to spend some quality time together. Usually you're hanging out in a bar on Friday 
nights, or going out of town on Saturdays, or playing the board games on Sundays. You want to simplify the process of gathering 
people and that's why you've decided to write a program which could automate this process.
You should create the class Party(place) which will send the invites to all of your friends. Also you should create the class 
Friend and each friend will be an instance of this class.
Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to 
another town). To form right connections you should create the Party class with the next methods:

add_friend(Friend(name)) - add friend 'name' to the list of the 'observers' (people, which will get the invitations, when the 
new party is scheduled).
del_friend(friend) - remove 'friend' from the 'observers' list.
send_invites() - send the invites with the right day and time to the each person on the list of 'observers'.
Class Friend should have the show_invite() method which returns the string with the last invite that the person has received 
with the right place, day and time. The right place - is the 'place' which is given to the Party instance in the moment of 
creation. If the person didn't get any invites, this method should return - "No party..."
In this mission you could use the Observer design pattern.

Examples:

  party = Party("Midnight Pub")
  nick = Friend("Nick")
  john = Friend("John")
  lucy = Friend("Lucy")
  chuck = Friend("Chuck")

  party.add_friend(nick)
  party.add_friend(john)
  party.add_friend(lucy)
  party.send_invites("Friday, 9:00 PM")
  party.del_friend(nick)
  party.send_invites("Saturday, 10:00 AM")
  party.add_friend(chuck)

  john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
  lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
  nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
  chuck.show_invite() == "No party..."

Input: The Party class methods and friends.

Output: The text of the last invite received by a person.

How it is used: For automatic notifications mailout about the information changes to all of the observers.

Precondition: All friends' names will be different.

'''

class Friend:
    def __init__(self, name):
        self.name = name
        self.invites = ['No party...']

    def show_invite(self):
        return self.invites[-1]
        
    def recieve_invite(self, invite):
        self.invites.append(invite)
        
        
class Party:
    def __init__(self, name):
        self.name = name
        self.friends = set()

    def add_friend(self, friend):
        self.friends.add(friend)
        
    def del_friend(self, name):
        self.friends.discard(name)
        
    def send_invites(self, invite):
        for friend in self.friends:
            Party_Friend_interface().interface(self.name + ': ' + invite, friend)
    
    
class Party_Friend_interface:
    def interface(self, invite, friend):
        friend.recieve_invite(invite)
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
    
