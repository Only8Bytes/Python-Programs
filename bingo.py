#Fall Guys Bingo Randomizer
#Programmed with Python

#Instructions:
#1. Run program with IDLE or any other program or website that runs Python code
#2. Copy the printed text
#3. On [bingosync.com], begin to make a room and for [Game] select: Custom (Advanced) and for [Variant] select: Randomized
#4. Paste printed text for [Board]
#5. Select any other options as needed and finish creating the room

import random
import pyperclip

choices = {
    14: "{\"name\": \"Win a finals without jumping\"}",
    15: "{\"name\": \"Win a finals without diving\"}",
    16: "{\"name\": \"Win a finals without grabbing\"}",
    22: "{\"name\": \"Earn a gold medal from a race round without jumping\"}",
    23: "{\"name\": \"Earn a gold medal from a race round without diving\"}",
    29: "{\"name\": \"Earn a gold medal on any Tail round\"}",
    59: "{\"name\": \"Earn a gold medal from a team round\"}",
    60: "{\"name\": \"Earn a silver medal from a team round\"}",
    61: "{\"name\": \"Qualify last on any race round\"}",
    62: "{\"name\": \"Qualify last on race rounds twice in a row\"}",
    63: "{\"name\": \"Qualify any round holding a pegwin\"}",
    64: "{\"name\": \"Find a Lil' Yeety\"}",
    65: "{\"name\": \"Win back-to-back episodes\"}",
    66: "{\"name\": \"Take the out of bounds shortcut on Whirlygig\"}",
    67: "{\"name\": \"Have any race or final round end by timing out\"}",
    68: "{\"name\": \"Qualify from Lily Leapers without retouching the ground\"}"
}

choicesTwo = {
    5: ["{\"name\": \"Eliminate a total of 2 beans on survival rounds from Season 1 (& Slime Climb)\"}", "{\"name\": \"Eliminate a total of 4 beans on survival rounds from Season 1 (& Slime Climb)\"}"],
    6: ["{\"name\": \"Eliminate a total of 1 bean on survival rounds from Season 3\"}", "{\"name\": \"Eliminate a total of 2 beans on survival rounds from Season 3\"}"],
    7: ["{\"name\": \"Eliminate a total of 2 beans on survival rounds from Season 4\"}", "{\"name\": \"Eliminate a total of 4 beans on survival rounds from Season 4\"}"],
    8: ["{\"name\": \"Eliminate a total of 2 beans on Roll Out / Roll Off\"}", "{\"name\": \"Eliminate a total of 4 beans on Roll Out / Roll Off\"}"],
    9: ["{\"name\": \"Grab 4 people off during a round of Big Fans\"}", "{\"name\": \"Grab 6 people off during a round of Big Fans\"}"],
    30: ["{\"name\": \"Succesfully land from a total of 5 Big Yeetuses\"}", "{\"name\": \"Succesffuly land from a total of 3 UNIQUE Big Yeetuses\"}"],
    31: ["{\"name\": \"Succesffuly land from a total of 10 Big Yeetuses\"}", "{\"name\": \"Succesffuly land from a total of 5 UNIQUE Big Yeetuses\"}"],
    32: ["{\"name\": \"Successfully land from a total of 15 Big Yeetuses\"}", "{\"name\": \"Succesffuly land from a total of 7 UNIQUE Big Yeetuses\"}"],
    33: ["{\"name\": \"Grab a plain bean\"}", "{\"name\": \"Grab an egg bean\"}"],
    34: ["{\"name\": \"Grab an among us bean\"}", "{\"name\": \"Grab a dragon bean\"}"],
    35: ["{\"name\": \"Grab a knight bean\"}", "{\"name\": \"Grab a shark bean\"}"],
    36: ["{\"name\": \"Grab a monkey bean\"}", "{\"name\": \"Grab a golden witch bean\"}"],
    37: ["{\"name\": \"Share a hug with 2 different beans\"}", "{\"name\": \"Share a hug with 4 different beans\"}"],
    38: ["{\"name\": \"Share a hug with 6 different beans\"}", "{\"name\": \"Share a hug with 8 different beans\"}"],
    39: ["{\"name\": \"Qualify from round 3 at least 3 times\"}", "{\"name\": \"Qualify from round 3 at least 4 times\"}"],
    40: ["{\"name\": \"Qualify from round 4 at least 2 times\"}", "{\"name\": \"Qualify from round 4 at least 3 times\"}"],
    41: ["{\"name\": \"Qualify from round 5 at least 1 time\"}", "{\"name\": \"Qualify from round 5 at least 2 times\"}"],
    43: ["{\"name\": \"Qualify from team rounds 1 time\"}", "{\"name\": \"Qualify from team rounds 2 times\"}"],
    44: ["{\"name\": \"Qualify from race rounds 6 times\"}", "{\"name\": \"Qualify from survival rounds 5 times\"}"],
    45: ["{\"name\": \"Qualify from survival rounds 3 times\"}", "{\"name\": \"Qualify from race rounds 9 times\"}"],
    46: ["{\"name\": \"Earn a total of 6 gold medals\"}", "{\"name\": \"Earn a total of 12 gold medals\"}"],
    47: ["{\"name\": \"Earn a total of 4 silver medals\"}", "{\"name\": \"Earn a total of 8 silver medals\"}"],
    48: ["{\"name\": \"Earn a total of 4 bronze medals\"}", "{\"name\": \"Earn a total of 8 bronze medals\"}"],
    49: ["{\"name\": \"Earn a total of 3 pink medals\"}", "{\"name\": \"Earn a total of 6 pink medals\"}"],
    51: ["{\"name\": \"Earn at least 4 gold medals in a single episode\"}", "{\"name\": \"Earn at least 3 silver medals in a single episode\"}"],
    52: ["{\"name\": \"Earn at least 3 bronze medals in a single episode\"}", "{\"name\": \"Earn at least 2 pink medals in a single episode\"}"],
    53: ["{\"name\": \"Earn a total of 1000 kudos\"}", "{\"name\": \"Earn a total of 1500 kudos\"}"],
    54: ["{\"name\": \"Earn a total of 2000 kudos\"}", "{\"name\": \"Earn a total of 2500 kudos\"}"],
    55: ["{\"name\": \"Earn a total of 3000 kudos\"}", "{\"name\": \"Earn a total of 3500 kudos\"}"],
    56: ["{\"name\": \"Jump through a total of 10 hoops\"}", "{\"name\": \"Jump through a total of 15 hoops\"}"],
    57: ["{\"name\": \"Jump through a total of 20 hoops\"}", "{\"name\": \"Jump through a total of 25 hoops\"}"],
    69: ["{\"name\": \"Stay on top of a swinging bar in Jump Club\"}", "{\"name\": \"Stay on top of the row of doors in Door Dash\"}"],
    70: ["{\"name\": \"Stay on top of a floating sign in Knight Fever\"}", "{\"name\": \"Stay on top of the moving blocks near the end of Block Party\"}"]
}

choicesThree = {
    12: ["{\"name\": \"Qualify 2 race rounds without jumping\"}", "{\"name\": \"Qualify 2 race rounds without diving\"}", "{\"name\": \"Qualify 2 race rounds without grabbing\"}"],
    13: ["{\"name\": \"Qualify 4 race rounds without jumping\"}", "{\"name\": \"Qualify 4 race rounds without diving\"}", "{\"name\": \"Qualify 4 race rounds without grabbing\"}"],
    17: ["{\"name\": \"Qualify 2 survival rounds without jumping\"}", "{\"name\": \"Qualify 2 survival rounds without diving\"}", "{\"name\": \"Qualify 2 survival rounds without grabbing\"}"],
    18: ["{\"name\": \"Qualify 3 survival rounds without jumping\"}", "{\"name\": \"Qualify 3 survival rounds without diving\"}", "{\"name\": \"Qualify 3 survival rounds without grabbing\"}"],
    19: ["{\"name\": \"Qualify from 4 UNIQUE race rounds without jumping\"}", "{\"name\": \"Qualify from 4 UNIQUE race rounds without diving\"}", "{\"name\": \"Qualify from 4 UNIQUE race rounds without grabbing\"}"],
    20: ["{\"name\": \"Qualify from 6 UNIQUE race rounds without jumping\"}", "{\"name\": \"Qualify from 6 UNIQUE race rounds without diving\"}", "{\"name\": \"Qualify from 6 UNIQUE race rounds without grabbing\"}"],
    21: ["{\"name\": \"Qualify from 8 UNIQUE race rounds without jumping\"}", "{\"name\": \"Qualify from 8 UNIQUE race rounds without diving\"}", "{\"name\": \"Qualify from 8 UNIQUE race rounds without grabbing\"}"],
    24: ["{\"name\": \"Earn a gold medal on 3 race rounds from Season 1\"}", "{\"name\": \"Earn a gold medal on 4 race rounds from Season 1\"}", "{\"name\": \"Earn a gold medal on 4 UNIQUE race rounds\"}"],
    25: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 2\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 2\"}", "{\"name\": \"Earn a gold medal on 5 UNIQUE race rounds\"}"],
    26: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 3\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 3\"}", "{\"name\": \"Earn a gold medal on 6 UNIQUE race rounds\"}"],
    27: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 4\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 4\"}", "{\"name\": \"Earn a gold medal on 7 UNIQUE race rounds\"}"],
    28: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 5\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 5\"}", "{\"name\": \"Earn a gold medal on 8 UNIQUE race rounds\"}"],
    42: ["{\"name\": \"Qualify from any round 10 times\"}", "{\"name\": \"Qualify from any round 15 times\"}", "{\"name\": \"Qualify from any round 20 times\"}"],
    58: ["{\"name\": \"Jump through a total of 4 gold hoops\"}", "{\"name\": \"Jump through a total of 5 gold hoops\"}", "{\"name\": \"Jump through a total of 6 gold hoops\"}"]
}

choicesFour = {
    10: ["{\"name\": \"Win a crown on Fall Mountain\"}", "{\"name\": \"Win a crown on Hex-a-gone\"}", "{\"name\": \"Win a crown on Lost Temple\"}", "{\"name\": \"Win a crown on Jump Showdown\"}"],
    11: ["{\"name\": \"Win a crown on Roll Off\"}", "{\"name\": \"Win a crown on Royal Fumble\"}", "{\"name\": \"Win a crown on Thin Ice\"}", "{\"name\": \"Win a low gravity final\"}"],
    50: ["{\"name\": \"Earn a total of 15 gold medals\"}", "{\"name\": \"Earn a total of 10 silver medals\"}", "{\"name\": \"Earn a total of 10 bronze medals\"}", "{\"name\": \"Earn a total of 8 pink medals\"}"]
}

choicesSix = {
    1: ["{\"name\": \"Earn a gold medal on Big Fans\"}", "{\"name\": \"Earn a gold medal on Bubble Trouble\"}", "{\"name\": \"Earn a gold medal on Door Dash\"}", "{\"name\": \"Earn a gold medal on Dizzy Heights\"}", "{\"name\": \"Earn a gold medal on Freezy Peak\"}", "{\"name\": \"Earn a gold medal on Fruit Chute\"}"],
    2: ["{\"name\": \"Earn a gold medal on Gate Crash\"}", "{\"name\": \"Earn a gold medal on Hit Parade\"}", "{\"name\": \"Earn a gold medal on Hoopsie Heroes\"}", "{\"name\": \"Earn a gold medal on Knight Fever\"}", "{\"name\": \"Earn a gold medal on Lily Leapers\"}", "{\"name\": \"Earn a gold medal on Pegwin Party\"}"],
    3: ["{\"name\": \"Earn a gold medal on Roll On\"}", "{\"name\": \"Earn a gold medal on See Saw\"}", "{\"name\": \"Earn a gold medal on Short Circuit\"}", "{\"name\": \"Earn a gold medal on Ski Fall\"}", "{\"name\": \"Earn a gold medal on Skyline Stumble\"}", "{\"name\": \"Earn a gold medal on Slime Climb\"}"],
    4: ["{\"name\": \"Earn a gold medal on Slimescraper\"}", "{\"name\": \"Earn a gold medal on Tip Toe\"}", "{\"name\": \"Earn a gold medal on Treetop Tumble\"}", "{\"name\": \"Earn a gold medal on Tundra Run\"}", "{\"name\": \"Earn a gold medal on Whirlygig\"}", "{\"name\": \"Earn a gold medal on Wall Guys\"}"]
}

numbers = random.sample(range(1, 70), 26)
output = "["

for x in range(26):
    numcheck = numbers[x]

    if numcheck in choices:
        output += choices[numcheck]

    if numcheck in choicesTwo:
        output += choicesTwo[numcheck][random.randint(1, 2) - 1]

    if numcheck in choicesThree:
        output += choicesThree[numcheck][random.randint(1, 3) - 1]

    if numcheck in choicesFour:
        output += choicesFour[numcheck][random.randint(1, 4) - 1]

    if numcheck in choicesSix:
        output += choicesSix[numcheck][random.randint(1, 6) - 1]

    if x == 25:
        output += "]"
    else:
        output += ","

pyperclip.copy(output)