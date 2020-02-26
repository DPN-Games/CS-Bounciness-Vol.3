#Variable declaration.

#Characters.
#define varname = Character("name")
define CS = Character("CS188")
define Craptop = Character("Craptop")
define Discord = Character("Discord")
define Nova = Character("Nova")
define CarGuy = Character("Car Guy")
define greeter = Character("Walmart Greeter")
define cashier = Character("Cashier")
define ycs = Character("Young CS")
define ed = Character("Ed")
define rich = Character("Richard")
define wes = Character("Wesley")

#Backgrounds.
#image name = "dir/file.filetype"
image csroom = "background/Cs_bedroom1.jpg"
image csroom_window = "background/Cs_bedroom2.jpg"
image craptop1 = "background/Craptop_error.jpg"
image craptop2 = "background/Craptop_Desktop.png"
image craptop3 = "background/Craptop_Updating.jpg"
image craptop4 = "background/Craptop_Desktop.png"
image cscaroutside = "background/Car_Driveway.jpg"
image cscarinside = "background/Car_Inside.jpg"
image walmartinside = "background/Walmart_Inside.jpg"
image walmartcheckout = "background/Walmart_checkout.jpg"
image walmartoutside = "background/Walmart_Outside.png"
image walmartshelf = "background/Walmart_shelf.jpg"
image cardealer = "background/CarDealer.jpg"
image outside = "background/Cs_house.jpg"
image doorclosed = "background/Door_closed.jpg"
image dooropen = "background/Door_open.jpg"
image factory = "background/Factory.jpg"
image elevator = "background/elevator.jpg"
image helipad = "background/Heli_pad.jpg"
image black = "background/black.jpg"
image office1 = "background/Office_1.jpg"

#Movies.
#image name = "dir/file.filetype"

#Character images.
#image name = "dir/file.filetype"
image csdefault = "characters/csocola_neutral.png"
image cshappy = "characters/csocola_happy.png"
image nova1 = "characters/nova.png"
image carguy = "characters/Carguy_anime.png"
image discord = "characters/discord.png"
image greeter = "characters/walmart CEO.png"
image youngcs = "characters/Csocola_young(chibi).png"
image wesley = "characters/wesley-chan.png"
image edimg = "characters/Ed.png"
image richard = "characters/Richard.png"
image corndog = "characters/CornWorker.png"
image diabeetus = "characters/DiaBeetusWorker.png"
image grrx = "characters/GrrxWorker.png"

label start:
    scene csroom
    
    #$ renpy.movie_cutscene("introHD.ogv")
    
    show csdefault at left

    CS "Welp, time to start up the ol' Craptop."

    scene craptop1
    show csdefault at left
    Craptop "Your PC sux. lol."
    
    scene craptop2
    show csdefault at left
    Character("Sticky Note") "Delete the CS Discord."
    CS "Eh, maybe tomorrow"
    
    scene craptop3
    show csdefault at left
    Craptop "Downloading update 200/13."
    show csdefault at left
    Craptop "Update complete"
    scene craptop4    
    hide csdefault at left
    show cshappy at left
    CS "OoOoOoOoO yes!"
    CS "Time to watch car crash videos for the next couple hours!"
    "Two hours later....."   
    scene csroom
    show csdefault at left
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
    show csdefault at left
    CS "It's pretty nice, but it's got some scratches."
    show carguy at right
    CarGuy "Nooot so nice scratch..."
    CarGuy "You should try Crotch Doctor!"
    hide csdefault
    show csdefault at left
    CS "OH GOD AN ADVERTISER!"
    CS "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    show csdefault at left
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
    greeter "Hello! Welcome to Walmart. Can I help you with anything?"
    CS "Wow! It's Walmart CEO Doug McMillon. You actually work here?"
    greeter "Of course, they were short a greeter today, so I filled the slot."
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
    show CarGuy at right
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
    hide csdefault
    "hey flashback time"
    
    scene csroom with irisin
    show youngcs
    ycs "Hey guys, Young CS here. Today I'm gonna be editing a new craAaAaAaAaAaAazy video!"
    "*keyboard tapping*"
    ycs "Ohhhhhh YeEeEeEeEess! This is lookin' good!"
    hide youngcs

    scene csroom with irisout
    show csdefault at left
    CS "Oh. Flashback over."
    show csdefault at right
    jump needfoundationrepair

label needfoundationrepair:  
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
    show csdefault at left
    CS "Hello! I am CS188, and I-"
    show edimg at right
    ed "Alright, that will be 200 cstars."
    CS "Okay, I guess they already told you what I need done... Lemme get my wallet."
    CS "Here you go. I'll get out of you guys' hair while you work."
    "{i}CS leaves.{/i}"
    hide csdefault
    show edimg
    ed "Come on in guys. CS left."
    show edimg at right
    ed "So now that we're here, what should we do to him?"
    "Ed, Wesley and Richard" "Hmmm..."
    ed "Let's go check his room. We might get some ideas"
    "{i} The three HoH SiS workers go upstairs. {/i}"
    
    scene csroom
    show wesley at right
    wes "Wow, I didn't know CS plays nekopara!"
    show edimg at left
    ed "CS surrrre loves those cute catgirls~ <3"
    show wesley at left
    wes "Alright, but now what should we do?"
    show richard at right
    rich "How about we mess with his laptop?"
    hide richard
    show edimg at left
    ed "Ehh..."
    ed "Alright! Let's get sabotagin'"
    "{i}Ed launches the craptop.{/i}"
    ed "Hehe... He won't know what hit him."
    show wesley at right
    wes "Quick, Let's get out of here before he comes back"
    hide wesley

    scene dooropen
    show wesley at right
    wes "Hurry up!"
    
    scene doorclosed
    "..."
    
    scene outside
    show richard at right
    rich "Lemme call our JoJ UFO."
    show edimg at left
    ed "Ready?"
    "Ed, Wesley and Richard" "I'm beaming up!"
    scene doorclosed
    show csdefault at left
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
    show csdefault at left
    "..."
    scene office1
    show csdefault at left
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
    show csdefault
    "..."
    scene helipad
    show csdefault at left
    show richard at right
    CS "You!"
    rich "Uh-oh."
    CS "You'll pay for what you did!"
    hide richard
    show wesley at right
    wes "Do you want a refund?"
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

    show CS at left
    with easeinleft

    show Wesley at right
    with easeinright
    CS "Take this!"

    "{i}CS punches Wesley and knocks him out.{/i}"

    hide Wesley
    with easeoutright

    CS "That'll teach you not to miss with a nerd's computer!"

    show Ed at right
    with easeinright

    Ed "Hello, 911? My boss just got knocked out by a disgruntled customer and appears to be dying! Send help!"

    CS "Dammit! Ed's calling the police! I gotta go after him!"

    Ed "911! Come quickly! He's chasing after me!"

    "{i}The police arrive and CS runs away.{/i}"

    hide Ed
    with easeoutright

    show Copguy at right
    with easeinright

    Copguy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide CS
    with easeoutleft

    hide Copguy
    with easeoutright

    hide Helipad
    with dissolve

    jump jail

    label chop:

    show CS at left
    with easeinleft

    show Wesley at right
    with easeinright

    CS "Take this!"

    "{i}CS chops Wesley and a fight ensues.{/i}"

    Wesley "You'll pay for that!"

    CS "Like hell I will!"

    hide CS
    with easeoutleft

    hide Wesley
    with easeoutright

    hide Helipad
    with fade

    show Office
    with fade

    show Ed at right
    with easeinright

    Ed "911? Help! My boss just got attacked by a customer and now they're fighting right here in the office!"

    hide Ed
    with easeoutright

    show CS at left
    with easeinleft

    CS "Dammit! Ed's calling the police! I need to finish this fast!"

    "{i}The fight continues and the police arrive.{/i}"

    "{i}CS runs away.{/i}"

    show Copguy at right
    with easeinright

    Copguy "Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he gets caught by the police.{/i}"

    hide CS
    with easeoutleft

    hide Copguy
    with easeoutright

    hide Office
    with dissolve

    jump jail

    label kick:
    $ renpy.movie_cutscene("kick.ogv")
    
    Ed "Hello, 911? My boss just got kicked off of our roof by a disgruntled customer and appears to be dying! Send help!"

    CS "Dammit! Ed's calling the police! I gotta go after him!"

    Ed "911! Come quickly! He's chasing after me!"

    "{i}The police arrive and CS runs away.{/i}"

    hide Ed
    with easeoutright

    show Copguy at right
    with easeinright

    Copguy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide CS
    with easeoutleft

    hide Copguy
    with easeoutright

    hide Helipad
    with dissolve

    jump jail

    label special:

    show CS at left
    with easeinleft

    show Wesley at right
    with easeinright

    CS "Take this!"

    hide CS
    with easeoutleft

    hide Wesley
    with easeoutright

    hide Helipad
    with fade

    show Office
    with fade

    "{i}CS uses the magic of YTP to make Wesley shoot his employees.{/i}"

    show CS at left
    with easeinleft
   
    CS "Dammit! The police are here! They must have heard the gun shots!!"

    "{i}The police arrive and CS runs away.{/i}"

    hide Ed
    with easeoutright

    show Copguy at right
    with easeinright

    Copguy "Hey! Get back here!"

    CS "You can't catch me, I'm the speedy Michael Rosen!"

    "{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

    hide CS
    with easeoutleft

    hide Copguy
    with easeoutright

    hide Helipad
    with dissolve

    jump jail