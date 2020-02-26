#Variable declaration.

#Characters.
#define varname = Character("name")
define CS = Character("CS188")
define Craptop = Character("Craptop")
define Discord = Character("Discord")
define Nova = Character("Nova")
define CarGuy = Character("Car Guy")
#Backgrounds.
#image name = "dir/file.filetype"

#Movies.
#image name = "dir/file.filetype"

#Character images.
#image name = "dir/file.filetype"
image csdefault = "characters/Cshocola.png"
image cshappy = "characters/csocola_happy.png"
image csscared = "characters/cs-ocola suprised.png"
image nova1 = "characters/Anime nova.png"
image carguy = "characters/Carguy_anime.png"
image discord = "characters/discord.png"

label start:
    scene csroom
    
    $ renpy.movie_cutscene("introHD.ogv")
    
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
    hide csdefault at left
    show cshappy at left
    CS "OoOoOoOoO yes!"
    hide cshappy
    show csdefault at left
    #full windows sound
    Craptop "{i}please end my suffering{/i}"
    CS "no"
    scene craptop
    scene craptop4
    show csdefault at left
    CS "Hey guys!"
    scene craptop2
    show discord
    Discord "Hihihihihihihihihihi"
    hide discord
    show csdefault at left
    CS "Okay bedtime! Bye guys!"
    hide csdefault
    show nova1 at right
    Nova "But it's like 8:04AM and you just woke up."
    hide nova1
    show csdefault at left
    CS "Bye!"
    hide csdefault

    scene craptop4
    show discord
    Discord "CS188 is now offline."
    hide discord
    show nova1 
    Nova "k bye"

    scene csroom
    show csdefault at left
    CS "Okay, what to do now?"
    CS "I could go outside, look at some flowers..."
    
    scene csroom_window
    show csscared
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
    show csscared at left
    CS "OH GOD AN ADVERTISER!"
    CS "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    show csdefault at left
    CS "Whew, that was close."
    CS "Should I go get groceries?"