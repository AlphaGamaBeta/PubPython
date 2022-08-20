convereter = {"a": " .- ", "b": " -... ", "c": " -.-. ", "d": " -..  ", "e": " . ", "f": " ..-. ", "g": " --. ", "h": " .... ",
              "i": " .. ", "j": " .--- ", "k": " -.- ", "l": " .-.. ", "m": " -- ", "n": " -. ", "o": " --- ", "p": " .--. ",
              "q": " --.- ", "r": " .-. ", "s": " ... ", "t": " - ", "u": " ..- ", "v": " ...- ", "w": " .-- ", "x": " -..- ",
              "y": " -.-- ", "z": " --.. ", }
text=input("Text to be converted:\n").lower()
text=list(text)
for counter,n in enumerate(text):
    try:
        text[counter]=convereter[n]
    except KeyError:
        continue

for c,n in enumerate(text):
    print(n,end="")
    if c==20:
        print("\n")

