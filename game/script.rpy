init:

    # Backgrounds
    $ backgroundDir    = "images/backgrounds"

    image bg oldOffice = "[backgroundDir]/office1.png"
    image bg newOffice = "[backgroundDir]/office2.png"
    image bg streets   = "[backgroundDir]/street.png"
    image bg city      = "[backgroundDir]/city.png"
    image bg cafe      = "[backgroundDir]/cafe.png"

    image cg train     = "[backgroundDir]/train.jpg"
    
    # Animations
    $ animationDir = "placeholders/images/backgrounds"
    $ screenwipe   = ImageDissolve("placeholders/images/backgrounds/screenwipe.jpg", 1, reverse=True)
    $ dissolvelong = Dissolve(2)
    $ fadelong     = Fade(1,1,1)

    # Placeholder Character Images
    $ placeholderDir = "placeholders/images/characters"

    image brent casual surprised = "[placeholderDir]/haruka_casual_excited_surprise.png"
    image brent casual happy     = "[placeholderDir]/haruka_casual_handfront_happy.png"
    image brent casual neutral   = "[placeholderDir]/haruka_casual_handstogether_neutral.png"
    image brent casual confused  = "[placeholderDir]/haruka_casual_handsbehind_sad2.png"
    
    image father neutral = "[placeholderDir]/father_neutral.png"
    image father mad     = "[placeholderDir]/father_mad.png"

    image mom neutral   = "[placeholderDir]/sora_casual_tanuki_neutral.png"
    image mom concerned = "[placeholderDir]/sora_casual_tanuki_sweatdrop.png"
    image mom surprised = "[placeholderDir]/sora_casual_tanuki_surprise.png"

    # Characters
    define allan    = Character("Allan")
    define boss     = Character("Boss")
    define brent    = Character("Brent")
    define manager  = Character("Manager")
    define host1    = Character("Host 1")
    define host2    = Character("Host 2")
    define maybelle = Character("Maybelle")
    define unknown  = Character("???")
    define guard    = Character("Guard")
    define mom      = Character("Mom")
    define radio    = Character("Radio")
    define robot    = Character("Robot")
    define article  = Character("Article")

label start:

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

    hide father with dissolve
    
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
    "{i}BUMB{/i}"
    allan "Oh, I’m so so-"
    unknown "Ah, no I’m-"
    "No way..."
    "It’s..."

    show brent casual surprised with dissolvelong:
        xanchor 0.5
        xpos    0.5

    allan "Brent?"
    brent "Allan?"
    "The smile on my face grows big and I trap him in my arm."
    allan "Brent! It’s been too long!"

    show brent casual happy with dissolve

    brent "No kidding! How’ve you been doing?"
    allan "Not gonna lie, I’ve had better times."

    show brent casual neutral with dissolve

    brent "Not that good, huh?"
    allan "I’ve been working for a badly smalltime publisher. I’m honestly surprised I have enough money to pay rent with our sales."
    brent "Oh, that publisher? Yeah I’ve read an article you’ve written."
    brent "I was reading it at my sister’s place and when I went to the loo, my nephew used it for his arts project;"
    brent " he’s 14 and actually reads the news from time to time."
    "I freaking knew it!"
    allan "God, are we that bad?"

    show brent casual confused with dissolve

    brent "The headline in that paper was about the Queen’s new corgi."
    allan "Yeah that’s fair."
    "This is Brent Norton, an old friend of mine back in the day."
    "Since my folks were always working and travelling to places for research, I had to stay in a boarding school to have a place to stay."
    "That's where I met Brent who was my roommate at the dorm."
    "We practically did everything together there, but by the time we graduated we lost contact."
    "This is the first time I've seen him is the last six years."

    show brent casual neutral with dissolve

    brent "Say, want to head to a cafe? There's a really good one nearby where we can catch up."
    allan "Sure, sounds good."

    # Scene 4
    # Setting: Cafe
    scene bg cafe with screenwipe

    "Brent wasn't kidding when he said this was a good cafe, this place was great!"
    "The barista was pleasant to talk to, the music in the radio was soothing, and the coffee is exquisite!"

    show brent casual happy with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Ah, man, this brings back memories."
    allan "Does it now?"
    brent "Yeah, you and I used to head to out to restaurants on the end of the month and spent whatever money we saved up on the place's best food."
    allan "Oh, yeah. Wow, I spent way too much money than I should have."
    
    show brent casual neutral with dissolve

    brent "Yeah, I remember your mother wouldn't stop yelling at you that one time we spent your entire allowance."
    allan "Yeah, I'm not too fond of that memory."
    brent "That reminds me, did your parents research take off?"
    allan "Kind of, but they're retired now and lent it to one of their workers. I heard they're doing good progress, though."
    brent "Hey, that's great! Why not do an article of it?"
    allan "I don't think it'll catch the eye of a lot of people. It's not really an ice breaker, honestly."
    brent "Oh, that's a shame."
    radio "{i}BZZT BZZT{/i}"

    show brent casual confused with dissolve

    brent "What the-"

    hide brent

    "The manager of the cafe suddenly leaves his post and starts banging on the radio."

    show father mad with dissolve:
        xanchor 0.5
        xpos    0.3

    manager "Grr, stupid thing!"
    "The music in the radio finally returns, but at this point the song ended and it returns to the radio host."

    show father neutral with dissolve

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
        xanchor 0.5
        xpos    0.3

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

    show mom surprised with dissolve

    mom "The gifts! We forgot the gifts!"
    "Realizing our terrible mistake, mom and I rushed back to the restaurant we ate at and, luckily enough, the lady at the store kept it with her."
    "Unfortunately, since the restaurant was pretty far from the harbor, the ship left without us."
    "Mom and I had to buy new tickets and missed my Grandad’s birthday by a day. He wasn’t mad at us, thank god, and my family had to stay there for a few more days to make up for lost time."

    jump toldContinue

label notTold:

    mom "Hmm... no, I don’t think so."
    "My mom looked a bit unsure though and for the rest of the way to the ship she was taking a double look on our bags."
    "We made it to the line and at the moment we were boarding the ship, my mom finally realized it."

    show mom surprised with dissolve

    mom "Oh my god, we left our gifts!"
    guard "Do you have a problem, ma’am?"

    show mom concerned with dissolve

    mom "Oh, uh, yes..."
    guard "Are you going to board, ma’am?"
    "My mom looked at her bags, then at me, then at the line."
    "It was really piling up."
    "Like, there was about 7 families waiting for us to get in so they can."
    "My mom stood there confused for a solid 2 minutes until she finally came to a decision."
    mom "I’m sorry, looks we aren’t."
    "Mom grabbed me by the arm and we trudged through the line."
    "The people in the line were all giving us the dirty eye, except for a little girl my age who looked just as confused as I was."
    "The ship left soon after, without us and quite a handful of passengers thanks to us."
    "We went back to the restaurant we ate at and got our stuff back thanks to the owner who kept it with her."

    jump toldContinue

label toldContinue:
    # (Scene 6)
    # (Setting: Back to the cafe)
    # Confused
    show bg cafe with screenwipe
    show brent casual confused with dissolve:
        xanchor 0.5
        xpos    0.5

    brent "Allan?"
    allan "Huh?"
    brent "Are you in there, mate? I lost you for a second there."
    allan "Ah, sorry. Just reminiscing."
    
    show brent casual neutral with dissolve

    brent "About what?"
    allan "Well..."
    "I tell Brent about the what happened twenty years ago with my mom."

    show brent casual surprised with dissolve

    brent "Damn, that nearly happened?"
    allan "Yup."

    show brent casual neutral with dissolve

    if toldMom:
        $toldMom = False
        brent "You could’ve been one of the victims if you hadn’t told your mom."
    
    else:
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
    #Thinking
    brent "Hmm..."
    brent "Y’know Allan, you don’t have a story right now, do you?"
    allan "I was on my way to the one I was going to write about, why?"
    "I take another sip from my coffee."
    #Neutral
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
    #Smiling
    brent "That’s what I’m talking about! Man, this is gonna be like old times. Ready to solve this case, buddy?"
    allan "You bet I am!"
    "And just like that, Brent and I went to work on the case."
    # (Screen fades to black)
    "I wish I knew at the time how much that decision changed everything."

    # Scene 7
    # (Setting: In front of a building, victorian era)
    "We left the cafe soon after. After taking a fairly long ride on the monorail here in the city, Brent took me into this building ways off from the city."
    "Why the hell would anyone want to live somewhere as far this?"
    allan "So, Sherlock, what’s the case for today?"
    #Smiling
    brent "Well, Watson, it’s a simple case. One might say its..."
    #Neutral
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
    "As soon as we step inside, loud sounds of metal clanking was heard."
    "Engines started springing into life, sounds of smoke puffing out and what sounded like wheels turning."
    "Wait, wheels?"
    unknown "Welcome, home, Professor Bradley."
    # (Picture of a steampunk robot appears (doesn’t have to be our drawing))
    "Woah, what the heck?"
    "Is this supposed to be...a butler?"
    #Confused
    brent "Did not see this coming..."
    "Looks like Brent is just as astonished as I am."
    allan "Wait, you’ve never seen this before?"
    #Neutral
    brent "Nope, first time I’ve been here."
    brent "Looks like this thing is supposed to answer to Mr. Bradley."
    robot "What can I do for you, Professor Bradley?"
    allan "Looks like it."
    robot "What can I do for you, Professor Bradley?"
    allan "Can this thing not tell we’re not Bradley?"
    brent "I don’t think so."
    robot "What can I do for you, Professor Bradley?"
    allan "Okay, this thing is starting to get on my nerves, what should we do with it?"
    #Thinking
    brent "Hmmm..."
    "Brent places his hand on his chin and thinks. After a short while, his signature smile crepts up."
    #Smiling
    brent "Hey, can you get me a snack, perhaps?"
    robot "Of course, Professor Bradley."
    "The robot leaves us and enters a room a bit farther down."
    allan "You’re not thinking about abusing the system, are you?"
    brent "Nah, just want to see what it can do. What’s important is that we got a way to find any info. All we got to do is ask the robot."
    allan "Good point."
    brent "Okay, I’ll sweep the place from the right. You’ll sweep the place from the left. Yell out anything you find that looks useful for the case."
    "I nod back, and the two of us separate."
    # (Brent portrait leaves)
    "Hmm..."
    "Where do I check?"
    # ----------------------------------------------------------------------------------------------------
    # Choices:
    # - The worktable
    # - The cabinet
    # - The desk
    # --(If "The worktable" was chosen)
    "I inspect the worktable."
    "So many little gears, scraps of metal, some wires, and a memo."
    "I pick up the memo and read what it says."
    "Things to work on: 1. Voice Recognition. 2. Artificial Intelligence. 3. Facial Recognition."
    "..."
    "Yeah I have zero what any of that means."
    "I glance up and see the robot from before."
    "The stuff in the note must be for the robot."
    # --(If "The desk" was chosen)
    "I walk over to the desk."
    "Not a lot to it, just some more papers and a couple of pencils."
    "Oh, and a framed picture."
    # ----------------------------------------------------------------------------------------------------
    # --(If "Tell mom" was chosen)
    "There’s two people in the picture."
    "Behind them is by the looks of it is the building I’m currently standing in."
    "There’s two adults, a man and a woman."
    "They look young."
    "The man has his arm around the shoulder of the girl. They’re both smiling brightly."
    "I look at year it’s signed. Looks like the photo was recently taken"
    # --(If "Don’t tell mom" was chosen)
    "It’s a family photo."
    "There’s the parents standing behind their two children."
    "Behind them is a cruise."
    "Actually, the cruise looks familiar. I can’t seem to put my finger on how"
    # ----------------------------------------------------------------------------------------------------
    "...I wonder..."
    # --(If "The cabinet" was chosen)
    "I walk over to the cabinet and I grab the handle and pull it."
    # (Locked door sound effect plays)
    "Damn, it’s locked."
    allan "Brent!"
    brent "Yeah?"
    allan "Do you have the keys to the cabinet here?"
    brent "There’s a lot of cabinets here. I’m searching one right now, even."
    "Forgot how much of a smartass he can be,"
    allan "Whatever, do you have the keys for them or not?"
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
    # ----------------------------------------------------------------------------------------------------
    # (After all three options have been explored)
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
    allan "Hm?"
    # (Maybelle portrait appears)
    #Confused
    unknown "How did you get in here?"
    "Ah, crud."
    allan "Uh, well you see, ma’am..."
    brent "Allan, find something?"
    # (Brent portrait appears)
    unknown "Oh, Ms. Bradley. Didn’t think you’d be here today."
    "Ms. Bradley?!"
    unknown "Detective Norton! Sorry, were you investigating?"
    brent "Yeah, me and my friend here were."
    "The woman turns her head to me."
    unknown "Oh, are you a friend of Detective Norton?"
    allan "Yeah, a very old friend. My name’s Allan Lorenz."
    maybelle "Maybelle Bradley. I’m a receptionist here for my brother’s workshop."
    allan "Oh, you’re Mr. Bradley’s sister?"
    #Smiling
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
    # ----------------------------------------------------------------------------------------------------
    # Choices:
    # -Why get Brent?
    # -When did you last see your brother?
    # -Can you tell me about your brother?
    # -No need to ask.
    # --(If "Why get Brent" was chosen)
    allan "No offense to my friend here but why get Brent to help? Couldn’t the police  work too?"
    #Neutral
    maybelle "I tried that, but they didn’t take me seriously."
    allan "What? It’s a missing person!"
    #Angry
    maybelle "That’s what I said! But they said my brother was probably just hiding somewhere cooped up and working on his new, and I quote, contraption."
    allan "Why are they like that?"
    #Sad
    maybelle "Well, my brother is a bit weird for some people’s standards."
    allan "Your brother is a genius though, right?"
    maybelle "He is! Lewis’s brilliant and works really hard. He’s just...well..."
    maybelle "People just don’t understand him."
    "Man, I’m starting to feel bad for this guy."
    "But the list of people in this log book proved he is good at what he does."
    "So why the hell do people treat him like that?"
    "Hmm..."
    # --(If "When did you last see your brother" was chosen)
    allan "When did you last see your brother?"
    #Neutral
    maybelle "Four weeks ago. Right in this same workshop."
    brent "According to Ms. Bradley, Lewis was working on this new robot for this company. He worked day and night for it."
    maybelle "Sometimes I find him asleep on his desk, working on the robot."
    maybelle "On the day he got the job, he never stopped working. I got worried about him but he kept insisting he kept on going."
    maybelle "Then on the first monday of the month, he wasn’t in the workshop."
    #Sad
    maybelle "He just disappeared."
    brent "She went to me after a week went by with no sign of him."
    brent "That leads us to today."
    "Hmm..."
    "Four weeks ago, huh?"
    # --(If "Can you tell me about your brother" was chosen)
    allan "Tell me more about Lewis."
    #Neutral
    maybelle "Well, he’s an inventor as you can see."
    "I turn my head towards the robot."
    allan "Yeah, I can see that. He’s working on robots."
    maybelle "He calls it animatronics."
    allan "Anima-wha?"
    brent "Animatronics. I don’t know why he calls them a different name."
    maybelle "He prefers it that way. He says it gives him an identity to stand out from other inventors."
    allan "He’s working on robots, though."
    maybelle "I know, but he wants more people to know about him and get more clients to get more money. He wants to make robots to help him in inventing."
    allan "Not humans?"
    #Sad
    maybelle "No, he doesn’t exactly trust humans with his inventions."
    maybelle "He says humans always make mistakes and needs his inventions to be one hundred percent flawless."
    allan "That’s a lot to ask for, even for a robots."
    maybelle "It is. He works days and nights to make sure they’re on top condition."
    "Talk about a hard worker. I hope he doesn’t kill himself out of exhaustion."
    # --(If "No need to ask was chosen" or all other questions have been asked)
    "I think I’m good on questions now."
    # ----------------------------------------------------------------------------------------------------
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
    #Thinking
    brent "Yeah, I can see it."
    maybelle "That’s why my brother works so hard. He focuses on quality than quantity."
    maybelle "At least in my eyes, my brother’s wishes are justifiable."
    allan "How so?"
    maybelle "Well..."
    # ----------------------------------------------------------------------------------------------------
    # --(If "Tell mom" was chosen)
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
    # (Brent changes to surprised portrait)
    "THE WHO AND WHAT NOW??"
    "She was on that ship?!"
    maybelle "I see you’re both surprised. Yes, we boarded that ship. All the way to the Atlantic to get to America. I think you can guess what happens next."
    allan "The sinking..."
    maybelle "Yup, everyone scrambled to get on the boats. The rule was mother and children first. But..."
    maybelle "They could only fit two people left on the lifeboat we found."
    maybelle "My father rationalized waiting for another lifeboat could mean our death so... he and mother agreed to let us go in the lifeboat."
    #Sad
    brent "So you two could live."
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
    # --(If "Don’t tell mom" was chosen)
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
    # ----------------------------------------------------------------------------------------------------
    brent "Thank you for telling us, Ms. Bradley. Telling us was probably not easy."
    #Neutral
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
    #Sad
    maybelle "Good luck getting through him. He might not even listen to you."
    allan "Okay, well he’s owns a huge corporation, how are we going to find him."
    #Smiling
    brent "Oh that’s easy, I know where he lives."
    allan "You do?"
    brent "Yup, saw him on my way back from a case. I know it’s his home because it has the logo for his company."
    allan "Well, that’s a lead too. Let’s go find him."
    maybelle "Good luck, you two. And please bring my brother back."
    brent "We’ll do what we can."
    "I nod back and then the two of us head out."

    # Scene 8
    # (Setting: in front of a house)
    allan "This is his place?"
    #Neutral
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
    "{i}Creeeeeeaaak{/i}"
    "The door swings open, as easy as 123."
    brent "Unlocked door..."
    allan "Nobody answering the door."
    "My body immediately tenses up. Brent walks through door cautiously and looks around the hall."
    brent "Looks like nobody’s home."
    allan "This doesn't look good. What should we do?"
    "Brent takes a minute to think."
    brent "I don't want to be that guy, but I think we should split up."
    allan "Ugh, for real? Guess I should've seen this coming."
    brent "I need you to be cautious, Allan. Who knows what or who could be here."
    "I nod in reply, and soon I go in the house."
    "Brent goes to the left and I later head to the right."
    "I search around the house for signs of Burns, sadly not a lot I could find."
    "Aside from a bunch of paintings of who I'm assuming are old family members there's nothing out of the ordinary."
    "THUMP THUMP"
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
    # Choices:
    # 1. Investigate sound
    # 2. Find Brent first
    # --(If "Investigate Sound" was chosen)
    "I go up the stairs."
    "It’s an empty hallway."
    allan "Hello?"
    "No answer."
    "{i}THUMP{/i} {i}THUMP{/i}"
    "It’s coming from a room."
    "{i}KNOCK{/i} {i}KNOCK{/i}"
    allan "Anyone in there?"
    "No answer again."
    "..."
    "{i}CREEEEAAAK{/i}"
    "I didn’t open that."
    "I walk inside, the room’s completely dark, except for the light from the moon."
    allan "Hello?"
    "Then I hear footsteps, someone’s coming out of the shadows."
    # Ghepetto
    unknown "..."
    allan "Who are y-"
    "I didn’t finish."
    "Something grabbed my mouth, and trapped me in its arms."
    "It squeezed my body inwards in agonizing pain."
    "It was like being crushed by two heavily loaded wardrobes."
    "The person from in front of me removes their mask."
    "And their smile is the last thing I see."
    "Later..."
    brent "Allan? Allan?"
    brent "I heard some knocking up here, was that you?"
    "{i}CREEEAAAK{/i}"
    brent "Gah!"
    brent "Jesus, man you scared me!"
    "..."
    brent "Find something in here? I’ll just go in."
    "..."
    "..."
    brent "Hey, listen, don’t assume I swing that way but..."
    brent "Have your eyes always been that glossy?"
    "GAME OVER"
    # --(If "Find Brent first" was chosen)
    "Yeah no, I've read enough horror books to know that's a bad idea."
    "I walk around the house until I find Brent."
    allan "Hey, Brent."
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
    "{i}KNOCK{/i} {i}KNOCK{/i} {i}KNOCK{/i}"
    "We wait for a response. Nothing at first."
    "Brent knocks again."
    "{i}KNOCK{/i} {i}KNOCK{/i} {i}KNOCK{/i}"
    "......"
    "......"
    "{i}CRAAAAASH{/i}"
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
    # (Ghepetto Killer portrait appears)
    unknown "......"
    brent "Who is that?"
    "The man looks at us for awhile."
    "And then finally, he jumps out the roof and into the alley."
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


    return