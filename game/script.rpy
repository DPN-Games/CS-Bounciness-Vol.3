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
image LinusOffice = "background/the-linus-group-office.jpg"
image InsideHortons = "background/inside-tim-hortons.jpg"
image WeddingScene = "background/Wedding.jpg"
###################################
#Background Declarations
###################################




###################################
#Game Start
###################################

label start:

"{i}Last time on CS Bounciness{/i}"

"{i}CS looks across the street to see Linus Media Group.{/i}"

hide Anno
with easeoutleft

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
