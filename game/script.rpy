label start:

    menu:
        "Which segment would you like to play through?"
        "CSB 1":
            jump csb1
        "CSB 2":
            jump csb2
        "CSB 3":
            jump csb3
    label csb1:
        call csb1_start

    label csb2:
        call csb2_start

    label csb3:
        call csb3_start