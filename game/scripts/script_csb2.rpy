label csb2_start:
    scene helipad
    show cs at left
    show richard at right
    
    CS "You!"
    Rich "Uh-oh."
    CS "You'll pay for what you did!"
    
    hide richard
    show wesley at right
    
    Wesley "Do you want a refund?"
    CS "I'll refund your face to the floor!"

    menu:
        "What attack would you like to use?"

        "Use Punch":
            jump punch

        "Use Chop":
            jump chop

        "Use Kick":
            jump kick
        
        "Use Special":
            jump special    

    label punch:
        CS "Take this!"
        "{i}CS punches Wesley and knocks him out.{/i}"

        hide wesley with easeoutright

        CS "That'll teach you not to mess with a nerd's computer!"

        show ed at right with easeinright

        Ed "Hello, 911? My boss just got knocked out by a disgruntled customer and appears to be dying! Send help!"
        CS "Dammit! Ed's calling the police! I gotta go after him!"
        Ed "911! Come quickly! He's chasing after me!"

        jump beforejail

    label chop:
        CS "Take this!"
        "{i}CS chops Wesley and a fight ensues.{/i}"
        Wesley "You'll pay for that!"
        CS "Like hell I will!"

        hide cs with easeoutleft
        hide wesley with easeoutright
        hide helipad with fade
        scene office1 with fade
        show ed at right with easeinright

        Ed "911? Help! My boss just got attacked by a customer and now they're fighting right here in the office!"

        hide ed with easeoutright
        show cs at left with easeinleft

        CS "Dammit! Ed's calling the police! I need to finish this fast!"
        "{i}The fight continues.{/i}"

        jump beforejail

    label kick:
        $ renpy.movie_cutscene("kick.ogv")

        hide wesley with easeoutright
        show ed at right with easeinright
        
        Ed "Hello, 911? My boss just got kicked off of our roof by a disgruntled customer and appears to be dying! Send help!"
        CS "Dammit! Ed's calling the police! I gotta go after him!"
        Ed "911! Come quickly! He's chasing after me!"

        jump beforejail

    label special:
        CS "Take this!"

        hide cs with easeoutleft
        hide wesley with easeoutright
        hide helipad with fade
        scene office1 with fade

        "{i}CS uses the magic of YTP to make Wesley shoot his employees.{/i}"

        show cs at left with easeinleft
    
        CS "Dammit! The police are here! They must have heard the gun shots!"

        jump beforejail

label beforejail:
        "{i}The police arrive and CS runs away.{/i}"

        hide ed with easeoutright
        show copguy at right with easeinright

        CopGuy "Hey! Get back here!"
        CS "You can't catch me, I'm the speedy Michael Rosen!"
        "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

        hide cs with easeoutleft
        hide copguy with easeoutright
        hide office1 with dissolve
        jump jail

label jail:
    scene jailinside with fade #TODO jail_inside is too big
    show cs at left with easeinleft
    show copguy at right with easeinright

    CopGuy "Alright, welcome to the slammer. How tough are ya?"
    CS "How tough am I?! How, tough, am, I?! I beat Cuphead!"
    CopGuy "So?"
    CS "In under 90 minutes!"
    CopGuy "Okay! You're tough enough to get your choice of cellmate, which one do you want?"

    menu:
         "Who do you want to be your cellmate?"
         
         "Arceus":
            jump arceuscellmate

         "Windy":
            jump windycellmate    

label arceuscellmate:
    CS "I choose Arceus."
    CopGuy "Alright, but be warned. This person was arrested for cutting a tax collector with his nose."

    hide copguy with easeoutright

    CS "Alrighty then..."
    CS "Hello, Arceus."

    show arceus at center with easeintop

    Arceus "Aye, Boss. .w."
    CS "So what are you in for?"
    Arceus "Didn't you hear the cop? \ I'm in for cutting a tax collector with my nose."
    CS "Well, I can see how. Your nose IS big enough."
    Arceus "And from my recent playthrough of CSBounciness, I assume you're in for killing workers at HoHSiS."
    CS "I was 100 percent unsatisfied."
    Arceus "As was I. As was I..."
    "{i}A brief moment of silence...{/i}"
    Arceus "Welp, I'm bored of this place... Wanna break out? :3"
    CS "Eh.. Sure, why not, I've played plenty of the Escapists, I should be able to figure it out."
    CS "We should break out at least one other person though."
    Arceus "Alright, who do ya wanna break out...?"
    CS "Let's just break out that guy next to us, I think his name was Windy..."
    Arceus "Windy? Eh... I mean,  he can drive a mean car... sure, he may be of use to us."
    CS "Alright then, let's get going!"

    hide arceus with easeoutbottom
    hide cs with easeoutleft
    jump breakout

label windycellmate:
    CS "I choose Windy."
    CopGuy "Okay." 

    hide copguy with easeoutright

    CS "Hey Windy."

    show windy at center with easeintop

    Windy "Hey..."
    CS "So what're you in for?"
    Windy "..."
    "{i}Windy  begins to stare longingly at CS...{/i}"
    CS "Well, you don't talk much do you?"
    Windy "Huh, sorry, I got lost in thought..."
    CS "About what?"
    Windy "Breaking out of here..."
    CS "Wow, Am I that bad of a cellmate that you want to breakout as soon as I get here?"
    Windy "No, I've been working with the prisoner in the next cell, Arceus, to breakout for 5 years now."
    CS "Wow, can I come with?"
    Windy "Only if you can figure out a way to escape, we've had no success, as you can tell given that we're still here."
    CS "I think I have some ideas, I've played a LOT of the escapists."
    Windy "Works for me, let's do this!"

    hide cs with easeoutleft
    hide windy  with easeoutbottom
    jump breakout


label breakout:
    show arceus at center with easeintop

    Arceus "So, what's the plan? I've been tryna break outta here for 5 years."
    CS "Well, for a start. I need to get a feel of the routine here."
    Arceus "Well, I'll quickly describe that for you, cause I can't stand another minute here." 
    "{i}Arceus quickly describes the prison routine to CS.{/i}"
    CS "I think I got all that."
    Arceus "So, what's our plan, Boss?"
    CS "I gotta grab a few plastic spoons from the mess hall, Cup of molten chocolate, a guard outfit, and a change of shorts."
    Arceus "Why a change of shorts?"
    CS "You kidding me? I'm gonna shit myself 'cuz this is scary as hell."
    Arceus "Fair enough."

    hide arceus with easeoutbottom

    "{i}The day ends, the next day progresses, CS and Arceus gather the required essentials for their escape. Along the way, they inform Windy, who more than happily complies with the plan.{/i}" 
    "{i}The next evening...{/i}"
    CS "Key, check."

    show arceus at right with easeinright

    Arceus "Uniforms, check."

    show windy  at left with easeinleft

    Windy "Spoons, check."
    CS "Extra shorts..."
    CS "Check."
    CS "Alright men, let's get the heck out of here!"

    hide arceus with easeoutright
    hide windy with easeoutleft

    "{i}The plan goes off without a hitch, the three ditch their prison outfits, and put on their guard uniforms.{/i}" 
    "{i}In the midst of them changing, Windy notices CS's butt and compliments it.{/i}"

    show windy at right with easeinright

    Windy "CS... Nice Ass..."
    CS "Thank you."

    show arceus at left with easeinleft

    Arceus "Save it for later, love birds." 

    hide arceus with easeoutleft
    hide windy with easeoutright

    "{i}The three dig their way out of the cell and make a break into the dark of the evening.{/i}"
    CS "Jeez... I didn't think that would actually work."

    show arceus at right with easeinright

    Arceus "You what?" 

    show windy at left with easeinleft

    Windy "Hey, CS... You looked sexy runnin’ outta that prison..."
    "{i}CS blushes.{/i} "
    CS "Thank you..."
    Arceus "Guys, save this for when we're all safe, we need to get a car and get over the border."
    Windy "How are we supposed to cross the border with the new wall?"
    Arceus "Not the Mexican border, the Canadian border, we're in New York, it's way closer and they're too polite to send us back."
    CS "Works for me, free healthcare."
    Arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."

    hide arceus with easeoutright
    hide windy with easeoutleft
    hide jailcell with dissolve
    jump bordercrossing

label bordercrossing:
    scene border with fade

    "{i}CS, Windy, and Arceus get to the border crossing.{/i}"
    "{i}A border guard appears.{/i}"

    show borderguard at center with easeintop

    BorderGuard "I'm going to need proof of citizenship, eh."

    show arceus at right with easeinright

    Arceus "Colour is spelled with a u, eh."
    BorderGuard "Works for me, eh."

    hide borderguard with easeoutbottom
    hide arceus with easeoutright

    CS "Now that we're over the border and can breathe easy, I wanted to ask you something Windy."

    show windy at center with easeintop

    Windy "Yeah?"
    CS "You made a couple passes at me on the trip to here. Was there anything behind that or were you just joking around?"
    Windy "Which one would you prefer?"
    CS "The former, I mean, I've been single for a while, so I'll take what I can get."
    Windy "Well, I suppose I have good news for you then..."

    hide windy with easeoutbottom
    show windy at left with easeinleft
    show arceus at right with easeinright

    Arceus "Are you lovebirds hungry? I'm gonna stop for food at Tim Horton's."

    hide arceus with easeoutright
    hide windy with easeoutleft
    hide border with fade
    show outsidehortons with fade

    "{i}At the Tim Horton's, Windy and CS share a donut. After they finish the donut, Windy steals a kiss.{/i}"

    hide outsidehortons with dissolve
    show insidehortons with fade

    CS "Wow, that was great!"
    "{i}Windy blushes...{/i}"

    show windy at center with easeintop

    Windy "Thanks..."
    CS "Oh, I was talking about the donut but the kiss was good too."
    CS "About 88 percent as good as the donut."
    Windy "I'll take it."

    hide windy with easeoutbottom
    show windy at left with easeinleft
    show arceus at right with easeinright

    Arceus "Sorry to interrupt you two, but we may have a problem, that donut cost me the last of my money, so we need to find a way to make some cash."
    "{i}CS looks across the street to see Linus Media Group.{/i}"

    hide arceus with easeoutright
    hide windy with easeoutleft

    CS "I have a lot of video editing experience, maybe I can get a joj... er, a job there."
    "{i}CS walks into the studio and asks for a job.{/i}"

    show linusoffice with fade
    show linus at center with easeintop

    Linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
    CS "Colour is spelled with a u, eh."
    Linus "I need actual papers. The last time I hired someone who used that as proof of citizenship, I got fined and had to sell one of my thousands of GTX Titans."
    CS "Ummmm... I'll be right back."

    hide linus with easeoutbottom
    hide linusoffice with dissolve

    "{i}CS leaves and talks to Windy.{/i}"
    show insidehort
    show windy at center with easeintop

    CS "I need to get proof of citizenship, or at least fake proof of citizenship before I can get a joj here."
    "{i}Windy gets an idea and begins to blush.{/i}"
    Windy "Trudeau is trying to make Canada more diverse by letting gay married couples get citizenship, we just have to get married and then you can work here."
    CS "We don't have the money to get married!"
    Windy "We can have a cheap wedding at one of your Canadian fan's houses."
    CS "Well, I know Nova lives around here, so we can have the wedding at their house."  # Switched this to "their", no one should question that.

    hide windy with easeoutbottom
    hide insidehortons with dissolve
    jump wedding

label wedding:
    show weddingscene with fade
    show cs at left with easeinleft
    show windy at right with easeinright
    show fatherdigbick at center with easeintop

    # TODO: Glitch text formatting on the NAME REDACTEDs.

    FatherDigBick "Do you, Windyman, take NAME REDACTED to be your lawfully wedded husband?"
    Windy  "I do."
    FatherDigBick "And do you, NAME REDACTED, take Windyman to be your lawfully wedded husband?"
    CS "I do."

    hide cs with easeoutleft
    hide windy with easeoutright
    hide fatherdigbick with easeoutbottom
    hide weddingscene
    hide helipad

    # jump trueend