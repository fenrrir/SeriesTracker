# Series Tracker

A simple script to parse html files from TVRage.com and get a list of episodes
for a given TV Show.

## Usage

    In [1]: import seriestracker

    In [2]: got = seriestracker.Serie("Game of Thrones")

    In [3]: got
    Out[3]: <Serie Game of Thrones>

    In [4]: got.episodes
    Out[4]: <generator object iterator at 0x9e4e1bc>

    In [5]: list(got.episodes)
    Out[5]: 
    [<Episode 1x01 - Winter is Coming>,
     <Episode 1x02 - The Kingsroad>,
     <Episode 1x03 - Lord Snow>,
     <Episode 1x04 - Cripples, Bastards, and Broken Things>,
     <Episode 1x05 - The Wolf and the Lion>,
     <Episode 1x06 - A Golden Crown>,
     <Episode 1x07 - You Win or You Die>,
     <Episode 1x08 - The Pointy End>,
     <Episode 1x09 - Baelor>,
     <Episode 1x10 - Fire and Blood>,
     <Episode 2x01 - The North Remembers>,
     <Episode 2x02 - The Night Lands>,
     <Episode 2x03 - What Is Dead May Never Die>,
     <Episode 2x04 - Garden of Bones>,
     <Episode 2x05 - The Ghost of Harrenhal>,
     <Episode 2x06 - The Old Gods And The New>,
     <Episode 2x07 - A Man Without Honor>,
     <Episode 2x08 - The Prince of Winterfell>,
     <Episode 2x09 - Blackwater>,
     <Episode 2x10 - Valar Morghulis>]

    In [6]: got.episodes_as_list
    Out[6]: 
    [<Episode 1x01 - Winter is Coming>,
     <Episode 1x02 - The Kingsroad>,
     <Episode 1x03 - Lord Snow>,
     <Episode 1x04 - Cripples, Bastards, and Broken Things>,
     <Episode 1x05 - The Wolf and the Lion>,
     <Episode 1x06 - A Golden Crown>,
     <Episode 1x07 - You Win or You Die>,
     <Episode 1x08 - The Pointy End>,
     <Episode 1x09 - Baelor>,
     <Episode 1x10 - Fire and Blood>,
     <Episode 2x01 - The North Remembers>,
     <Episode 2x02 - The Night Lands>,
     <Episode 2x03 - What Is Dead May Never Die>,
     <Episode 2x04 - Garden of Bones>,
     <Episode 2x05 - The Ghost of Harrenhal>,
     <Episode 2x06 - The Old Gods And The New>,
     <Episode 2x07 - A Man Without Honor>,
     <Episode 2x08 - The Prince of Winterfell>,
     <Episode 2x09 - Blackwater>,
     <Episode 2x10 - Valar Morghulis>]

    In [7]: got.episodes_as_list[0]
    Out[7]: <Episode 1x01 - Winter is Coming>

    In [8]: got.episodes_as_list[0].season
    Out[8]: 1

    In [9]: got.episodes_as_list[0].synopsis
    Out[9]: u'A Night\xe2\x80\x99s Watch deserter is tracked down outside of Winterfell, prompting swift justice by Lord Eddard \xe2\x80\x9cNed\xe2\x80\x9d Stark and raising concerns about the dangers in the lawless lands north of the Wall.  Returning home, Ned learns from his wife Catelyn that his mentor, Jon Arryn, has died in the Westeros capital of King\xe2\x80\x99s Landing, and that King Robert is on his way north to offer Ned Arryn\xe2\x80\x99s position as the King\xe2\x80\x99s Hand.  Meanwhile, across the NarrowSeain Pentos, Viserys Targaryen hatches a plan to win back the throne, which entails forging an allegiance with the nomadic Dothraki warriors by giving its leader, Khal Drogo, his lovely sister Daenerys\xe2\x80\x99 hand in marriage.  Robert arrives at Winterfell with his wife, Queen Cersei, and other members of the Lannister family:  her twin brother Jaime, dwarf brother Tyrion and Cersei\xe2\x80\x99s son and heir to the throne, 12-year-old Joffrey.  Unable to refuse his old friend and king, Ned prepares to leave for King\xe2\x80\x99s Landing, as Jon Snow decides to travel north to Castle Black to join the Night\xe2\x80\x99s Watch, accompanied by a curious Tyrion.   But a startling act of treachery directed at young Bran may postpone their departures.Source: HBO'

    In [10]: seriestracker.search_serie("Game Thrones")
    Out[10]: 
    [<Serie Game of Thrones>,
     <Serie Game Show Moments Gone Bananas>,
     <Serie Afghanistan: The Great Game With Rory Stewart>,
     <Serie The Game>,
     <Serie The Lying Game>,
     <Serie I Survived A Japanese Game Show>,
     <Serie Rise of the Video Game>,
     <Serie The Name of the Game>,
     <Serie Match Game>,
     <Serie The Cartoon Network Hall of Game Awards>]
