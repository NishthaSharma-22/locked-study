# detective talks to all
# clara - the culprit
# will seekig person - forced her
# letter - hinted towards will seeking person
# the whole point was to get revenge on the doctor
# and clara was being protected - she did not commit the muder, but she thought she did.

# eugene gave her a harmless substance, and then he killed the doctotr by other means (insulin overdoe) 
# clara confesses - but th eautopsy does not match
# doctor had written his will reecenyly - and left eugene out o fthe will
# clara herself had been embexxling small amount s form the doctora accounts and eugene found. 
# the housemad knows more. she overheard the conversation bw them and thought they were just folling around, but it was something darker after the murder.
# turns out the doctor wanted to die. he orchestrated it all to punish them both - and set them up to tuen on each other. Dark and cold blooded.
# 
# 
# 
# 
# 

default found_letter = False
default suspect_choice = ""
default drawer_locked = True



label start:
    scene manor
    with fade

    "The wind clawed at the windows of Edevane Manor. Thunder somewhere in the distance. Of course."
    "I arrived at 7:50 PM/ Ten minutes before the police. Twenty minutes before the whole case was swept  under a velvet rug."

    "The victim? Lord Cyril Edevane. 72. Aristocrat. Bit of a recluse. Dead in his provate study, door locked from the inside."

    "Clara Vale, his secratary, had called it in. She was waiting for me at the front hall, pale as salt."

    "Clara: Mr. Robert, thank goodness. It's... it's terrible."


    menu:
        "What happened?":
            "Clara: I-I found him at 7:40. Slumped at the desk. The door was locked. I had to fetch the groundskeeper to force it open."
        "Why call me, not the police?":
            "Clara: Lord Edevance said... if anything strange happended... I should call *you.* "
            "Clara's hands were still shaking. Thin fingers clutching a lace handkerchief like it could hold back the storm."
    jump choose_next_step




label choose_next_step:
    menu:
        "Inspect the study":
            jump inspect_study
        "Talk to Clara":
            jump talk_to_clara
        "Talk to Lady Imogen":
            jump talk_to_imogen
        "Talk to Mr. Fern":
            jump talk_to_fern
        "Read the letter (if found)":
            if found_letter:
                jump read_letter
            else:
                "You have not found the letter yet."
                jump choose_next_step

label inspect_study:
    scene bg study_night
    with dissolve
    "The door creaked. Even dead, Lord Edevane commanded the room."
    "Oil paintings stared down from the walls. Dust motes hung like ghosts."
    "The body was still there. Slumped forward. Pool of something dark and dry under the desk."
    "No sign of struggle. No broken window. Just that eerie calm that always follows a clean kill."
    "I scan the room."
    menu:
        "Check the desk drawers":
            "The top drawer was locked. Of course it was."
            "The second? Empty, except for a star shaped keychain."
            "Why would he keep a keychain in an empty drawer?"
            "Old. Faded. Covered in cuts like it had stories to tell. Made no sense in his possession. Which meant it mattered. I took it."

            
        "Look at the body":
            "The body did not have any signs of physical assault."
            "Putting my hands on the poor fellow's arm, and on his leg."
            "The muscles are hard as a board."
            "They are in a state of extreme contraction, far exceeding the usual rigor mortis."
            "Coupled with this distortion of the face, this Hippocratic smile, or \'risus sardonicus\', it seems... "
            "death from some powerful vegetable alkaloid"
            "someone probably tried to poison the Lord subtly so that there could be no solid evidence of murder."




        "Check the windows":
            "Window is snibbed on the inner side. The framework is solid.No hinges at the side."
            "I open it. No water pipe near. Roof quite out of reach."
            "I could see some marks on the wall at the bottom, as if something slid down violently."
            "If the door was locked from the inside, and the only person in the room was Lord Edevane, then someone probably used the windows to get here."
            "No solid observation. You plan to look elsewhere."




        "Return to the hall":
            "I think "

            jump choose_next_step


label talk_to_clara:
    "What have you been doing this late in the Lord's room?"
    "Clara: Everynight, I sort the papers Lord read throughout the day in his study. It's a part of my routine."
    "I was about to go sort them as usual, but the door was locked. I decided to come back after half an hour, and it was still locked."
    "I was a little annoyed as it was getting late and I was tired. I asked the Lord if and when I should sort the papers. He did not answer."
    "I tried again, louder. Still no reply."
    "I banged on the door in case the Lord slept, and the bangs were loud enough to wake someone up from a loud slumber."
    "At this point, I was worried, and went to get the security man. They tried the same, and then resorted to breaking the door as there was no sign of Lord on the inside."
    ""

    

label explore_manor:

