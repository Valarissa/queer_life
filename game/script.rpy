# You can place the script of your game in this file.

init python:

    # Use a widescreen resolution.
    config.screen_width = 960
    config.screen_height = 540

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image splash e1 = "images/title1.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define p = Character('???', color="#000000")
define gender = 'x'
define sexuality = 'x'

# The game starts here.
label start:
    window hide
    
    scene splash e1
    
    pause(3)
    
    play sound "door_knock.mp3"
    
    window show dissolve
    
    m "Who is it?"
    
    menu:
        "It's Mom":
            $ p = Character('Mom', color="#ff007f")
            jump talk
        
        "It's Dad":
            $ p = Character('Dad', color="#3333ff")
            jump talk

        "It's your sibling":
            $ p = Character('Sibling', color="#3333ff")
            jump talk
         
    label talk:
        
    p "Can we talk?"
    
    m "Sure, what's up?"
    
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
    
    menu:
        "I am gay":
            $ sexuality = 'gay'
            jump e1_2done

        "I am trans":
            $ sexuality = 'trans'
            jump e1_2done

        "I am bi":
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
    p ".. I.. I see..."
    
    define family = 'They'
    
    if p.name == 'Mom':
        p "Please don’t tell dad."
        $family = "He"
    elif p.name == 'Dad':
        p "Please don’t tell mom."
        $family = "She"
    else:
        p "Please don't tell our hentai parents"
        $family = "They"
        
    define child = 'child like this'    
    if sexuality == 'gay':
        $child = 'gay child'
    elif gender == 'f':
        $child = 'daughter'
    else:
        $child = 'son'
    
    #TODO fix me
    $ conv = "Yeah... I’m not really sure how " + family.lower() + "would take this." + family + "told me one time" + family.lower() + " is not sure if they would be able to deal with having a " + child + ". I can’t just keep this to myself though, I’m sorry."
        
    p "[conv]"
    
    m "... This had been bothering me for a while, I felt trapped with this secret for so long already and now this? I didn’t exactly feel safe with how my (mom, dad, parents) would react. So I left, not really sure where I would end up."
    
    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    return
