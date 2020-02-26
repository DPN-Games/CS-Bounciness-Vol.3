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

#Movies.
#image name = "dir/file.filetype"

#Character images.
#image name = "dir/file.filetype"
image csdefault = "characters/csocola_neutral.png"
image cshappy = "characters/csocola_happy.png"
image nova1 = "characters/nova.png"
image carguy = "characters/Carguy_anime.png"
image discord = "characters/discord.png"

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
    show text "Two hours later....." at truecenter   
    scene csroom
    show csdefault at left
    CS "Okay, what to do now?"
    CS "I could go outside, look at some flowers..."
    
    scene csroom_window
    show csdefault
    CS "Oh, look out the window, there's a Michael Rosen!"
    CS "Yeah, let's go outside."
    
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
        "No.":
            CS "Screw you, I'm going anyway."

    scene walmartoutside
    show cshappy at right
    CS "Oh yes, EmployeeExploitationMart is open!"
    
    show text "CS walks inside."
    scene walmartinside
    show greeter at right
    greeter "Hello! Welcome to Walmart. Can I help you with anything?"
    CS "Wow! It's Walmart CEO Doug McMillon. You actually work here?"
    greeter "Of course, they were short a greeter today, so I filled the slot."
    CS "Wow! He seems like a good man and definitely not a ruthless oligarch who mistreats and underpays employees despite massive profit margins."
    CS "Now, let's find some food."
    
    scene walmartshelf
    show csdefault at left
    CS "*pop* Noice! Genergy is 2 for $5! I'll take them all!"
    CS "Ooh, pringles are on sale too. Yoink!"
    show text "CS walks to checkout."
    scene walmartcheckout
    CS "Here's my stuff."
    cashier "That'll be $11.88"
    CS "Here you go."
    cashier "Have a good day."
    CS "You too. Bye!"

    scene walmartoutside
    CS "Let's get to the car."
    
    scene cscarinside
    CS "Let's get home"
