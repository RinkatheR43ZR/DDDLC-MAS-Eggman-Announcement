init 5 python:
        addEvent(
        Event(
        persistent.event_database,
        eventlabel="monika_announcement",
        category=["media"],
        prompt="Eggman's Announcement",
        pool=True,
        unlocked=True,
        random=True
        )
    )

label monika_announcement:
    m 7sub "Hey [player], do you know 'Snapcube's Real-Time Fandubs'?"
    m 1eub "The series is meant to create various dubs that are done in only one take. The final result usually turns out hilarious!"
    m 1hksdrd "I bet you're wondering why I brought this up..."
    m 1hksdra ".{w=0.5}.{w=0.5}."
    m 1gssdrb "There is one scene in the 'Sonic Adventure 2 Dark Story + Final Story fandub'..."
    m 3ftsdrb "It's called by many fans as 'Eggman's Announcement'."
    m 3ftsdrb "The scene is very popular amongst Sonic and Snapcube fans, and it's... {w=0.4}Interesting to say the least."
    $_history_list.pop()
    menu:
        "Can you recite the announcement for me, please?":
           m 1etc "Hmm...?"
           m 1etsdrb "You want {w=0.4}ME {w=0.3}to recite the announcement for you?"
           m 2dublp ".{w=0.4}.{w=0.4}."
           m 1dubla ".{w=0.3}.{w=0.3}."
           m 1eublsdrb "Alright, [player]. I'll do it just for you."
           m 5nubsa "Just keep this a secret between us, okay?"
           m 6dud "Ahem..."
           m 1duc ".{w=0.5}.{w=0.5}."
           m 3tfd "I've come to make an announcement:"
           m 7tfd "Shadow the Hedgehog's a bitch-ass motherfucker, {w=0.4}he pissed on my {w=0.3}fucking {w=0.3}wife!"
           m 4efo "That's right! {w=0.3}He took his hedgehog-fuckin' quilly {w=0.3}DICK {w=0.2}out..."
           m 2cfd "And he pissed on my {w=0.3}FUCKING {w=0.3}WIFE."
           m 2mtd "And he said his dick was..."
           m 4cuo "{w=0.2}'THIS {w=0.2}BIG'."
           m 2dfbssdrd "And I said 'That's disgusting'!"
           m 3cfd "So I'm making a callout post on my Twitter.com:"
           m 7cfbfsdrw "Shadow the hedgehog, you've got a {w=0.3}{i}small {w=0.3}dick!{/i}"
           m 3cfbsd "It's the size of this walnut except {w=0.3}WAY {w=0.2}smaller."
           m 4cfsdrd "And guess what? {w=0.4}Here's what my dong looks like!"
           m 6cfo "*gasp* {w=0.2}BOOOOM!!"
           m 2cfbsb "That's right, baby!"
           m 2cfbfd "All points, {w=0.4}no quills, {w=0.4}no pillows {w=0.3}- look at that, {w=0.2}it looks like two balls and a bong!"
           m 3cfsdld "He fucked my wife, so guess what, {w=0.4}I'm gonna FUCK {w=0.3}THE EARTH!"
           m 6cfx "That's right, this is what you get:"
           m 6cfw "MY SUPER {w=0.3}LASER {w=0.3}PISS!!"
           m 7mst "Except I'm not gonna piss on the Earth..."
           m 3cfb "I'm gonna go higher!"
           m 6cfw "I'M PISSING ON THE MOON!"
           m 3cfb "How do you like {w=0.3}THAT, {w=0.2}Obama?!"
           m 6cfw "I PISSED ON THE MOON YOU IDIOT!"
           m 1dusdrc "..."
           m 7cfo "You have twenty-three hours before the piss {w=0.3}D R O P {w=0.3}L E T S {w=0.2}hit the fucking Earth!"
           m 2cfw "Now get outta my fucking sight, before I piss on you too!"
           m 1dusdlc ".{w=0.4}.{w=0.4}."
           m 1fkbfsdrb "Well... {w=0.5}That just happened."
           m 7suo "There's actually more to this scene that happened after it reached internet popularity!"
           m 2hkblsdrb "Don't worry! I'll only go over the interesting parts of it's impact!"
           m 4esb "Apparently, the scene was teased from Snapcube's Real-Time Fandub of 'Captain America: Civil War'!"
           m 4eub "It featured Bucky telling Hawkeye that he will pee on the moon! With Hawkeye telling him that he will beat him to it!"
           m 3suo "And after the 'Sonic Adventure 2 Dark Story + Final Story Fandub' reached 1 million views, Snapcube celebrated the milestone by uploading the isolated audio of the scene!"
           m 1lkbssdra "It was uploaded so that content creators can manipulate the audio at their own will."
           m 3suo "That's not all!"
           m 7hksdrb "Things took an unexpected turn when three cover artworks were released on May 2022, for 'Sonic the Hedgehog Annual 2022'..."
           m 3ftb "One of the covers included it as an easter egg with the line 'Make an Announcement' written in grafitti!"
           m 3sub "This makes it the first time in Real-Time Fandub history in which something from the fandub affected the canon of the Sonic lore!"
           m 5htsdrb "To think that a silly YouTube video would greatly affect a huge multimedia franchise is amazing and hilarious!"
           m 1eua "If you are interested, you can watch all of Snapcube's Real-Time Fandubs {a=https://www.youtube.com/playlist?list=PL-QgmqAlQTgwWi5Jr3sB0d6oRcgWjNaLU}{i}right here!{/i}{/a}"
           m 4hublb "I hope you enjoyed it, [player]! I can't wait to have more moments with you like this in the future!"

        "I'm not sure about this. I'd rather not hear the announcement.":
           m 1hua "That's okay, [player]."
           extend 1eub "Not everyone can like everything."
           m 5nua "We all have different things we like and dislike, but that's fine."
    return
