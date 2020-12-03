label start_edittechquickie: 
    
    CS "{i}Dammit Teran, you can edit your own macro fetish content.{/i}"
    CS "I guess I'll edit the livestreaming one."
    "{i}CS starts working on editing the TechQuickie video and Linus comes in to check on him.{/i}"

    show linus at right with dissolve

    Linus "Hey CS, how's the new video coming along?"
    CS "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."
    Linus "Wow! You're a fast worker, you'll get off of those old 2080s in no time."
    CS "Thanks Linus."
    Linus "Speaking of livestreaming, we need a new PC for the WAN Show, can you go and buy parts for one?"
    CS "Sure, what parts do you need?"
    Linus "We need eggs, milk..."
    Linus "Just kidding."
    Linus "I'll leave the details up to you since you've done a lot of livestreaming, just get the highest end available."
    CS "Alright, I'll go get the parts from the warehouse..."
    # Jumpcut, fade to black
    CS "I have your new streaming PC, it runs quite well too! Way better than my computer!"
    Linus "Awesome! Lemme go move this into the othe-- WOAAAHHH!!!"
    "{i}Linus trips and falls, immediately destroying the insides and outsides of the PC that CS just built.{/i}"
    CS "Oh damn, you okay there?"
    Linus "No of course not! I just destroyed _another _one of these $20,000 computing machines! How the hell am I going to get another just like this?"    
    CS "Well, you could just always buy more parts like these, I’m sure you have the budget for that."
    Linus "No no, that’s too expensive and wasteful, let me think…"
    Linus "Hmmm….."
    LInus "Wait! I just got a brilliant idea! Why don’t you go buy more parts for me, we certainly have the budget to do that!"
    CS "Uhmm… I literally just said--"
    Linus "Alright! The plan is settled! You can go fetch me some more parts for the ultimate streaming machine, and you get to decide what parts should belong in the computer!"
    CS "Okay but, are there any recommendations you would give me for building this? This is YOUR money, you know."
    Linus "Nah, it’s fine. I’m sure you will do well picking out parts, make sure to get the highest quality you can!"
    CS "Alrighty, I’ll get going now."
    "{i}CS goes to Microcenter.{/i}"
    CS "Okay gamers, we are buying some parts for our epic computing machine. Let's go inside the magical concrete structure to buy some computing parts."
    S "{i}Wow, this building looks a lot bigger than the places I would go shopping at near home.{/i}"
    "{i}CS enters the building.{/i}"
    CS "Woah! This place is huge!"
    CS "There are so many options to pick from! And I have as much money as I’ll ever need too!"
    CS "Before I get too carried away though, I should probably start by buying the processor."
    "{i}CS goes to the CPU aisle.{/i}"
    CS "My goodness, there are so many options."
    CS "I honestly don’t know which one to pick."
    CS "Let’s see here…"
    CS "I could get a super high-end Intel CPU since Linus still seems to default to Intel even after shilling for AMD…"
    CS "Or I could get a Threadripper, more cores would probably be better for streaming..."
    CS "Too many good options! I don’t know what one to pick!"
    CS "Whatever, I’ll get {i}whatever choice since this doesn’t change the path{/i}"
    CS "Now for the GPU."

    menu:
        "\"Get a low end card?\""

        "Yes":
            low_end_card = True

        "No":
            low_end_card = False


    if (low_end_card == True):
        pass

    CS "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he’s not actually that rich."
    "{i}CS flags down an employee.{/i}"
    CS "I’m trying to get a graphics card, and I want to save money, what do you have?"
    Worker "Everything here is pretty expensive, lemme check the back…"
    "{i}The worker comes back.{/i}"
    Worker "Alright, I got this. It’s pretty old, and it’s covered in dust, but it’s like $50."
    CS "Sounds great, I’ll take it."