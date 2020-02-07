###################################
#CS Declarations
###################################
define CS = Character("CS188")
define CSPhone = Character("CS188")
define CSInsane = Character("CS188")
define CSSurprised = Character("CS188")
define CSHappy = Character("CS188")
define CSThink = Character("CS188")
define CSYoung = Character("CS188")
image CS = "characters/CSocola_Neutral.png"
image CSPhone = "characters/CshocolaPhone.png"
image CSInsane = "characters/Cs-ocolaInsane.png"
image CSSurprised = "characters/Cs-ocolasuprised.png"
image CSHappy = "characters/CSocola_Happy.png"
image CSDisappointed = "characters/CSocola_Disappointed"
image CSThink = "characters/CSocola_Worried.png"
image CSYoung = "characters/CsocolaYoung.png"
image CSGuard = "characters/CSgod-ocola.png"
###################################
#CS Declarations
###################################




###################################
#Character Declarations
###################################
define Anno = Character("Anno")
image Anno = "characters/Anno.png"

define Linus = Character("Linus")
image Linus = "characters/Linus.png"

define FatherDigBick = Character("Father Bick")
image FatherDigBick = "characters/Digbick.png"
###################################
#Character Declarations
###################################




###################################
#Background Declarations
###################################
image Black = "background/black.jpg"
image LinusOffice = "background/the-linus-group-office.jpg"
image InsideHortons = "background/inside-tim-hortons.jpg"
image WeddingScene = "background/Wedding.jpg"
image LinusOfficeOutside = "background/linusofficeoutside.jpeg"
image CSDesk = "background/CSDesk.jpeg"
image Microcenter = "background/microcenter.png"
image LinusHallway = "background/LinusHallway.jpg"
###################################
#Background Declarations
###################################

###################################
#Background Declarations
###################################
define fastdissolve = Dissolve(.3)
###################################
#Background Declarations
###################################


###################################
#Game Start
###################################

label start:

"{i}Last time on CS Bounciness...{/i}"

show LinusOfficeOutside with fade

"{i}CS looks across the street to see Linus Media Group.{/i}"

CS "I have a lot of video editing experience, maybe I can get a joj there."
"{i}CS walks into the studio and asks for a job.{/i}"

show LinusOffice with fade

show Linus at center with fastdissolve

Linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
CS "Colour is spelled with a u, eh."
Linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my 1000s of GTX Titans."
CS "Ummmm, I'll be right back."

hide Linus with fastdissolve

hide LinusOffice with dissolve

"{i}CS leaves and talks to Anno.{/i}"
show InsideHortons with fade

show Anno at center with fastdissolve

CS "I need to get proof of citizenship, or at least fake proof of citizenship before I can get a joj here."
"{i}Anno gets an idea and begins to blush.{/i}"
Anno "Trudeau is trying to make Canada more diverse by letting gay married couples get citizenship, we just have to get married and then you can work here."
CS "We don't have the money to get married!"
Anno "We can have a cheap wedding at one of your Canadian fan's houses."
CS "Well, I know Nova lives around here, so we can have the wedding at his house."

hide Anno with fastdissolve

hide InsideHortons with dissolve

show WeddingScene with fade

show CS at left with fastdissolve

show Anno at right with fastdissolve

show FatherDigBick at center with fastdissolve

FatherDigBick "Do you, Anno, take NAME REDACTED to be your lawfully wedded husband?"
Anno "I do."
FatherDigBick "And do you, NAME REDACTED, take Anno, to be your lawfully wedded husband?"
CS "I do."

hide CS with fastdissolve

hide Anno with fastdissolve

hide FatherDigBick with fastdissolve

hide WeddingScene with fade

show LinusOffice with fade

show CS at left with fastdissolve

show Linus at right with fastdissolve

CS "Okay Linus, I got my proof of citizenship."

Linus "Okay, you can start tomorrow. Sorry to make you get that, but I need my GTX Titans, eh."

CS "It's okay, I get it. Thanks for the job, I'll see you tommorow."

hide Linus with fastdissolve

hide CS with fastdissolve

hide LinusOffice with dissolve

show LinusHallway with dissolve

show CS at left with fastdissolve

show Linus at right with fastdissolve

Linus "Welcome to Linus Media Group, come on in, I'll show you your desk."

CS "Thanks Linus."

hide CS with fastdissolve

hide Linus with fastdissolve

hide LinusHallway with dissolve

show CSDesk with fade

show CS at left with fastdissolve

show Linus at right with fastdissolve

CS "Wow! I thought this was an office, why do I get such a cool desk?"

Linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."

CS "Holy shit, really? This is way better than any setup I've seen, let alone had."

Linus "You must've had really bad setups then, this only has 2080s, everyone else has 2080 TIs or GTX Titans."

CS "I have absolutely no problem with 2080s."

Linus "Well, enjoy!"

hide Linus with fastdissolve

CS "I guess I better get to work on editing, let's see what videos I need to edit..."

CS "Let's see, I have the new TechQuickie video on how livestreaming works, or the video on how at least half of the keys on your keyboard should be macros..."

CS "{i}Dammit Teran, you can edit your own macro fetish content.{/i}"

CS "I guess I'll edit the livestreaming one."

"{i}CS starts working on editing the TechQuickie video and Linus comes in to check on him.{/i}"

show Linus at right with fastdissolve

Linus "Hey CS, how's the new video coming along?"

CS "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."

Linus "Wow! You're a fast worker, you'll get off of those old 2080s in no time."

CS "Thanks Linus."

Linus "Speaking of livestreaming, we need a new PC for the WAN Show, can you go and buy parts for one?"

CS "Sure, what parts do you need?"

Linus "We need eggs, milk..."

Linus "Just kidding."

Linus "I'll leave the details up to you since you've done a lot of livestreaming, just get the highest end available."

CS "Alright, I'll go get the parts."

hide Linus with fastdissolve

hide CS with fastdissolve

hide CSDesk with dissolve

show Microcenter with fade

show CS with fade

CS "Okay gamers, we are buy some parts for our epic comuting machine. Let's go inside the magical concrete structure to buy some computing parts."
