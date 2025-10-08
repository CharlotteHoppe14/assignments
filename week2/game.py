import time
import sys

def typing(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_int(prompt, min_v, max_v):
    while True:
        inp = input(prompt)
        if not inp.isdigit():
            print('❌ Enter a valid number.')
            continue
        n = int(inp)
        if n < min_v or n > max_v:
            print(f'❌ Number must be between {min_v} and {max_v}.')
            continue
        return n

def page_intro():
    typing("🌑  Welcome to Midnight Manor! 🌑")
    time.sleep(0.5)
    uname = input("Enter your name: ")
    typing(f"Hi {uname}. You're at the manor's gate. Go in? (yes/no)")
    ans = input().strip().lower()
    if ans != "yes":
        typing("Gate slams behind you! No escape, only forward!")
    else:
        typing("You step inside. The door shuts behind you.")
    return uname

def page_weapon():
    wpn = input("Pick your weapon: sword / candle / book: ").strip().lower()
    while wpn not in ["sword", "candle", "book"]:
        print("Please choose sword, candle, or book.")
        wpn = input("Pick your weapon: sword / candle / book: ").strip().lower()
    return wpn

def page_door():
    typing("Three doors stand ahead: red / blue / green.")
    dr = input("Which door? ").strip().lower()
    while dr not in ["red", "blue", "green"]:
        print("Pick one: red, blue, green.")
        dr = input("Which door? ").strip().lower()
    return dr

def page_code():
    return get_int("Enter code for the locked chest (3-7): ", 3, 7)

def page_light(wpn):
    if wpn == "candle":
        typing("It's pitch dark. Light your candle? (yes/no)")
        l = input().strip().lower()
        return l
    return None

def page_branch(wpn, dr, code, light):
    # All main conditionals, including a nested if
    if wpn == 'sword':
        typing("Your sword feels heavy. Ready for battle.")
        if dr == 'red':
            typing("A dragon blocks your way!")
            if code == 5:
                typing("Victory! You find golden treasure. 🗝️")
            else:
                typing("You swing, but the treasure chest stays locked.")
        elif dr == 'blue':
            typing("Frosty air chills you. Swing or run?")
            if code == 6:
                typing("A hidden shield saves you from icy harm.")
            else:
                typing("A shadow stalks you... You run!!")
        else: # green
            typing("Vines grab you! You escape, but lose your sword.")
    elif wpn == 'candle':
        if light == 'yes':
            typing("Warm light fills the room. Ghosts murmur secrets.")
            if dr == 'green':
                typing("You discover a hidden path behind a tapestry!")
            else:
                typing("Figures flicker... but nothing stops you yet.")
        else:
            typing("You grope through darkness and feel invisible webs.")
    elif wpn == 'book':
        typing("Mysterious energy hums from your book.")
        if dr == 'blue':
            typing("The book glows blue—protection spell active!")
            if code == 7:
                typing("The code works! An exit opens, swirling with magic.")
            else:
                typing("A puzzle remains. The exit stays closed.")
        else:
            typing("Creepy laughter spills from the pages, but you press on.")
    else:
        typing("You're unarmed but hopeful. Sometimes luck wins out!")
        if code == 3:
            typing("The wall slides away! Secret door found.")
        else:
            typing("Nothing happens. Time ticks on...")

def main():
    uname = page_intro()
    wpn = page_weapon()
    dr = page_door()
    code = page_code()
    light = page_light(wpn)
    page_branch(wpn, dr, code, light)
    typing(f"Good job, {uname}! 👻 Thanks for playing Midnight Manor.")

if __name__ == '__main__':
    main()
