#Variable declaration.

#Characters.
#define varname = Character("name")
#Character names should be PascalCase.
define CS = Character("CS188")
define Craptop = Character("Craptop")
define CopGuy = Character("Cop Guy")
define Discord = Character("Discord")
define Nova = Character("Nova")
define CarGuy = Character("Car Guy")
define Greeter = Character("Walmart Greeter")
define Cashier = Character("Cashier")
define YCS = Character("Young CS")
define Ed = Character("Ed")
define Rich = Character("Richard")
define Wesley = Character("Wesley")
define Windy = Character("Windyman")
define Arceus = Character("Arceus")
define BorderGuard = Character("Border Guard")

#Backgrounds.
#image name = "dir/file.filetype"
#Image variables should be all lowercase.
image csroom = "background/CS_bedroom1.jpg"
image csroom_window = "background/CS_bedroom2.jpg"
image craptop1 = "background/craptop_error.jpg"
image craptop2 = "background/craptop_desktop.png"
image craptop3 = "background/craptop_updating.jpg"
image craptop4 = "background/craptop_desktop.png"
image cscaroutside = "background/car_driveway.jpg"
image cscarinside = "background/car_inside.jpg"
image walmartinside = "background/walmart_inside.jpg"
image walmartcheckout = "background/walmart_checkout.jpg"
image walmartoutside = "background/walmart_Outside.png"
image walmartshelf = "background/Walmart_shelf.jpg"
image cardealer = "background/car_dealer.jpg"
image outside = "background/CS_house.jpg"
image doorclosed = "background/door_closed.jpg"
image dooropen = "background/door_open.jpg"
image factory = "background/factory.jpg"
image elevator = "background/elevator.jpg"
image helipad = "background/helipad.jpg"
image black = "background/black.jpg"
image office1 = "background/office1.jpg"
image jailcell = "background/jail_cell.jpg"

#Movies.
#image name = "dir/file.filetype"

#Character images.
#image name = "dir/file.filetype"
#Image variables should be all lowercase.
image arceus = "characters/arceus3251.png"
image cs = "characters/csocola_neutral.png"
image cshappy = "characters/csocola_happy.png"
image nova1 = "characters/nova.png"
image carguy = "characters/carguy_anime.png"
image copguy = "characters/copguy.png"
image discord = "characters/discord.png"
image greeter = "characters/walmart_CEO.png"
image youngcs = "characters/csocola_young.png"
image wesley = "characters/wesley.png"
image ed = "characters/ed.png"
image richard = "characters/richard.png"
image corndog = "characters/corn_worker.png"
image diabeetus = "characters/diabeetus_worker.png"
image grrx = "characters/grrx_worker.png"

label start:
    scene csroom
    
    #$ renpy.movie_cutscene("introHD.ogv")
    
    show cs at left

    CS "Welp, time to start up the ol' Craptop."

    scene craptop1
    show cs at left
    Craptop "Your PC sux. lol."
    
    scene craptop2
    show cs at left
    Character("Sticky Note") "Delete the CS Discord."
    CS "Eh, maybe tomorrow"
    
    scene craptop3
    show cs at left
    Craptop "Downloading update 200/13."
    show cs at left
    Craptop "Update complete"
    scene craptop4    
    hide cs at left
    show cshappy at left
    CS "OoOoOoOoO yes!"
    CS "Time to watch car crash videos for the next couple hours!"
    "Two hours later....."   
    scene csroom
    show cs at left
    CS "Okay, what to do now?"
    CS "I could go outside, look at some flowers..."
    
    scene csroom_window
    CS "Oh, look out the window, there's a Michael Rosen!"
    CS "Yeah, let's go outside."
    jump outside

label outside:
    scene outside
    show cshappy at left
    CS "Nice day!"
    CS "Well, I guess it's car time."
    
    scene cscaroutside
    show carguy at right
    CarGuy "*walks up* Nice car!"
    show cs at left
    CS "It's pretty nice, but it's got some scratches."
    show carguy at right
    CarGuy "Nooot so nice scratch..."
    CarGuy "You should try Crotch Doctor!"
    hide cs
    show cs at left
    CS "OH GOD AN ADVERTISER!"
    CS "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    show cs at left
    CS "Whew, that was close."
    CS "Should I go get groceries?"

    menu grocerymenu:
        "Get groceries?"

        "Yes.":
            CS "Yeah, it's a good idea to get some stuff."
            jump walmart
        "No.":
            CS "Screw you, I'm going anyway."
            jump walmart

label walmart:
    scene walmartoutside
    show cshappy at right
    CS "Oh yes, EmployeeExploitationMart is open!"
    "CS walks inside."
    scene walmartinside
    show greeter at right
    Greeter "Hello! Welcome to Walmart. Can I help you with anything?"
    CS "Wow! It's Walmart CEO Doug McMillon. You actually work here?"
    Greeter "Of course, they were short a greeter today, so I filled the slot."
    CS "Wow! He seems like a good man and definitely not a ruthless oligarch who mistreats and underpays employees despite massive profit margins."
    CS "Now, let's find some food."
    
    scene walmartshelf
    show cshappy at left
    CS "*pop* Noice! Genergy is 2 for $5! I'll take them all!"
    CS "Ooh, pringles are on sale too. Yoink!"
    "CS walks to checkout."
    scene walmartcheckout
    CS "Here's my stuff."
    cashier "That'll be $11.88"
    CS "Here you go."
    cashier "Have a good day."
    CS "You too. Bye!"

    scene walmartoutside
    CS "Let's get to the car."
    show carguy at right
    CarGuy "Noooooot so nice scratch."
    CS "Not you again!"
    CS "I gotta get outta here!"
    
    scene cscarinside
    CS "Let's get home before that guy doctors my crotch!"
    "CS drives home and manages to avoid reenacting one of his favorite car crash videos."
    jump homefromwalmart

label homefromwalmart:    
    scene outside
    "CS walks inside and to his room."
    CS "Ahh. It's good to be home!"
    

    scene csroom
    CS "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    "CS walks to his craptop and opens up premiere"
    
    scene craptop4
    CS "Ooh, here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    "CS watches the in-progress video."
    CS "This is pretty good, but I'm feeling uninspired. I don't know where to go from here...."
    CS "I know! I should watch some other YTPs for inspiration."
    "CS opens up youtube and begins watching YTPs. After a while, CS runs into some old YTPs."
    CS "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now......."

    CS "Oh look, a flashback. What a coincidence..."
    hide cs
    "hey flashback time"
    
    scene csroom with irisin
    show youngcs
    YCS "Hey guys, Young CS here. Today I'm gonna be editing a new craAaAaAaAaAaAazy video!"
    "*keyboard tapping*"
    YCS "Ohhhhhh YeEeEeEeEess! This is lookin' good!"
    hide youngcs

    scene csroom with irisout
    show cs at left
    CS "Oh. Flashback over."
    show cs at right
    jump needfoundationrepair

label needfoundationrepair:
    # Put like, a crash sound and a particle effect here.  
    CS "Woah. I was dreaming so long that the foundation fell apart. My house just fell to the side."
    CS "I really need to get some foundation repair."
    CS "Better call HoH SiS!"
    CS "They are really good at giving me the JoJ!"
    CS "{i} Dials 1-800-HOH-SIS{/i}"
    CS "Hello, can you give me the JoJ?"
    Character("HoH SiS Operator") "Is this a prank caller on the line?"
    CS "No! My house really needs foundation repair! I need your help ASAP!"
    "HoH SiS operator" "Alright, that will be 200 CStars. You can pay us afterwards."
    "HoH SiS operator" "{i}hangs up{/i}"
    CS "Well, that is one thing taken care of."
    CS "I guess I'll work on my new YTP while I wait."
    "{i}Time passes and the doorbell rings{/i}"
    CS "Oh! They're here!"
    CS "Lemme go get the door"
    
    scene dooropen
    show cs at left
    CS "Hello! I am CS188, and I-"
    show ed at right
    Ed "Alright, that will be 200 cstars."
    CS "Okay, I guess they already told you what I need done... Lemme get my wallet."
    CS "Here you go. I'll get out of you guys' hair while you work."
    "{i}CS leaves.{/i}"
    hide cs
    show ed
    Ed "Come on in guys. CS left."
    show ed at right
    Ed "So now that we're here, what should we do to him?"
    "Ed, Wesley and Richard" "Hmmm..."
    Ed "Let's go check his room. We might get some ideas"
    "{i} The three HoH SiS workers go upstairs. {/i}"
    
    scene csroom
    show wesley at right
    Wesley "Wow, I didn't know CS plays nekopara!"
    show Ed at left
    Ed "CS surrrre loves those cute catgirls~ <3"
    show wesley at left
    Wesley "Alright, but now what should we do?"
    show richard at right
    rich "How about we mess with his laptop?"
    hide richard
    show Ed at left
    Ed "Ehh..."
    Ed "Alright! Let's get sabotagin'"
    "{i}Ed launches the craptop.{/i}"
    Ed "Hehe... He won't know what hit him."
    show wesley at right
    Wesley "Quick, Let's get out of here before he comes back"
    hide wesley

    scene dooropen
    show wesley at right
    Wesley "Hurry up!"
    
    scene doorclosed
    "..."
    
    scene outside
    show richard at right
    Rich "Lemme call our JoJ UFO."
    show ed at left
    Ed "Ready?"
    "Ed, Wesley and Richard" "I'm beaming up!"
    scene doorclosed
    show cs at left
    CS "Things sure are boooooring around here."
    CS "I should check on the HoH SiS folks. They should be making some progress by now"
    "{i}CS walks into his room.{/i}"
    jump hohsisrevenge

label hohsisrevenge:
    scene csroom
    CS "What!? They're gone?!"
    CS "The house is still on the side, and my computer is messed up!!"
    CS "They set Chocola x Azuki vore art as my desktop background!"
    CS "That image was meant to stay hidden deep in my hard drive!"
    CS "What if CSMom saw that?!"
    CS "I need to go get those guys!"
    CS "I'm gonna go to HoH SiS HQ and show them who's boss!"
    scene cscarinside
    show cs at left
    "..."
    scene office1
    show cs at left
    show corndog at right
    CS "Alright, where are the head JoJites?!"
    "Worker 1" "I don't know!"
    CS "BullShisH!"
    CS "{i}Punches worker.{/i}"
    hide corndog
    show grrx at right
    "Worker 2" "They-- They're on the roof!"
    CS "Good!"
    scene elevator
    show cs
    "..."
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

    hide wesley
    with easeoutright

    CS "That'll teach you not to miss with a nerd's computer!"

    show ed at right
    with easeinright

    Ed "Hello, 911? My boss just got knocked out by a disgruntled customer and appears to be dying! Send help!"

    CS "Dammit! Ed's calling the police! I gotta go after him!"

    Ed "911! Come quickly! He's chasing after me!"

    "{i}The police arrive and CS runs away.{/i}"

    hide Ed
    with easeoutright

    show copguy at right
    with easeinright

    CopGuy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide cs
    with easeoutleft

    hide copguy
    with easeoutright

    hide helipad
    with dissolve

    jump jail

    label chop:

    CS "Take this!"

    "{i}CS chops Wesley and a fight ensues.{/i}"

    Wesley "You'll pay for that!"

    CS "Like hell I will!"

    hide cs
    with easeoutleft

    hide wesley
    with easeoutright

    hide helipad
    with fade

    scene office1
    with fade

    show ed at right
    with easeinright

    Ed "911? Help! My boss just got attacked by a customer and now they're fighting right here in the office!"

    hide ed
    with easeoutright

    show cs at left
    with easeinleft

    CS "Dammit! Ed's calling the police! I need to finish this fast!"

    "{i}The fight continues and the police arrive.{/i}"

    "{i}CS runs away.{/i}"

    show copguy at right
    with easeinright

    CopGuy "Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he gets caught by the police.{/i}"

    hide cs
    with easeoutleft

    hide copguy
    with easeoutright

    hide office1
    with dissolve

    jump jail

    label kick:
    $ renpy.movie_cutscene("kick.ogv")

    hide wesley
    with easeoutright

    show ed at right
    with easeinright
    
    Ed "Hello, 911? My boss just got kicked off of our roof by a disgruntled customer and appears to be dying! Send help!"

    CS "Dammit! Ed's calling the police! I gotta go after him!"

    Ed "911! Come quickly! He's chasing after me!"

    "{i}The police arrive and CS runs away.{/i}"

    hide Ed
    with easeoutright

    show copguy at right
    with easeinright

    CopGuy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide cs
    with easeoutleft

    hide copguy
    with easeoutright

    hide Helipad
    with dissolve

    jump jail

    label special:

    CS "Take this!"

    hide cs
    with easeoutleft

    hide wesley
    with easeoutright

    hide Helipad
    with fade

    scene office1
    with fade

    "{i}CS uses the magic of YTP to make Wesley shoot his employees.{/i}"

    show cs at left
    with easeinleft
   
    CS "Dammit! The police are here! They must have heard the gun shots!!"

    "{i}The police arrive and CS runs away.{/i}"

    hide ed
    with easeoutright

    show copguy at right
    with easeinright

    CopGuy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide cs
    with easeoutleft

    hide copguy
    with easeoutright

    hide office1
    with dissolve

    jump jail

    label jail:

    scene jailcell
    with fade

    show cs at left
    with easeinleft

    show copguy at right
    with easeinright

    CopGuy "Alright, welcome to the slammer. How tough are ya?"
    CS "How tough am I?! How, tough, am, I?! I beat Cuphead!"
    CopGuy "So?"
    CS "In under 90 minutes!"
    CopGuy "Okay! You're tough enough to get your choice of cellmate, which one do you want?"
    menu:

         "Who do you want to be your cellmate?"
         
         "Arceus":
            jump arceuscellmate

         "Windy ":
            jump windycellmate    

    label arceuscellmate:
    CS "I choose Arceus."
    Copguy "Alright, but be warned. This person was arrested for cutting a tax collector with his nose."

    hide copguy
    with easeoutright

    CS "Alrighty then…."
    CS "Hello, Arceus."

    show arceus at center
    with easeintop

    Arceus "Aye, Boss. .w."
    CS "So what are you in for?"
    Arceus "Didn't you hear the cop? \ I'm in for cutting a tax collector with my nose."
    CS "Well, I can see how. Your nose IS big enough."
    Arceus "And from my recent playthrough of CSBounciness, I assume you're in for killing workers at HoHSiS"
    CS "I was 100 percent unsatisfied."
    Arceus "As was I.. As was I.."
    "{i}A brief moment of silence..{/i}"
    Arceus "Welp, I'm bored of this place… Wanna break out? :3"
    CS "Eh.. Sure, why not, I've played plenty of the Escapists, I should be able to figure it out."
    CS "We should break out at least one other person though."
    Arceus "Alright, who do ya wanna break out..?"
    CS "Let's just break out that guy next to us, I think his name was Windy...."
    Arceus "Windy? Eh... He's a bit of a stick in the mud, but sure. He may be of use to us."
    CS "Alright then, let's get going!"

    hide arceus
    with easeoutbottom

    hide cs
    with easeoutleft

    jump breakout

    label windycellmate:
    CS "I choose Windy."
    CopGuy "Okay." 

    hide copguy
    with easeoutright

    CS "Hey Windy ."

    show windy at center
    with easeintop

    Windy "Hey.."
    CS "So what're you in for?"
    Windy "..."
    "{i}Windy  begins to stare longingly at CS…{/i}"
    CS "Well, you don't talk much do you?"
    Windy "Huh, sorry, I got lost in thought.."
    CS "About what?"
    Windy "Breaking out of here.."
    CS "Wow, Am I that bad of a cellmate that you want to breakout as soon as I get here?"
    Windy "No, I've been working with the prisoner in the next cell, Arceus, to breakout for 5 years now."
    CS "Wow, can I come with?"
    Windy "Only if you can figure out a way to escape, we've had no success, as you can tell given that we're still here."
    CS "I think I have some ideas, I've played a LOT of the escapists."
    Windy "Works for me, let's do this!"

    hide cs
    with easeoutleft

    hide Windy 
    with easeoutbottom

    jump breakout


    label breakout:

    show Arceus at center
    with easeintop

    Arceus "So, what's the plan? I've been tryna break outta here for 5 Years."
    CS "Well, for a start. I need to get a feel of the routine here."
    Arceus "Well, I'll quickly describe that for you, cause I can't stand another minute here." 
    "{i}Arceus quickly describes the prison routine to CS.{/i}"
    CS "I think I got all that."
    Arceus "So, what's our plan, Boss?"
    CS "I gotta grab a few plastic spoons from the mess hall, Cup of molten chocolate, a guard outfit, and a change of shorts."
    Arceus "Why a change of shorts?"
    CS "You kidding me? I'm gonna shit myself 'cuz this is scary as hell."
    Arceus "Fair enough."

    hide arceus
    with easeoutbottom

    "{i}The day ends, the next day progresses, CS and Arceus gather the required essentials for their escape. Along the way, they inform Windy , who more than happily complies with the plan.{/i}" 
    "{i}The next evening....{/i}"
    CS "Key, Check."

    show arceus at right
    with easeinright

    Arceus "Uniforms, Check."

    show windy  at left
    with easeinleft

    Windy "Spoons, Check."
    CS "Extra Shorts."
    CS "Check."
    CS "Alright men, let's get the heck out of here!"

    hide arceus
    with easeoutright

    hide windy
    with easeoutleft

    "{i}The plan goes off without a hitch, the three ditch their Prison Outfits, and put on their guard uniforms.{/i}" 
    "{i}In the midst of them changing, Windy  notices CS's butt and compliments it.{/i}"

    show windy at right
    with easeinright

    Windy "CS.. Nice Ass.."
    CS "Thank you."

    show arceus at left
    with easeinleft

    Arceus "Save it for later, love birds." 

    hide arceus
    with easeoutleft

    hide windy
    with easeoutright

    "{i}The Three dig their way out of the cell and make a break into the dark of the evening.{/i}"
    CS "Jeez.. I didn't think that would actually work."

    show arceus at right
    with easeinright

    Arceus "You what?" 

    show windy at left
    with easeinleft

    Windy "Hey, CS.. You looked sexy runnin’ outta that prison.."
    CS "{i}Blush{/i}  Thank you.."
    Arceus "Guys, save this for when we're all safe, we need to get a car and get over the border."
    Windy "How are we supposed to cross the border with the new wall?"
    Arceus "Not the Mexican border, the Canadian border, we're in New York, it's way closer and they're too polite to send us back."
    CS "Works for me, free healthcare."
    Arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."

    hide arceus
    with easeoutright

    hide windy
    with easeoutleft

    hide jailcell
    with dissolve

    jump bordercrossing

    label bordercrossing:

    show border
    with fade

    "{i}CS, Windy , and Arceus get to the border crossing.{/i}"
    "{i}A border guard appears.{/i}"

    show borderguard at center
    with easeintop

    BorderGuard "I'm going to need proof of citizenship, eh."

    show arceus at right
    with easeinright

    Arceus "Colour is spelled with a u, eh."
    BorderGuard "Works for me, eh."

    hide BorderGuard
    with easeoutbottom

    hide arceus
    with easeoutright

    CS "Now that we're over the border and can breathe easy, I wanted to ask you something Windy ."

    show windy at center
    with easeintop

    Windy "Yeah?"
    CS "You made a couple passes at me on the trip to here. Was there anything behind that or were you just joking around?"
    Windy "Which one would you prefer?"
    CS "The former, I mean, I've been single for a while, so I'll take what I can get."
    Windy "Well, I suppose I have good news for you then…."

    hide windy
    with easeoutbottom

    show windy at left
    with easeinleft

    show arceus at right
    with easeinright

    Arceus "Are you lovebirds hungry? I'm gonna stop for food at Tim Horton's."

    hide arceus
    with easeoutright

    hide windy
    with easeoutleft

    hide border
    with fade

    show uutsidehortons
    with fade

    "{i}At the Tim Horton's, Windy and CS share a donut. After they finish the donut, Windy steals a kiss.{/i}"

    hide outsidehortons
    with dissolve

    show insidehortons
    with fade

    CS "Wow, that was great!"
    "{i}Windy blushes..{/i}"

    show windy at center
    with easeintop

    Windy "Thanks…."
    CS "Oh, I was talking about the donut but the kiss was good too."
    CS "About 88 percent as good as the donut."
    Windy "I'll take it."

    hide windy
    with easeoutbottom

    show windy at left
    with easeinleft

    show arceus at right
    with easeinright

    Arceus "Sorry to interrupt you two, but we may have a problem, that donut cost me the last of my money, so we need to find a way to make some cash."
    "{i}CS looks across the street to see Linus Media Group.{/i}"

    hide Arceus
    with easeoutright

    hide windy
    with easeoutleft

    CS "I have a lot of video editing experience, maybe I can get a joj... er, a job there."
    "{i}CS walks into the studio and asks for a job.{/i}"

    show linusoffice
    with fade

    show linus at center
    with easeintop

    Linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
    CS "Colour is spelled with a u, eh."
    Linus "I need actual papers. The last time I hired someone who used that as proof of citizenship, I got fined and had to sell one of my 1000s of GTX Titans."
    CS "Ummmm..... I'll be right back."

    hide linus
    with easeoutbottom

    hide linusoffice
    with dissolve

    "{i}CS leaves and talks to Windy .{/i}"
    show insidehortons

    show Windy at center
    with easeintop

    CS "I need to get proof of citizenship, or at least fake proof of citizenship before I can get a joj here."
    "{i}Windy gets an idea and begins to blush.{/i}"
    Windy "Trudeau is trying to make Canada more diverse by letting gay married couples get citizenship, we just have to get married and then you can work here."
    CS "We don't have the money to get married!"
    Windy "We can have a cheap wedding at one of your Canadian fan's houses."
    CS "Well, I know Nova lives around here, so we can have the wedding at his house."

    hide windy
    with easeoutbottom

    hide insidehortons
    with dissolve

    jump wedding

    label wedding:

    show weddingscene
    with fade

    show cs at left
    with easeinleft

    show windy at right
    with easeinright

    show fatherdigbick at center
    with easeintop

    FatherDigBick "Do you, Windyman, take NAME REDACTED to be your lawfully wedded husband?"
    Windy  "I do."
    FatherDigBick "And do you, NAME REDACTED, take Windyman to be your lawfully wedded husband?"
    CS "I do."

    hide cs
    with easeoutleft

    hide windy
    with easeoutright

    hide fatherdigbick
    with easeoutbottom

    jump trueend

    hide weddingscene

    hide helipad

    jump trueend