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
        "Look around the manor":
            jump explore_manor

label inspect_study:
    scene bg study_night
    with dissolve
    "The door creaked. Even dead, Lord Edevane commanded the room."
    "Oil paintings stared down from the walls. Dust motes hung like ghosts."
    "The body was still there. Slumped forward. Pool of something dark and dry under the desk."
    "No sign of struggle. No broken window. Just that eerie calm that always follows a clean kill."
    "I scanned the room."
    menu:
        "Check the desk drawers":
            "The top drawer was locked. Of course it was."
            "The second? Empty, except for an old key and a folded letter."

            
        "Look at the body":
            "The body did not have any signs of physical assault."
            "Putting my hands on the poor fellow's arm, and on his leg."
            "The muscles are hard as a board."
            "They are in a state of extreme contraction, far exceeding the usual rigor mortis."
            "Coupled with this distortion of the face, this Hippocratic smile, or \'risus sardonicus\', it seems... "
            "death from some powerful vegetable alkaloid"
            "some"




        "Check the windows":
            "Window is snibbed on the inner side. The framework is solid.No hinges at the side."
            "I open it. No water pipe near. Roof quite out of reach."
            "I could see some marks on the wall at the bottom, as if something slid down violently."
            "If the door was locked from the inside, and the only person in the room was Lord Edevane, then someone probably used the windows to get here."




        "Return to the hall":

            jump choose_next_step
default found_letter = False


label talk_to_clara:


    

label explore_manor:

