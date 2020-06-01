msg = "Heybroareyouok?"
out = ""

for i in range(0, len(msg), 3):
    out = out + msg[i:i+3] + " "

print(out)
