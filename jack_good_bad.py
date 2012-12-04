##### This python program opens an input file into a dictionary structure.
####
####
####
####The content file must have lines separated by or bars like "|" that look like.
####Each line has a situation description, good and bad action, and good and bad result.
####
####situation_description|good_action|good_result|bad_action|bad_result
content_format = ['situation','good_choice','good_result','bad_choice','bad_result']
content_file = "content.txt"

storyline = '''
Welcome to TITLE.  In this game, you must choose between good and bad.
Make the right choices, please.
'''
#this score goes down for bad and up for good


#Here is the array that will contain our list of stories
story_content = []
player_goodness = 0


#this function loads story content into the story_content array
def load_story_content():
    file = open(content_file)
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split("|")#this line separates each line by the | character
        story_entry_dict = {}#create a dictionary to store in story_content
        for i in range(0,len(content_format)):#this loops for all content_format items
            content_type = content_format[i]
            story_entry_dict[content_type] = parts[i]
        story_content.append(story_entry_dict)#adds this content to story_content

#fruitful functiont that returns "good" or "bad" and takes a story content entry as an argument
good_in_a_row = 0


def player_choose(content):
    global good_in_a_row
    choice = 0
    while not (choice==1 or choice==2):
        print "You can:"
        print "(1)",content['good_choice']
        print "(2)",content['bad_choice']
        choice = input("Type 1 or 2:")
   
    if choice == 1:
        good_in_a_row+=1
        print "you have" ,good_in_a_row, "good bonus points"
        if good_in_a_row == 2:
            print "You get a good bonus!!!"
        return "good"
    else:
        good_in_a_row = 0
    
    
bad_in_a_row = 0    
    
    
    if choice == 2:
        bad_in_a_row+=1
        print "you have" ,bad_in_a_row, "evil bonus points"
        if bad_in_a_row == 1:
            print "You get a evil bonus MWHAHAHA!!!"
        return "bad"
    else:
        bad_in_a_row = 0



  

def print_summary():
    kind_of_player = "a meh kind of person."
    if player_goodness > 0:
        kind_of_player = "a pretty good guy."
    if player_goodness < 0:
        kind_of_player = "a pretty bad dude."
    print "The way you played, you must be",kind_of_player

def start_story():
    global player_goodness#this is required becasue we are changing player_goodness
    for scene in story_content:
        print scene['situation']
        choice = player_choose(scene)
        print scene[choice+"_result"]
        if choice == "good":
            player_goodness += 1
        if choice == "bad":
            player_goodness -= 1
       

load_story_content()

start_story()
print_summary()