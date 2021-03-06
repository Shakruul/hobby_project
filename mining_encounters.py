		if dice == 1:
			desc = f'but you realize you\'re walking in circles and that you\'re just lost.'
		elif dice == 2:
			desc = f'and come across a humanoid skeleton.'
		elif dice == 3:
			desc = f'and see something written in dwarvish on the walls: ||\'You are being watched\'||'
		elif dice == 4:
			desc = f'and find a small node of coal worth **{roll("1d24mi6")}sp** Make a **DC8 STR check** to break it out and add the silver directly to your pouch.'
		elif dice == 5:
			desc = f'but you get to a dead end and trace your steps back'
		elif dice == 6:
			desc = f'and come across a bunch of rocks and boulders. They seem worthless.'
		elif dice == 7:
			desc = f'and you find some brown fungi. Make a **DC14 Nature check** {roll("1d8mi3")}gp. Add the gold directly to your pouch'
		elif dice == 8:
			desc = f'and you find some yellow small fungi. You easily collect them, they are worth **{roll("1d36mi18")}sp**. Add the silver directly to your pouch'
		elif dice == 9:
			desc = f'but you come across some rats running away from something, you get an unnerving feeling creeping upon you.'
		elif dice == 10:
			desc = f'and you find a wooden door. It is locked. Make a **DC14 Thieves\' Tools check** if you have one with `!tool thi dex`. Or maybe even break it open? **Make a DC18 STR check**. If you get past, you get deeper into this cave system.'
		elif dice == 11:
			desc = f'and you come across a small iron node worth **{roll("1d12mi8")}gp**. Make a **DC8 STR check** to add the gold directly to your pouch'
		elif dice == 12:
			desc = f'and find some skulls tied to a rope hanging from the ceiling. If you succeed on a **DC15 Investigation check**. You can identify that most are humanoid besides 2 others that are from beasts. You are unsure if you wanna continue your journey deeper.'
		elif dice == 13:
			desc = f'but you come across two giant bats sleeping from the ceiling. Make a **DC10 Stealth check** to pass unnoticed!'
		elif dice == 14:
			desc = f'and you come across a mediocre sized node of coal worth **{roll("1d96mi32")}sp**. Make a **DC10 STR check** to add the silver direcly to your pouch'
		elif dice == 15:
			desc = f'and you come across a larger part of this cavern and the ground is mostly covered in white fungi. As you step into the cavern, make a **DC13 Stealth Check**, on failure the fungi start screaming and force you to go different way.'
		elif dice == 16:
			desc = f'and you come across a burning camp-fire that seems deserted. You feel the unnerving sensation of being watched and hastily leave the area'
		elif dice == 17:
			desc = f'and you come across some vines leading upwards deeper into this cave system. Make a **DC10 Athletics Check** to climb up.'
		elif dice == 18:
			desc = f'and find a treasure chest. Add **{roll("1d20mi7")}gp** to your pouch'
		elif dice == 19:
			desc = f'but you come across a wooden barricade that blocks the way further into the cave. (It has **AC 14** and **30HP**, destroy it down however you like).'
		elif dice == 20:
			desc = f'and you find some geodes worth **{roll("1d20mi10")}sp**. Add the silver directly to your pouch' 
		elif dice == 21:
			desc = f'but you fall down a small 10ft deep pit. Make **DC10 Acrobatics check** to avoid it.' 
		elif dice == 22:
			desc = f'and you find an abandoned mine-cart rail running deeper into the caves.'
		elif dice == 23:
			desc = f'and you find some bloody daggers laying around.'
		elif dice == 24:
			desc = f'and you find some loot scattered around including a Potion of Healing and a pouch with **15gp** in it. You also see a note saying: \'Take whatever you need, and maybe leave something behind for those following\'.'
		elif dice == 25:
			desc = f'when you faintly make out the whispers and murmuring of a ritual being cast.'
		elif dice == 26:
			desc = f'but some rocks fall from above. Make a DC10 **DEX SAVE** or type `!hp -d4 [Bludgeoning]`'
		elif dice == 27:
			desc = f'but you only find a water source running deeper into the cave.'
		elif dice == 28:
			desc = f'and you find a rope leading a steep way down, far deeper into the cave.'
		elif dice == 29:
			desc = f'and you discover a mediocre node of coal on the wall worth **{roll("1d96mi32")}sp**. Make a **DC10 STR check** to add the silver directly to your pouch.'
		elif dice == 30:
			desc = f'but you come to a hollow cave with some empty sheets of paper on the ground.'
		elif dice == 31:
			desc = f'and you find a perfectly symmetrical room, odd.'
		elif dice == 32:
			desc = f'but you suddenly get envoloped in sheer darkness as you watch your most dreaded nightmare come lumbering out of the shadows, towards you. Make a **DC16 WIS Saving throw**, on success, you realize it was an illusion to ward off explorers'
		elif dice == 33:
			desc = f'and you find a statue resembling a fiend. On a successful **DC14 Religion Check**, you remember that you can offer an skull in exchange for **15gp**'
		elif dice == 34:
			desc = f'but you\'ve accidentally walked into a Stirge\'s nest. **Make a DC13 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 35:
			desc = f'but a **crawling claw** tries to reach out and grab your foot, as you turn around you see 5 more...' 
		elif dice == 36:
			desc = f'and you find a small node of gold!. Make a **DC8 STR check** to add **{roll("1d25mi10")}gp** directly to your pouch.'
		elif dice == 37:
			desc = f'and you come across a large room with a high ceiling and you can see some torches lit along the wall.'
		elif dice == 38:
			desc = f'and you find a dead end Make **DC 14 Arcana Check to discover that it is just an illusion and behind it the cave network continues.' 
		elif dice == 39:
			desc = f'but you enter an room with gruesome bones with rotting flesh laying around, you have a really bad feeling that something terrible has happened here.'
		elif dice == 40:
			desc = f'but you find three rotting corpses with their hands ripped off.'
		elif dice == 41:
			desc = f'and you come across a mediocre iron node on the floor worth **{roll("1d26mi14")}gp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 42:
			desc = f'and you find a sentient fishing rod that talks to you in a funny voice.'
		elif dice == 43:
			desc = f'and you find four chairs and a table with a book on it, titled \'How to Have Fun in a Cave\' and two bottles of fine mead.'
		elif dice == 44:
			desc = f'but as you go deeper two giant centipedes crawl out of a hole in the side of the cave! {disengage}'
		elif dice == 45:
			desc = f'but you enter a room full of thick purplish gas. Make a **DC 15 CON Saving throw** or become poisoned and roll all ability checks at disadvantage for 30 minutes.'
		elif dice == 46:
			desc = f'and you find a gemstone with an magical aura in the wall worth **{roll("1d50mi30")}gp**. Make a **DC15 STR check** to add the gold directly to your pouch.'
		elif dice == 47:
			desc = f'and you enter a strange room where the floor is made out of glass letting you see all that\'s going on inside the tavern!'
		elif dice == 48:
			desc = f'and you find a small node of coal worth **{roll("1d24mi6")}sp** Make a **DC 8 Strength Check** to retreive it and add the silver directly to your pouch.'
		elif dice == 49:
			desc = f'and you see a cultist going further into one of the three ways. You also find some lavender scented candles on the floor.'
		elif dice == 50:
			desc = f'but you come across a Spectator that telepathically tells you: \'Leave this part of the Cavern and let me rest!\' **Make a DC15 Perception Check** to notice a crate with 3 Potions of Healing behind the Spectator.'
		elif dice == 51:
			desc = f'and somebody tells you through telepathy: \'Tread carefully\''
		elif dice == 52:
			desc = f'but you fall into a pit with a glowing aura and mysteriously wake up in the tavern!' 
		elif dice == 53:
			desc = f'and you find an amethyst stuck in the floor! **Make a DC 12 Strength Check** to retrieve it, on success add **45gp** directly to your pouch!'
		elif dice == 54:
			desc = f'and you come across a perfectly refreshing fountain. If you drink from it, the water stops flowing and type: `!hp + 2d4+2`.'
		elif dice == 55:
			desc = f'and you discover a small node of iron worth **{roll("1d12mi8")}gp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 56:
			desc = f'and you discover a large node of coal worth **{roll("1d2mi10")}gp**. Make a **DC12 STR check** to Add the gold directly to your pouch.'
		elif dice == 57:
			desc = f'and you discover a mediocre node of iron worth **{roll("1d26mi14")}gp**! **Make a DC10 Strength Check** to add the gold directly to your pouch..'
		elif dice == 58:
			desc = f'and you find a coupon wedged between some rocks for a free drink and meal from Denzel! You can skip paying for two orders with this!'
		elif dice == 59:
			desc = f'but you find an empty room with two exits, you notice a gelatinous cube right in the center of the room!'
		elif dice == 60:
			desc = f'and in surprise, you find a massive node of gold worth **{roll("1d140mi100")}gp**. Make a **DC12 STR check with Advantage** to add the gold directly to your pouch.'
		elif dice == 61:
			desc = 	f'and you find a statue resembling you. The statue animates after a minute and roams around the world for one day, spreading lies and rumours about you, it has **3 HP** and you can kill it to prevent it leaving the caves. (If you choose to RP it, use the tupperbot NPC to RP the statue: `tul!help` for more info!'
		elif dice == 62:
			desc = 	f'but you come across some chains tied to the wall, that seem broken. You get an anxious-inducing feeling.'
		elif dice == 63:
			desc = 	f'and you come across some barrels with some old rations aswell as unlit torches.'
		elif dice == 64:
			desc = 	f'but you come across an exact copy of the <#745568550676070420>?'
		elif dice == 65:
			desc = 	f'and you find a small node of copper worth **{roll("1d24mi7")}sp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 66:
			desc = 	f'and you find a mediocre node of copper worth **{roll("1d16mi15")}sp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 67:
			desc = 	f'and you come across a room with a magical pickaxe, that you can use 5 times to skip an strength check until it breaks.'
		elif dice == 68:
			desc = 	f'but you come across an room dimly lit with an table in the centre and you see 3 goblins and a hobgoblin drinking. Make a **DC8 Stealth check** to pass unnoticed!'