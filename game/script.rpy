init:

    # Backgrounds
    $ backgroundDir    = "images/backgrounds"

    image bg oldOffice  = "[backgroundDir]/office1.png"
    image bg newOffice  = "[backgroundDir]/office2.png"
    image bg streets    = "[backgroundDir]/street.png"
    image bg city       = "[backgroundDir]/city.png"
    image bg cafe       = "[backgroundDir]/cafe.png"
    image bg black      = "[backgroundDir]/black.jpg"
    image bg workshop   = "[backgroundDir]/workshop.jpg"
    image bg frontHouse = "[backgroundDir]/front_house.jpg"
    image bg gameOver   = "[backgroundDir]/game_over.jpg"
    image bg sewers     = "[backgroundDir]/sewers.jpg"
    image bg warehouse  = "[backgroundDir]/warehouse.jpg"
    image bg factory    = "[backgroundDir]/factory.jpg"

    image cg steampunkT = "[backgroundDir]/steampunk_train"
    image cg train      = "[backgroundDir]/train.jpg"

    # Animations
    $ animationDir   = "placeholders/images/backgrounds"
    $ screenwipe     = ImageDissolve("placeholders/images/backgrounds/screenwipe.jpg", 1, reverse=True)
    $ dissolvelong   = Dissolve(2)
    $ fadelong       = Fade(1,1,1)

    # Placeholder Character Images
    $ placeholderDir = "placeholders/images/characters"
    $ characterDir   = "images/characters"

    image brent surprised   = "[characterDir]/brent_very_mad.png"
    image brent happy       = "[characterDir]/brent_happy.png"
    image brent smiling     = "[characterDir]/brent_happy.png"
    image brent neutral     = "[characterDir]/brent_neutral.png"
    image brent confused    = "[characterDir]/brent_very_mad.png"
    image brent thinking    = "[characterDir]/brent_neutral.png"

    image father neutral    = "[placeholderDir]/father_neutral.png"
    image father mad        = "[placeholderDir]/father_mad.png"

    image manager neutral   = "[characterDir]/manager_neutral.png"
    image manager mad       = "[characterDir]/manager_mad.png"

    image host1 neutral     = "[characterDir]/host1_neutral.png"
    image host1 happy       = "[characterDir]/host1_happy.png"

    image host2 neutral     = "[characterDir]/host2_neutral.png"
    image host2 happy       = "[characterDir]/host2_happy.png"

    image mom neutral       = "[characterDir]/mom_neutral.png"
    image mom concerned     = "[characterDir]/mom_concerned.png"
    image mom concerned t   = "[characterDir]/mom_concerned_talking.png"
    image mom shocked       = "[characterDir]/mom_shocked.png"
    image mom happy         = "[characterDir]/mom_happy.png"

    image maybelle confused = "[characterDir]/maybelle_very_mad.png"
    image maybelle happy    = "[characterDir]/maybelle_happy.png"
    image maybelle neutral  = "[characterDir]/maybelle_neutral.png"
    image maybelle sad      = "[characterDir]/maybelle_mad.png"

    image simon neutral     = "[characterDir]/simon_neutral.png"
    image simon happy       = "[characterDir]/simon_happy.png"
    image simon very mad    = "[characterDir]/simon_very_mad.png"
    image simon mad         = "[characterDir]/simon_mad.png"

    image ghepetto = "[characterDir]/ghepetto.png"

    # Main Characters
    define allan     = Character("Allan")
    define brent     = Character("Brent")
    define maybelle  = Character("Maybelle")
    define ghepetto  = Character("Ghepetto")

    # Side Characters
    define boss      = Character("Boss")
    define manager   = Character("Manager")
    define guard     = Character("Guard")
    define mom       = Character("Mom")
    define robot     = Character("Robot")

    define police    = Character("Policeman")
    define leblanc    = Character("LeBlanc")
    
    define chambers  = Character("Chambers")
    define reception = Character("Receptionist")
    define host1     = Character("Host 1")
    define host2     = Character("Host 2")
    define bishop1   = Character("Bishop 1")
    define bishop2   = Character("Bishop 2")
    define bishopb   = Character("Bishop Boss")
    define hawkins   = Character("Hawkins")
    define doctor    = Character("Doctor")
    define henry     = Character("Henry")
    define man       = Character("Man")
    define hayes     = Character("Hayes")
    define inspector = Character("Inspector")
    define dawson    = Character("Dawson")

    # Characterless
    define unknown   = Character("???")
    define article   = Character("Article")
    define diary     = Character("Diary")
    define journal   = Character("Journal")

    # Special
    define allanbrent = Character("Allan & Brent")

    # Sound effects
    $ soundEffectDir     = "sounds/effects"
    define audio.door_break   = "sounds/effects/Door_Break.wav"
    define audio.door_close   = "sounds/effects/Door_Close_Click.wav"
    define audio.door_knock   = "sounds/effects/Door_Knocking.wav"
    define audio.door_creak   = "sounds/effects/Door_Creaking.wav"
    define audio.door_slam    = "sounds/effects/Door_Slam.wav"
    define audio.footsteps    = "sounds/effects/Footsteps.wav"
    define audio.floor_creak  = "sounds/effects/Footsteps_Floor_Creaking.wav"
    define audio.metal_wheels = "sounds/effects/metal_wheels.wav"
    define audio.person_bump  = "sounds/effects/Bump.wav"
    define audio.radio_noise  = "sounds/effects/Radio_Noise.wav"
    define audio.remote_beep  = "sounds/effects/Remove_Beep.wav"
    define audio.phone_ring   = "sounds/effects/Telephone_Ring.wav"
    define audio.gun_shot     = "sounds/effects/Gun_Shot.wav"
    define audio.slap_face    = "sounds/effects/Slap_Face.wav"
    define audio.metal_wheels = "sounds/effects/metal_wheels.mp3"
    define audio.metal_bang   = "sounds/effects/Metal_Bang.wav"
    define audio.gun_empty    = "sounds/effects/Gun_Empty.wav"

label start:
    play music "placeholders/sound/music/Thanks.ogg" fadeout 1.5 loop
    # Scene 1:
    # (Setting: Old-timey office)
    # Article

    scene bg oldOffice

    article "A butterfly can lead to the world’s next disaster?!"
    article "Hit bestseller novel, Ripple, by newcomer writer Arthur Lexington tells a rousing tale about how a man's small and innocent action lead to a series of disasters that he must now fix."
    article "Lexington states the idea of the novel came to him when he read an article about the Chaos theory called the Butterfly Effect."
    article "The theory states that a small, seemingly minuscule action, like a flap of a butterfly, can actually lead to a huge event."
    article "When Lexington had finished reading the article, he knew this would make a great story and got to work almost immediately."
    article "This is Lexington's first ever novel and it has sold millions of copies all over Great Britain."
    "...."
    "Well, this is brilliant."
    "This guy just made one novel and already it's a bestseller."
    "And I got the fantastic opportunity of meeting him."
    "I mean, don't get me wrong, he's not a bad guy, but when you're stuck working for a low time publisher where your only readers are people who are in need of paper mache you kinda get tired of the mediocre stories that aren't even newsworthy."
    "Especially if you only work here to pay rent."
    "Lexington's fame is like a punch to the guy for me."
    "All my life I've been trying to pitch my novel idea to publishers everywhere and none said yes to a single idea or sample I made."
    "Meanwhile this guy just made one novel and all of a sudden he's hit with the people now."
    "So until I can even get a publisher to say yes to my book, I'm stuck working here."
    "At least it pays though."
    "But what I would do just to get a greenlight for my book."
    "Not a book about some stupid 'theory' about how all I have to do is step on a bug and all of a sudden there's another world war."
    "...That could just be me being salty, though."

    show father mad with dissolve:
        xanchor 0.5
        xpos    0.5

    boss "Allan?"
    allan "Yeah, sir?"

    show father neutral with dissolve

    boss "Well done on your new article. It will surely be a hit."
    "Yeah, if those paper mache guys actually read the paper. I don’t actually tell him that, though."
    allan "Thank you, sir. Is there any extra work for me to do?"
    "I don’t really have much to do but the very least I could use the time for my rent money."
    boss "No, you can have the rest of the day off if you would like."
    allan "I’ll be sure to do that."

    hide father with fadelong

    "My boss leaves and once again I’m left to my own devices."
    "Everyone else around here is basically doing whatever the hell they want and not doing work."
    "We barely have any stories to write about and I’m always getting a constant writer’s block so I can’t write anything."
    "With nothing else to do, I decided to leave for home and see if I can get some inspiration out there."

    # Scene 2:
    scene bg city with screenwipe

    "I go through the bustling streets of London, passing by vendors, covering my mouth from the smoke every now and then, swatting off beggar children on the way to my home."
    "It’s not much of a home, but really an entire floor I’ve been lended so I pay the landlord every month. It’s in decent condition and not too far from where I work; I can usually walk there within 30 minutes."
    "Everything here’s the same as I left it."
    "My dishes that I don’t bother to wash are still sitting where they are. Though next thing I know, they start shaking slightly along with some other furniture around here."

    # (Picture of a steampunk styled train pops up)
    scene cg train with screenwipe

    "Oh, the trains passing by again. That’s the sole reason why I could afford this place. It’s pretty close to the rails."
    "I don’t mind, though, I find it kinda nice."
    "I go to my room and find my typewriter still on its desk."
    "That was the first thing I bought when I got my first paycheck."
    "Of course I ended up having to pay my rent twice as much that time but, hey, typewriter!"
    "Unfortunately, I haven’t exactly been using it..."
    "The only thing on my desk aside from the typewriter is the paper crimped in it."
    "And the only thing written there is ‘The’."
    "I slumped on my bed and stared at the ceiling."
    "What am I doing?"
    "I used to have it all back in the day, my parents were famous researchers and we were practically loaded."
    "Was it karma for not choosing a science career in my life?"
    "I could be writing novels set in fantastical worlds and be having fans from London to New York. But instead I’m writing articles for a publisher that barely anyone knows about."
    "I’ve barely done anything in my life and I’m done with it."
    "I wish there was some decision I made in my life that actually made some significance."

    # Scene 3:
    # (Setting: Street)
    scene bg streets with screenwipe

    "Thanks to some contacts I have thanks to my parents, I got some really good info about something that would make a good article."
    "Zeppelins."
    "A new mode of transportation that’s in the works right now and the company that’s making it says they’re ready to announce it."
    "Apparently it involves using hot air and propellers to move around. Basically, it’s a gigantic hot air balloon."
    "But cooler."

    play sound person_bump

    allan "Oh, I’m so so-"
    unknown "Ah, no I’m-"
    "No way..."
    "It’s..."

    show brent surprised with dissolvelong:
        xanchor 0.5
        xpos    0.5

    allan "Brent?"
    brent "Allan?"
    "The smile on my face grows big and I trap him in my arm."
    allan "Brent! It’s been too long!"

    show brent happy with dissolve

    brent "No kidding! How’ve you been doing?"
    allan "Not gonna lie, I’ve had better times."

    show brent neutral with dissolve

    brent "Not that good, huh?"
    allan "I’ve been working for a badly smalltime publisher. I’m honestly surprised I have enough money to pay rent with our sales."
    brent "Oh, that publisher? Yeah I’ve read an article you’ve written."
    brent "I was reading it at my sister’s place and when I went to the loo, my nephew used it for his arts project;"
    brent " he’s 14 and actually reads the news from time to time."
    "I freaking knew it!"
    allan "God, are we that bad?"

    show brent confused with dissolve

    brent "The headline in that paper was about the Queen’s new corgi."
    allan "Yeah that’s fair."
    "This is Brent Norton, an old friend of mine back in the day."
    "Since my folks were always working and travelling to places for research, I had to stay in a boarding school to have a place to stay."
    "That's where I met Brent who was my roommate at the dorm."
    "We practically did everything together there, but by the time we graduated we lost contact."
    "This is the first time I've seen him is the last six years."

    show brent neutral with dissolve

    brent "Say, want to head to a cafe? There's a really good one nearby where we can catch up."
    allan "Sure, sounds good."

    # Scene 4
    # Setting: Cafe
    scene bg cafe with screenwipe

    "Brent wasn't kidding when he said this was a good cafe, this place was great!"
    "The barista was pleasant to talk to, the music in the radio was soothing, and the coffee is exquisite!"

    show brent happy with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Ah, man, this brings back memories."
    allan "Does it now?"
    brent "Yeah, you and I used to head to out to restaurants on the end of the month and spent whatever money we saved up on the place's best food."
    allan "Oh, yeah. Wow, I spent way too much money than I should have."

    show brent neutral with dissolve

    brent "Yeah, I remember your mother wouldn't stop yelling at you that one time we spent your entire allowance."
    allan "Yeah, I'm not too fond of that memory."
    brent "That reminds me, did your parents research take off?"
    allan "Kind of, but they're retired now and lent it to one of their workers. I heard they're doing good progress, though."
    brent "Hey, that's great! Why not do an article of it?"
    allan "I don't think it'll catch the eye of a lot of people. It's not really an ice breaker, honestly."
    brent "Oh, that's a shame."

    python:
        _preferences.set_volume('music', 0.25)

    play sound radio_noise fadeout 1.5 loop

    show brent confused

    brent "What the-"

    hide brent with dissolve

    "The manager of the cafe suddenly leaves his post and starts banging on the radio."

    show manager mad with dissolve:
        xanchor 0.5 xpos 0.3
        yanchor 1.0 ypos 1.0
        zoom    1.75

    manager "Grr, stupid thing!"

    stop sound

    "The music in the radio finally returns, but at this point the song ended and it returns to the radio host."

    show manager neutral with dissolve

    host1 "And that was Anna Comstock’s new hit Songbird! Ah, she’s a lovely lady, ain’t she?"
    host2 "Yes, she is, George. You know I met her a couple days ago at a restaurant."
    host1 "Really now, what she like?"
    host2 "Very adventurous. She’s truly an idol for the ages."
    host1 "Just goes to show you that meeting your heroes can be a good thing!"
    host2 "Ain’t that right, George."
    host2 "And now the news! Today’s the day of the anniversary of the tragic sinking of the RMS Grandiose."
    host1 "Oh, you mean the cruise line that sank twenty years ago?"
    host2 "That’s right, the same one. The reports say a boiler had exploded in the ship, causing a chain reaction and a giant hole in the bowl of the liner."
    host1 "At least 50 passengers had died in the explosion, 50 more during the evacuation, and triple that amount when the ship sank."
    host2 "Everyone in the world couldn’t help but compare the sinking with this to the Titanic’s. Thanks to both sinkings, funnily enough, governments everywhere started funding researchers and engineers for both better ways for ship travel and air travels."
    host1 "I don’t think you should be saying ‘funnily enough."
    host2 "My apologies, ladies and gents. It’s just that the irony is funny here."
    "The cafe started erupting in a bunch of sneers and insults at the radio hosts."
    "Looks like that guy’s not gonna work for the station ever again."
    "Hm..."
    "RMS Grandiose, huh?"

    # (Scene 5)
    # (Setting: The front of a harbor)
    scene cg train with screenwipe

    "Crazily enough, I was almost on that ship."
    "It was twenty years ago, while my mom and dad were still researchers and I was still in boarding school and summer was approaching."
    "There was a new development in the research of my parent’s in America but I needed to be picked up from boarding school."
    "My dad decided to head there first while my mother went to pick me up. We stayed in Britain for a few more days to get ready for the trip to America."
    "My grandparents retired in America and my Grandad’s 65th birthday was coming up so naturally we had to visit."
    "It was going to be a one week trip on the Grandiose cruise liner that my mom bought tickets to. We were going to ride it to America."
    "One slip up changed everything, though."
    "We left early so to not miss our trip. We ended up skipping breakfast and eating at a restaurant."
    "We were in a rush."
    "After eating, we rushed to the ship but halfway there my mom realized something."

    show mom neutral with dissolve:
        xanchor 0.5 xpos 0.3
        yanchor 1.0 ypos 1.0
        zoom    1.75


    mom "Did we leave something?"
    "I looked at our bags, at first I didn’t see anything out of the ordinary but then I realized we may have missed something."

    menu:
        "Tell mom we may have lost something.":
            $ toldMom = True
            jump toldMom

        "Don't say anything.":
            $ toldMom = False
            jump notTold

label toldMom:

    allan "Did we forget something? I have a feeling we did."
    mom "Wait..."

    show mom concerned with dissolve

    "My mom looked through our bags again, that was when her eyes widened."

    show mom shocked with dissolve

    mom "The gifts! We forgot the gifts!"
    "Realizing our terrible mistake, mom and I rushed back to the restaurant we ate at and, luckily enough, the lady at the store kept it with her."
    "Unfortunately, since the restaurant was pretty far from the harbor, the ship left without us."
    "Mom and I had to buy new tickets and missed my Grandad’s birthday by a day. He wasn’t mad at us, thank god, and my family had to stay there for a few more days to make up for lost time."

    jump toldContinue

label notTold:

    show mom concerned with dissolve

    mom "Hmm... no, I don’t think so."

    show mom shocked with dissolve

    "My mom looked a bit unsure though and for the rest of the way to the ship she was taking a double look on our bags."
    "We made it to the line and at the moment we were boarding the ship, my mom finally realized it."

    show mom concerned t with dissolve

    mom "Oh my god, we left our gifts!"
    guard "Do you have a problem, ma’am?"

    show mom concerned with dissolve

    mom "Oh, uh, yes..."
    guard "Are you going to board, ma’am?"

    show mom shocked with dissolve

    "My mom looked at her bags, then at me, then at the line."
    "It was really piling up."
    "Like, there was about 7 families waiting for us to get in so they can."
    "My mom stood there confused for a solid 2 minutes until she finally came to a decision."

    show mom concerned t with dissolve

    mom "I’m sorry, looks we aren’t."
    "Mom grabbed me by the arm and we trudged through the line."
    "The people in the line were all giving us the dirty eye, except for a little girl my age who looked just as confused as I was."
    "The ship left soon after, without us and quite a handful of passengers thanks to us."
    "We went back to the restaurant we ate at and got our stuff back thanks to the owner who kept it with her."

    jump toldContinue

label toldContinue:

    # (Scene 6)
    # (Setting: Back to the cafe)
    scene bg cafe with dissolve
    show brent confused with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Allan?"
    allan "Huh?"
    brent "Are you in there, mate? I lost you for a second there."
    allan "Ah, sorry. Just reminiscing."

    show brent neutral with dissolve

    brent "About what?"
    allan "Well..."
    "I tell Brent about the what happened twenty years ago with my mom."

    show brent surprised with dissolve

    brent "Damn, that nearly happened?"
    allan "Yup."

    show brent neutral with dissolve

    if toldMom:
        $ toldMom = True
        brent "You could’ve been one of the victims if you hadn’t told your mom."

    else:
        $ toldMom = False
        brent "You could’ve been one of the victims if your mom didn’t realize it then."
        allan "Yeah, looks like lady luck was on our side that day."
        brent "Yeah, thank god."

    allan "Enough about me, though, what have you been doing after graduation?"
    brent "I’m glad you asked. I’m actually a Private Investigator."
    allan "Really now? I figured, though."
    brent "Is it the clothes?"
    allan "No, back in boarding school you always had a knack for figuring out puzzles and mysteries. I remember there was this book series I got you into and you made theories about the book’s mystery. I remember being concerned for you"
    brent "It wasn’t THAT unhealthy."
    allan "Your side of the room was covered in investigation maps and you rambled to the school cat about your theories."
    brent "At least the cat wanted to listen."
    allan "He looked just as done with you as I was."
    "We kept talking for a while about the old times."
    "Brent, out of nowhere though, closes his eyes for a moment and rests his hand on his chin."

    show brent thinking with dissolvelong

    brent "Hmm..."
    brent "Y’know Allan, you don’t have a story right now, do you?"
    allan "I was on my way to the one I was going to write about, why?"
    "I take another sip from my coffee."

    show brent neutral with dissolve

    brent "Well, I was thinking maybe you’d like to help me with this case."
    "Then I empty the contents of it back into the cup in one spit."
    allan "WHAT?"
    brent "Well, you and I used to be great back in the day, remember?"
    allan "Well, yeah, but why do you want my help?"
    brent "Well not really 'help me' help me, but I do know you’re down in your luck in that gazette your working in, right?"
    allan "Yeah, but..."
    brent "I honestly need a bit more exposure. Only through word of mouth do people know about my office. Kinda have been down on my luck too."
    allan "Damn..."
    brent "Yeah, I know your gazette doesn’t have a lot of readers but don’t you think a detective case is exactly the kind of story readers would be interested in reading?"
    "Hmm..."
    "This would give me a boost in my career, at least to get a better job."
    "And the gazette does need more readers."
    "I mean, yeah I do plan on leaving there but that doesn’t mean I want it to be bankrupt."
    "The very least this story could help the workers there."
    "And this might make a good novel"
    "..."
    allan "Yeah, sure, screw it. I’m down for it!"

    show brent happy with dissolve

    brent "That’s what I’m talking about! Man, this is gonna be like old times. Ready to solve this case, buddy?"
    allan "You bet I am!"
    "And just like that, Brent and I went to work on the case."

    scene bg black with dissolvelong

    "I wish I knew at the time how much that decision changed everything."

    # Scene 7
    # (Setting: In front of a building, victorian era)
    scene bg city with screenwipe

    "We left the cafe soon after. After taking a fairly long ride on the monorail here in the city, Brent took me into this building ways off from the city."
    "Why the hell would anyone want to live somewhere as far this?"
    allan "So, Sherlock, what’s the case for today?"

    show brent smiling with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Well, Watson, it’s a simple case. One might say its..."

    show brent neutral with dissolve

    brent "Well actually, it’s NOT elementary. It’s pretty interesting."
    allan "Really? How so?"
    brent "Nothing too bad, the very least. It’s a missing person case."
    allan "Missing person? Who’s missing?"
    brent "Lewis Bradley."
    allan "Oh."
    "..."
    "Wait-"
    allan "Woah, woah, woah, wait! You mean that new inventor that everyone’s been talking about?"
    brent "Same one."
    allan "He’s been missing? No wonder there hasn’t been any news about him lately."
    allan "Why hasn’t there been any news?"
    brent "That’s the thing, my client hasn’t told anyone else about it. Just me."
    brent "And I guess you to an extension now."
    allan "Damn..."
    "I feel like I stumbled upon a web I shouldn’t have."
    brent "Anyway, this is his workshop. And also his office."
    allan "Both at the same time, huh? Do you got the keys to this place?"
    "Brent digs into his pockets, getting out a roll of keys."
    brent "Client gave me a spare."
    allan "Sweet."
    "He turns the key inside the keyhole and the door swings open."

    # (Setting changes to a steampunk styled workshop)
    scene bg workshop with screenwipe

    "As soon as we step inside, loud sounds of metal clanking was heard."
    "Engines started springing into life, sounds of smoke puffing out and what sounded like wheels turning."
    "Wait, wheels?"
    unknown "Welcome, home, Professor Bradley."

    # (Picture of a steampunk robot appears (doesn’t have to be our drawing))
    #TODO: Have character

    "Woah, what the heck?"
    "Is this supposed to be...a butler?"

    show brent confused with dissolve:
        xanchor 0.5
        xalign  0.5

    brent "Did not see this coming..."
    "Looks like Brent is just as astonished as I am."
    allan "Wait, you’ve never seen this before?"

    show brent neutral with dissolve

    brent "Nope, first time I’ve been here."
    brent "Looks like this thing is supposed to answer to Mr. Bradley."
    robot "What can I do for you, Professor Bradley?"
    allan "Looks like it."
    robot "What can I do for you, Professor Bradley?"
    allan "Can this thing not tell we’re not Bradley?"
    brent "I don’t think so."
    robot "What can I do for you, Professor Bradley?"
    allan "Okay, this thing is starting to get on my nerves, what should we do with it?"

    show brent thinking with dissolve

    brent "Hmmm..."
    "Brent places his hand on his chin and thinks. After a short while, his signature smile crepts up."

    show brent happy with dissolve

    brent "Hey, can you get me a snack, perhaps?"
    robot "Of course, Professor Bradley."

    #TODO: Hide robot

    "The robot leaves us and enters a room a bit farther down."
    allan "You’re not thinking about abusing the system, are you?"
    brent "Nah, just want to see what it can do. What’s important is that we got a way to find any info. All we got to do is ask the robot."
    allan "Good point."
    brent "Okay, I’ll sweep the place from the right. You’ll sweep the place from the left. Yell out anything you find that looks useful for the case."
    "I nod back, and the two of us separate."

    hide brent with dissolve

    "Hmm"
    "Hmm..."
    "Where do I check?"

    menu:
        "The worktable":
            $ cabinet = False
            "...I wonder..."
            jump worktable

        "The cabinet":
            $ cabinet = True
            "...I wonder..."
            jump cabinet

        "The desk":
            $ cabinet = False
            "...I wonder..."
            jump desk

label worktable:
    "I inspect the worktable."
    "So many little gears, scraps of metal, some wires, and a memo."
    "I pick up the memo and read what it says."
    "Things to work on: 1. Voice Recognition. 2. Artificial Intelligence. 3. Facial Recognition."
    "..."
    "Yeah I have zero what any of that means."
    "I glance up and see the robot from before."
    "The stuff in the note must be for the robot."

    jump continueCheck

label desk:
    "I walk over to the desk."
    "Not a lot to it, just some more papers and a couple of pencils."
    "Oh, and a framed picture."

    if toldMom:
        "There’s two people in the picture."
        "Behind them is by the looks of it is the building I’m currently standing in."
        "There’s two adults, a man and a woman."
        "They look young."
        "The man has his arm around the shoulder of the girl. They’re both smiling brightly."
        "I look at year it’s signed. Looks like the photo was recently taken"

    elif !toldMom:
        "It’s a family photo."
        "There’s the parents standing behind their two children."
        "Behind them is a cruise."
        "Actually, the cruise looks familiar. I can’t seem to put my finger on how"

    jump continueCheck

label cabinet:
    "I walk over to the cabinet and I grab the handle and pull it."

    play sound door_knock

    "Damn, it’s locked."
    allan "Brent!"

    show brent neutral with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Yeah?"
    allan "Do you have the keys to the cabinet here?"

    show brent happy with dissolve

    brent "There’s a lot of cabinets here. I’m searching one right now, even."
    "Forgot how much of a smartass he can be,"
    allan "Whatever, do you have the keys for them or not?"

    show brent neutral

    brent "No I don’t, ask the robot. I’m sure it can help you."
    "I glance at the robot again."
    "Man that thing gives me the creeps."
    "He’s not wrong though."
    "I walk over to the robot."
    allan "Hey..."
    robot "How can I serve you, Professor Bradley."
    allan "Can I have the keys to that cabinet over there?"
    "I point to the cabinet and the robot eerily follows my hand."
    robot "Of course, Professor Bradley."
    "He moves towards the front desk of the workshop and I follow."
    "There I notice a plaque."
    "'Maybell Bradley, receptionist.' it says."
    "Bradley? So a relative maybe."
    "The robot moves to me and hands me the keys."
    allan "Uh...thanks. At ease...robot?"
    "The robot leaves again and head to the cabinet."
    "I unlock it and I find..."
    "More papers. Paper rolls to be exact."
    "I grab one and unroll it."
    "Woah."
    "Looks like they’re blueprints."
    "For a new robot."
    "Using context clues, I’m able to figure out what’s what."
    "And then I notice..."
    "The figure, the head..."
    "They’re all... humanlike."
    "They look like people."
    "What in the world is he doing?"
    "I put it back where I found it and locked the cabinet."

    "I walk to the front desk, not finding much back in my side."
    "I figured the front desk should have something."
    "That’s when I see it."
    "A book, a red book."
    "Looks interesting."
    "I take it and open the book."
    "Looks like a log book; a log book for clients I’m assuming."
    "I recognize most of these names. They’re all famous businessmen who own a lot of companies."
    "No wonder Bradley got famous. He worked for some of the biggest companies out there."
    "I inspect the names until I reached the last one."
    "Most of the names here are aligned by how much money they have to pay and the payment."
    "But the last one in the list doesn’t have a payment."
    "'Burns'"
    "That’s the last name on the list."
    "So he doesn’t have a payment, but he’s on the list."
    "So that means-"
    unknown "Um, who are you?"

    show maybelle neutral with dissolve:
        xanchor 0.5
        xpos 0.5

    allan "Hm?"

    jump continueCheck

label continueCheck:

    show maybelle neutral with dissolve:
        xanchor 0.5
        xpos 0.5

    unknown "How did you get in here?"
    "Ah, crud."
    allan "Uh, well you see, ma’am..."
    brent "Allan, find something?"

    show maybelle:
        ease 1.5 xpos 0.25

    show brent neutral with dissolve:
        xanchor 0.5
        xpos 0.75

    unknown "Oh, Ms. Bradley. Didn’t think you’d be here today."
    "Ms. Bradley?!"
    unknown "Detective Norton! Sorry, were you investigating?"
    brent "Yeah, me and my friend here were."
    "The woman turns her head to me."
    unknown "Oh, are you a friend of Detective Norton?"
    allan "Yeah, a very old friend. My name’s Allan Lorenz."
    maybelle "Maybelle Bradley. I’m a receptionist here for my brother’s workshop."
    allan "Oh, you’re Mr. Bradley’s sister?"

    show maybelle happy with dissolve

    maybelle "Yup, nice to meet you Mr. Lorenz."
    allan "Just ‘Allan’ is fine."
    maybelle "Okay."
    brent "Allan is a journalist. He’s helping me with the case."
    maybelle "Oh, really? Well, thanks for helping out."
    "I haven’t done much of that but I accept the praise nonetheless."
    brent "And Ms. Bradley here is my client."
    allan "The client?"
    "Maybelle nods back to me."
    allan "Oh, so you got Brent to do the case?"
    maybelle "Yeah, I heard a bit about Detective Norton so I asked him for help."
    "She just wants to find her brother, huh?"
    "Well since she’s here maybe I can get some light into this situation."

    menu:
        "Why get Brent?":
            jump whyGet
        "When did you last see your brother?":
            jump seeBrother

        "Can you tell me about your brother?":
            jump tellBrother

        "No need to ask.":
            "I think I’m good on questions now."
            jump brotherContinue


label whyGet:
    allan "No offense to my friend here but why get Brent to help? Couldn’t the police  work too?"

    show maybelle neutral with dissolve

    maybelle "I tried that, but they didn’t take me seriously."
    allan "What? It’s a missing person!"

    show maybelle angry with dissolve

    maybelle "That’s what I said! But they said my brother was probably just hiding somewhere cooped up and working on his new, and I quote, contraption."
    allan "Why are they like that?"

    show maybelle neutral with dissolve

    maybelle "Well, my brother is a bit weird for some people’s standards."
    allan "Your brother is a genius though, right?"
    maybelle "He is! Lewis’s brilliant and works really hard. He’s just...well..."
    show maybelle happy with dissolve
    maybelle "People just don’t understand him."
    "Man, I’m starting to feel bad for this guy."
    show maybelle neutral with dissolve
    "But the list of people in this log book proved he is good at what he does."
    "So why the hell do people treat him like that?"
    show maybelle confused with dissolve
    "Hmm..."

label seeBrother:
    allan "When did you last see your brother?"

    show maybelle neutral with dissolve

    maybelle "Four weeks ago. Right in this same workshop."
    brent "According to Ms. Bradley, Lewis was working on this new robot for this company. He worked day and night for it."
    show brent neutral with dissolve
    maybelle "Sometimes I find him asleep on his desk, working on the robot."
    maybelle "On the day he got the job, he never stopped working. I got worried about him but he kept insisting he kept on going."
    maybelle "Then on the first monday of the month, he wasn’t in the workshop."

    show maybelle sad with dissolve

    maybelle "He just disappeared."
    brent "She went to me after a week went by with no sign of him."
    brent "That leads us to today."
    show brent confused with dissolve
    "Hmm..."
    "Four weeks ago, huh?"
    jump brotherContinue

label tellBrother:
    allan "Tell me more about Lewis."

    show maybelle neutral with dissolve

    maybelle "Well, he’s an inventor as you can see."
    "I turn my head towards the robot."
    allan "Yeah, I can see that. He’s working on robots."
    maybelle "He calls it animatronics."

    show maybelle confused with dissolve

    allan "Anima-wha?"
    brent "Animatronics. I don’t know why he calls them a different name."

    show maybelle neutral with dissolve

    maybelle "He prefers it that way. He says it gives him an identity to stand out from other inventors."
    allan "He’s working on robots, though."
    maybelle "I know, but he wants more people to know about him and get more clients to get more money. He wants to make robots to help him in inventing."
    allan "Not humans?"

    show maybelle sad with dissolve

    maybelle "No, he doesn’t exactly trust humans with his inventions."
    maybelle "He says humans always make mistakes and needs his inventions to be one hundred percent flawless."
    allan "That’s a lot to ask for, even for a robots."
    maybelle "It is. He works days and nights to make sure they’re on top condition."
    "Talk about a hard worker. I hope he doesn’t kill himself out of exhaustion."
    jump brotherContinue

label brotherContinue:
    "I flip through the book again, but as I’m doing it I notice Maybelle looking at the ground."
    "Somewhat in dismay."
    allan "Something wrong?"
    maybelle "Oh no, it’s nothing you did it’s just that..."
    maybelle "Talking about my brother’s work has me thinking about how down on his luck he is."
    allan "The log book begs to differ."
    maybelle "It may seem that way but look at the time between each client."
    "I take a look at the book."
    "Took me a while to notice it but I find out the time gap between each client is separated by months, hell one was an entire year."
    "Wow, what a bad break."
    allan "Yeah you’re right. This IS bad."
    brent "Wait, let me see."
    "I hand Brent the book and he inspects the contents."

    show brent thinking with dissolve

    brent "Yeah, I can see it."
    maybelle "That’s why my brother works so hard. He focuses on quality than quantity."
    maybelle "At least in my eyes, my brother’s wishes are justifiable."
    allan "How so?"
    maybelle "Well..."

    if toldMom:

        $toldMom = True
        
        show maybelle neutral with dissolve
        maybelle "Back in the day, it was me, my brother, and our parents. We were a very happy family."
        maybelle "Our parents were also inventors, they were my brother’s inspirations; he really looked up to them."
        maybelle "They struggled to make ends meet, like my brother, but we were happy nonetheless."
        maybelle "That is until... the accident."
        allan "Accident?"
        brent "This is a first for me too, can you tell us about the accident?"
        maybelle "Sure."
        maybelle "It was twenty years ago. I was very young and my brother was around ten I believe."
        maybelle "We were going to board this cruise line to take us to America for a business trip for my parents."
        brent "What was the cruise?"
        maybelle "The RMS Grandiose."

        show brent surprise with dissolve

        "THE WHO AND WHAT NOW??"
        "She was on that ship?!"
        maybelle "I see you’re both surprised. Yes, we boarded that ship. All the way to the Atlantic to get to America. I think you can guess what happens next."

        show brent neutral with dissolve
        allan "The sinking..."
        maybelle "Yup, everyone scrambled to get on the boats. The rule was mother and children first. But..."
        maybelle "They could only fit two people left on the lifeboat we found."
        maybelle "My father rationalized waiting for another lifeboat could mean our death so... he and mother agreed to let us go in the lifeboat."
        show maybelle neutral with dissolve
        show brent happy with dissolvelong

        brent "So you two could live."

        show maybelle happy with dissolve

        maybelle "Yes. Mother assured us they would get on the next boat, but from the look on her face, I figured we’d never see her again."
        maybelle "We got on the boat and it drifted off into the ocean. We watched as the boat started to sink as people upon people fell to their deaths."
        maybelle "And I swear I could see my parents clinging on the table before falling to their deaths."
        "A tear rolls out her eye. A sniffle escapes her mouth."
        "I reach into my pocket and give Maybelle my handkerchief."
        maybelle "Thank you, Allan."
        allan "No need to. I’m sorry for bringing up bad memories."
        maybelle "Don’t apologize. You asked and I just cooperated."
        maybelle "Anyway, since their deaths my brother had assigned himself as the breadwinner for us and worked to provide for us."
        maybelle "He picked up on our parents researched and worked to the bone to provide."
        maybelle "He always worked, just for us. To make sure we lived a happy life."
        maybelle "I worry about him. He’s all I have left."

    elif !toldMom:

        $toldMom = False

        maybelle "Back in the day, it was me, my brother, and our parents. We were a very happy family."
        maybelle "Our parents were also inventors, they were my brother’s inspirations; he really looked up to them."
        maybelle "They struggled to make ends meet, like my brother, but we were happy nonetheless."
        maybelle "My parents always worked hard for us. I remember there was this big business trip my parents were supposed to go to, they even brought us with them."
        maybelle "But...we got delayed. Actually, our trip was cancelled."
        brent "What, how?"
        maybelle "I don’t remember, it was twenty years ago."
        maybelle "Anyway, when it got cancelled our parents were frantic because it could mean the end for their career."
        maybelle "Luckily it wasn’t, but my parents had to work twice as hard that time to compensate for the loss."
        brent "Guess being a workaholic runs in the family."
        maybelle "Yeah, I guess."
        maybelle "Anyway, my parents didn’t make enough money to happily retire and my brother found that fact as an injustice."
        maybelle "To him, our parents deserve as much money as they need since they were really brilliant. So he picked up on their inventions and worked to provide for them and us."
        allan "But it’s still not enough."
        maybelle "Not so much. Our parents assure him it’s fine and he doesn’t need to provide but he’s stubborn."
        allan "So he keeps working."
        maybelle "Exactly."
        maybelle "We all worry about him. He’s brilliant but we don’t think he should go far for us."

    brent "Thank you for telling us, Ms. Bradley. Telling us was probably not easy."

    show maybelle neutral with dissolve

    maybelle "It’s nothing, really. It is nice to get it out every once in a while."
    "Brent looks back at the book."
    "Eventually, he grabs me and reels me in."
    brent "Allan, look at this."
    "He points to the last name in the log book."
    allan "Oh yeah, this Burns person was his last client, Maybelle?"
    maybelle "Oh, yes."
    maybelle "He’s a very strict man. He wants the robot he needed from my brother by next month. Though, my brother insists it would take at least 3 to finish it."
    allan "Let me guess, he’s not listening."
    maybelle "Yup."
    brent "You know how capitalists are. They’re impatient and only want to hear progress."
    brent "Anyway what’s important here is that he’s the last client. Look at the date. He made the request some time well before Lewis went missing."
    allan "Seriously?"
    brent "We need a lead, and looks like Burns is the best one we got."

    show maybelle sad with dissolve

    maybelle "Good luck getting through him. He might not even listen to you."
    allan "Okay, well he’s owns a huge corporation, how are we going to find him?"

    show brent happy with dissolve

    brent "Oh that’s easy, I know where he lives."
    allan "You do?"
    brent "Yup, saw him on my way back from a case. I know it’s his home because it has the logo for his company."
    allan "Well, that’s a lead too. Let’s go find him."
    show maybelle happy with dissolve
    maybelle "Good luck, you two. And please bring my brother back."
    brent "We’ll do what we can."
    "I nod back and then the two of us head out."

    # Scene 8
    # (Setting: in front of a house)
    scene bg frontHouse with screenwipe

    allan "This is his place?"

    show brent neutral with dissolve:
        xanchor 0.5
        xpos 0.5

    brent "Yeah, surprisingly normal right?"
    "Yeah I expected a mansion. Not a simple big house on the hill somewhere."
    brent "Well, let’s go ring him up."
    "Brent presses the doorbell."
    "No answer."
    "He presses on it again."
    "And still no answer."
    allan "That’s weird, maybe he’s not home?"
    brent "It’s 16:00, he has to be home."
    "Brent grabs the door knob."
    "Yeah, like turning it would-"

    play sound door_creak

    "The door swings open, as easy as 123."

    brent "Unlocked door..."
    allan "Nobody answering the door."
    "My body immediately tenses up. Brent walks through door cautiously and looks around the hall."

    show brent thinking with dissolve

    brent "Looks like nobody’s home."
    allan "This doesn't look good. What should we do?"
    "Brent takes a minute to think."
    brent "I don't want to be that guy, but I think we should split up."

    show brent surprised with dissolve

    allan "Ugh, for real? Guess I should've seen this coming."
    brent "I need you to be cautious, Allan. Who knows what or who could be here."

    show brent neutral with dissolve

    "I nod in reply, and soon I go in the house."
    "Brent goes to the left and I later head to the right."
    "I search around the house for signs of Burns, sadly not a lot I could find."
    "Aside from a bunch of paintings of who I'm assuming are old family members there's nothing out of the ordinary."
    
    play sound footsteps

    allan "Hm?"
    "There's footsteps upstairs."
    "Brent maybe?"
    "I head to the stairs leading to the upstairs."
    "It's completely dark so I can't see much."
    "Wait..."
    "There's a shadow. I can make one from the where I'm standing."
    "Wait..."
    "It's..."
    "Tall. Very tall."
    "It looks like a human, but..."
    "Something about it unnerves me."
    "Should I check it out?"

    menu:
        "Investigate sound":
            jump investigateFirst
        "Find Brent first":
            jump brentFirst

label investigateFirst:

    hide brent with dissolve

    "I go up the stairs."
    "It’s an empty hallway."
    allan "Hello?"
    "No answer."

    play sound footsteps

    "It’s coming from a room."

    play sound door_knock

    allan "Anyone in there?"
    "No answer again."
    "..."

    play sound door_creak

    "I didn’t open that."
    "I walk inside, the room’s completely dark, except for the light from the moon."
    allan "Hello?"
    "Then I hear footsteps, someone’s coming out of the shadows."

    show ghepetto with dissolvelong:
        xanchor 0.5
        xpos 0.5

    unknown "..."
    allan "Who are y-"
    "I didn’t finish."
    "Something grabbed my mouth, and trapped me in its arms."
    "It squeezed my body inwards in agonizing pain."
    "It was like being crushed by two heavily loaded wardrobes."
    "The person from in front of me removes their mask."
    "And their smile is the last thing I see."
    "Later..."

    hide ghepetto

    play sound person_bump

    brent "Allan? Allan?"
    brent "I heard some knocking up here, was that you?"
    show brent confused with dissolve:
        xanchor 0.5
        xpos    0.5
    
    play sound door_creak

    brent "Gah!"

    show brent neutral with dissolve

    brent "Jesus, man you scared me!"
    "..."
    brent "Find something in here? I’ll just go in."
    "..."
    "..."
    brent "Hey, listen, don’t assume I swing that way but..."
    brent "Have your eyes always been that glossy?"

    scene bg gameOver with fadelong

    return

label brentFirst:
    
    "Yeah no, I've read enough horror books to know that's a bad idea."
    "I walk around the house until I find Brent."
    allan "Hey, Brent."

    show brent with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Allan? what's up?"
    allan "There's something upstairs."
    brent "Something not someone?"
    allan "I'm...I'm not sure."
    brent "Stay close, follow me."
    "I stay close behind Brent as he approaches the door."
    "It takes him a bit of time before he finally decides to head upstairs."
    "We climb the stairs carefully, we make sure our footsteps don’t make even the slightest sound."
    "We make it to the door where I think the sound came from."
    brent "Is there where you heard it?"
    allan "I think so."
    "Brent stands beside one side of the door, and I stand at the other."
    "He reaches his hand for the door, not the doorknob though."
    "He looks and me and fakes a knocking motion."
    "I nod, looks like he’s trying to tell me to get ready."
    
    play sound door_knock

    "We wait for a response. Nothing at first."
    "Brent knocks again."
    
    play sound door_knock

    "......"
    "......"
    
    play sound door_break

    show brent surprised with dissolve:
        ease 1.5 xpos 0.25

    "What the-"
    brent "Oh shit!"
    "We bust the door open and run in."
    "It’s an abandoned room, practically nothing in here."
    "Except for a broken window."
    brent "Not good!"
    "We hurriedly look out the window."
    "At first I couldn’t find anyone in the roofs of London."
    "But then I saw it."
    allan "Over there!"
    "I point at a roof far from us."
    "There’s a man standing there."

    show ghepetto with dissolvelong:
        xanchor 0.5
        xpos 0.75

    unknown "......"
    brent "Who is that?"
    "The man looks at us for awhile."
    "And then finally, he jumps out the roof and into the alley."

    show ghepetto:
        ease 0.5 xpos 1.5

    hide ghepetto

    allan "Hey, wait!"
    "No luck."
    "He’s gone."
    allan "Why was he here?"
    "And then as if on cue, the two of us here a small creaking sound."
    brent "That’s...That’s the door, right?"
    allan "Should be...?"
    "We turn around, and I was not prepare for what was there."
    "A body, a body was there."
    "Still, hanging from his arms."
    "With no skin, and no jaw."
    hide brent
    # Chapter 2

    show simon neutral with dissolve:
        xanchor 0.5
        xalign 0.55
        ease 1.5 xpos 0.75

    show brent neutral with dissolve:
        xanchor 0.5
        xpos    0.25
    police "So, the two of you found that body there?"
    brent "Yes."
    police "And the door was unlocked when you found it..."
    allan "Like we said, yes."
    police "And Mr. Norton here is an expert in picking locks, right?"
    brent "Ugh, Simon, are you always going to ask that when I happen to find a person’s dead body in a house somewhere?"

    show simon mad with dissolve

    leblanc "It’s Detective LeBlanc! And it’s standard procedure, son. I need to check the facts and find all suspects."
    brent "Okay, but aren’t you jumping the gun a bit when there’s no evidence against me?"
    leblanc "You mean aside form the fact you made it here first?"
    "..."
    "Man, this guy does not like Brent."
    allan "Um, sir?"
    leblanc "Yes?"
    allan "We have an alibi. We met up with a woman before this, Maybelle Bradley. You can confirm with her that we didn’t exactly have time to kill him."
    leblanc "Well, alright. I’ll check it with her. But don’t think you two aren’t out of my radar yet! I’m watching the two of you!"
    
    hide simon with dissolve

    "..."
    "...."
    allan "Well, he seems nice."


    brent "Don’t mind him, he’s like that to every person I’m associated with."
    allan "Yeah, I noticed you called him Simon?"
    brent "Yeah, we know each other. I’ve solved some of cases that he was supposed to."
    allan "So he’s bitter about it?"
    brent "I think so. Guy can’t seem to let go."
    "After finding the body of  Burns, we naturally would call the police."
    "Took them quite fast to get here, in fairness."
    "Still I may not be a detective, but if that were me I would have just moved on; how long can someone hold a grudge?"
    brent "Anyway, let’s keep investigating."
    allan "Su-"
    "Wait.."
    allan "WHAT! With the police here?"
    brent "It’s a risky move, but since I’m a licensed private eye I’m allowed to check the scene and look at the body."
    brent "Besides, I think that would lower their suspicion of us. Why would the culprits look for clues in their crime scene, right?"
    show brent thinking with dissolve    
    allan "To look for the evidence against them and get rid of it and any charges against them?"
    brent "..."
    allan "..."
    brent "Look, I promised Maybelle we’d solve this case so let’s get on it."
    "Heh, heh, looks like I got ‘im."
    show brent happy with dissolve
    "We approach LeBlanc as he’s talking to one of his officers."
    show simon neutral with dissolve
    leblanc "So the same way?"
    police "Yup, we’re sure it was him."
    brent "Sure it’s who, Simon?"
    show brent surprised with dissolve
    leblanc "Ugh, you’re still here, Norton?"
    show simon mad with dissolve
    "LeBlanc signals his officer away and holds a piece of paper in his hands."
    brent "My client was the one who sent me here, I have every right to investigate the scene as much as you, Simon."
    show brent neutral with dissolve
    leblanc "Of course you do, what do you want?"
    show simon neutral with dissolve
    brent "You said you know who the culprit is?"
    leblanc "Well, kinda. We know who the culprit is, we just don’t know  their identity?"
    allan "Their identity?"
    "LeBlanc looks at me, and I’m pretty sure he’s giving me the evil eye."
    leblanc "And who are you, son?"
    brent "No worries, he’s my partner for this case."
    leblanc "Hm, well alright."
    leblanc "Anyway, yes, we don’t know their identity; we only got a name for him."
    brent "What’s that?"
    show brent thinking with dissolve
    leblanc "The Ghepetto Killer."
    allan "Woah... how’d you come up with a name like that?"
    leblanc "From one of the ways they left their victims. Hanging from a string looking like a puppet."
    "Just like the way we found Burns’ body."
    leblanc "We haven’t had any luck finding him. God it’s getting on my nerves."
    brent "With a name like that, I’m assuming this isn’t his second kill?"
    leblanc "Nope, this is his fourth."
    allan "Fourth?!"
    leblanc "Yup, three other ones."
    brent "Any patterns between the victims?"
    show brent neutral with dissolve
    leblanc "Nope, even worse we can’t identify the victims."
    show simon neutral with dissolve
    brent "Why not?"
    leblanc "The skin is removed, without it we can’t find fingerprints. Not only that, but also the jaw is missing. We can’t use their teeth to find their identity. No other credentials were found with the body."
    show simon mad with dissolve
    brent "What about location?"
    show brent thinking with dissolve
    leblanc "All in abandoned warehouses."
    brent "Damn, this guy left no trace, did he?"
    show brent thinking with dissolve
    leblanc "And no M.O we can find."
    leblanc "Anyway, I need to get going. I’ll see you two when I see you."
    "LeBlanc heads to his carriage and leaves us to our own devices."
    brent "Let’s investigate."
    "I nod back, and the two of us go in."
    "Brent shows his license to the guard and allows us to go investigate."
    brent "Alright, if I were a sleazy capitalist who probably pissed off the wrong people, where would I keep my contacts?"
    show brent thinking with dissolve
    allan "...I’m sorry, what?"
    brent "If he was in contact with Lewis Bradley, he probably exchanged letters with him a bunch of times. We can use those letters to hopefully find a lead."
    show brent thinking with dissolve
    allan "What if they contacted each other through telephone?"
    brent "We’ll just have to hope they haven’t. Right now, a letter is out best bet."
    "Brent sure does like to rely on luck."
    "Then again, it’s not like this is the first time."
    "He had always relied on hunches and they almost always have never been wrong before."
    allan "Okay, you’re the expert."
    brent "Glad you trust me. Now where does a capitalist keep his letters in a place like this?"
    show brent thinking with dissolve
    "Brent stands there, clearly pondering, and so do I."
    "After a couple of minutes, the revelation pops in our heads."
    allanbrent "His office!"
    show brent smiling with dissolve
    "Though the joy quickly flushed out of me when I realized where the office was."
    allan "I...think I know where that is. Let’s go."
    "I head upstairs with Brent in tow. He followed me where the office was."
    "Scratch that, where I found Burns’ CORPSE."
    brent "Son of a- of course it’s here!"
    show brent surprised with dissolve
    allan "Makes the most sense. If he was at home, one of the best places to get killed in would be an office."
    brent "Let’s just go in and look for clues."
    show brent neutral with dissolve
    "I go in first and Brent follows."
    "Looks like the police already made their mark in here."
    allan "You think there’s anything left we can find?"
    brent "Hopefully, if not we’ll just have to check it with the police."
    "Brent and I begin our search."
    "I go through the bookshelf and the contents of each book."
    "I found a book of transactions, but they were for clients of HIS company."
    "I head to the desk instead and go through the drawers."
    "Not much I can find except-"
    "Oh..."
    allan "Hey, I think I found something."
    brent "What is it?"
    show brent thinking with dissolve
    "I grab the stack of paper I found."
    "Like I suspected, they’re business letters."
    "Brent takes them from me and goes through them one by one."
    brent "Looks like they’re say the same thing, a meeting that happened last month."
    "Last month..."
    "Wait..."
    allan "As in four weeks ago?"
    brent "Yup."
    allan "As in EXACTLY four weeks ago."
    brent "Yeah, that’s what I-"
    show brent surprised with dissolve
    "Brent eyes widened"
    "Looks like he finally caught on to what I mean."
    "I take a letter from him and read the contents."
    "I read the name of the recipient:"
    "Hugo Chambers"
    allan "Chambers..."
    brent "Another successful capitalist. Looks like the two were working with each other."
    show brent thinking with dissolve
    allan "Along with the other guys here?"
    brent "Probably, why?"
    "Hmm..."
    "Something about this doesn’t add up."
    allan "Where’s the nearest phone booth? I think we need to make a phone call."
    # Later...
    play sound phone_ring
    maybelle "Okay, I got the log book."
    allan "Thanks, Ms. Bradley."
    maybelle "You can call me ‘Maybelle’ now, Allan. I like to believe we’re better acquainted with each other to go beyond last name basis."
    allan "Oh, uh, well, thank you, Maybelle."
    brent "I can hear the butterflies flap in your stomach."
    show brent smiling with dissolve
    allan "You can’t hear a butterfly flap, let alone in a stomach!"
    maybelle "Umm..."
    allan "Oh, sorry, just talking to Brent."
    "There’s an awkward silence between the two of us. I can see Brent smiling in the corner of my eye."
    "I swat him off and continue talking to May- MS. BRADLEY."
    allan "Anyway, is there a Hugo Chambers in the log book?"
    maybelle "Give me a second."
    maybelle "..."
    maybelle "Oh, yes there is!"
    allan "Okay how about... an Elliot Hayes?"
    maybelle "Oh, yes, he’s here too."
    allan "That was fast."
    show allan surprised with dissolve
    maybelle "That’s because he’s before Chambers."
    allan "He’s what?!"
    brent "What’s wrong?"
    show brent thinking with dissolve
    allan "A transaction was made by Hayes right before Chambers."
    brent "What? Give me the phone, I want to talk to Ms. Bradley."
    "I hand the phone to Brent and he begins talking to Ms. Bradley."
    brent "It’s me, Norton. Is Chambers before Burns?"
    "..."
    brent "Ah, shit, he is?"
    "Interesting..."
    show brent neutral with dissolve
    brent "Allan, give me the names of the other two."
    allan "Right."
    "I read the other two letters and read aloud the recipients."
    brent "Allan’s going to read two more names, tell us if they’re there."
    "Brent holds the phone in front of me, I can hear Ms. Bradley on the other end as clear as glass."
    allan "I’m reading them to you now. Charles Hawkins."
    maybelle "Right here, right before Hayes."
    allan "Owen Dawson."
    maybelle "Also here, before Hawkins."
    "Brent takes the phone back to him."
    brent "Thank you, Ms. Bradley. We’ll take it from here."
    show brent happy with dissolve
    allan "Uh, bye, Maybelle."
    maybelle "Goodbye, Allan."
    "Maybelle hangs up from the other end, leaving me and Brent alone."
    brent "You two are getting chummy, ain’t ya?"
    show brent smiling with dissolve
    allan "Shut up!"
    "Brent laughs a bit, but then his face turns serious."
    brent "So, all five of these guys were all clients of Lewis, not only that but they were also his clients in a row."
    show brent neutral with dissolve
    allan "Does that mean anything or is that just a coincidence?"
    brent "We won’t know unless we investigate it."
    allan "What’s the plan?"
    brent "We investigate them in order of their transaction. We’ll first go to Chambers and then go up from there."
    allan "Sounds good, when do we go?"
    brent "10:00 tomorrow, let’s meet at that cafe we went to and head to Chambers’ office."
    allan "Alright, listen it’s late, I think I should head back to my apartment."
    brent "Sure, you’ll need the energy tomorrow. See you there, my friend."
    show brent smiling with dissolve
    allan "See ya, Brent."
    # Scene 2

    scene bg cafe with screenwipe
    "The next day, Brent and I meet up at the cafe."
    "We then leave and head to the Chambers’ office."
    brent "Hey, listen I’ve been thinking about that thought you had."
    allan "What thought?"
    brent "About the transactions being a coincidence."
    brent "I did a bit of research last night and I think it couldn’t be a coincidence."
    show brent thinking with dissolve:
        xanchor 0.5
        xpos 0.5
    allan "What makes you think that?"
    brent "Chambers’ business is creating suits, Burns’ runs a bank."
    allan "Maybe he was asking for a loan?"
    brent "Those two and three others? Unless Chambers’ agreed to make them uniforms for all their companies, I doubt they would hold a PRIVATE meeting just for that."
    show brent neutral with dissolve
    allan "So uniforms is still in the air for possibilities?"
    brent "Get in the head of a capitalist, Allan, why would your workers need uniforms if they’re going to work in a factory?"
    allan "Okay, okay, point taken."
    allan "So how do we meet with Chambers?"
    brent "Right about...."
    play sound footsteps
    "In cue, a carriage stopped in front of the office. Stepping out of it was a man being followed by a couple of policemen."
    brent "Now."
    show brent neutral with dissolve
    "We walk and stop Chambers in front of his office."
    chambers "Anything I can do for you two?"
    brent "Actually, yeah. We would like to ask you a few questions."
    show brent confused with dissolve
    chambers "For what?"
    "Brent opens his mouth, but he shuts it quickly."
    "I guess saying directly the case isn’t a good idea."
    "He still tries to find a good answer."
    "Looks like I have to step in."
    allan "I’m writing a paper you see, and I need to speak with you for it."
    "Chambers stays silent, he holds his chin with his hand."
    "He then nods."
    chambers "What the hell, I’m not busy. Meet me in my office upstairs."
    "He leaves with his bodyguards and steps in his office."
    brent "Nice recovery."
    show brent smiling with dissolve
    allan "Thanks, you learn a lot when you’re a journalist."
    "We head in and go upstairs."
    "We find his guards standing in front of a door."
    "If I were a betting man, I guess that’s where Chambers’ office is."
    "The guards let us in and we meet face to face with Chambers sitting in his chair."
    chambers "Alright boys, what would you like to know."
    "Brent and I nod at each other and he steps up."
    brent "What was your relationship with Burns?"
    show brent neutral with dissolve
    chambers "Burns?"
    allan "Yes, have you two worked with each other?"
    chambers "You aren’t implicating me for something, are you?"
    brent "We aren’t implicating you, are we, partner?"
    show brent smiling with dissolve
    allan "No, absolutely not."
    brent "We would just like to know since there has been word going around the two of you have been meeting up?"
    "Chambers stays silent, and I think his body tenses up as well."
    chambers "I just asked him for a loan."
    brent "Just a loan?"
    show brent surprised with dissolve
    chambers "Just a loan?"
    "Brent and I look at each other, I guess that was an easy question to answer regarding a banker."
    allan "Okay, how about Hawkins?"
    chambers "Hawkins?"
    allan "Yes, word on the street is you meet up with him too."
    chambers "We’re drinking buddies. We meet up with each other every saturday night for drinks at a local bar."
    allan "Weird that the two of you are drinking buddies, if I can recall Hawkins is a lot younger than you."
    chambers "Even people as old as me can have friends as young as you, son."
    "Brent looks at me and furiously shakes his head. He then drags me off to the otherside of the room."
    brent "Allan, don’t say anything that sounds remotely insulting. We want his cooperation as much as possible."
    show brent neutral with dissolve
    allan "Right, right sorry. Anyway, this is getting us nowhere; he keeps dodging the questions. I say we drop the big guns."
    brent "Big guns...?"
    show brent confused with dissolve
    "I walk back over to Chambers and I get my notebook, pretending to write something."
    "I think it makes it look more convincing."
    allan "Next question, what was your relationship between you, Charles Hawkins, and Lewis Bradley."
    "Chamber eyes widened, that seem to got him."
    "He coughs and then continues talking."
    chambers "I don’t know this ‘Lewis Bradley’ you speak of."
    allan "Really? A bunch of other reports beg to differ."
    brent "Al-"
    allan "Relax, man, I got this."
    allan "Did you two meet up? For more drinks? Or was it for a machine you wanted him to build?"
    "Chambers stays silent, he doesn’t bother to say anything."
    "I look at Brent, expecting him to be impressed, but instead his face is neutral."
    "Finally Chambers opens his mouth."
    chambers "Security!"
    "What"
    play sound door_break
    "The door slams open and the two guards come in."
    "They grab me and Brent by our arms and haul us out."
    chambers "I won’t be badgered by these questions anymore. Take them out now!"
    "The guards nod to him and next thing I know the two of us are outside."
    brent "You know what you’re doing, huh?"
    show brent neutral with dissolve
    allan "Okay, so maybe being a journalist doesn’t translate well with being a detective."
    allan "Sorry, Brent."
    brent "It’s okay, judging by Chambers’ reaction to your questions we were getting on to something."
    show brent neutral with dissolve
    allan "You think so?"
    brent "Yeah, I think he knows something about Lewis."
    show brent thinking with dissolve
    allan "Well, how do we investigate? He locked us out."
    brent "Don’t worry, there’s a way. What time is it now?"
    show brent thinking with dissolve
    "That’s a weird question to ask."
    "I look at my watch and read the time."
    allan "Almost noon."
    brent "Good, follow me, I have an idea."
    show brent smiling with dissolve
    "I follow brent to the back of the building."
    "There’s a fire escape at the back."
    brent "I think that escape leads to the hallway that Chambers’ office is located in."
    brent "We just need him and his guards out. How much longer until noon?"
    show brent neutral with dissolve
    allan "Um, it’s noon now actually."
    brent "We can’t waste time then. Come on, follow me."
    show brent neutral with dissolve
    "Brent climbs up the fire escape and I follow suit. He ducks under an open window but peers through it; I do the same."
    "The two guards are still standing there, but soon Chambers’ walks out as well."
    "He tells the guards something but I can’t read lips."
    "The guards nod at him and the three leave the hallway."
    brent "It’s noon, right? Y’know what time is noon?"
    show brent smiling with dissolve
    "I wonder for a moment, and then it hits me."
    allan "Lunchtime!"
    "Brent quickly shushes me and clamps my mouth."
    brent "Not so loud! Anyway, yeah, let’s go in before they head back."
    "Brent climbs through the window, I try to follow suit but he signals me to stop."
    "He looks around, then he signals me to go in."
    "I climb in and the two of us head in the office."
    brent "Quick, his desk, look for clues."
    "I nod and I start rummaging through his desk."
    brent "Be sure to leave things like how you found them, we don’t him to know we were here."
    allan "Right, of course."
    "Man, being a detective involves being really meticulous."
    "Brent was always the more organized among us, I was more in the middle of messy and organized, leaning in slightly on messy."
    "Probably one of the many signs why I was never going to be a scientist like my parents."
    "I open another drawer and I find a bunch more documents."
    "I take each of them out, lo and behold, they’re letters for our four clients."
    "If that’s not a sign, I don’t know what is."
    "I read the first paper I found, it was made two months ago for Elliot Hayes."
    brent "Find something?"
    show brent confused with dissolve
    allan "Yeah, a letter for Hayes."
    "I give it to Brent and he starts scanning it."
    brent "Mr. Bradley is mentioned here."
    show brent surprised with dissolve
    allan "Seriously?"
    "He nods."
    brent "With a mention of a ‘body’."
    show brent confused with dissolve
    "I take a big gulp, that’s a BIG red flag."
    allan "Define ‘body’?"
    brent "I’m...not sure. It says here, quote, ‘Bradley lacks the parts nor the funds for it. I suggest Burns starts paying for it once my contract is done.’"
    show brent neutral with dissolve
    allan "Wait, so he knew Burns was going to create a contract with Lewis?"
    brent "Sounds like it, yeah. But why?"
    show brent neutral with dissolve
    "I scratch my head, this really doesn’t make sense. I get another letter and read its contents."
    "It’s not for one of the clients, but instead someone I’ve never heard before."
    "It also mentions...."
    allan "Hey, was Chambers a devout Christian?"
    brent "What makes you say that?"
    show brent confused with dissolve
    allan "There’s a letter here mentioning bishops. What does he want with the Church?"
    "Brent eyes widens at the word of 'bishops.'"
    brent "How is it spelt?"
    show brent neutral with dissolve
    allan "I’m sorry?"
    brent "Bishops. Is there a capital ‘B’ in all of its mentions."
    "I scan the letter again."
    "Just like Brent said, all of mention of 'Bishop' has its B capitalized."
    allan "Uh, yeah."
    brent "Son of a- they have ties to them?!"
    show brent surprised with dissolve
    allan "To who?"
    brent "I’ll tell you later. We just got another lead. Let’s get the hell out of here before Chambers gets back."
    show brent neutral with dissolve
    "I quickly put back the letters where I found them and we quickly leave the office."
    "We climb back out through the window and down the fire escape."
    "After we distance quite a bit from the office, I finally asked Brent."
    allan "So what was so important about ‘Bishops’, anyway?"
    brent "They’re a gang here in London."
    allan "Oh, okay."
    "...."
    "...."
    "Woah, wait, hold the phone!"
    allan "They have ties to a gang!"
    brent "And one of the more ruthless one’s too. Looks like these guys are more corrupt than we thought."
    show brent neutral with dissolve
    allan "You aren’t thinking about confronting them, are you?"
    brent "No choice, it’s out best lead. I know where they gather. Just stick by me."
    "I gulp and I nod."
    "Brent and I head get a carriage."

    # Scene 3
    scene bg cafe with screenwipe
    "The carriage takes us into a bar."
    "It’s not far from the office, but far enough to not be able to walk here."
    "At least in short notice."
    "We go in and find a bustling place. Glass clinking, endless chattering and laughter, music from a piano, and the reeking of booze"
    "It’s mostly filled with men. The only women here are the bar hostesses."
    allan "Seems lovely."
    show brent neutral with dissolve:
        xanchor 0.5
        xpos    0.5
        
    brent "I guess."
    show brent thinking with dissolve
    "Brent holds his chin and scans the entire bar."
    brent "If I had to guess everyone in this bar are members of the Bishops."
    "I’m pretty sure Brent unintentionally said that loud enough for the whole bar to hear."
    "The music stops playing and all sounds stop in an instant."
    "The entire bar then turn their heads to us."
    show brent confused with dissolvelong
    brent "Did I say something wrong?"
    "A big guy with a cigar from a far stands up and walks towards us."
    bishop1  "You got a problem wit’ us, mate?"
    show brent confused with dissolve
    brent "Um...no?"
    bishop1 "Well how da hell did ya know we lot here are Bishops?"
    show brent surprised with dissolve
    brent "Are you denying that or-"
    "Another Bishop stands up, knocking his chair down."
    bishop2 "And what if we were deniyin’ it? You got a problem wit’ that?"
    "I nudge Brent as hard as I can with my arm."
    show brent surprised with dissolve
    allan "This is a bad idea....! We need to go...!"
    show brent thinking with dissolve
    brent "Not until we get our answers."
    bishop1 "Answer you say? What are you a cop?"
    "At the word 'cop', like fifteen other people started standing up and started to walk to us."
    show brent thinking with dissolve
    brent "A private eye?"
    bishop2 "Oh, private eye, well ‘aye, aye’ to you sir."
    "The Bishop salutes to Brent and a couple of people laugh it off."
    "I was confused at first, then the joke clicks in."
    allan "I don’t think you salute to a private."
    "That got their attention. One of the Bishops then turn to me."
    bishop2 "Smart guy, eh?"
    "From afar, I heard the sound of a piece of wood being broken."
    "I look over at the direction and see the piece of wood being thrown at the guy in front of me."
    bishop1 "What exactly does a private eye want wit’ us?"
    show brent neutral with dissolve
    brent "Just to ask questions...?"
    "Brent and I slowly back off to the door, but then two other beefy guys show up and block our only exit."
    bishop1 "Questions for a case?"
    show brent confused 
    brent "Yes...?"
    bishop1 "Sorry, lads."
    bishop1 "But the Bishops don’t tell no secrets!"
    "The two guys behind us grab our arms and then more Bishops start to surround us."
    allan "Wait, at least hear us out!"
    bishop2 "Sorry, mate, but we don’t any law enforces snoopin’ around!"
    allan "Hugo Chambers! We want to talk about Hugo Chambers and his associates!"
    bishop2 "Don’t care, lad!"
    "He raises his 2x4 in the air and I close my, bracing for impact."
    unknown "Enough!"
    "The Bishop stops mid-swing and turns around."
    "The Bishops surrounding us swarm off, revealing a man sitting at a bar counter."
    unknown "Let them speak. I want to talk to them."
    bishop2 "But boss-"
    bishopb "We need to do this! Bring them to me."
    "The two guys let us go and the Bishops start to back away from us."
    "Nervously, we walk to the bar counter."
    show brent thinking with dissolve
    brent "Why did you save us?"
    bishopb "Killing isn’t in our morals; we don’t condone it."
    show brent surprised with dissolve
    brent "Seriously?"
    bishopb "Yes, you also mention Old Man Chambers?"
    "The two of us nod. The Boss gestures to us to the seats next to him."
    bishopb "Have a seat, I’ll tell you what I know."
    "We take a seat and soon the bar goes back to normal."
    "Damn, I’m so glad for the return to normalcy. I can feel my heart wanting to take the next train out of my body."
    bishopb "Sorry about my boys, they can get a bit rowdy."
    "I look back behind me and see the same two Bishops that threaten us laugh at a some joke someone made."
    allan "‘A bit’ is an understa-"
    play sound slap_face
    "*SMACK*"
    "Brent hits my arm again, I turn to him and he just puts his finger on his lips and shushes."
    "Right, don’t say something remotely insulting."
    bishopb "What do you two want to know about?"
    show brent confused with dissolve
    brent "What kind of business did Chambers have with you guys?"
    "The Boss takes another drink from his mug."
    bishopb "Ah, yes, that was a long time ago."
    allan "When did you stop doing business with him?"
    bishopb "Last month, really. But yes, he and some other capitalists did business with us."
    show brent confused with dissolve
    brent "Other?"
    bishopb "You see, back then, him and some of his friends came to us to strike a deal."
    bishopb "It was a simple job, find some doctors and threaten them for a discount on medicine for them specifically."
    allan "You guys did that?"
    bishopb "For two years that was what they wanted us to do. But then one day they came to us for a different plan."
    "He took another drink and smack the mug to the counter."
    "The bar hostess takes his mug and brings him another full one."
    bishopb "They started asking us to find these people and bring them to them. We didn’t really care at the time and I just assumed they were friends of theirs."
    bishopb "Soon, though, I started noticing the ones asking for certain people weren’t in their age group, nor did they even know them personally. I started to get suspicious but I didn’t act because for all I knew I was just jumping to conclusions."
    "He stayed silent for a few moments. He took a big breath and continued."
    bishopb "Then I found a missing person poster for one of the people they asked me to bring."
    "Our eyes widen."
    bishopb "I confronted them about it. Y’see, threatening and things like that is something we don’t mind doing, but killing is a level we will never stoop to. They denied my accusations when I said they killed them so I later broke off our contract and never spoke to them again."
    show brent confused with dissolve
    brent "If you knew about this why didn’t you call the police?"
    bishopb "Brilliant idea, kid, a crime boss going to the police about a crime some people were doing that I was involved in. Yeah, that won’t get me to prison."
    "Brent huffed as the Boss took another drink."
    bishopb "Sorry, kid, but I like my freedom. Besides I don’t got evidence to point at them."
    allan "So why talk to us?"
    bishopb "Because you two are smart, I can tell. You went to us directly wanting to know what the hell Chambers is doing. If anyone is going to catch those bastards and what they’re doing I think it will be you two."
    show brent neutral
    brent "Finding the truth of this case might get you guys in trouble, though."
    bishopb "Well, then I have time to find a lawyer. Whatever happens to us, or at least the ones involved, me included, is our own fault. We never condone killing, even if we are indirectly responsible."
    "For some reason, I find some new respect for these guys."
    "Mind you, not enough to consider forgiving them for almost beating me up, but they at least have enough moral standards. At least enough to show us tell us something."
    allan "One last question, is that okay?"
    bishopb "Spill."
    allan "Have they ever mention a ‘Lewis Bradley’ to you guys?"
    "The Boss taps his chin."
    bishopb "Bradley...Bradley...Bradley...."
    bishopb "Ah, yes, they mention a Bradley."
    "A Bradley."
    "I looked over to Brent, there were only two Bradleys right now."
    show brent neutral
    brent "Which one?"
    bishopb "Can’t remember. It was a really long time ago. It was one of their last request before I decided to break off."
    "I’m pretty sure I’m out of questions for him."
    "I nod at Brent and the two of us stand."
    brent "Thank you for the info."
    "I nod in agreement and we head for the door."
    bishopb "Good luck, boys! You two are going to need it."
    "We get another carriage and head back to Chamber’s office."
    "The receptionist at the front desk stops us before we go in."
    reception "Do you two have any business here?"
    allan "Yeah, we would like to talk to Mr. Chambers."
    "With the info we got from the Bishops, there’s no doubt in my mind that Chambers has something to do with Lewis’ disappearance."
    reception "Sorry, but Mr. Chambers is unavailable right now."
    show brent surprised with dissolve
    brent "He’s what?"
    reception "Yeah, he and his guards left during lunch break."
    "I curse to myself, they slipped past us while we were out."
    "We head back out and I talk to Brent."
    allan "You think they’re trying to run from us?"
    show brent neutral
    brent "I don’t know about the guard but Chambers is for sure."
    allan "How do we find them?"
    brent "Same way we found our last lead."
    "Brent walks behind the building and I follow suit."
    "We climb the fire escape and go in through the window."
    "It was past 18:00 so no one was probably still here. We go inside the office, but it’s completely dark."
    "Though knowing the rich bastard, he’d probably have..."
    allan "Found it."
    "I switch on the lights in the room."
    show brent neutral
    brent "Man’s got electricity running in his office, should’ve known."
    "These damn rich people and their luxuries."
    allan "We need to hurry, people will notice the light’s on so find what we need."
    "Brent nods, and we head to the desk."
    "There are two papers there."
    show brent thinking with dissolve
    brent "Were those always there?"
    "I shrug, and I take the paper on top."
    "'Winchester Building, Westminster Abbey' it says."
    brent "Westminster Abbey, that’s one of the slums here in London."
    allan "Why would it mention that place?"
    show brent neutral
    brent "I dunno, but it’s worth checking."
    "I nod, but I also grab the other letter."
    "It looks like a standard business letter, it’s not addressed to any of the clients we’re investigating, instead its recipient is 'Kasper Clark'."
    show brent thinking with dissolve
    brent "Clark?"
    allan "I know that guy, he was a capitalist who was arrested for smuggling opium to China, right?"
    brent "He was. Why is there a letter for him here out in the open?"
    allan "Chambers was most likely reading through some old letters. I don’t think Clark has something to do with this."
    brent "Yeah, I guess you’re right. The man’s arrested, anyway."
    brent "Let’s go head to Westminster."
    "I nod back and put the letters back where we found them."
    "We sneak out the building and get a carriage to Westminster."
    "..."
    "Clark..."

    # Scene 4:
    scene bg oldOffice with dissolvelong
    "Remember that gazette I hate working for?"
    "Well, when I was starting to work there I was a bit thrilled."
    "And in need for rent."
    "I remember my first job there. I had two options on what I needed to write about."
    "Either the queen’s trip to Japan,"
    "Or about the famed capitalist Kasper Clark who plans on extending his work to China."
    "On one hand it’s about the queen, and everyone loves to hear about the queen."
    "On the other, it’s very informative and more important to know about in today’s time."
    
    menu:
        "Write about Clark, the queen’s story is overrated.":
            $ wroteTo = "Clark"
            jump writeClark
        "Write about the queen, I might get a chance to meet her!":
            $ wroteTo = "Queen"
            jump writeQueen

label writeClark:

    "Clark is more important to the new anyway."
    "The queen may be royalty, but writing about Clark might get us some new info about products Clark’s making."
    "Besides, I doubt I’ll get a story out of the queen without getting kicked out by the guards."
    "In the next week, I was able to write a good enough story about Kasper Clark."
    "Extending to China was his plan so that he’ll have more space to construct factories and access to more resources."
    "Unfortunately, the paper didn’t sell a lot."
    "It was my first set back, but I slowly began to realize how literally zero people know about my gazette."
    "But that wasn’t the shocking part of the story."
    "Two weeks after I published my story, Clark was arrested for charges against smuggling."
    "Apparently he was smuggling opium into China to make more money."
    "The police arrested him and soon closed down his company and everyone working for it."
    "Did I take the opportunity to write about it?"
    "Yes, yes I did, but that STILL didn’t garner more people into reading our paper."

    jump writeContinue

label writeQueen:

    "Screw it, if I’m going to start being a journalist, I need to write something big."
    "The queen it is!"
    "I was able to get enough information from the queen in her little conference with a bunch of other reporters."
    "I’m also proud to say I even got a chance to ask her some questions."
    "By the week after, I wrote a good story about the queen’s trip and it was published."
    "Unfortunately, the paper didn’t sell a lot."
    "It was my first set back, but I slowly began to realize how literally zero people know about my gazette."

    jump writeContinue

label writeContinue:
    "But that set back wasn’t going to stop me!"
    "...Is what I told myself at first."
    "The more stories I wrote, the lesser people bothered to read them, the more I got discouraged into even wanting to work here."

    # Scene 5
    scene bg city with screenwipe
    show brent neutral with dissolve:
        xanchor 0.5
        xpos 0.5
    brent "Allan, are you spacing again?"
    allan "Hm?"
    brent "Something up?"
    allan "Sorry, I was just thinking about Kasper Clark."
    brent "Oh, what about him?"
    show brent thinking with dissolve
    allan "Well..."
    
    if wroteTo == "Clark":

        allan "I wrote an article about him and his new business plan. It was my first article working for the gazette."
        brent "Oh, yeah, I know."
        show brent neutral with dissolve
        allan "You do?"
        brent "Yeah, remember when I said I read an article? Well the article was the Clark incident. You mentioned his partner company in China and I remember they were rumors about them being smugglers."
        brent "In a few days I was able to find proof they were smuggling opium and forwarded it to the police."
        allan "Oh..."
        brent "So in a sense I should thank you. I wouldn’t have solved that case if you hadn’t wrote that article."
        allan "Don’t mention it."
    
    elif wroteTo == "Queen":
        
        allan "I had a choice between writing about the queen and writing about Clark when I first wrote for the gazette."
        allan "Ended up writing about the queen."
        brent "Oh."
        allan "It just brought up memories, that’s all."
        brent "I had a case about Clark once."
        allan "Really?"
        brent "Find someone’s relative working for him. But I couldn’t find any clues or evidences. It wasn’t until LeBlanc arrested him that I was able to find the lost relative, though that took a year’s time."
        allan "First hard case for you?"
        brent "Yeah, basically."
    
    "The carriage stops and I look out. We’re by Westminster."
    brent "Let’s go."
    "We head out and walk down Westminster Abbey. The slums are as dirty and dark as one would think."
    "Expected no less from one of the most notorious slums in London."
    "We make it to the Winchester building."
    brent "Guard up. This looks suspicious."
    "I nod and we go in carefully."
    scene bg black with screenwipe
    "It’s dark..."
    scene bg warehouse with screenwipe
    "I can only make out the a few stuff in here."
    "I think it’s a warehouse?"
    "Wha-?"
    unknown "So you’ve come."
    "Who...?"
    show ghepetto with dissolve 
    brent "Are you the Ghepetto Killer?"
    show brent confused with dissolve
    "Getting straight to the point??? Is that a good idea???"
    unknown "A fitting name... I like it."
    show ghepetto with dissolve
    allan "Do you know where Chambers is?"
    ghepetto "Oh..you mean..."
    "He points somewhere behind us."
    "It’s a room."
    "The window lights up, there’s three silhouettes."
    allan "Is that..."
    ghepetto "Chambers and his two bodyguards, yes."
    show ghepetto with dissolve 
    allan "Why are they here?"
    ghepetto "To pay for their crimes."
    show ghepetto with dissolve
    brent "Crimes?"
    show brent confused with dissolve
    ghepetto "You two are still unaware. No surprise there. Mankind is so ignorant to things that serves no interest to them. They show no consideration to others unless it serves them. Like survival, or money..."
    
    if wroteTo == "Clark":
        ghepetto "Or maybe even fame. Isn’t that correct, Brent?"
        show ghepetto with dissolvelong
        brent "...How do you know my name?"
        show brent confused with dissolve
        ghepetto "Have you, Brent Norton, even consider the weight of your actions? How arresting one man could hurt or change anything?"
        show ghepetto with dissolve
        brent "I’ve no idea what you mean. I haven’t exactly got that many people arrested."
        show brent confused with dissolve
        ghepetto "You wouldn’t be aware obviously. Like I said, humanity is ignorant unless it’s in their interest."
        "Who the hell was this guy? Why’s he telling us his manifesto?"
    
    ghepetto "But enough about that, let’s get this started. I’m sure you’re dying to know what will happen to Chambers, no?"
    play sound metal_wheels
    "*CLANK* *CLANK*"
    "That sounds like metal..."
    "We look back at the room, there’s another figure standing behind the three men."
    brent "What the hell’s that?"
    show brent confused with dissolve
    ghepetto "Let’s just say it really wants to know the inside of Chambers."
    show ghepetto with dissolve
    "Inside?"
    "INSIDE?!"
    allan "I don’t like the sound of that!"
    "Brent and I rush in."
    "There’s no stairs leading to the room from our end, but there is at the end of the building."
    brent "Allan, up!"
    show brent surprised with dissolve
    "I look up, and I see metal bars falling over us!"
    "We dodge in time, and I look up to see some figure looking over us."
    allan "What the hell’s that?"
    brent "I don’t know, just run!"
    show brent thinking with dissolve
    "We rush to the stair and get our butss moving then-"
    scene bg black with screenwipe
    "The lights go out."
    allan "Crap! I can’t see!"
    "I could hear more metal clanking, it’s coming from above us."
    "The windows on the roof is revealed; a skylight. It barely manages to illuminate the warehouse."
    "That helps..."
    "*CLANK* *CLANK*"
    "That came from behind us."
    "We turn around."
    "In the shadows, I see a figure-"
    "No, a face."
    "And it’s got a sinister smile."
    "Ever saw a clown smiling before? Always creeped you out, right?"
    "That’s what it was."
    "And I could only say one thing."
    allan "RUN!"
    "We bolt out and head up the stairs."
    "Clanks and more clanks came from behind us."
    brent "Whatever that thing is, it’s not human!"
    show brent surprised with dissolve
    "I turn to my left and I see metal barrels."
    "Could I...?"

    menu:
        "Topple the barrels.":
            jump toppleBarrels

        "Leave them alone.":
            jump leaveBarrels

label toppleBarrels:
    "It might be able to trip it."
    "I rush to the barrels and throw them to the ground."
    "They slid across the floor blocking our path."
    brent "Smart plan, Al-"
    "I can’t hear him, adrenaline is rushing over me. I keep running, until I realize my footsteps are the only one that’s heard."
    allan "Brent?"
    "Upon my request, something was thrown to me."
    "It was a body, a limp body."
    "With a bloody blow on Brent’s head."
    allan "Brent?"
    "My voice trembles, and I see the figure walk to me again."
    "There’s something in its hand."
    "It’s one of the barrels."
    "Its smile is the last thing I remember before the barrel is thrown to my face."

    "GAME OVER"
    scene bg gameOver with fadelong

    return

label leaveBarrels:
    "Nevermind, there’s no time!"
    "We pass the barrels and rush to the room."
    "Brent grabs a hold of the doorknob but it isn’t budging."
    brent "It’s locked!"
    "He reaches into his pocket and grabs a hair pin...and a screwdriver."
    "Guess he just keeps that around."
    "He inserts the pin into the lock and starts doing his magic, lock picking."
    "Wait..."
    "The metal clanking stopped."
    "Did...did that thing stop chasing us?"
    "*CRASH*"
    "That came from the inside of the room!"
    allan "Hurry, man!"
    brent "I’m doing my be-"
    "*SPLAT*"
    "I look at the window, I can’t see the shadows."
    "Mostly because the window is covered in red."
    brent "GOT IT!"
    "Brent slams the door open and I go in with him."
    "There wasn’t a killer, a machine, or a living person in the room."
    "Just three bodies with no skin, no jaw, and no clothes."

    # Chapter 3:
    scene bg streets with dissolvelong    
    show simon mad with dissolve:
        xanchor 0.5
        xpos 0.5
    show brent neutral with dissolve:
        xanchor 0.5
        xpos 0.75
    leblanc "..."
    brent "..."
    allan "..."
    brent "So...fancy meeting you here, Simon."
    leblanc "Quiet, Norton. And it’s Detective LeBlanc!"
    "LeBlanc was around the area, we looked for a police in order to send the bodies out and hopefully get help."
    "We were lucky LeBlanc was a few blocks away."
    leblanc "Anyway why are you two here?"
    brent "My job, I’m investigating a case."
    leblanc "That happens to involve the murder of the Ghepetto Killer?"
    allan "Look, I can vouch for him, we’re just doing a case."
    leblanc "Sorry, boy, but you don’t exactly get a say in this. You’re just as suspicious."
    show brent confused with dissolve
    brent "Suspicious?!"
    leblanc "Look, I’m just doing my job. Right now you two are potential suspects. I’m not saying you are, but you are potentially."
    allan "Well, we’re not! Ask Chambers’ receptionist, we wouldn’t have enough time to get their skin off in 2 hours!"
    show simon neutral with dissolve
    leblanc "How do you know the victim was Chambers?"
    "I flinch."
    brent "You don’t know it’s Chambers and his bodyguards?"
    leblanc "No skin, so no fingerprints. No clothes, so no way of finding indication of an ID. And no jaw, so no dental checking to find a match."
    leblanc "And you said it was Chambers?"
    "Brent holds the bridge of his nose and sighs."
    brent "He wasn’t in his office when we checked."
    leblanc "He could’ve not been there. Either way there’s to ID the bodies so for all we know it might not be Chambers’."
    "That’s reassuring because that means we’re not getting arrested, but..."
    "We know it’s Chambers."
    leblanc "Look, I have a job to do. You two try to stay out of my way next time."
    "He leaves, but I pull him in one more time."
    allan "Has anyone else gone missing this past month?"
    leblanc "I’m not allowed to tell you that."
    allan "Yeah, but I’m a reporter, I’m obliged to know."
    "LeBlanc sighs and pulls out a piece of paper."
    leblanc "I’m allowed to not reply but maybe if you write about it that will convince the people to be more careful at night."
    "He passes me the paper and leaves."
    hide simon
    "I look at the paer, five people in the list."
    brent "Why the missing people report?"
    allan "I have a hunch."
    hide brent
    scene bg cafe with dissolvelong
    "The next day..."
    "Brent and I meet up with Maybelle at the cafe from two days ago."
    "She has the log book with her."    
    show maybelle happy with dissolve:
        xanchor 0.5
        xpos 0.5
    show brent neutral with dissolve:
        xanchor 0.5
        xpos 0.75
    allan "Thanks, we really need this."
    maybelle "Anything to help."
    "I take the log book out of her hands and look over the clients again."
    "And as luck, or rather bad luck, would have it..."
    "The five missing persons are in the list. All in a row."
    show brent thinking
    brent "Bingo."
    brent "If these guys were killed by the Ghepetto Killer, then that means he’s targeting them specifically."
    allan "Okay, but why? And what connection does it have to Mr. Bradley?"
    brent "Well, I have one theory."
    show brent surprised with dissolve
    maybelle "Um, excuse me?"
    show maybelle neutral with dissolve
    "I flinch at Maybelle’s voice, we look up from the book and see her worried"
    "face."
    maybelle "Are the men in your list dead?"
    allan "Well, more like missing."
    maybelle "And they were all clients of my brother?"
    "I don’t like the looks of this."
    "She turns to Brent."
    maybelle "And your theory is...?"
    show brent neutral
    brent "...I’m sorry, Ms. Bradley. But given the circumstances, I have to place your brother as a suspect. Everything that’s going here can’t be a coincidence."
    show maybelle confused with dissolve
    "Maybelle’s eyes turn dark."
    "*SMACK*"
    "She slaps Brent flat on the face and takes the book from me."
    maybelle "This is absurd! My brother wouldn’t go to such lengths!"
    "Brent rubs his face. You can actually see the hand mark on his cheek."
    show brent surprised with dissolve
    brent "How would you know that?"
    maybelle "Because he’s my brother! He would have told me if something was going on with him!"
    brent "Again, how would you know that?"
    "She doesn’t reply, instead..."
    "*SMACK*"
    "Another smack on his face. With that she leaves the cafe."
    hide maybelle
    show brent neutral with dissolve:
        ease 1.5 xpos 0.5
    allan "Well, that went well..."
    brent "Yeah, totally."
    allan "Can you really suspect her brother? Maybe it IS just a coincidence."
    brent "Not from what were gathering. Besides..."
    "He looks away and rubs his cheek again."
    brent "Even the people you least expect can be a suspect."
    "I can’t read his face."
    "It looks... hurt."
    unknown "Got smacked by a client again, Brent?"
    "Someone else approaches us."
    "And his grin is very noticable."
    brent "Yeah..."
    unknown "Boy, you got to learn to keep some suspicions to yourself. Otherwise, YOU might end up in the police’s missing persons list."
    brent "Let’s not go there."
    allan "Hey, um... who’s this?"
    "The other guy looks at me and gives another toothy grin."
    unknown "Oh, where are my manners? I’m Henry, an informant of Brent. You must be the new partner."
    "He reaches out his hand and I shake it."
    allan "Allan Lorenz. I’m a reporter for this case."
    henry "Cool!"
    brent "Got what I need?"
    henry "Yup."
    "He takes a seat and his face turns serious."
    henry "So all those capitalist, from what I’ve gathered haven’t just been seen in the same bar form time to time. They also contracted various illnesses. All of which are very fatal."
    allan "Fatal?"
    henry "Yup, TB, cancer, one has HIV, not fatal but still something to worry about, and plenty more."
    "He says it with a bit too much enthusiasm..."
    allan "That explains why they were hiring the Bishops to intimidate people."
    henry "Found that out too, but that’s not all. They all went to the same neurological doctor."
    show brent thinking with dissolve
    brent "Neurological doctor?"
    henry "Yup, don’t know why, though. Here’s the name of the doctor and his address."
    "He hands us a piece of paper and I take it."
    "Why would a bunch of capitalist with fatal illnesses go to a neuro doctor? To trick their brain into not being sick?"
    henry "Well, that’s all I got. Need anything else?"
    brent "No, thanks for your help, Henry."
    henry "Gladly!"
    "Henry leaves the cafe and waves at us as he goes."
    allan "He’s really cheerful."
    brent "He’s a bit of a masochist. And probably crazy."
    allan "Should we be worried?"
    brent "Not yet."
    "I look a the paper and it’s address. It’s not a place I;ve been to before in London."
    allan "Well, we got an address. I say we head there."
    "Brent nods and we head out."
    # Scene 2
    scene bg streets with screenwipe
    "It’s at a slum."
    "How the hell does a neuro doctor live in a place like this?"
    "Is he not making enough money?"
    "Well, whatever, we find his clinic after a short walk. At least it’s not far."
    "I shudder about having to knock another door."
    "Luck hasn’t exactly been on my side when it comes to doors."
    "I knock it anyway."
    scene bg oldOffice with screwdriver
    "After a few moments, the door opens again."
    "An elderly man with glasses meets us."
    show brent neutral:
        xanchor 0.5
        xpos 0.5
    doctor "Do you two have an appointment?"
    brent "No, sir, but we do need to talk to you."
    "The doctor nods and lets us in."
    "The clinic is filled with a bunch of diagrams of the brain, models of the brain, but there’s also some normal stuff to see here like cabinets and pills."
    doctor "I’ve been living in this part of London so I can care for the people here, they’re in desperate need of a doctor you see."
    allan "Aren’t you a neuroscientist?"
    doctor "I am, but I also have knowledge in medicine."
    "Brent and I look at eachother."
    brent "Well, if that’s the case, were you threatened by the Bishops by any chance?"
    doctor "The Bishops? No, never."
    allan "Then did you have an appointment with Hugo Chambers?"
    doctor "Oh, wait let me check my log book. The name rings a bell."
    "The doctor picks a book from his cabinet and goes through it."
    doctor "Here we are! Hugo Chambers, about two years ago."
    "We go over to the doctor and sure enough he was there."
    show brent thinking with dissolve
    brent "Was he with a bunch of other people around his age?"
    doctor "No, just some young fellow. Very charming."
    "Hawkins, I’m assuming."
    doctor "Though, if memory serves me right, they didn’t come here for a check-up."
    allan "They didn’t?"
    doctor "No, they talked wanted to talk about some of my old researches that didn’t go far. They were all about brain mapping and the brain itself, you see."
    "Wait...I think I recognize the word brain mapping."
    allan "What was your research about?"
    doctor "Oh, well, I wanted to see if it was possible that the brain would still retain all its information stored inside it even if it was removed."
    brent "Sounds complicated."
    doctor "It was, and if my research team and I had enough budget and a way to test our research, we could’ve proven whether or not it was possible!"
    brent "Wait, so is it?"
    doctor "We never got to find out. Our budget was removed so me and my team went our separate ways. That’s how I ended up here."
    brent "Where’s the research?"
    doctor "Oh, I don’t have it. I gave it to the young man. He said he was also doing a research like it and needed mine to understand so I gave it to him, don’t need it now anyway."
    "Brent pulls me away far from the doctor’s ear."
    brent "Hawkins, doesn’t specialize in a science like neuroscience in anyway. He runs a railroad, there’s no way he would need this."
    allan "Okay, but why?"
    show brent thinking with dissolve
    brent "I don’t know, but..."
    "Brent takes out a paper, it’s the list of the other clients in Lewis’ log book."
    brent "I do know the other guys have something to do with it, and I know they’re next."
    "I nod back, he’s right."
    "We know what’s gonna happen to them if we don’t do anything."
    brent "Thank you, doctor. We’ll be on our way."
    doctor " No, thank you, it’s nice to have visitors every now and then."
    "I smile at him, what a nice old man. Naive, but nice."
    "We leave the slums and get a carriage."
    "Brent rationalizes that the Ghepetto Killer is getting them by order of the date they made the transaction, so up next in our list is Elliot Hayes."
    "Hayes runs a factory that creates machinery for other factories, and word has it he stays in his factory for awhile longer to tinker."
    "So that’s where we go."
    "We find his factory, but it’s locked."
    allan "Can you pick the lock?"
    brent "Too risky, not out in the open."
    "We look around the factory, and we find a fire escape."
    allan "Every building in London has one, don’t they?"
    brent "Seems like it."
    "We climb the stairs and luckily enough the window is unlocked. We climb in."
    scene bg newOffice with screenwipe
    "I expected it to be a hallway, but it isn’t, it’s an office."
    show brent confused with dissolve
    brent "Who’s..."
    "I grabbed the plaque, it reads, 'Elliot Hayes, CEO.'"
    allan "Son of a gun has his own fire escape..."
    "Brent goes through his drawers."
    allan "Looking for more clues?"
    brent "You never know."
    "He goes through the drawers and stops somewhere."
    "He gets whatever is in the drawer, it’s a book."
    brent "No way..."
    "{i}Retaining information in the brain when detached.{/i}"
    allan "It’s the doctor’s research."
    brent "Guess they transfer the research between themselves."
    "He flips through the book, and finds a page that has been folded."
    "He opens it and we read it together."
    "The page is full of some stuff I’m able to understand thanks to my scientist parents, but that’s only like 50%."
    "The rest is chinese to me."
    "But I’m able to understand it’s about detaching the brain and how it keeps the memory in it."
    "So basically the important part of the research."
    brent "Why do they need to know this?"
    allan "I don’t know, can it be that harmful?"
    "Brent shrugs and puts the book back the way he found it."
    "We leave the office, we have a good look at the factory."
    scene bg factory with screenwipe
    "I look down, there’s a candle there that’s lit."
    "That’s where I see him."
    allan "Hayes."
    "I point to his station and we watch from afar."
    "Brent pushes me aside and creeps to the stairs, he signals me to follow."
    "Soon we’re in a station behind him and he has no idea we’re here."
    "Hayes shakes his head, and shouts. He pushes whatever’s on the station and leaves to a door nearby."
    "Luckily, he leaves it open."
    brent "Let’s follow."
    "We sneak to the door, making sure not to make a single sound and find him in a basement."
    "There’s a pipe leading down and a drain that’s really freaking huge."
    "You could fit an entire person down there."
    play sound phone_ring
    "There’s a phone there too, Hayes picks it up."
    "He waits a bit, waiting for someone to answer."
    hayes "About damn time! Listen, Chambers’ is dead!"
    "He knows?!"
    hayes "No, I don’t think he’s missing. Burns is dead and so is Emsworth, Lang, Ramsey, Hamilton, and Burton!"
    hayes "...No they’re obviously NOT missing. They all were reported missing and Burns winds up dead! He’s after us!"
    "He?"
    hayes "Yes, I mean Lewis. Who else, you dunce!"
    "I gulp, and I look at Brent, who has a conflicted look on his face."
    hayes "We need to tell the police! But we need to cover our tracks first to not get arrested."
    "Arrested? Okay, what the hell did these guys do?!"
    
    play sound metal_wheels
    
    "Ours eyes widen, and Hayes stays dead silent."
    "The drain opened up, it’s lid pushed aside."
    "Then something climbs up, poking its head out."
    "Its entire body was made of metal, but not blocky metal like Lewis’ robot."
    "It looked like bone, it was like seeing a skeleton."
    "A 6 feet tall skeleton."
    "With a smile that pierced my soul."
    allan "It’s the same robot from before."
    "It looms over Hayes, who’s too frozen to move."
    "It smiles wickedly and grabs his body."
    hayes "AHHHHHHHHHHHH!"
    "It jumps back down the drain and Hayes’ scream is echoed through the room."
    brent "Get him!"
    "Brent bolts out and I gather my composure. I start running too."
    "We look down the drain, the robot didn’t bother to cover the hole."
    brent "Time to jump, it looks like it’s not that far."
    show brent confused with dissolve
    "Brent jumps down and I get ready."
    "But before that I look up."
    "It’s a poster, a machine convention hosted by Hayes’ company."
    "In Dublin, Ireland."
    brent "Allan!"
    show brent surprised with dissolve
    "I look down, now’s not the time for that."
    "I jump down, but I can’t help but let the memories flood back into me."
    # Scene 3
    scene cg steampunkT with dissolvelong
    "It was a few years in when I first worked at the gazette."
    "I was going to visit some relatives for a family reunion in Ireland."
    "Since you can’t get to Ireland from London, I had to get a connecting trip to Wales."
    "From there I have to take a connecting trip, via a ferry, to get to Dublin."
    "To get to Wales, I took a train."
    "It was pretty early in the day, around 3 I believe, and my trip is at 5 on the dot."
    "And I was up pretty late last night to finish a report."
    "I was very sleepy and I knew I needed to catch some sleep."
    "I had the ticket at hand, but I needed to decide where should I keep it while I sleep."
    
    menu:
        "Bag":
            $ put = "Bag"
            jump putBag

        "Pocket":
            $ put = "Pocket"
            jump putPocket
        
label putBag:
    $ put = "Bag"
    "Bag’s a safe place, can’t go wrong there."
    "I doze off with the ticket in my bag."
    "..."
    "..."
    "I wake up from my nap. God, I needed that."
    "I look at the clock to see the time."
    "..."
    "Crap! It’s 5:45!"
    "I bolt back up and grab my bag."
    "I run to the platform as fast as I could."
    "I hurriedly get my ticket from my bag and present it to the inspector."
    inspector "Wow, you’re lucky. The train was just about to leave. I think you’re the last passenger here."
    "Phew! That was a close call!"
    "I go in and wait for my trip to Wales."

    jump putContinue

label putPocket:
    $ put = "Pocket"
    "Pockets are always convenient."
    "I doze off with the ticket on me."
    "..."
    "..."
    "I wake up from my nap. God, I needed that."
    "I look at the clock to see the time."
    "..."
    "Crap! It’s 5:45!"
    "I bolt back up and grab my bag."
    "I run to the platform as fast as I could."
    "I hurriedly get my ticket from my pocket-"
    "Wait..."
    "It’s not there!"
    inspector "Sir, is there a problem?"
    "I rummage through all my pockets on me to find my ticket."
    "Starting to get memories of my trip to America years ago."
    allan "I’m sorry I don’t have my ticket, what time does the train leave?"
    inspector "Now, sir. You’ll have to catch the next train to Dublin if you don’t have your ticket."
    "Damn!"
    "I didn’t make it to Dublin that day, all the other trips were taken."
    "Something about a machine convention was taking place there so a bunch of people reserved their trips."
    "There’s a trip for tomorrow though, thank god."
    "I head back home that day and went straight to Dublin the next."

    jump putContinue

label putContinue:

    # Scene 4:
    scene bg sewers with dissolvelong
    "Ugh, no time for flashbacks!"
    "Brent and I are still chasing this thing!"
    "We go deep down the sewers, following the sounds of thumping metal."
    "Eventually, the thumping stopped, and in its place was clanking metal."
    brent "I think it’s going up a ladder!"
    allan "How do you know?"
    brent "The only way out of these sewers are through the manholes in the city. The only way up those holes are through a ladder that’s made of metal. It’s going up one right now!"
    "Yeah, I don’t want to know how Brent knows how the sewers work. Either way, we know where it’s heading."
    "We follow the sounds until we find the ladder."
    "It’s pretty high, and the lid’s open."
    brent "No way it left it there by accident. It wants us to follow."
    allan "Okay, but why us?"
    "Brent just shrugs, and goes up the ladder."
    "I follow close behind him."
    "We’re inside another building. It looks abandoned too. Lights are off as well."
    scene bg black with dissolvelong
    unknown "So you’ve made it."
    scene bg warehouse with screenwipe
    "The lights turn on, and standing on a platform above is the Ghepetto Killer."
    show ghepetto with dissolve:
        xanchor 0.5
        xpos 0.5
    ghepetto "I'm sure you’ve seen my little masterpiece."
    "He points somewhere behind us and we follow his finger."
    "The robot is standing, it’s smile creepy as ever."
    "And the body of Hayes hanging limp off of his arm."
    show ghepetto with dissolve:
        xanchor 0.5
        ease 1.5 xpos 0.25
    show brent surprised with dissolve:
        xanchor 0.5
        xpos 0.75
    brent "What are you going to do with him?"
    ghepetto "Now, now, don’t worry. He’ll be fine. I’ll be simply..."
    ghepetto "Sending him where he belongs."
    brent "And where’s that?"
    ghepetto "..."
    show brent neutral
    brent "...You’re not gonna talk, are you?"
    ghepetto "Now, now, some things must be kept outside of the public."
    
    if put == "Pocket":
        ghepetto "Much like your relation to Ben Carter."
        "Ben Carter..."
        "I’ve heard about him, he was an infamous serial killer."
        "I look over to Brent, he doesn’t seem to react much."
        brent "What do you know about us?"
        ghepetto "More than you think"
    
    
    ghepetto "But enough about that!"
    "He snaps his fingers and then-"
    "*FLICK*"
    scene bg black with screenwipe
    "The lights go out again!"
    ghepetto "Let’s see if you can save him before I take my leave!"
    "I hear metal thumping echo in the building at a rapid pace."
    "That robot must be running with the Hayes."
    allan "Brent, let’s go!"
    brent "R-right!"
    hide brent
    "Standing around darkness so much helped my eyes see through it."
    "I can make out some stairs and we go up them."
    play sound radio_noise
    "*BZZT* *BZZZT*"
    allan "What the hell’s that?"
    brent "Must be the speakers!"
    ghepetto "You two may want to run fast."
    ghepetto "Hayes is so excited to go, he just can’t keep his mouth shut about it."
    "If that’s a goddamn joke about the jaw, I’m gonna punch this guy in his!"
    "We continue running as the Ghepetto Killer cackles through the speakers"

    if put == "Pocket":
        ghepetto "Tell me, Brent. How does it feel to put a close friend behind bars?"
        "Okay, for real, what does this guy know?"
        "I look over to Brent but he just keeps running with me."
        ghepetto "Does it feel nice? You finally get to enact your own justice. Ben must’ve felt close to you, y’know."
        brent "Shut up."
        "His voice is stern, cold even."
        ghepetto "’We’re like brothers’ I believe is what he said to you. He had so much trust in you and you repaid him with a jail cell. Isn’t that sweet?"
        brent "I said shut up!"
        "The Ghepetto Killer laughs again as Bent keeps yelling at him."
        
    brent "Do you think this is some game to you?! Is it?!"
    "Brent stops in place and just yells in to the darkness."
    brent "You’re toying with human lives, enacting your own wicked sense of justice! You don’t get the right to decide that!"
    "*CLANK* *CLANK*"
    "More clanking noises, but it sounds like it’s above us."
    "I look up, and though it’s dark I can make out a shape falling over Brent."
    "Cylindrical."
    "Metal barrels!"
    
    menu:
        "Warn Brent.":
            jump warnBrent
        "Push Brent.":
            jump pushBrent

label pushBrent:
    "Crap, I don’t have time to think!"
    "I push him out of the way."
    "He drops on the floor but picks himself up soon after. He looks up and his eyes widen."
    brent "Allan!"
    "I look up, and the last thing I remember were the barrels falling on me."

    "GAME OVER"

    scene bg gameOver with fadelong
    
    return

label warnBrent:
    
    allan "Brent, up!"
    "That registered to his head."
    "He looked up and quickly dodged over to me."
    "The barrels missed him completely, and I pick him up from the floor."
    brent "Thanks for that, I lost myself for a second there."
    allan "It’s fine. Let’s just get to Hayes."
    "He was always like this. While he’s one to think before acting, his passion for his ideals tend to get the better of him."
    "He’ll always need someone to keep an eye on him."
    "We keep running towards the sounds of the robot."
    "He leaps and runs across the building trying to lose us."
    "It seems to be faster than before for some reason."
    "Soon, the thumping stops, and the lights turn back on."
    brent "Did...did we..."
    "There’s no sound nor sight of the Ghepetto Killer, nor of the robot."
    "But there is someone on a platform."
    allan "Brent, it’s Hayes!"
    "I point to the platform and we rush to him."
    "Brent nudges him, but he doesn’t move."
    "We topple him over, and despite what we’ve seen we were not prepared for the next sight."
    "His clothes were intact, but his skin, hair, and aw were gone."

    # Chapter 4
    # Scene 1:
    brent "Son of a bitch! We lost again!"
    allan "This is getting serious."
    brent "Yeah, obviously, slimy bastard keeps escaping our gr-"
    "There’s a loud knocking from the door."
    unknown "This is the London Police Force, open up!"
    brent "Crap, we’ll get arrested for sure."
    allan "What do we do, then?"
    "Brent frantically looks around, and spots the manhole."
    brent "We’ll go through the sewer."
    "I nod, even though I hate the idea."
    "We climb down the sewer and walk through it."
    allan "Where do we go?"
    brent "Far from here."
    "We walk for miles until Brent finds a ladder."
    "He climbs up and moves the manhole."
    "We’re in a different street."
    "Clearly it’s far from the abandoned building."
    "Wait..."
    allan "I know this street!"
    brent "You do?"
    allan "Yeah, my place isn’t far from here."
    brent "Let’s camp there in the meantime. That’ll throw the cops off our trail."
    "I nod and guide Brent to my apartment."
    "The next day..."
    "Brent had to sleep in my couch that day."
    "After preparing breakfast for the both of us, we discuss the case."
    allan "Still think the Ghepetto Killer’s Lewis?"
    brent "There are signs pointing to him but his voice doesn’t match his."
    "Voice..."
    allan "Wait, Maybelle said she hired you to find him after he went missing, how do you know what his voice sounds like?"
    brent "Oh, he made some tapes talking about his works. I watched it to see what he looks like. Interesting stuff, let me tell you."
    "Huh, convenient."
    
    if pocket:

        allan "He also mentioned Ben Carter. Do you know him?"
        "He looks touchy about the subject, I can tell."
        "But if I’m going to work with him I need to know everything that’s bothering him."
        allan "Well?"
        brent "...He was my partner."
        "Woahwoahwoahwoahwoah. WHAT?"
        allan "You were partners with a serial killer?"
        brent "I didn’t know he was a killer until I figured it out. He escaped to escaped on a train but I knew he would be at Dublin, there was a bar there that he said he wanted to try out."
        brent "God knows how he got a ticket though, his little trip was premature."
        "Ticket..."
        "Wait, I lost my ticket."
        "Did he escape on the same day I was supposed to leave?"
    
    play sound phone_ring

    allan "Oh, that’s my phone."
    "I go over to my phone and pick it up."
    allan "Hello?"
    unknown "Is this Allan Lorenz?"
    "I blink in surprise."
    allan "Who is this?"
    unknown "Hawkins."
    allan "How’d you get my number?"
    hawkins "Contacts."
    hawkins "Listen, I know you and Brent Norton have been investigating the disappearance of Lewis Bradley, I can help you."
    allan "And why do we want that? We know your an associate with him."
    hawkins "Because I know what happened to him, and who the Ghepetto Killer is."
    "My eyes widen."
    allan "Do you?"
    hawkins "Well, a theory, really. Come to my office, I’ll tell you both what I know there."
    "Before I can answer, Hawkins hangs up on me."
    brent "Please tell me that was good news."
    allan "I was talking with Hawkins."
    brent "So, no."
    allan "He said he has info on our missing man. Do you think we can trust him?"
    "Brent holds his chin and wanders around the room."
    "He then sighs and turns to me."
    brent "We don’t have a lead, so I think it’s for the best."
    "I nod, if that’s where we’re going, then so be it."
    # Scene 2:
    "It didn’t take long for us to find where Hawkins’ building was."
    "He does run a very successful business."
    "We had to wear disguises to get there since we don’t know if the police is looking for us, better safe than sorry."
    brent "Excuse me?"
    reception "Yes?"
    brent "We have an appointment with Mr. Hawkins."
    reception "Are you two the Smith Brothers from Smithing Corp?"
    "Real creative name there, Hawkins..."
    allan "Yes."
    reception "He’s expecting you in his office, first room to the right in the second floor."
    "We follow the receptionist directions and enter Hawkins’ room."
    "He’s sitting in his chair looking over some papers when he finally notices us."
    hawkins "Mr. Lorenz, and  Mr. Norton. I was beginning to think you two would ditch on me."
    brent "We don’t want to hear it Hawkins, tell us why you’re here."
    hawkins "Straight to the point, good. Then I’ll get to it."
    "He gestures us to the two chairs and we take a seat."
    hawkins "Okay, so I know you two are investigating the case of Lewis Bradley."
    allan "How do you know that?"
    hawkins "Please, of course I would have kept tabs on him. When I lost contact with him I had to contact him through his sister. When she wouldn’t cooperate, though, I had some other P.I look into her. He found out she was talking to you guys."
    allan "Fair enough."
    hawkins "Anyway, I’ll tell you what our plan was."
    "He stays silent for a minute until he finally speaks."
    hawkins "The others had recently contracted some deadly diseases. Some were just finally succumbing to old age. They didn’t like the idea of death and honestly neither did I."
    allan "Thanatophobia."
    hawkins "Excuse me?"
    allan "It’s the term for the fear of death."
    hawkins "Right, so because of that we needed to find ways to stay alive."
    hawkins "It wasn’t until I went to New Orleans that I had discovered the answer"
    brent "And that is?"
    hawkins "To create a body for us that would last forever. One that was made of metal."
    "Made of metal...?"
    "..."
    "..."
    "Wait..."
    allan "You used Lewis to create that body for you!"
    "Hawkins nodded, not looking guilty in the slightest."
    hawkins "Indeed, genius, right?"
    hawkins "Anyway, we told him the plan and had other researchers help him to hook wire our brains to the machine. As months passed, our initial funder, Paxton, was losing pocket money for the project. It proved to be more expensive than we thought."
    hawkins "We decided that we would pay Mr. Bradley in intervals in the same amount. After we decided that, everything went fine. Until Lewis decided to leave the project."
    brent "Because you guys were kidnapping other people, weren’t you?"
    "I stare at Brent and at his accusation."
    "How the hell did he come up with that??"
    brent "It took me some time, and running from that metal monstrosity, to finally put 2 and 2 together."
    brent "A metal body wouldn’t be able to replicate a human perfectly, too many things would stand out. After seeing the carved off skin of the victims I wondered why did he kill them so specifically."
    brent "Then I found out the answer. The Bishops mentioned you guys were kidnapping people and they went missing. I found one of those missing persons poster and saw one of them had a slight semblance to Old Chambers."
    brent "You guys needed them so you could have faces on the robots, and if they looked just like you nobody would’ve found out."
    "Insteading of being angry, Hawkins smiled."
    hawkins "You’re smarter than you look! I like you."
    "Brent narrowed his eyes, and I could only look at him with disgust."
    "Did he feel NO remorse for his actions??"
    hawkins "Anyway, you got the right idea, but Lewis didn’t know why we needed those people. He tried to backed off the job so we threatened to...let’s say, do something to him that he wouldn’t like."
    "I don’t like how vague that was, but I decided not to press on."
    hawkins "One day, Lewis said he would finish the project soon and we went to check on it, he could only present one body. He said we technically didn’t specify more than one body but he had the proof to show us most of the money went into that one robot."
    hawkins "At the time, everyone’s sickness was reaching to the point of untreatable, so we fought for a long time on who would get the body."
    hawkins "Then one day, Paxton went missing. No one knew how and soon four more people went missing."
    hawkins "Around that time, Bradley turned up missing as well and the rest of us feared for the worst. The body was gone and we had no idea where Bradley was."
    brent "Okay, but we’ve heard the Ghepetto Killer’s voice, it doesn’t match Lewis."
    hawkins "Then that means there’s only one possible person left, Owen Dawson."
    allan "Why Dawson?"
    hawkins "He was always the most...unhinged out of all of us. If anyone was going to be the Killer it has to be him."
    "Another big accusation to make, but since we don’t have any way to know if it ISN’T Dawson, we can’t exactly leave it out of the table."
    hawkins "I think he kidnapped Bradley and is forcing him to finish the body. He’s killing the others to make sure there’s no witnesses as well. It makes the most logical sense."
    hawkins "I know where’s he’s being kept. It’s in a building where Bradley was building the bodies. I can take you there."
    "This all seems fishy, but we also don’t have a lead."
    "Dawson has more than proved he isn’t exactly to be trusted, but what else are we supposed to do?"
    "Brent stands up and grabs my arm."
    brent "Give us until evening, I have some unfinished business."
    hawkins "That’s all I ask."
    "Brent and I grab our disguises and we leave the building."
    allan "Last time I checked, we don’t have unfinished business."
    brent "Well, you don’t, but I do. I had someone inside the police force look at LeBlanc."
    "LeBlanc???"
    allan "Why him?"
    brent "Call it a hunch. Anyway, what about you, what do you want to do?"
    "I think about it for a minute."
    "Time is of the essence right now and I need to think my next actions carefully."
    allan "I’ll go check out the workshop again. I’ll go see if we missed anything."
    brent "Sounds like a plan. Here’s the keys, assuming Ms. Bradley isn’t there."
    "He gives me the key and I keep it in my pocket."
    "I nod to him and the two of us separate."
    # Scene 3:
    robot "Hello, Professor Bradley."
    "Right, forgot he was there."
    "I make it to the workshop by 8:00. Looks like Maybelle isn’t here."
    "Time to start searching."
    "I go through every drawer, every cabinet, for a smidget of a clue."
    "At first i have no luck."
    "Until I find a locked drawer."
    "I try the key Brent gave me, but it’s no luck."
    robot "Do you need assistance, Professor Bradley?"
    "I turn to the robot, that things been following me everywhere."
    "It creeps me out...but..."
    allan "Can you get this open?"
    robot "Of course, Professor Bradley."
    "It goes to one of the top cabinets and grabs something from inside."
    "It goes to me and hands me a bronze key."
    "I take it and use it to open the drawer."

    if toldMom && wroteTo == "Clark" && pocket:
        $ chosenRoute = "Accomplice"
        
    elif (toldMom && wroteTo == "Queen") || (!toldMom && wroteTo == "Queen" && pocket):
        $ chosenRoute = "Lewis"

    elif (toldMom && put == "Bag") || (!toldMom && put == "Pocket"):
        $ chosenRoute = "Maybelle"

    elif (!toldMom && put == "Bag"):
        $ chosenRoute = "Simon"
        
    if (chosenRoute == "Accomplice") || (chosenRoute == "Lewis"):
        "There’s a bunch of tapes."
        "And a journal?"
        "I take the journal and flip through it."
        "It’s a log update for his machines. I go through the final pages and like I guessed the updates for the bodies Hawkins and the others commissioned were there."
        "But something’s off about it."
        "It’s a lot more wordy."
        "At least not in the first updates."
        "Around the third or fourth update log he starts to get wordy."
        "It actually feels like a diary."
        journal "Those bastards! If I knew they were kidnapping human beings I would’ve said ‘no’ from the start! I can’t keep working for them, I need to get out of here."
        journal "I’m leaving for Dublin, if I can meet a lawyer there he can help me expose them and get out of the contract. I have the day off tomorrow and no one’s going to keep an eye on me."
        
        if put == "Bag":
            journal "I was wrong. I was very wrong."
            journal "I couldn’t get on the train on time and the Bishops had me taken away."
            journal "I tried calling the police for help...but they didn’t bat an eye to me. Not one."
        
        elif put == "Pocket":
            hawkins "I made it to Dublin. All I have to do is arrange a meeting with a good enough lawyer, I should have enough money to pay them."
            journal "FUCK. The Bishops found me!"
            hawkins "I tried threatening them with the fact I got a good lawyer...but they weren’t budging."
            journal "Worse, they bribed the lawyer I got. Convince him to drop my case."
            journal "He didn’t care about my problems."
            journal "Even worse, even if I try to find someone else...they’ll threaten my sister. I..I can’t live with that."

        "Lewis..."
        "Wait, the date..."
        "No way..."
        "It’s the same day I was supposed to leave for Dublin!"
        "There’s no year though..."
        "Coincidence maybe?"
        "I hope so..."
        "Wait, there’s more in the book."
        "I turn to the next page."
        "No writing, just regular update logs."
        "I go through the book again but then something catches my eye."
        "The pictures in the journal, they’re radically different from the others."
        "As in a million times different."
        "I flip through the pages and slowly but surely, the pictures started to form a familiar shape."
        "I drop the book in horror."
        "It’s the robot."
        "The robot that was chasing us..."
        "No..."
        "How can I break this to Maybelle?"
        "..."
        "I take the journal with me."
        "It’s enough evidence."

    # --(After interaction or if the player is NOT on the Lewis or Accomplice route)
    "I grab a tape from the pile."
    "I look for a nearby TV and play the tape in the player."
    "*FLICK*"
    "The video plays..."
    "There’s a man standing there."
    unknown "Hello, my name is Lewis Bradley."
    "Bradley?!"
    "Wait..."
    "Brent mentoned tapes Lewis made."
    "Is this one of them?"
    lewis "I’m here to show you today a new invention I made."
    "He brings up a device in his hand. There’s a rather large black circle on it with a somewhat checkered pattern."
    lewis "This device here can modify the voice of a person simply by speaking into it. Let me demonstrate."
    "He twists the knob on the device and brings it over his mouth."
    lewis "What do you think?"
    "Woah, his voice is changed!"
    "It’s the same voice as Elizabeth Comstock!"
    lewis "Impressive, isn’t it? It will surely revolutionize the broadcasting industry as a whole. I call it the Voice Synthesizer."
    "The video stops."
    "A voice synthesizer?"
    "Guess he was just tinkering."
    "Still..."
    "I put the tape back into the drawer, and I notice something else was in there too."
    "An envelope."
    "I take the envelope and open it."
    "...It’s just a party invitation."
    "I guess Maybelle wanted to celebrate them finally moving into London."
    "Wait... there’s an address."
    "Could this be where the Bradleys live?"
    "I check the clock."
    "{i}9:30.{/i}"
    "Yeah, I got time."
    "I leave the workshop and head to the Bradleys apartment."

    # Scene 4:
    # --(If the player is on the Maybelle route or Accomplice route)--------------------
    if chosenRoute == "Maybelle" || chosenRoute == "Accomplice"):

        "It takes me two hours to get to the Bradley’s home."
        "It’s actually kind of a nice place to live in."
        "I knock on the door."
        "No one answers."
        "I try again, but I get the same response."
        "I turn the doorknob, but it’s locked."
        "Hm..."
        "This does look like a place one could find clues."
        "..."
        "I take out a screwdriver that I found in the workshop."
        "I had a feeling something like this would happen."
        "Back in the day, Brent actually taught me how to pick locks. He said it could be a survival skill that I’ll need."
        "Well, he wasn’t wrong."
        "I pick the lock, I may not be that good as Brent, but it doesn’t hurt to try."
        "..."
        "..."
        "*CLICK*"
        "Hell yeah!"
        "I open the door and go in."
        "Not much in here, just a quaint little home."
        "I head upstairs, there’s three rooms. One for Lewis and one for Maybelle I’m assuming. And one is the bathroom, surely."
        "I open the door to my left."
        "Hm, pretty normal, but there is a vanity mirror with a desk lamp."
        "I’m guessing Maybelle sleeps here."
        "Speaking of the vanity mirror, there’s a book on the desk."
        "I look at it and it has the word "Diary" written on it in all caps."
        "Interesting choice for a design."
        "..."
        "Damn it, I’m way too curious!"
        "I grab the diary and start reading it’s contents."
        "Not much in it, just some stuff she’s been doing with her brother."
        "I keep flipping through the pages, more stuff about her brother."
        "‘My brother is amazing’, ‘He’s so brilliant’, yadda yadda yadda."
        "Wow, there’s... a lot about her brother, isn’t there?"
        "...More stuff about her brother. This is just getting weird."
        "...Okay this is getting concerning."
        "ALL she talks about is her brother."
        "Doesn’t she have friends??"
        "They had a party so I’m assuming she does."
        "Or was it for her and her brother only??"
        "This diary is becoming a deal breaker for me."
        "...Oh thank god! There’s an entry with a mention of a girl here."
        "Okay..."
        diary "Lewis met a girl today during his work. She’s really nice...but..."
        diary "I can’t help but notice she’s very touchy with Lewis.Actually, she’s really touchy with him. She always makes an effort to grab a hold of his arm whenever she can."
        "...Slowly getting scared."
        diary "Only I’m allowed to do that, you bitch."
        "THIS CAME OUT OF MAYBELLE’S MIND?!"
        "That nice girl who’s only out of character trait I’ve seen all day is her slapping Brent’s face."
        "THIS CAME OUT OF HER MIND?!"
        diary "That girl won’t be bothering my brother anymore. I was able to convince her that my brother is off limits at the moment."
        "Define 'convince'???"
        "Shit..."
        "She’s not...in love with her brother..."
        "Is she?"
        diary "My brother has a new client today! And he’s offering a lot of money. It’s for this very rich businessman named Clark. I hope he does well. We really need the money and my brother desperately needs the fame."
        "Wait, Clark???"
        "He was Lewis’ client at one point?"
        "Why is he here?"
        diary "It’s been a few months after Lewis accepted the contract with Clark.  He should be finished with his project by now, he told me."
        diary "Or he should be finished. Turns out Clark was smuggling opium to China. He got arrested and now everyone in the company, including my brother, was fired."
        diary "It’s been hard on him. No one wants to hire him. He’s struggling to meet ends meet, even taking a few part-time jobs."
        diary "He’s in pain, I know he is. I know him better than anyone."
        diary "I don’t care if Clark was sending drugs to China, my brother as NOTHING to do with that."
        diary "The news says the police arrested him, but word gets around fast here. It wasn’t the police who found him."
        diary "Brent Norton, a private eye who found about the operation."
        diary "He’s the one to blame for my brother’s pain."
        diary "He is."
        "I drop the book in horror, and I kick it away for good measure."
        "I’m not going anywhere NEAR that thing after what I just learned."
        "God knows what she does near that when she’s writing about her brother."
        "That being said, I never thought it was possible."
        "As much as I don’t want to think about it... could the Ghepetto Killer be..."
        "*CREEEEAK*"
        "That came from downstairs!"
        "Shit, Maybelle is home!"
        "I don’t have time to get out of here, I need to hide until I can escape."
        "But where?"
        
        menu:
            "Outside the window":
                jump hideWindow

            "The Closet":
                jump hideCloset

label hideWindow:

    "The window’s a good option."
    "I try opening it in a hurry, but it won’t budge"
    "The locks still on!"
    "I unlock in and step outside."
    "I wait out there for what feels like an eternity."
    "Then I hear footsteps."
    "Coming inside Maybelle’s bedroom."
    "I gulp and wait in terror."
    "The footsteps stop and I hear nothing."
    "Not a voice, not a creak, nothing."
    "After awhile, I hear the footsteps move and the door close."
    "Sounds like she’s heading out."
    "I sigh in relief and head back in."
    "I look around and no one’s inside the room."
    "I breathe out and grab the diary, at this point it’s damning evidence and who knows what else is in there."
    "I head to the door but my eyes dart to the vanity mirror."
    "Wait..."
    "Wasn’t there a desk lamp there?"
    "*CREEEAK* *THUMP* *THUMP* *THUMP*"
    "I turn around to the sound of the footsteps...."
    "To be greeted by Maybelle and a swing from her lamp."
    "*CRASH*"
    "The lamp shatters upon hitting my head and I fell on the floor, holding it in pain."
    "The diary falls from my hands and I try to grab it, but Maybelle’s foot stops me."
    maybelle "I can’t believe you read it."
    "Her voice is dark and monotone, absolutely no emotion in it."
    maybelle "So, did you figure it out?"
    "I groan in pain, I can’t reply."
    maybelle "I was going to let you live, Allan. You are innocent, and I did really like you."
    "She smiles at me, but somehow I feel no warmth seeing it."
    "Only fear."
    maybelle "But you know too much, I can’t let you go. I’ll just tell Mr. Norton you ran away in the last second."
    "Maybelle retrieves something from her bag."
    "It’s a knife."
    "I try to get on my feet or crawl, or anything to get out."
    "But she stabs the knife onto my leg and I groan again."
    maybelle "Now, now, don’t leave."
    maybelle "I did say I like you. I’m gonna have my fun with you before you ‘go’."
    "She smiles at me, and it gives me the same feeling the robot did."
    
    "GAMEOVER"

    return

label hideCloset:
    "Okay, I know I said I read a lot of horror novels to know what’s a bad idea, but I don’t exactly have a lot of options right now!"
    "I hurriedly put the diary where I found it and head inside the closet."
    "I wait for a bit until I hear the door to the room open."
    "From the cracks in the closet, I can see it’s Maybelle, just like I thought."
    "She looks around, clearly she’s looking for something."
    "And I hope it’s not someONE."
    "She turns to the closet."
    "She stares at it for a minute and approaches it."
    "Shit, shit, SHIT!"
    "She’s getting closer!"
    "SHe reaches for the handle-"
    "*RIIIIIIING*"
    maybelle "Oh, the phone."
    "She retracts her hand and leaves the room."
    "Did...did I just get a lucky break??"
    "No time to celebrate, she’ll come back soon!"
    "I grab the diary, at this point it’s damning evidence and for all I know there’s something I missed."
    "I can’t head out the door, so I decide to go through the window."
    "I go out, but there’s nowhere I can jump."
    "Except to the roof of the next door neighbor."
    "Don’t have more options, so I just go for it and take a leap."
    "I land on the roof tiles and slide down them onto the lawn."
    "The owner of the house goes outside and confronts me."
    man "Hey, what’s the big idea?"
    allan "Sorry, I’ll pay the damages, tab it to Alexander Lorenz!"
    "I give him my dad’s number and I bolt it out the house."
    "My dad will get pissed, but it’s for a good reason!"
    "I run and head straight for the cafe where I would meet Brent."
        
    # --(If the player is NOT on the Maybelle route or the Accomplice Route)-------
    if (chosenRoute != "Maybelle") && (chosenRoute != "Accomplice"):
        "It takes me two hours to get to the Bradley’s home."
        "It’s actually kind of a nice place to live in."
        "I knock on the door."
        "To my surprise, the door actually opens."
        "Maybelle was actually home."
        maybelle "Oh, Allan, I didn’t know you know where I lived."
        allan "Did some sleuthing, found out where you and your brother lived."
        maybelle "Sleuthing, huh? At this point you can become a detective like Mr. Norton."
        allan "Heh, maybe."
        maybelle "Would you like to come in?"
        "I nod and head inside."
        "It’s a quaint place, has a nice "home" feeling into it."
        maybelle "Um..."
        allan "Something wrong?"
        maybelle "Is Mr. Norton not with you?"
        allan "We’re investigating separately right now. I’m here to find anything that’s worth checking."
        maybelle "No clues here, I told Mr. Norton that. My brother kept everything business in his workshop."
        "I nod in understanding, guess I didn’t have to go here."

    # --(If the player is on the Lewis Route)---------------------------------------------------
    if chosenRoute == "Lewis":
        "Not that I need any clues. I got more than enough but..."
        "Can I really tell her?"
        
    maybelle "To be honest, I wanted to apologize."
    allan "To Brent?"
    maybelle "Yes, I shouldn’t have slapped him. He’s just doing his job as an investigator."
    maybelle "To be honest, I may have had some suspicions towards my brother. He’s not exactly stable, like I said. It’s just that..."
    allan "He’s your brother?"
    "She nods."
    allan "I understand, it’s only natural to feel concern and doubt over your brother. You just want to believe in him. I can’t say I can relate, but I understand."
    maybelle "I’m glad you understand."
    "..."

    # --(If the player is on the Lewis Route)---------------------------------------------------
    if chosenRoute == "Lewis":
        allan "What would you do if he is the culprit?"
        "Maybelle doesn’t answer, instead she looks  down on the floor twiddling her thumbs."
        "I sigh."
        allan "You don’t have to answer that."
        maybelle "Hm?"
        allan "Just promise me you will accept whatever happens. Good or bad."
        "Her eyes widen, but they turn soft and she nods."
        allan "Thank you."
        "I head out the door and say my goodbyes."
        "I..."
        "I can’t tell her."
        "But I may have lead her to think that her brother is it."
        "Is this what Brent goes through every time?"
        "If so, then I can finally sympathize."
        "But now’s not the time."
        "I have to meet up with my partner."
        "We’re ending this case."

    # --(If the player is NOT on the Lewis Route)--------------------------------------------
    if chosenRoute != "Lewis":
        allan "Maybelle, listen,"
        "I turn to her, I’m suddenly filled with conviction."
        allan "I don’t think you’re brother’s it."
        maybelle "You don’t?"
        allan "No, and I think neither does Brent."
        allan "We’ve been finding evidences lately that don’t point to him anymore and we have a new lead that can hopefully prove your brother’s innocence."
        "And hopefully ours too now that I think about it."
        maybelle "It can?"
        allan "Yeah."
        "She smiles at me, and grabs me in a big hug."
        maybelle "Thank you so much!"
        "I feel myself blushing she finally lets go and looks at me."
        maybelle "Please, bring my brother back."
        "I nod at her."
        "So, this must be what Brent has to go through every time he gets a case."
        "Conviction and determination, and the weight of hope being on you."
        "It’s a lot for someone, but it feels good at the same time."
        "Even if it is heavy."
        "Now’s not the time to think about that though."
        "I have to meet up with Brent."
        "I say farewell to Maybelle and head to Brent."
        "Time to end this."

        # Scene 5:
        "15:00."
        "I stay at the cafe and drink as much coffee as I can."
        "I’m gonna need all of that later just in case."
        "It takes a while, but Brent finally makes it."
        brent "Hey, how was your investigation?"
        allan "Eventful."
        brent "Define that."
        allan "I found those tapes you mentioned."
        brent "Oh good. The voice doesn’t fit, right?"
        allan "Yeah, for sure. Too different. The one I saw was a tape about a voice synthesizer."
        brent "A what now?"
        allan "A device that makes your voice different when you speak into it."
        brent "Oh."
        "Before I can say something again, Brent’s eyes widened and he slaps his hand on his face."
        brent "AHHH! The voice synthesizer! How could I forget?!"
        allan "You know about it?"
        brent "Yeah, I played with it for an hour!"
        "..."
        brent "..."
        brent "Don’t tell Ms. Bradley I said that."
        allan "Uh, sure."
        brent "Anyway, this makes this case even MORE annoying to solve!"
        allan "What?! How?"
        brent "I think the Ghepetto Killer got his hands on that device and has been using it to hide his voice."
        "Oh."
        "OH."
        "OH CRAP!"
        brent "Literally anyone we can think off in the top of our heads could be the Killer. And the only way to know their identity is if we go with goddamn Hawkins!"

    # --(If the player is on the Lewis route)----------------------------------------------------
    if chosenRoute == "Lewis":
        allan "Okay, calm down, did you find anything about LeBlanc?"
        brent "No, I was suspicious of him because he kept making it to the crime scenes pretty fast. Turns out it was just luck that got him by."
        allan "Seems to be a common trend lately."
        brent "Yeah, but our lucks ran out. We got no more leads."
        allan "I wouldn’t be so sure about that."
        "I present the journal I got from the workshop to Brent."
        brent "What’s this?"
        allan "It’s from Lewis Bradley. He wrote it. Go through the last few pages."
        "He flips through the book and I can see in his eyes the realization I got."
        "He closes the book and buries his head in his hands."
        brent "Have you told Ms. Bradley?"
        allan "No, but I did meet with her. She might’ve caught on to what I was thinking."
        brent "And she’s fine with it?"
        "I stay silent, I can’t find an answer to that."
        brent "Look, I don’t like this either, you and me both don’t like this."
        "He grabs my shoulder and looks at me in the eye."
        brent "But that doesn’t change the fact he’s killed people, good or bad. And we need to do something about it."
        "I nod in understanding."
        "I hate to do it, but he’s right."
        "No matter how much it will hurt her, I have to do it."

    # --(If the player is on the Maybelle route)------------------------------------------------
    if chosenRoute == "Maybelle":
        allan "Okay, calm down, did you find anything about LeBlanc?"
        brent "No, I was suspicious of him because he kept making it to the crime scenes pretty fast. Turns out it was just luck that got him by."
        allan "Seems to be a common trend lately."
        brent "Yeah, but our lucks ran out. We got no more leads."
        allan "I wouldn’t be so sure about that."
        "I hand him the diary I got from Maybelle’s room."
        brent "Where did you get this?"
        allan "The Bradley residence. Read it, it’s...kind of enlightening."
        "Brent raises an eyebrow at me but shrugs sand grabs the diary."
        "He flips through the pages and a wave of emotions sweep his face."
        "First indifferent, then confused, then disgust, and then what I can only describe as horror."
        "He closes the book and throws it back at me."
        brent "It’s not enlightening, it’s disgusting!"
        allan "Tell me about it, she’s crazy!"
        brent "And she blames me? C’mon! That’s ridiculous!"
        allan "Should you really be saying that? I mean it does sound like her brother was struggling."
        brent "Still no reason to blame me!"
        brent "I can’t believe it! If she was this crazy why come to me?"
        allan "You don’t think she’s planning something, do you?"
        brent "Depends if she is the Killer. There’s no mention of the business men though."
        allan "Maybe she found out about them?"
        brent "Maybe."

    # --(If the player is on the Simon Route)--------------------------------------------------
    if chosenRoute == "Simon":
        allan "Okay, calm down, did you find anything about LeBlanc?"
        "Brent face turns serious and calms himself down."
        brent "I did, it’s actually quite compelling."
        brent "First things first, why did I have him investigated? Simple, he was at every crime scene we;ve been to."
        allan "How’s that suspicious?"
        brent "In Burns’ place, he and his squad were a few blocks away. So were they when Chambers’ died. And at the last place, they came to the abandoned warehouse as soon as Hayes died, we didn’t even called them."
        "Oh."
        "Oh, right!"
        allan "Yeah, how did they make it to the last building?"
        brent "The excuse was someone saw the lights turn on and off, but according to my intel there wasn’t anyone who called."
        brent "And apparently Simon’s been stressed lately."
        brent "Crime has significantly increased during the industrialization and many other people are doing a lot of shady business. Like Carter and the Opium incident."
        brent "A lot of people in the police force have noticed he’s unhinged lately, and some others have began to think he was planting evidence on criminals."
        allan "For real? That’s illegal, right?"   
        brent "It is. I have noticed Simon has been a little too zealous with his detective work after the Carter incident."
        "I honestly couldn’t exactly see LeBlanc having to stoop that low for the sake of capturing the criminal."
        "Though all of this could just not have to anything with each other."
        "...Right?"
        
    # --(If the player is on the "Accomplice Route")-----------------------------------------
    if chosenRoute == "Accomplice":
        allan "Okay, calm down, did you find anything about LeBlanc?"
        brent "No, I was suspicious of him because he kept making it to the crime scenes pretty fast. Turns out it was just luck that got him by."
        allan "Seems to be a common trend lately."
        brent "Yeah, but our lucks ran out. We got no more leads."
        allan "I wouldn’t be so sure about that."
        "I pass him the journal from Brent’s workshop and the Maybelle’s diary."
        brent "And these are?"
        allan "Something you might want to check."
        "Brent shrugs and reads the journal first."
        "As he goes through each page, his eyes slowly widen."
        "He goes to the diary next and reads them."
        "Now his face is filled with disgust."
        "He puts the book down."
        brent "Okay so this..."
        "He points to the journal."
        brent "I’m pretty sure is solid evidence of our old theory."
        "He then points to the diary."
        brent "This though?"
        "He pushes the diary back to me, with one finger."
        brent "Is plain disgusting."
        allan "Tell me about it. Talk about a total turn off."
        brent "...I’m not gonna comment on that. How’d you get this anyway?"
        allan "I snuck in the Badley home and took the book."
        brent "So she may be a bit unhinged, cool. But I don’t think this has something to do with the case."
        "He says that but..."
        "There was one thing that has been bugging me about the case."
        allan "Hey, remember back in Chambers’ office we found a note to the place where he died?"
        brent "Yeah?"
        allan "Don’t you find it weird we found a note out in the blue, on his desk?"
        allan "Don’t you think that’s weird? Did anyone else but us know what we were doing?"
        brent "..."
        allan "...Brent?"
        brent "Okay, so Maybelle may have called me for updates on the case."
        allan "You told her?!"
        brent "I had to, she’s my client! Look, there’s evidence pointing to Lewis, and she may be crazy but there’s no way she can be the killer."
        brent "There’s no way both of our theories could be right!"
        "I try to retort, but something Brent says sparks something in me."
        allan "What if they are?"
        brent "What?"
        allan "Lewis has a grudge against the businessmen, and Maybelle knows who you were before the day she became your client."
        allan "Lewis clearly knows how to build them and Maybelle was your client."
        allan "What if she was trying to trap us while Lewis was going to kill the businessmen?"
        brent "Are you telling they BOTH have a grudge against me?"
        allan "Well, did you do anything to piss off Lewis?"
        brent "Well, no, but..."
        "He stays silent."
        brent "If they’re both it, why would they mention Ben?"
        allan "Your old partner that was a serial killer?"
        brent "The media over exaggerates his story, actually. He wasn’t a serial killer, he was a hitman."
        allan "A hitman!? Shouldn’t you have told me that?"
        brent "Didn’t think it was important, well until now."
        brent "He worked with me because he needed leads on how to find his targets. He had killed ten people in his contracts."
        allan "He must’ve been rich."
        brent "We were going to some expensive restaurants, I should’ve been suspicious."
        brent "Anyway, he told me he was midway in his last contract when I visited him in jail. He had apparently killed three people in that last contract."
        brent "He didn’t say who he was working for, but he did say it he had killed some businessmen."
        allan "Businessmen? You don’t think there were MORE people  in that project, do you?"
        brent "Possibly, Hawkins never mentioned how many people were involved, it’s most likely the ones Ben killed hadn’t contributed to the project yet."
        "Jesus Christ, how deep does this rabbit hole go? For all I know the Queen is part of this too!"
        
    # ----------------------------------------------------------------------------------------------------
    brent "Anyway, what we have right now are just theories and speculation."
    allan "Right, I guess we won’t know until we go with Hawkins, will we?"
    brent "Yeah, I don’t like the look of this just as much as you do, but we don’t have much of a lead."
    allan "I agree, but do you think we can trust him?"
    brent "With someone who most likely killed a bunch of people? No, but it looks like he’s scared of being the next victim. I think he’ll cooperate."
    allan "That’s putting a lot of faith in him, but I think I can trust your instincts."
    brent "Then I guess that means we’re ready."
    "I nod, and then the two of us leave the cafe and head to Hawkins."

    # Scene 6:
    "We meet Hawkins in the outskirts of London."
    "He takes us for a trek until we reach an abandoned building."
    "It’s on a hill overlooking the city."
    hawkins "This is where we conducted the project. It’s far off and not a lot of people know about it."
    allan "And you think he’s in here?"
    hawkins "Positive."
    brent "Well, let’s go in, then."
    "Hawkins opens the door, and we go in the building."
    "He directs us to one door, and immediate we’re met with a maze of hallways."
    "God, how can anyone navigate this everyday?"
    "At least the turns aren’t that much but it’s annoying how much we have to do."
    "What were the directions, again?"

    # (JC’S NOTE: PUT EMPHASIS ON THE NEXT SET OF  TEXTS)
    "{i}Right.{/i}"
    "{i}Right.{/i}"
    "{i}Left.{/i}"
    "{i}Forward.{/i}"
    "{i}Forward again.{/i}"
    "{i}And then a left.{/i}"
    "{i}God, imagine doing this backwards.{/i}"

    # (JC’s note: Okay, the next are just regular text)
    "We finally make it to an iron door."
    "Hawkins opens the door and gestures us to go in."
    "..."
    "The rooms dark, we can’t see anything."
    hawkins "Okay....I brought you to them!"
    "What?"
    "*FLICK*"
    "The lights go back on!"
    "The Ghepetto Killer is standing on the far end of the room!"
    brent "Wait, ‘brought you to them’?"
    ghepetto "Very good, Hawkins. You’ve done well."
    "My eyes widen."
    "Damn it, we even saw this coming!"
    allan "Hawkins, you double-crossed us!"
    "He doesn’t say anything to us."
    "Hawkins runs back and grabs the door handle."
    "But it’s not budging."
    hawkins "Huh?"
    ghepetto "Now, now, Hawkins. You deserve a reward for your efforts."
    "*CLICK*"
    "That came from the door."
    "*SLAM*"
    "The door busts open, and a pair of metal claws grab Hawkins."
    hawkins "Wha-"
    "But before he can finish, it pulls him in, and the door slams shut."
    hawkins "AHHH! AHHH!"
    hawkins "NO, NO!"
    hawkins "YOU PROMISED, YOU PROMISED! YOU PRO-"
    "*SPLAT*"
    "That sounded really squishy."
    "Later, a pool of red starts seeping through the door."
    ghepetto "He was a fool to think he was going to live."
    brent "What the hell do you want with him? What the hell do you want with us!"
    "The Ghepetto Killer doesn’t reply to me."
    "Instead, his shoulders shake and he throws his head up."
    ghepetto "Ha, ha, ha, ha, AHAHAHAHAHAHA!"

    if chosenRoute == "Maybelle":
        jump maybelleRoute
    
    elif chosenRoute == "Accomplice":
        jump accompliceRoute

    elif chosenRoute == "LewisRoute":
        jump LewisRoute
    
    elif chosenRoute == "simonRoute":
        jump simonRoute

label maybelleRoute:
    # Chapter 5a
    # (Maybelle Route)
    # Scene 1:
    ghepetto "Don’t you realize what you’ve done, Brent Norton?"
    ghepetto "What you’ve done in the past with what you call justice?"
    "..."
    "That confirms it for me."
    allan "You can take off that mask now. I know who you are."
    allan "Maybelle."
    "The Ghepetto Killer doesn’t react again."
    "He reaches for his mask and takes it off."
    "I wince at the identity."
    maybelle "You’re a better sleuth than you look."
    brent "Ms. Bradley?"
    maybelle "Hello, Mr. Norton."
    brent "...If you’re the killer, then what happened to your brother?"
    "Maybelle eyes widen, she stays silent before continuing."
    maybelle "Dead. This entire time he’s been dead."
    allan "What?"
    maybelle "He killed himself two months ago in his workshop."
    allan "Why didn’t you tell anyone else?"
    maybelle "Because I knew he didn’t want anyone else to know. He left a note writing about what the Hawkins and the others had done to him."
    maybelle "He couldn’t live with the guilt of not stopping them, but I know I he also wanted revenge."
    maybelle "He finished his robots, the ones chasing you two, and left them at his workshop.If there was anyone who would enact what he wanted, I knew it would be me."
    brent "And where would I come in?"
    maybelle "You ruined his chances of gaining a better life."
    allan "How?"
    maybelle "Read the log, Clark’s payment for my brother was the biggest then and now. Imagine how successful he would’ve been if you hadn’t arrested him!"
    "She really does blame him, huh?"
    "..."
    "Wait..."
    "Brent said he arrested after finding a clue."
    "And he found that clue after reading MY article."
    "Could..."
    "What would’ve happened if I hadn’t written that article?"
    brent "Clark would’ve kept smuggling drugs into China!"
    maybelle "They can get high as much as they want, for all I care! You ruined my brother’s chances of a successful career, you, Hawkins and his confidants!"
    allan "Clark could’ve been working with them too! Have you ever thought about that?"
    "Maybelle’s eyes turn dark, and she slams her hands into the railings."
    maybelle "SHUT UP! Or else..."
    "We hear more metal clanking."
    "From the shadows under the platforms, more of those robots emerged."
    brent "What the..."
    maybelle "I did say {i}robots{/i}, didn’t I?"
    "Maybelle turns around to some large metal column. She does something there that I can’t see."
    maybelle "I’ll give you two about ten minutes."
    "Sh runs back to the door behind her."
    allan "Wait-"
    brent "Allan, look!"
    "Brent points to the platform Maybelle was standing on. Specifically, he’s pointing to the metal column."
    "Wait no, it’s more of a cylinder."
    "With a cone tope and a pipe sticking out of it."
    "Wait..."
    brent "She set off a boiler! We’re in a boiler room! It’s gonna blow if we don’t get the hell out of here!"
    "I nod and we rush to the door."
    "We stand in the hall-"
    "Damn it! I forgot how much of a maze this place is!"
    "Which way’s the exit?"
    
    menu:
        "Right, Right, Left, Forward, Forward, Left.":
            "We take a right-"
            "Shit!"
            "It’s blocked!"
            allan "Isn’t this the way?!"
            brent "Let’s just go back-"
            "But we can’t."
            "The robots cornered us in the back."
            "ANd we only wait for them to come to us."
            "GAME OVER."

            scene bg gameOver with fadelong

            return 

        "Left, Left, Right, Forward, Forward, Right.":
            pass

    "Right, reverse."
    "We’re facing the other way."
    "We take those directions, we hear the robots behind us, but thanks to pure adrenaline we can outrun them."
    "We make it to the lobby room."
    brent "We’re almost out of time, run!"
    "With all of our strength, we leap towards the door."

    # Scene 2:
    "We land hard on the dirt."
    "Then the building explodes behind us in a blaze of..."
    "I want to say glory but..."
    brent "Jesus, what was in there?!"
    allan "I don’t know, dynamite?"
    "I get up and I pull Brent up as well."
    unknown "Wha-"
    "We turn around, and we see Maybelle looking dumbfounded."
    maybelle "You two..."
    "She glares at us and starts running."
    brent "GET HER!"
    "{i}Later...{i/}"
    allan "She’s surprisingly fast."
    "We chase her to the streets of London. It’s busy, probably since it’s a Friday."
    unknown "Everybody move!"
    "That voice..."
    "We turn to see LeBlanc pushing away civilians with his other policemen."
    brent "We have to tell him!"
    "I nod, but I also turn and I see Maybelle still running."
    allan "She’s getting away!"
    brent "What- Damn it!"
    "Maybelle head is drowned in the sea of people in the streets. I can see her, but I can barely make her out."
    allan "Go get LeBlanc, I’ll get Maybelle!"
    brent "What, but Al-"
    allan "Just do it! We don’t have time!"
    "Brent looks reluctant, but he nods."
    "I run towards the direction of Maybelle."
    "The more I run in, the more I can see of her."
    "She must’ve seen me too, she’s starting to pick up the pace."
    "Well, I won’t lose either."
    "I chase her down, and eventually she turns to an alleyway."
    "I chase her there."
    "She runs to the end of the alley, but she’s stopped by a wall."
    "Now’s my chance."
    allan "Game’s over."
    maybelle "Why, Allan?"
    maybelle "WHY CAN’T YOU JUST LET ME HAVE MY REVENGE?!"
    allan "Why do you want to do this?!"
    maybelle "Because it’s my brother! I know my brother would want this! I-I-I..."
    "She crouches down, and I hear a hiccup from her."
    allan "You love him, don’t you?"
    maybelle "Of course I do."
    "Her voice is weak, barely a whisper."
    allan "No, I mean the other love."
    "She bring her head up, and she just nods."
    allan "I figured."
    "I crouch down, I had to look at her eye to eye."
    allan "I think you’re right about how your brother killed himself out of guilt, but I think you’re wrong about the reason."
    allan "I’ve been running away from those things all week and I can tell how deadly they are. I bet your brother knew as well. The guilt he was living with, Maybelle, was the fact he stooped that low."
    maybelle "Low?"
    allan "He went to the level of wanting to kill someone to escape. He didn’t want that for himself, and I know he wouldn’t want that for you either."
    allan "I don’t think it will be easy to atone for what you’ve done, but I know you can at least regret them. So please, turn yourself in. For him."
    maybelle "Lewis..."
    "I smile at her, she seems to be getting it."
    "But then the color of her eyes go away."
    maybelle "Lewis, you’re back!"
    "My smile drops."
    allan "Um, Maybelle?"
    maybelle "I thought I lost you."
    "She grabs something from behind her, looks like a crate of supplies."
    "Kitchen supplies I think."
    "It’s a knife!"
    maybelle "And I’m not going to lose you again."
    "She leaps towards me, but I dodge in time."
    "I’m on the ground, and she’s able to pin me with the knife raised."
    maybelle "Sit still, it’ll only be a second."
    "Her smile is creepy, I can’t help but think of those robots chasing me."
    "She brings the knife down on me, but I’m able to grab her wrists."
    allan "Not...today!"
    "With all my strength, I throw her down and pin her."
    "I grab her other hand and push the knife out of reach."
    "She struggles, but she’s no match for me."
    unknown "LONDON POLICE! STAY WHERE YOU ARE!"
    "I turn to my left, and the London Police arrive with LeBlanc and Lewis."

    # Epilogue
    "{i}Two months have passed and the Ghepetto Killer is behind bars.{/i}"
    "{i}The identity of the killer is Maybelle Bradley, sister of inventor Lewis Bradley.{/i}"
    "{i}The many missing capitalist have been confirmed to have been dead and killed by Maybelle Bradley via the robots her brother created.{/i}"
    "{i}Maybelle Bradley will be behind bars until her sentence has been decided.{/i}"
    "...."
    "This article was a big hit."
    "The Gazette really blew up since their reporter was the one who discovered this story."
    "Speaking of story, I’ve finally started writing."
    "It’s about the case and my firsthand experience with it. I’ve already got a deal up with a publisher."
    "But...there’s still one thing I need to do."
    brent "You sure you want to do this?"
    "We were at the prison Maybelle was being kept at."
    "LeBlanc agreed to give us visitor’s time for her."
    allan "I..need to do this."
    "Brent nods at me, and we go in."
    police "You have thirty minutes."
    "We go to the table where Maybelle is at."
    "It’s weird seeing her without her usual clothes and her bright eyes."
    brent "Morning, Ms. Bradley."
    maybelle "Morning Mr. Norton. Hello to you too, Lewis."
    "Even after all these months, she still mistakes me for her brother."
    "It hurts me."
    brent "Listen we just have one more question for you."
    maybelle "What is it?"
    brent "The skin carving. What’s up with that?"
    maybelle "Catharsis, really. I was in so much pain, it felt nicer than hurting myself. But I’m fine now."
    "She smiles at me."
    maybelle "My brother is here now, it’s all good."
    "It still hurts."
    allan "You know you will face harsh punishment for what you’ve done,  right?"
    "She nods."
    maybelle "I know but I’ll accept whatever it has to be."
    allan "Do you regret what you’ve done?"
    "She nods again."
    allan "Do you still blame me- I mean Allan?"
    maybelle "For what?"
    allan "Don’t you think that he had a part in ruining my career?"
    maybelle "No, I don’t see how."
    allan "Well, how about Brent?"
    maybelle "A part of me does, but I’ve done some time to think about it. So maybe not so much now."
    "That’s all I need to know."
    allan "We have to go. Behave yourself, okay?"
    maybelle "I will. Goodbye, brother."
    "Brent and I leave."
    "We go back to the lobby and I slump on a chair."
    allan "It’s my fault."
    brent "How?"
    allan "I wrote that article, remember? You said it gave you a clue on how to arrest Clark. It’s been on my mind ever since we arrested her."
    "Brent stays silent."
    brent "It’s not your fault, Allan. These things happen all the time, so I know your pain."
    "Brent sits with me and pats me on the shoulder."
    unknown "You know the punishment might be execution, right?"
    "LeBlanc stands over us."
    leblanc "The people she killed were too much. It’s not enough for all their life sentences."
    lewis "Not now, Simon. My friend’s taking it too much."
    leblanc "Right, sorry. My bad, Lewis."
    "The two share a smile, and really the sight’s nice to see,."
    "But the pain is still raw."
    brent "Hey, Allan,I was thinking about something."
    brent "Would you like to stay as partners?"
    "My eyes widen and I look at him."
    brent "It brought back a lot of good memories in me. I was wondering if you would like that?"
    "He looks at me smiling."
    "It’s comforting, it brings back memories in me too."
    "But..."
    allan "Sorry."
    allan "This...was too much for me to take."
    allan "I don’t think this is the life for me."
    "Brent stays quiet, but he smiles."
    brent "I understand.I guess this kind of job isn’t for everyone."
    leblanc "It isn’t, but it doesn’t have to be."
    "I smile at them."
    allan "Thanks for understanding."
    leblanc "What will you do now, boy?"
    allan "I still got that book job. Maybe I can start with there."
    allan "I’ll write stories. I’ll do that as my part to make the world a better place."
    brent "That’s sounds like you, alright."
    "I smile at them again."
    "Even if it’s a small way, I’ll do my best to change the world."

    # ENDING 1: Twisted Sister.
    return

label lewisRoute:
    # (Lewis Route)
    # Scene 1
    ghepetto "I’ve nothing to do with you, Brent Norton."
    ghepetto "But, you and that guy have been a thorn in my bush fall all week."
    ghepetto "I just need to get rid of you."
    allan "...Hey, tell me."
    allan "Are you...Lewis Bradley?"
    "The Ghepetto doesn’t reply."
    "Instead, he reaches for his mask and takes it off."
    "My eyes widen, but somehow I’m not surprised."
    "The face underneath was the same one on the tape."
    lewis "You’re smart, I’ll commend you for that."
    brent "Looks like we were right."
    lewis "You theorized it was me? Well I suppose it was kind of obvious."
    brent "Why kill them?"
    "Lewis laughs at that."
    lewis "Is that really a hard question? They were crooks of the worst kind."
    lewis "No matter what evidences anyone can find against them, they will never be able to enact justice on them."
    lewis "There would have to be one person to do it, and it will be me!"
    "Lewis laughs again, louder and more hysterical."
    "There was one thing buggin me, though."
    allan "Wait, why remove the skin?"
    lewis "Ah, brilliant question! You see, with what we have gathered about finding out one’s identity and knowing how powerful they are, I decided why not make use of it."
    lewis "I can create an animatronic that’s identical to a human. No one would be able to tell the difference!"
    lewis "I can use those as my puppets and find every single criminal out there!"
    lewis "I’ll be able to purge this city of any injustice!"
    lewis "HAHAHAHAHAHAHAHAHAH!!"
    "My eyes widen. This guy’s gone insane."
    "But my fear quickly turn into anger."
    allan "What about Maybelle?!"
    "Lewis stops laughing, and then he looks at me."
    "His face turns serious"
    lewis "What does she have to do with this?"
    allan "Do you want her to see you like this? Your own sister?"
    "My voice rises up, I can’t help but imagine how she of all people would feel."
    allan "How would she feel if she knew you killed people?"
    "Lewis glares at me, and slams his fistson the railings."
    lewis "SHUT UP! I’VE ALREADY SOLD MY SOUL TO THE DEVIL! IF IT MEANS ENACTING JUSTICE, THEN SO BE IT!"
    "He brings out a match and lights it up."
    "He throws it to the ground, and only now did I notice the pool of black."
    brent "Is that..."
    lewis "Gasoline."
    "WHAT?!"
    lewis "But that’s not my only surprise."
    "He snaps his fingers, and we hear more metal clanking."
    "From the shadows under the platforms, more of those robots emerged."
    brent "There’s more?!"
    lewis "Of course there’d more! You didn’t think I was foolish enough to make one!"
    "He turns around and runs to the back from where he’s standing."

    play sound door_slam

    "We hear a door slam."
    allan "Wait"
    brent "Allan, look!"
    "Brent points to the platform Maybelle was standing on. Specifically, he’s pointing to the metal column."
    "Wait no, it’s more of a cylinder."
    "With a cone tope and a pipe sticking out of it."
    "Wait..."
    brent "We’re in a boiler room! It’s gonna blow if we don’t get the hell out of here!"
    "I nod and we rush to the door."
    "We stand in the hall-"
    "Damn it! I forgot how much of a maze this place is!"
    "Which way’s the exit?"

    menu:
        "Right, Right, Left, Forward, Forward, Left.":
            "We take a right-"
            "Shit!"
            "It’s blocked!"
            allan "Isn’t this the way?!"
            brent "Let’s just go back-"
            "But we can’t."
            "The robots cornered us in the back."
            "ANd we only wait for them to come to us."
            "GAME OVER."
            scene bg gameOver with fadelong
            return
            
        "Left, Left, Right, Forward, Forward, Right.":
            pass

    "Right, reverse."
    "We’re facing the other way."
    "We take those directions, we hear the robots behind us, but thanks to pure adrenaline we can outrun them."
    "We make it to the lobby room."
    brent "We’re almost out of time, run!"
    "With all of our strength, we leap towards the door."
    
    # Scene 2
    "We land hard on the dirt."
    "Then the building explodes behind us in a blaze of..."
    "I want to say glory but..."
    brent "Jesus, what was in there?!"
    allan "I don’t know, dynamite?"
    "I get up and I pull Brent up as well."
    lewis "What the-"
    "We turn behind us, Lewis is standing there."
    "He glares at us, and then he runs."
    brent "Get him!"
    "Later..."
    allan "Jesus, all that building must’ve did something to him!"
    "We chase him to the streets of London. It’s busy, probably since it’s a Friday."
    unknown "Everybody move!"
    "That voice..."
    "We turn to see LeBlanc pushing away civilians with his other policemen."
    brent "We have to tell him!"
    "I nod, but I also turn and I see Lewis still running."
    allan "He’s getting away!"
    brent "What- Damn it!"
    "Lewis’ head is drowned in the sea of people in the streets. I can see him, but I can barely make him out."
    allan "Go get LeBlanc, I’ll get Lewis!"
    brent "What, but Al-"
    allan "Just do it! We don’t have time!"
    "Brent nods, and runs towards LeBlanc and his police force."
    "I then started chasing Lewis in the sea of people."

    "{i}Elsewhere...{/i}"
    maybelle "Hm...."
    maybelle "I wonder how they’re doing?"
    play sound phone_ring
    maybelle "Huh, is that the fire department?"
    maybelle "Wha-"
    maybelle "That building’s on fire!"
    maybelle "...."
    maybelle "I got a bad feeling about this. Maybe I should check it out."
    "{i}Back with Allan....{/i}"
    "I chase Lewis for a good while. He seemed to have lost any other solution, he just took a turn inside an alleyway."
    "I chase him there and he stops at a wooden barricade."
    lewis "Damn it!"
    "I corner him there."
    allan "Game’s over."
    lewis "You think you’ve won?! I still have their skins AND my animatronics, I’ll just escape scot free!"
    allan "I won’t let you do that. It’s over, Lewis. You can’t run anymore."
    "He grits his teeth."
    lewis "SCREW YOU!"
    "He lunges forward at me, and I don’t have time to react. He pins me down on the ground and has his hands around my neck."
    lewis "I’M THE GREATEST MIND IN THE WORLD! ONLY I KNOW WHAT JUSTICE IS! AND I’LL STOP ANYONE WHO GETS IN MY WAY!"
    "I can’t reply, his grip is too strong. He’s too far gone."
    "I can’t breathe, the air in my lungs is fading. "
    "I’m sorry, Brent. I couldn’t stop him."
    "I’m sorry I couldn’t save him."
    "I’m sorry..."
    unknown "Lewis?"
    "Maybelle?"
    "Lewis let’s go of my neck. I quickly gasp in more air."
    "Maybelle rushes over to me and pulls me up."
    lewis "Maybelle?"
    "He approaches her, but she recoils back."
    "Lewis staggers back, and his eyes start to flood."
    lewis "It’s me, sis, it’s me."
    maybelle "..."
    "Maybelle can’t reply either, she just hides behind me slightly."
    lewis "No."
    "Lewis falls on the floor and and hangs his head low."
    lewis "What have I become?"
    "His voice is weak."
    "I hear more footsteps behind me."
    "I turn around and I see Brent and LeBlanc."
    "Brent shakes his head, and approaches Lewis with cuffs."

    # Epilogue
    "{i}The identity of the Ghepetto Killer has been found!{/i}"
    "{i}Inventor Lewis Bradley has confessed to his crimes of killing and carving away the skins of multiple businessmen around London.{/i}"
    "{i}Lewis used his robots, which he calls animatronics, to find and subsequently kill the victims.{/i}"
    "{i}He will be behind bars until his judgement has been decided.{/i}"
    "This article was a big hit."
    "The Gazette really blew up since their reporter was the one who discovered this story."
    "Speaking of story, I’ve finally started writing."
    "It’s about the case and my firsthand experience with it. I’ve already got a deal up with a publisher."
    "It’s been a few months since that night in the alley."
    "Maybelle and I have stayed in contact since then and I can safely say we’ve become good friends."
    "Though Brent says otherwise."
    "Anyway, it’s only fitting that we were here on this day."
    police "You three are here for visitation?"
    maybelle "I’m here to see my brother."
    police "Of course, right this way"
    "It was me, Brent, and Maybelle in the prison."
    "It was visiting time and she wanted to visit Lewis before his judgement tomorrow."
    "He sat on the table waiting for us."
    lewis "Morning everyone."
    maybelle "Morning."
    lewis "..."
    maybelle "..."
    lewis "So..."
    maybelle "I can’t forgive you for lying to me."
    lewis "I know."
    maybelle "And neither the fact you killed those men."
    lewis "I don’t think I can to myself, either."
    "Maybelle’s eyes widen, and so do mine."
    lewis "I was so focused on escaping from their clutches I lost my sense of morality. I guess with what else has been happening to me I lost my way in the end."
    lewis "I don’t think I can atone for my sins."
    brent "You can’t."
    "Lewis stares at him, his eyes blank."
    brent "But as long as you know you’ve done and regret them, then maybe you can start anew. If you ever make it out of here, I want to see that man."
    maybelle "So do I."
    "Lewis then looks at his sister."
    lewis "Wha.."
    maybelle "It’s true what you’ve done is despicable, but I can’t bring myself to hate you. You’re my brother, and I want to help you like I’ve always have."
    "Lewis eyes soften, and a smile creeps up on him."
    lewis "Can you leave me and him alone for a minute? I would like to talk."
    "He points at me, and the other nod."
    "When they leave, Lewis starts speaking."
    lewis "She talks about you a lot, you know?"
    allan "Maybelle?"
    lewis "Who else? I can see she’s happy with you."
    "He looks down on the table and twiddles his thumbs."
    lewis "I don’t think I’ll leave this place alive. I might be here for awhile. So can I ask you something?"
    "He looks at me, and his eyes aren’t the same one that tried to kill me on that night."
    "Instead it’s just the eyes of a broken man."
    lewis "Take care of her? For me?"
    "I wasn’t expecting such a request."
    "Luckily, though, it’s a request I can do."
    allan "I will."
    "I say my goodbye and leave the visiting area."
    "Brent and Maybelle are sitting in the lobby, chatting about something."
    maybelle "Oh, hey. What did he say?"
    allan "Nothing much. He just wanted to talk."
    brent "Yeah, about what?"
    allan "Nothing important, I assure you."
    "The two chuckle softly, and I turn to Maybelle."
    allan "You want to go somewhere later? It’s almost lunch."
    maybelle "Just the two of us?"
    "I blush slightly, realizing the implication of what I said."
    allan "I mean Brent can come too! It doesn’t have to be you and me."
    "She smiles, and I swear I could see a tinge of pink on her."
    "I’ll get a carriage."
    "She leaves the building, leaving me and Brent alone."
    brent "I got a thing to do, so go get ‘em tiger."
    allan "S-Shut up!"
    "Brent laughs to himself."
    brent "I take it you don’t want to be partners anymore?"
    allan "Huh?"
    brent "I get the feeling you can’t be my partner. I’ve been meaning to look for one and I thought you could be it, but I guess not anymore, huh?"
    "I look out the window and I see Maybelle waiting with a carriage nearby."
    allan "I think I got plans now."
    brent "I figured."
    "Brent exits through the door, and before I leave I see Lewis being escorted elsewhere in the prison."
    "He sees me, smiles, and nods."
    "I nod back."

     # Ending 2: Twisted Justice

label leblancRoute:
     # (LeBlanc Route)
     # Scene 1:
    "The Ghepetto Killer’s laugh echoes through the building."
    "This guy’s gone off the edge."
    unknown "Augh..."
    "Wait, that doesn’t sound like him."
    "Under the shadows of the platforms, I can make out a figure."
    "He’s slumped on the floor, surrounded by tools."
    brent "Wait..."
    "Brent squints, and then gasps."
    brent "That’s Lewis!"
    "We rush to him, and drag him out."
    allan "Hey, are you alright?"
    "I shake his shoulders, but he doesn’t respond."
    "He opens his eyes and looks at us."
    lewis "Who..."
    brent "I’m a detective, and this is my partner. You’re sister hired me to find you."
    lewis "Maybelle did?"
    ghepetto "So it seems you’ve found my little friend! His inventions were marvelous, weren’t they?"
    "We look at Lewis."
    allan "You did?"
    lewis "I was forced to. They would’ve killed my family if I didn’t cooperate."
    brent "Who’s the man under the mask?"
    lewis "Owen Dawson. One of my clients."
    "Dawson? So Hawkins was telling the truth."
    dawson "What will that information do for you? I got all three of you cornered!"
    "He throws his hands in the air and looks up to the roof."
    dawson "I can’t exactly leave any witnesses today, now can I? I will become immortal, no one can st-"
    
    play sound gun_shot
    
    "His hand is stained red, and there’s a visible hole through it."
    "Standing in the platform, LeBlanc had his gun pointed at him."
    dawson "You! Why would you-"
    "But he was interrupted again."
    "LeBlanc fired another shot straight to the chest, multiple times."
    "When he was done, Dawson’s body became still and fell through the railings."
    "LeBlanc looked down and stares at us."
    brent "Thanks, Simon! You saved us back there!"
    "LeBlanc doesn’t say anything. Lewis meanwhile holds his chins and starts muttering to himself."
    brent "Can you help us with Lewis Bradley here? We finally f-"
    "Brent stops and his eyes narrow."
    brent "Wait, how do you know this place?"
    "LeBlanc doesn’t reply again. He raises his gun at Brent."
    lewis "Run! He’s with Dawson!"
    "Our eyes widen, and LeBlanc fires his gun."
    "Brent moves in time and I carry Lewis under one of the platforms."
    "LeBlanc finds us, and aims his gun down."
    "We run before the bullet hits us."
    leblanc "Your machines are impressive, Mr. Bradley. Ever considered using them for another means?"
    lewis "What?"
    leblanc "Imagine how much crime could be reduced if you sold this machine to the London Police. We can use them to terminate any criminals we find."
    "Terminate?"
    brent "What does Lewis mean ‘you’re with Dawson’?"
    leblanc "He asked me for help finding ways to find a hole in the security of the businessmen. I ensure no crimes from them, and he gets no competition for the body."
    allan "Then why kill him?"
    leblanc "He’s a criminal. What else is there to do with people like him?"
    brent "This isn’t justice, Simon! You made an oath to the police force that you would do it lawfully, didn’t you?!"
    leblanc "And I believed that all my life until I joined the force. Crime only perpetuates crime. No matter what, there will always be one person who will commit crime after another. But if we show them what will happen if they step out of line..."
    "Another shot is fired, directly in front of us."
    "I don’t think he missed."
    leblanc "That will surely convince them."
    brent "In fear?!"
    leblanc "Why not? Fear is a good motivator."
    "To think someone like him could go that far."
    leblanc "Anyway, you two know too much. I won’t allow you two to spill my plans."
    "We hear footsteps moving away from us."
    "We step out of the shadows and LeBlanc is standing in front of something."
    # *CRANK* *CRANK*
    "I don’t know what he did, but whatever it was he bolts it out to the door."
    allan "Wait-"
    brent "Allan, look!"
    "Brent points to the platform LeBlanc was standing on. Specifically, he’s pointing to the metal column."
    "Wait no, it’s more of a cylinder."
    "With a cone tope and a pipe sticking out of it."
    "Wait..."
    lewis "We’re in a boiler room. It’s gonna blow if we don’t get the hell out of here!"
    "I nod and we rush to the door."
    "We stand in the hall-"
    "Damn it! I forgot how much of a maze this place is!"
    "Which way’s the exit?"
    
    menu:
        "Right, Right, Left, Forward, Forward, Left.":
            "We take a right-"
            "Shit!"
            "It’s blocked!"
            allan "Isn’t this the way?!"
            brent "Let’s just go back-"
            "But we can’t."
            "The robots cornered us in the back."
            "ANd we only wait for them to come to us."
            "GAME OVER."
            scene bg gameOver with fadelong

            return

        "Left, Left, Right, Forward, Forward, Right.":
            pass

    "Right, reverse."
    "We’re facing the other way."
    "We take those directions, we hear the robots behind us, but thanks to pure adrenaline we can outrun them."
    "We make it to the lobby room."
    brent "We’re almost out of time, run!"
    "With all of our strength, we leap towards the door."
    
    # Scene 2:
    scene bg 
    "We land hard on the dirt."
    "Then the building explodes behind us in a blaze of..."
    "I want to say glory but..."
    brent "Jesus, what was in there?!"
    allan "I don’t know, dynamite?"
    "I get up, so does Brent, and I pull Lewis up."
    allan "Are you alright, Lewis?"
    lewis "I’m fine. A bit sore, but I’ll manage."
    brent "Let’s get you to a hospital. Then we’ll call the police to report-"
    
    play sound gun_sh
    
    "Brent stops talking."
    "His shirt is stained red."
    "He holds his chest, and he falls on the ground."
    allan "BRENT!"
    "Lewis and I rush to him, we turn him over and there’s a hole in his chest."
    "I look up, and I see LeBlanc standing there, smoke fresh out of his gun."
    leblanc "And that takes care of the vigilante."
    "So much emotions rush through me."
    "Fear, confusion, so many. Until finally..."
    "Rage."
    "With a loud cry, I leap towards LeBlanc and pin him to the ground."
    "With all my strength I punch him the face."
    "It must’ve been pretty strong, he let’s go of his gun."
    "I reach for it and I point it to his face."
    allan "You..you...!"
    "All I could see was him, the man who shot my best friend."
    "My vision goes blurry, and it feels like all I could see is red."
    "I pull the trigger."
    
    play sound gun_empty

    allan "What?"
    leblanc "That was my last bullet."
    "LeBlanc punches me square in the face, it felt like some of my teeth were knocked out."
    "LeBlanc gets up and starts running to the countryside."
    allan "He’s getting away..."
    lewis "No he’s not."
    "Lewis reaches into his pocket, it’s a rectangular device with a red button on it."
    "He presses it, and I suddenly hear metal clanking."
    "Form the building."
    "A large metallic skeleton bursts through the rubble and starts running."
    "Towards LeBlanc."
    "It leaps at him and he’s pinned to the ground."
    lewis "I’ll get him."
    "He walks towards his robot and I dropped the gun."
    "I can’t believe I almost killed a man."
    "I feel disgusted at myself."
    "I throw the gun away, and then I immediately remember the bigger problem."
    allan "Brent!"
    "I rush to him, there’s a large pool of blood under him."
    "I shake his shoulders and I yell his name."
    "He mouths something, but I can’t make it out."
    "His lips stops moving and it’s left ajar,"
    "I call his name again."
    "But he doesn’t reply."
    "His eyes turned blank."

    "Epilogue"
    "A conspiracy amongst the Police! The identity of the Ghepetto Killer found!"
    "Detective Simon LeBlanc has been found guilty of allowing the murders of multiple businessmen in London."
    "His co-conspirator, Owen Dawson, was found dead at the scene."
    "Owen Dawson was the infamous Ghepetto Killer and the two worked with each other until Simon LeBlanc betrayed him."
    "The bullet wounds have been confirmed to have bee from the gun issued to him."
    "Another victim was found directly outside the building where LeBlanc was found."
    "The victim has been identified as Brent Norton, a private investigator hired to find the missing Lewis Bradley who was found at the scene as well."
    "Lewis was forced to build robots to kidnapped the businessmen."
    "He was saved by Brent Norton and even used his machines, which he still had control of, to capture and subdue Simon LeBlanc."
    "...."
    "This article was a big hit."
    "The Gazette really blew up since their reporter was the one who discovered this story."
    "Speaking of story, I’ve finally started writing."
    "It’s about the case and my firsthand experience with it. I’ve already got a deal up with a publisher."
    "I met up with LeBlanc a few days after the case to get some more clarity."
    "Specifically the carving skin part."
    "Turns out he wanted the case to be as gruesome as possible so he would be famous for solving."
    "He was going to put the blame on Dawson but then we got in the way."
    "Tch..."
    "Fame..."
    "He killed my friend for fame."
    "I’m at the funeral today."
    "For Brent."
    "I recognize his parents and I become acquainted with his other family."
    "My parents came with me too, since they know Brent."
    "I was asked to make a speech about him during his wake."
    allan "Brent was a great man. Probably one of the greatest I’ve ever knew. He was always reckless and running into danger just to help someone. It was only fitting he became a detective."
    allan "When I came to London I was down on my luck, struggling a bit but otherwise doing well, but I wasn’t really happy. That is, until I ran into Brent. He wanted to do the case with him, of course I had to say yes."
    allan "He tried to say something to me, before he died, but I couldn’t make it out. I only wish I could say goodbye one last time."
    "I choke on my tears, it’s hard for everyone here but it’s mostly hard on me."
    "I was there when he died, and I couldn’t save him."
    "All those times when he said we should have each other’s back, this was the one time I couldn’t do it."
    "Everyone shoveled dirt and threw it to his coffin."
    "Soon, everyone left for the reception, but I stayed by the gravestone."
    "I don’t know if I could face his family knowing I could save him."
    unknown "Allan."
    "I turn around, it’s the Bradley siblings."
    "Maybelle has a bouquet of flowers  and Lewis has an envelope with him."
    "Maybelle approaches the gravestone and places the flowers on it."
    "She turns to me and gives me a hug. I return the hug."
    maybelle "I’m sorry."
    brent "You don’t have to apologize."
    "Maybelle lets go of me and looks at the gravestone."
    "Lewis approaches me but he looks somewhere in the distance."
    lewis "I never got a chance to thank him. If it wasn’t for him I wouldn’t be able to be here. I honestly feel it’s kinda my fault."
    allan "It’s not your fault, Bren would’ve said that."
    lewis "I know it’s now, but it a part of me feels that way."
    lewis "Anyway, you also helped. You were his partner, so you must’ve contributed just as much."
    "He then turns to me, and smiles."
    lewis "So thank you."
    "Before I can say anything, he hands me the envelope."
    lewis "You left when they were emptying his clothes. Since I was the only one nearby who more or less knew him, they gave me the key to his office. I went there out of curiosity and found this."
    lewis "I read it by the way, sorry."
    allan "That’s fine. Is it for me?"
    "Lewis nods, and so I rip the envelope and read it."
    "Dear Allan,"
    "If you’re reading this, this means I’m dead."
    "I wasn’t sure if I would make it to the end of this case but I had a feeling you would."
    "You and I were always side by side since elementary. Always getting into any trouble that finds us."
    "And you always made sure I didn’t kill myself."
    "Knowing you, you would think that it was your fault about whatever happens to me. Well let me tell you this:"
    "It’s not."
    "I always know what I’m getting myself into when I do these cases, so it’s always a life or death scenario."
    "If anything it’s mine, I got myself into that mess."
    "Don’t blame yourself, your better than to self-loathe yourself."
    "If there’s anything I learned in this case it’s that you, yourself, have your own talents."
    "You’ve got much more than writing stories, you’ve got the intelligence and wit to match."
    "So I’m gonna ask you something."
    "My office is open now, I doubt anyone will keep an eye on it for it in the meantime."
    "That’s why I’m lending it to you."
    "My hands shake, and my tears start to flow again."
    "You’re in charge of the office from now."
    "You can do whatever the hell you want with it."
    "I read the next words, and I suddenly realize what Brent’s last words to me were."
    "Take care of everything for me. See you, buddy."
    "I look at the Bradley siblings again, and Lewis is holding up a key."
    "It must be the key to Brent’s office."
    "I look at the letter, than back at the key, then to Brent’s grave."
    "He’s counting on me, I realize that."
    "People like Hawkins, Dawson, and LeBlanc are out there."
    "If the police can’t do it, someone else has to."
    "I’ve made up my mind."
    "I grab the key, and the two smile at me."
    "If my only sin is not saving my friend then so be it."
    "I’ll make sure no one else has to go through that."

    # Ending 3: Taking up the mantle

label accompliceRoute:
    # (Accomplice Route)
    # Scene 1
    "The Ghepetto Killer’s laugh echoes through the building."
    "This guy’s gone off the edge."
    unknown "Augh..."
    "Wait, that doesn’t sound like him."
    "Under the shadows of the platforms, I can make out a figure."
    "He’s slumped on the floor, surrounded by tools."
    brent "Wait..."
    "Brent squints, and then gasps."
    brent "That’s Lewis!"
    "We rush to him, and drag him out."
    allan "Hey, are you alright?"
    "I shake his shoulders, but he doesn’t respond."
    "He opens his eyes and looks at us."
    lewis "Who..."
    brent "I’m a detective, and this is my partner. You’re sister hired me to find y-."
    
    play sound metal_bang
    
    "Brent was smacked hard on the face!"
    "With a wrench."
    "By Lewis."
    allan "Brent!"
    "I rush to him, there’s a trickle of blood on his mouth."
    allan "What the hell was that for?!"
    "I glare at Lewis, but he chuckles."
    lewis "And the pieces are finally together. Ain’t that right, sis?"
    "We look at the platform, and the Ghepetto Killer chuckles."
    "He reaches for the mask, and my eyes widen."
    maybelle "So it seems, brother."
    allan "Maybelle?"
    "She turns to me and smiles."
    "But the warmth I felt from it before is gone."
    maybelle "Hello, Allan."
    brent "You both were a part of this?"
    "Lewis claps his hands and points at us."
    lewis "Bingo! He gets it!"
    "The siblings laugh together, but the laugh sent chills to my spine."
    allan "Why kill them?"
    "Lewis laughs at that."
    lewis "Is that really a hard question? They were crooks of the worst kind."
    lewis "No matter what evidences anyone can find against them, they will never be able to enact justice on them."
    lewis "There would have to be one person to do it, and it will be me!"
    "Lewis laughs again, louder and more hysterical."
    "There was one thing buggin me, though."
    allan "Wait, why remove the skin?"
    lewis "Ah, brilliant question! You see, with what we have gathered about finding out one’s identity and knowing how powerful they are, I decided why not make use of it."
    lewis "I can create an animatronic that’s identical to a human. No one would be able to tell the difference!"
    lewis "I can use those as my puppets and find every single criminal out there!"
    lewis "I’ll be able to purge this city of any injustice!"
    allan "You’re crazy!"
    maybelle "Don’t you dare say that about my brother!"
    "I turn to Maybelle, and her eyes turn dark."
    maybelle "He’s the most brilliant mind in the world. He’s right about the world. Crime only perpetuates crime. No matter what, there will always be one person who will commit crime after another."
    brent "And you’re going to kill them all with these things?!"
    lewis "Why not? They’re the perfect hitman."
    "Hitman…"
    allan "Wait, what does Brent have to do with all of this?"
    maybelle "With this? Simple."
    lewis "He arrested the one person who could help me."
    "The one person?"
    "My eyes widen in realization."
    allan "Ben Carter."
    lewis "Right! You’re smart too!"
    brent "You were his last client?"
    lewis "I was. We had a great deal going on. Until you arrested him. I was stuck in a rock in a hard place. I learned there was no other way to stop them them to use my animatronics."
    "I turn to Maybelle."
    allan "And you agreed with him?!"
    maybelle "My brother is right. Ever since our parents died, no one else could look after us. Not even our other families. No one bat an eye towards the two helpless kids who needed a home."
    maybelle "After hearing my brother, I agreed that this is the only way to enact justice."
    "They’re both crazy. I guess this all started when they lost their parents."
    lewis "But enough about that..."
    "Lewis snapped his fingers, and I heard metal clanking."
    "We turned around, and one of his robots trapped us in its arms."
    lewis "I think it’s time you meet the maker himself. Maybelle?"
    "Maybelle nodded and turned around to some large metal column. She does something to it but I can’t figure out what."
    lewis "I’ll give you two maybe ten minutes before the boiler blows."
    "Boiler?!"
    "Lewis smiles and darts to the stairs."
    "He and his sister leave to a door nearby."
    "Brent and I struggle out of the robot’s grip."
    "But it’s like an iron vice!"
    "...Okay it is but that’s besides the point!"
    "I look down and I notice something."
    "A rectangular device with a red button on it."
    "Just within my foot’s reach!"
    "I extend my foot and with the tip of my toe, I’m able to press the button!"
    "Whirring noises came from the robots, and soon it lets go of us."
    brent "We have to run, now!"
    "I nod and we rush to the door."
    "We stand in the hall-"
    "Damn it! I forgot how much of a maze this place is!"
    "Which way’s the exit?"
    menu:
        "Right, Right, Left, Forward, Forward, Left.":
            "We take a right-"
            "Shit!"
            "It’s blocked!"
            allan "Isn’t this the way?!"
            brent "Let’s just go back-"
            "But we can’t."
            "The robots cornered us in the back."
            "ANd we only wait for them to come to us."
            "GAME OVER."
            scene bg gameOver with fadelong
            return

        "Left, Left, Right, Forward, Forward, Right.":
            pass
            
    "Right, reverse."
    "We’re facing the other way."
    "We take those directions, we hear the robots behind us, but thanks to pure adrenaline we can outrun them."
    "We make it to the lobby room."
    brent "We’re almost out of time, run!"
    "With all of our strength, we leap towards the door."
    # Scene 2


    "We land hard on the dirt."
    "Then the building explodes behind us in a blaze of…"
    "I want to say glory but…"
    brent "Jesus, what was in there?!"
    allan "I don’t know, dynamite?"
    "I get up and I pull Brent up as well."
    "..."
    "Huh, weird."
    "It feels like we should be meeting with someone."
    "..."
    allan "The Bradleys!"
    brent "Oh, crap! We need to find-"
    
    play sound phone_ring
    
    "We look at the road, and soon the fire department and the police make it to us."
    "LeBlanc stands with them as he approaches us."
    leblanc "You two again?!"
    "We were surrounded."
    "With a weary smile, we raised our hands in the air."
    scene bg black with dissolvelong
    "..."
    "..."
    "Huh?"
    "I wake up and I’m not inside my apartment."
    "It’s a dark room with bars on one side."
    "Oh, that’s right."
    "Brent and I were arrested after last night and we’re being interrogated in the morning."
    "So today."
    "The officer knocks on my cell."
    police "You’re up, Detective LeBlanc wants to talk to you two."
    "I nod and I get up."
    "I enter the interrogation room where LeBlanc and Brent were hanging out."
    "With cards."
    brent "Hey, I was just playing Old Maid with Simon! I’m winning by the way."
    "He actually was. His pile was filled."
    "Same old Brent, looking at the brighter side of things."
    "I smile and I sit with him."
    allan "So are we going to jail?"
    leblanc "Actually, no. I came here to talk."
    "We were both stunned."
    "LeBlanc reaches for the ace on Lewis’ hand and places his pair on his pile."
    brent "I still win."
    leblanc "Not now."
    "He goes to his briefcase and opens it."
    "Inside we see a device. I feel like I’ve seen it before."
    brent "The voice synthesizer!"
    "Woah, it is!"
    leblanc "Is that what it’s called? Well anyway we found it in the rubble of the building."
    "Brent grabs it and holds it up on his mouth."
    "He presses the button on it and his voice changes."
    "Into Maybelle’s."
    brent "I’m Maybelle Bradley. And I’m a crazy strumpet in love with my brother."
    "..."
    "He wasn’t kidding when he said he played with it."
    leblanc "Give me that."
    "He takes Voice Synthesizer."
    leblanc "This thing here has the evidence that proves your innocence. We had an expert study it and here’s what he found."
    "He presses a button on it, from the inside of the device, and a voice plays."
    lewis "{i}And the pieces are finally together. Ain’t that right, sis?{/i}"
    maybelle "{i}So it seems, brother.{/i}"
    allan "{i}Maybelle?{/i}"
    maybelle "{i}Hello, Allan.{/i}"
    brent "{i}You both were a part of this?{/i}"
    lewis "{i}Bingo! He gets it!{/i}"
    allan "{i}Why kill them?{/i}"
    lewis "{i}Is that really a hard question? They were crooks of the worst kind.{/i}"
    lewis "{i}No matter what evidences anyone can find against them, they will never be able to enact justice on them.{/i}"
    "LeBlanc stops it there and looks at us."
    leblanc "I believe that’s evidence against them, don’t you two think?"
    "He smiles at us and puts it back into the briefcase."
    leblanc "We talked it over to the Bishops, they vouched for you two as well as a bunch of other people. You two are lucky you’ve met a lot of people."
    "Relief flushes through me."
    "Thank god, I wasn’t in the mood of being anyone’s little spoon."
    "But Brent doesn’t look satisfied."
    brent "They got away, though."
    "I didn’t get it at first until I realize what he meant."
    "And I curse to myself."
    "They got away scot free."
    leblanc "I believe you’re right that they are the Ghepetto Killer, but unless we find them, people will have another opinion."
    "Brent hits the table, and then stands up."
    brent "Let me find them. They’re my responsibility."
    leblanc "Norton-"
    brent "My job is to find Lewis Bradley and I will damn not stop until I do. Not when those two are out there somewhere."
    "I look at him, and I remember that look."
    "That’s the same look he had when we were kids, when he always helped anyone."
    "I stand up and look at him."
    allan "You’re not doing it by yourself."
    "He looks at me, visibly stunned."
    allan "I want to see this case through, whether or not you want me to."
    brent "You want to be partners?"
    "I don’t reply."
    "Instead, I reach my hand to him."
    "He smiles, and grabs it."
    "LeBlanc stands up."
    leblanc "You two are going to need more than what you have, you two need official help."
    "We look at him."
    brent "You sure you want to help me, Simon?"
    leblanc "I made an oath, an oath to protect this city. Anyone who wants to do that is my ally.."
    "He smiles at us and reaches his hand."
    leblanc "Brent."
    "We smile, and we shake his hand."
    "From a distance, I hear Big Ben ringing it’s bells."
    "It’s a new day, and a new life for me."

    # Ending 4: Partners

    return