def draw_carpet(width, height):
    print("\u2591"+"\u2593"*(width-2)+"\u2591")
    for i in range(height-2):
        print("\u2591" + "\u2593" + '\u2592' * (width-4)+ "\u2593" + "\u2591")
    print("\u2591" + "\u2593" * (width - 2) + "\u2591")

def draw_carpet_2(w, h):
    for i in range(h):
        for j in range(w):
            if j in [0, w-1]:
                print("\u2591", end='')
            elif j in [1, w-2] or i in [0, h-1] and j in range(2, w-2):
                print("\u2593", end='')
            else:
                print("\u2592", end='')
        print('\n')



draw_carpet_2(5,4)
