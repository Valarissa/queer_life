# You can place the script of your game in this file.

init python:

    # Use a widescreen resolution.
    config.screen_width = 960
    config.screen_height = 540

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image splash e1 = "images/title1.png"
image splash e2 = "images/title2.png"
image splash e3 = "images/title3.png"
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
image bg outside = "images/house.png"
image bg inside = "images/inside.png"
image bad man = "images/bad man.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define p = Character('???', color="#000000")
define n = Character('Narrative', color="#f0f0f0")
define o = Character('???', color="#000000")
define b = Character('Officer')
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

    "{b}Day 1, Night{b}"

    play sound "sound/door_knock.mp3"

    window show dissolve

    "Door Knock."

    pause(0.5)

    show unknown

    m "Who is it?"

    # Choice 1.0a
    menu:
        "It's Mom.":
            $ p = Character('Mom', color="#ff007f")
            $ o = Character('Dad', color="#ff007f")
            jump talk

        "It's Dad.":
            $ p = Character('Dad', color="#3333ff")
            $ o = Character('Mom', color="#ff007f")
            jump talk

        "It's your sibling.":
            $ p = Character('Sibling', color="#3333ff")
            $ o = Character('Mom', color="#ff007f")
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

    p "I’ve been concerned about a few things. You seem withdrawn, your grades have been slipping, and I barely see you anymore."

    m "..."

    p "You come home, then just lock yourself in your room until dinner’s ready. You don’t talk to us about your day. I’ve been worried."

    # Choice 1.1
    menu:
        "I… I don’t really want to talk about it.":
            jump e1_1a

        "Yeah, it’s… It’s complicated.":
            jump e1_1b

        "...":
            jump e1_1c

        "Leave me alone!":
            jump e1_1d

    # Response 1.1
    label e1_1a:

    p "You can talk to me. You’re my child, I love you. Just, please don’t shut me out if you’re hurting."

    jump e1_1_done

    label e1_1b:

    p "I understand, it’s sometimes hard to really feel anyone will get it. But I do. Let me know what’s going on."

    jump e1_1_done

    label e1_1c:

    if p.name == 'Sibling':
        p "I get it. I don’t really feel like I can turn to our parents either, but just know that I'm here for you."
    else:
        p "I get it. I didn’t really feel like I could turn to my parents either when I was younger, but just know that I love you."

    jump e1_1_done

    label e1_1d:

    p "I’m really worried about you. I’m not your enemy, I want to help. Please."

    jump e1_1_done

    label e1_1_done:

    p "Talk to me. I know I’m usually not around that often, but I’m here now, I’m listening. What’s been going on?"

    m "... Fine. I’ve… I’ve had something I’ve wanted to tell you for a while, I just didn’t know how to talk about it with you."

    m "..."

    m "I... I... am..."

    # Choice 1.2
    menu:
        "I am... gay.":
            $ sexuality = 'gay'
            jump e1_2done

        "I am... trans.":
            $ sexuality = 'trans'
            jump e1_2done

        "I am... bi.":
            $ sexuality = 'bi'
            jump e1_2done

    label e1_2done:

    p "I… I’m not sure I understand."

    if sexuality == 'gay' or sexuality == 'bi':
        # Choice 1.2a/c
        menu:
            "I like boys.":
                $ gender = 'm'
                jump e1_3done
            "I like girls.":
                $ gender = 'f'
                jump e1_3done
    elif sexuality == 'trans':
        # Choice 1.2b
        menu:
            "I’m actually your daughter, not your son.":
                $ gender = 'f'
                jump e1_3done
            "I’m actually your son, not your daughter.":
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
        # Dialogue 1.0a
        hide mom none
        show mom mad
        m "Please don’t tell dad."
        $ family = "He"
    elif p.name == 'Dad':
        # Dialogue 1.0b
        hide dad none
        show dad mad
        m "Please don’t tell mom."
        $ family = "She"
    else:
        # Dialogue 1.0c
        m "Please don't tell our parents."
        $ family = "They"

    define child = 'child like this'
    if sexuality == 'gay':
        $ child = 'gay child'
    elif gender == 'f':
        $ child = 'daughter'
    else:
        $ child = 'son'

    $ family_is = family.lower()

    if p.name == 'Sibling':
        $ family_is += " are"
    else:
        $ family_is += " is"

    p "Yeah... I’m not really sure how [family_is] would take this. [family] told me one time [family_is] not sure if [family_is] would be able to deal with having a [child]. I can’t just keep this to myself though, I’m sorry."

    p "We were proud of you. And now you are telling me this... I think I need a moment. (Sigh)"

    scene bg bedroom

    play sound "sound/door_close.mp3"

    "[p.name] left"

    pause 2

    m "..."

    pause 1

    n "This had been bothering me for a while, I felt trapped with this secret for so long already and now this? I didn’t exactly feel safe with how my [p.name] would react. So I left, not really sure where I would end up."


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

    "{b}Day 2, 1 am{b}"

    pause 1

    n "1am, the chilled night air clings to you. You hug yourself, partially to keep warm, partially to console yourself that “home” now feels so hostile and alien to you."

    n "More so than it had been for years as you drew further and further into yourself. Holding in aspects of your identity, of your very self, was and continues to be painfully isolating."

    n "Friends inferring things about your life, being [sexuality]. They felt so utterly awkward and alienating that they wrench you from the moments you want to be able to enjoy, even if just for a moment. "

    n "The loneliness normally cuts so deep, but now? With nowhere to turn? It’s almost too much."

    pause 1

    m "Uh… I’m so tired… I just want to sleep, but where can I go?"

    pause 1

    menu:
        "Find a bench to sleep on in the park.":
            jump e2_1a
        "Call a friend.":
            jump e2_1b
        "Look for the nearest homeless shelter.":
            jump e2_1c
        "Call your older sibling who moved out.":
            jump e2_1d
   
    label e2_1a:

    n "Walking through the park, you find a bench. It doesn’t exactly look comfortable, but the thought of dealing with other people seems a bit too much right now. Laying down, you unpack some clothes to cover yourself to keep out the chill. You close your eyes and drift asleep."
    
    show unknown

    n "A sharp pain in your rib jolts you awake and you see a silhouetted figure standing over you."

    # Decision 2.1a.0
    $ agression = 0

    menu:
        "What the hell?!":
            $ agression += 2
            jump e2_2
        "(Stand up)":
            jump e2_2
        "Hrnnngh… go away.":
            $ agression += 1
            jump e2_2
        "What? What’s going on?":
            jump e2_2

    label e2_2:

    hide unknown
    
    show bad man

    n "The figure grabs you and hauls you bodily to your feet. In the new perspective, you can tell the person is a police officer."

    b "I said on your feet!"

    jump e2_3

    label e2_3:

    menu:
        "I’m sorry officer! I couldn’t tell your were a policeman":
            jump e2_4
        "Get off of me!":
            $ agression += 2
            jump e2_4
        "What did I do?":
            $ agression += 1
            jump e2_4

    label e2_4:

    if agression == 0:
        b "It’s alright, listen. Do you have any ID on you?"
        jump e3_0
    elif agression <= 2:
        b "Let me see your ID."
        jump e3_0
    else:
        b "I’m so sick of dealing with f*cking punks like you. Give me your ID, now."
        jump e3_0

    label e2_1b:

    n "Your friend takes you in and you crash on their couch."

    jump e3_0

    label e2_1c:

    n "You are lucky to get the last bed available in the youth shelter."

    jump e3_0

    label e2_1d:

    n "Your sibling picks you up and drives you to their place."

    jump e3_0

    label e3_0:

    n "You’re left in the room, your only companion the receptionist behind a plate of bulletproof glass. (** She still stares at you disapprovingly when she thinks you aren’t looking)"

    n "A ticking clock provides a constant noise, punctuated by the clacking of the receptionists keyboard, occasional doors closing, and footsteps in distant hallways. The thought of the officer calling your parents is a grim reminder of how much more likely your parents are to blow up at you now."

    play sound "sound/tick.mp3" fadein 2

    n "Being queer is bad enough, but now you’re already getting in trouble with police because of it!” Their condemning voice(s) run through your mind in a downward spiral as someone comes into the room."

    b "No answer. I tried calling a few times, but they never picked up. You can make one call for someone to potentially release you, they have to be an adult in order for us to release you to their custody"

    stop sound fadeout 2

    menu:
        "Call no one. (Wait for parents)":
            jump ep2_7
        "Call older sibling":
            jump ep2_7
        "Call friend to see if their parent will help":
            jump ep2_7
        "Call relative":
            jump ep2_7
    label ep2_7:

    m "..."

    n "Eventually you drift off to sleep. You’re awoken by the click of the key in the lock and the sounds of the door being opened"

    b "Your parent is here. They’ve filled out all the release forms. You’re free to go. Try to stay out of trouble. Next time, stay with a friend or something, just, don’t sleep in the park or on the street, it’s dangerous"

    # Episode III
    stop music fadeout 3

    pause 2

    window hide

    play sound "sound/new_ep.mp3" fadein 3.5

    show splash e3

    with Fade(2, 2, 2)

    stop sound fadeout 4.5

    pause 4

    scene bg outside

    with Fade(2, 2, 2)

    window show

    play music "music/newStart.mp3" fadein 3

    n "The car ride feels like an eternity, your [p.name] barely looks at you the entire way. They occasionally sigh, and shake their head. The first words they say are as you pull up to your house"

    if p.name == 'Mom':
        $ other_parent = 'dad'

    else:
        $ other_parent = 'mom'

    p "We are going to have a talk to your [other_parent]"

    p "We were worried sick about you. I mean, honestly, how could you think to run off like that? Did you think we wouldn’t worry?"

    n "You get out of the car, looking at the house you normally would call home. A sense of dread and trepidation washes over you as you take your first steps towards your confrontation with your [other_parent]"

    play sound "sound/door_open.mp3" fadein 1

    n "You open the door slowly, you hear chairs being pushed and hurried footsteps in adjacent room. Your [other_parent] rush forward and hug you tight, then hold your shoulders at arms length so they can stare at you."

    scene bg inside

    if p.name == 'Mom':
        show dad mad
    else:
        show mom mad

    o "Oh thank god you’re alright. I was so worried about you!"

    o "Why would you run off like that?! What were you so scared of?"

    menu:
        "I have something that I… That I was afraid to tell you.":
            jump ep3_2
        "Honestly? You.":
            jump ep3_2
        "I just… I didn’t feel comfortable.":
            jump ep3_2
        "...":
            jump ep3_2

    label ep3_2:

    if p.name == 'Mom':
        hide dad mad
        show dad none
    else:
        hide mom mad
        show mom none

    o "Is this what your [p.name] told me about?"

    menu:
        "... Yeah":
            jump ep3_3
        "I can't believe they told you when I told them not to": 
            jump ep3_3
        "Please don't be upset":
            jump ep3_3
        "...":
            jump ep3_3

    label ep3_3:

    o "You know we love you. The only thing any parent should ever want is for their child to be happy. It’ll take some time to get used to, but we’ll try to do our best to support you."

    if p.name == 'Mom':
        #hide dad none
        show dad happy at left
    else:
        #hide mom none
        show mom happy at left

    p "We always love you and we are always pround of you."

    if p.name == 'Mom':
        show mom happy at right
    else:
        show dad happy at right

    menu:
        "I ... I LOVE you too":
            jump end
        "Thank you... I was so worried how you'd act":
            jump end
        "Thanks for being so awesome about this":
            jump end
        "... * tear up * ...":
            jump end

    label end:

    scene fadein 5
    
    "Fin"

    stop music fadeout 7

    pause 10

    return
