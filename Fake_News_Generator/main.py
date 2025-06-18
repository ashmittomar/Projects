import random

subjects = ["Virat Kohli","Akshay Kumar","Salman Khan","Shahrukh Khan","A Cat","A Group of monekys","Auto driver from Delhi","PM Modi"]
actions = ["launches","cancels","dance with","eats","declare war on","orders","celebrate","fights"]
places = ["Red Fort","in Mumbai local train","a plate of samosa","inside Parliament","at Ganga ghat","during IPL match","at India Gate"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS: {subject} {action} {place} "
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day")