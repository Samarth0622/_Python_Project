import random

subjects =[
    "Shah Rukh Khan",
    "Amitabh Bachchan",
    "Priyanka Chopra",
    "Ranveer Singh",
    "Kareena Kapoor",
    "Alia Bhatt",
    "Salman Khan",
    "Akshay Kumar",
    "Deepika Padukone",
    "Hrithik Roshan", 
    "Ranbir Kapoor", 
    "Sonam Kapoor"
]
actions = [
    "discovers",
    "destroys",
    "launches",
    "reveals",
    "bans",
    "confirms",
    "debunks",
    "hugs",
    "builds",
    "announces"
]

place_or_event=[
    "in Mumbai",
    "in Delhi",
    "in Bengaluru",
    "in Chennai",
    "in Hyderabad",
    "in Kolkata",
    "in Goa",
    "in Srinagar",
    "on Mars", 
    "under the Taj Mahal",
    "in a haunted palace",
    "at a film festival",
    "on a secret island"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(place_or_event)

    Headline = f"Breaking News: {subject} {action} {place}!"
    print( "\n"+ Headline)

    user_input = input("Press Enter to generate another headline or type 'exit' to quit: ").strip().lower()
    if user_input == "exit":
        break
    
print("\n Thank you for using the Fake News Generator!")