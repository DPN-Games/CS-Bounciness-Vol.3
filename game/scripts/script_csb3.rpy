label csb3_start:
    show linusoffice with fade
    hide weddingscene
    show cs at left with dissolve
    show linus at right with dissolve

    CS "Okay Linus, I got my proof of citizenship."
    Linus "Okay, you can start tomorrow. Sorry to make you get that, but I need my GTX Titans, eh."
    CS "It's okay, I get it. Thanks for the job, I'll see you tommorow."

    hide linus with dissolve
    hide cs with dissolve
    hide linusoffice with dissolve
    show linus_hallway with dissolve
    show cs at left with dissolve
    show linus at right with dissolve

    Linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    CS "Thanks Linus."

    hide cs with dissolve
    hide linus with dissolve
    hide linus_hallway with dissolve
    show csdesk with fade
    show cs at left with dissolve
    show linus at right with dissolve

    CS "Wow! I thought this was an office, why do I get such a cool desk?"
    Linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    CS "Holy shit, really? This is way better than any setup I've seen, let alone had."
    Linus "You must've had really bad setups then, this only has 2080s, everyone else has 2080 TIs or GTX Titans."
    CS "I have absolutely no problem with 2080s."
    Linus "Well, enjoy!"

    hide linus with dissolve

   label csb3_start:
    show linusoffice with fade
    show cs at left with fastdissolve
    show linus at right with fastdissolve

    CS "Okay Linus, I got my proof of citizenship."
    Linus "Okay, you can start tomorrow. Sorry to make you get that, but I need my GTX Titans, eh."
    CS "It's okay, I get it. Thanks for the job, I'll see you tommorow."

    hide linus with fastdissolve
    hide cs with fastdissolve
    hide linusoffice with dissolve
    show linushallway with dissolve
    show cs at left with fastdissolve
    show linus at right with fastdissolve

    Linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    CS "Thanks Linus."

    hide cs with fastdissolve
    hide linus with fastdissolve
    hide linushallway with dissolve
    show csdesk with fade
    show cs at left with fastdissolve
    show linus at right with fastdissolve

    CS "Wow! I thought this was an office, why do I get such a cool desk?"
    Linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    CS "Holy shit, really? This is way better than any setup I've seen, let alone had."
    Linus "You must've had really bad setups then, this only has 2080s, everyone else has better than that."
    CS "I have absolutely no problem with 2080s."
    Linus "Well, enjoy!"

    hide linus with fastdissolve

    CS "I guess I better get to work on editing, let's see what videos I need to edit..."
    CS "Let's see, I have the new TechQuickie video on how livestreaming works, or Teran's video on how at least half of the keys on your keyboard should be macros..."
    
    menu:
        "What would you rather work on?"

        "Edit the TechQuickie video.":
            call start_edittechquickie

        "Edit Teran's video.":
            call start_editforteran
