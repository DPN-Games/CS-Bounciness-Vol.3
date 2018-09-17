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
image CS = "characters/Cshocola.png"
image CSPhone = "characters/CshocolaPhone.png"
image CSInsane = "characters/Cs-ocolaInsane.png"
image CSSurprised = "characters/Cs-ocolasuprised.png"
image CSHappy = "characters/csocola_happy.png"
image CSThink = "characters/Csocola_think.png"
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
image BlackPlaceHolder = "background/BlackPlaceHolder.png"
image LinusOffice = "background/the-linus-group-office.jpg"
image InsideHortons = "background/inside-tim-hortons.jpg"
image WeddingScene = "background/Wedding.jpg"
image LinusOfficeOutside = "background/linusofficeoutside.jpeg"
image CSDesk = "background/CSDesk.jpeg"
###################################
#Background Declarations
###################################




###################################
#Game Start
###################################

label start:

show BlackPlaceHolder

"{i}Last time on CS Bounciness{/i}"

"{i}CS looks across the street to see Linus Media Group.{/i}"

CS "I have a lot of video editing experience, maybe I can get a job there."
"{i}CS walks into the studio and asks for a job.{/i}"

show LinusOffice
with fade

show Linus at center
with easeintop

Linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
CS "Colour is spelled with a u, eh."
Linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my 1000s of GTX Titans."
CS "Ummmm, I'll be right back."

hide Linus
with easeoutbottom

hide LinusOffice
with dissolve

"{i}CS leaves and talks to Anno.{/i}"
show InsideHortons
with fade

show Anno at center
with easeintop

CS "I need to get proof of citizenship, or at least fake proof of citizenship before I can get a joj here."
"{i}Anno gets an idea and begins to blush.{/i}"
Anno "Trudeau is trying to make Canada more diverse by letting gay married couples get citizenship, we just have to get married and then you can work here."
CS "We don't have the money to get married!"
Anno "We can have a cheap wedding at one of your Canadian fan's houses."
CS "Well, I know Nova lives around here, so we can have the wedding at his house."

hide Anno
with easeoutbottom

hide InsideHortons
with dissolve

show WeddingScene
with fade

show CS at left
with easeinleft

show Anno at right
with easeinright

show FatherDigBick at center
with easeintop

FatherDigBick "Do you, Anno, take NAME REDACTED to be your lawfully wedded husband?"
Anno "I do."
FatherDigBick "And do you, NAME REDACTED, take Anno, to be your lawfully wedded husband?"
CS "I do."

hide CS
with easeoutleft

hide Anno
with easeoutright

hide FatherDigBick
with easeoutbottom

hide WeddingScene
with fade

show LinusOffice
with fade

show CS at left
with easeinleft

show Linus at right
with easeinright

CS "Okay Linus, I got my proof of citizenship."

Linus "Okay, you can start tomorrow. Sorry to make you get that, but I need my GTX Titans, eh."

CS "It's okay, I get it. Thanks for the job, I'll see you tommorow."

hide Linus 
with easeoutright

hide CS
with easeoutleft

hide LinusOffice
with fade

show LinusOfficeOutside
with fade

show CS at left
with easeinleft

show Linus at right
with easeinright

Linus "Welcome to Linus Media Group, come on in, I'll show you your desk."

CS "Thanks Linus."

hide CS
with easeoutleft

hide Linus
with easeoutright

hide LinusOfficeOutside
with dissolve

show CSDesk
with fade

show CS at left
with easeinleft

show Linus at right
with easeinright

CS "Wow! I thought this was an office, why do I get such a cool desk?"

Linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."

CS "Holy shit, really? This is way better than any setup I've seen, let alone had."

Linus "You must've had really bad setups then, this only has 1080s, everyone else has 1080 TIs or Titans."

CS "I have absolutely no problem with 1080s"

Linus "Well, enjoy!"




