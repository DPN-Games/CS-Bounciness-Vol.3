label csb1_start:
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
    CS "Eh, maybe tomorrow."
    
    scene craptop3
    show cs at left
    Craptop "Downloading update 200/13."
    show cs at left
    Craptop "Update complete."
    scene craptop4    
    hide cs at left
    show cshappy at left
    CS "OoOoOoOoO yes!"
    CS "Time to watch car crash videos for the next couple hours!"
    "Two hours later..."   
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
    define Greeter = Character("Doug")
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
    Cashier "That'll be $11.88."
    CS "Here you go."
    Cashier "Have a good day."
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
    "CS walks to his craptop and opens up Premiere."
    
    scene craptop4
    CS "Ooh, here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    "CS watches the in-progress video."
    CS "This is pretty good, but I'm feeling uninspired. I don't know where to go from here..."
    CS "I know! I should watch some other YTPs for inspiration."
    "CS opens up youtube and begins watching YTPs. After a while, CS runs into some old YTPs."
    CS "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now......"

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
    # TODO: Put like, a crash sound and a particle effect here.  
    CS "Woah. I was dreaming so long that the foundation fell apart. My house just fell to the side."
    CS "I really need to get some foundation repair."
    CS "Better call HoH SiS!"
    CS "They are really good at giving me the JoJ!"
    CS "{i} Dials 1-800-HOH-SIS{/i}"
    CS "Hello, can you give me the JoJ?"
    Character("HoH SiS Operator") "Is this a prank caller on the line?"
    CS "No! My house really needs foundation repair! I need your help ASAP!"
    "HoH SiS operator" "Alright, that will be 200,000 Embers. You can pay us afterwards."
    "HoH SiS operator" "{i}hangs up{/i}"
    CS "Well, that is one thing taken care of."
    CS "I guess I'll work on my new YTP while I wait."
    "{i}Time passes, and the doorbell rings.{/i}"
    CS "Oh! They're here!"
    CS "Lemme go get the door."
    
    scene dooropen
    show cs at left
    CS "Hello! I am CS188, and I-"
    show ed at right
    Ed "Alright, that will be 200,000 Embers."
    CS "Okay, I guess they already told you what I need done... lemme get my wallet."
    CS "Here you go. I'll get out of you guys' hair while you work."
    "{i}CS leaves.{/i}"
    hide cs
    show ed
    Ed "Come on in, guys. CS left."
    show ed at right
    Ed "So now that we're here, what should we do to him?"
    "Ed, Wesley and Richard" "Hmmm..."
    Ed "Let's go check his room. We might get some ideas."
    "{i} The three HoH SiS workers go upstairs. {/i}"
    
    scene csroom
    show wesley at right
    Wesley "Wow, I didn't know CS plays Nekopara!"
    show ed at left
    Ed "CS surrrre loves those cute catgirls~ <3"
    show wesley at left
    Wesley "Alright, but now what should we do?"
    show richard at right
    Rich "How about we mess with his laptop?"
    hide richard
    show ed at left
    Ed "Ehh..."
    Ed "Alright! Let's get sabotagin'!"
    "{i}Ed launches the craptop.{/i}"
    Ed "Hehe... He won't know what hit him."
    show wesley at right
    Wesley "Quick, Let's get out of here before he comes back!"
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
    Character("Ed, Wesley and Richard") "I'm beaming up!"
    scene doorclosed
    show cs at left
    CS "Things sure are boooooring around here."
    CS "I should check on the HoH SiS folks. They should be making some progress by now."
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
    Character("Worker 1") "I don't know!"
    CS "BullShisH!"
    CS "{i}Punches worker.{/i}"
    hide corndog
    show grrx at right
    Character("Worker 2") "They-- They're on the roof!"
    CS "Good!"
    scene elevator
    show cs
    "..."