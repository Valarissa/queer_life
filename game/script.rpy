# You can place the script of your game in this file.

init python:

    # Use a widescreen resolution.
    config.screen_width = 960
    config.screen_height = 540

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image splash e1 = "images/title1.png"
image splash e2 = "images/title2.png"
image bg bedroom = "images/bedroom.png"
image mom none = "images/mom-n.png"
image mom happy = "images/mom-h.png"
image mom mad = "images/mom-m.png"
image sib = "images/sibling.png"
image dad none = "images/dad-n.png"
image dad happy = "images/dad-h.png"
image dad mad = "images/dad-m.png"
image unknown = "images/unknown.png"
image bg street = "images/outside.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define p = Character('???', color="#000000")
define n = Character('Narrative', color="#f0f0f0")
define gender = 'x'
define sexuality = 'x'

# The game starts here.
label start:
    window hide
    
    play sound "sound/new_ep.mp3"
    
    show splash e1
    
    with Dissolve(0.75)
    
    stop sound fadeout 4.5
    
    pause(3.5)
    
    scene bg bedroom
    
    with Fade(0.75, 0.5, 1)
    
    "Day 1, Night"
    
    play sound "sound/door_knock.mp3"
    
    window show dissolve
    
    "Door Knock."
    
    pause(0.5)
    
    show unknown
    
    m "Who is it?"
    
    menu:
        "It's Mom":
            $ p = Character('Mom', color="#ff007f")
            jump talk
        
        "It's Dad":
            $ p = Character('Dad', color="#3333ff")
            jump talk

        "It's a hentai game.":
            $ p = Character('Hentai Game-', color="#3333ff")
            jump talk
         
    label talk:
        
    hide unknown
        
    if p.name == 'Mom':
        show mom none
    elif p.name == 'Dad':
        show dad none
    else:
        show sib
        
    p "Can we talk?"
    
    m "Sure, what's up?"
    
    play music "music/Anguish.mp3" fadein 1.0
    
    p "I’ve been concerned about a few things. You seem withdrawn, your grades have been slipping and I barely see you anymore."
    
    m "..."
    
    p "You come home, then just lock yourself in your room until dinner’s ready. You don’t talk to us about your day. I’ve been worried."
    
    menu:
        "I… I don’t really want to talk about it.":
            jump e1_1a
        
        "Yeah, it’s… It’s complicated.":
            jump e1_1b
            
        "...":
            jump e1_1c
        
        "Leave me alone!":
            jump e1_1d
            
    label e1_1a:
        
    p "You can talk to me. You’re my child, I love you. Just, please don’t shut me out if you’re hurting."
    
    jump e1_1_done
    
    label e1_1b:
        
    p "I understand, it’s sometimes hard to really feel anyone will get it. But I do. Let me know what’s going on."
    
    jump e1_1_done
    
    label e1_1c:
        
    p "I get it I didn’t really feel like I could turn to my parents either when I was younger, but just know that I love you."
    
    jump e1_1_done
            
    label e1_1d:
        
    p "I’m really worried about you. I’m not your enemy, I want to help. Please."
    
    jump e1_1_done
    
    label e1_1_done:
        
    p "Talk to me. I know I’m usually not around that often, but I’m here now, I’m listening. What’s been going on?"
    
    m "... Fine. I’ve… I’ve had something I’ve wanted to tell you for a while, I just didn’t know how to talk about it with you."
    
    m "..."
    
    m "I... I... am..."
    
    menu:
        "I am... gay":
            $ sexuality = 'gay'
            jump e1_2done

        "I am... trans":
            $ sexuality = 'trans'
            jump e1_2done

        "I am... bi":
            $ sexuality = 'bi'
            jump e1_2done
            
    label e1_2done:
        
    p "I… I’m not sure I understand."
        
    if sexuality == 'gay' or sexuality == 'bi':
        menu:
            "I like boys":
                $ gender = 'm'
                jump e1_3done
            "I like girls":
                $ gender = 'f'
                jump e1_3done
    elif sexuality == 'trans':
        menu:
            "I’m actually your daughter, not your son":
                $ gender = 'f'
                jump e1_3done
            "I’m actually your son, not your daughter":
                $ gender = 'm'
                jump e1_3done
            "I’m not your son... I don’t really feel like a boy or girl.":
                $ gender = 'tf'
                jump e1_3done
            "I’m not your daughter... I don’t really feel like a boy or girl.":
                $ gender = 'ts'
                jump e1_3done
                
    label e1_3done:
        
    stop music fadeout 1.0
    
    pause 1
        
    play music "music/Despair.mp3" fadein 1.5
    
    p "... I... I see..."
    
    $ family = 'They'
    
    if p.name == 'Mom':
        hide mom none
        show mom mad
        m "Please don’t tell dad."
        $ family = "He"
    elif p.name == 'Dad':
        hide dad none
        show dad mad
        m "Please don’t tell mom."
        $ family = "She"
    else:
        m "Please don't tell our hentai parents"
        $ family = "They"
        
    define child = 'child like this'
    if sexuality == 'gay':
        $ child = 'gay child'
    elif gender == 'f':
        $ child = 'daughter'
    else:
        $ child = 'son'
    
    $ conv = "Yeah... I’m not really sure how " + family.lower() + " would take this. " + family + " told me one time " + family.lower() + " is not sure if they would be able to deal with having a " + child + ". I can’t just keep this to myself though, I’m sorry."
        
    p "[conv]"
    
    p "We were proud of you. And now you are telling me this... I think I need a moment. (Sigh)"
    
    scene bg bedroom
    
    play sound "sound/door_close.mp3"
    
    $ left = p.name + " left."
                                 
    "[left]"
            
    pause 2
    
    m "..."
    
    pause 1
    
    $ end_ep1 = "This had been bothering me for a while, I felt trapped with this secret for so long already and now this? I didn’t exactly feel safe with how my " + p.name + " would react. So I left, not really sure where I would end up."
    
    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"
    
    "End of Episode 1"
    
    stop music fadeout 3.0
    
    window hide
    
    play sound "sound/new_ep.mp3" fadein 3.5
    
    show splash e2
    
    with Fade(2, 2, 2)
    
    stop sound fadeout 4.5
    
    pause 4
    
    scene bg street
    
    with Fade(1, 0.5, 1)
    
    play music "music/evening.mp3" fadein 1
    
    pause 3
    
    window show
    
    "Day 2, 1 am"
    
    pause 1
    
    n "1am, the chilled night air clings to you. You hug yourself, partially to keep warm, partially to console yourself that “home” now feels so hostile and alien to you."
    
    n "More so than it had been for years as you drew further and further into yourself. Holding in aspects of your identity, of your very self, was and continues to be painfully isolating."

    $ e2nv = "Friends inferring things about your life, being " + sexuality + ". They felt so utterly awkward and alienating that they wrench you from the moments you want to be able to enjoy, even if just for a moment. " 
    
    n "[e2nv]"
    
    n "The loneliness normally cuts so deep, but now? With nowhere to turn? It’s almost too much."
    
    pause 2
    
    m "uh… I’m so tired… I just want to sleep, but where can I go?"
    
    pause 1
    
    return
