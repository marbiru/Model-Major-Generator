print "\n Welcome to the Major System program. This gives you an image for any number \n"

single_digit_peg_list = [
"hose",
"hat",
"hen",
"home",
"arrow",
"whale",
"shoe",
"cow",
"hoof",
"pie"
]

pegs_list = [
"sauce",
"seed",
"sun",
"sumo",
"sierra",
"soil",
"sachet",
"sky",
"sofa",
"soap",
"daisy",
"tattoo",
"tuna",
"dome",
"diary",
"tail",
"dish",
"dog",
"dove",
"tuba",
"nose",
"net",
"onion",
"enemy",
"winery",
"nail",
"nacho",
"neck",
"knife",
"honeybee",
"mouse",
"meadow",
"moon",
"mummy",
"hammer",
"mole",
"match",
"mug",
"movie",
"map",
"rice",
"road",
"rain",
"rum",
"warrior",
"railway",
"archway",
"rag",
"roof",
"rope",
"louse",
"lady",
"lion",
"lime",
"lorry",
"lily",
"leech",
"leg",
"lava",
"lip",
"cheese",
"cheetah",
"chin",
"gem",
"shrew",
"chilli",
"cha-cha",
"chick",
"chef",
"jeep",
"goose",
"cat",
"coin",
"game",
"crow",
"clay",
"cage",
"cake",
"cave",
"cube",
"vase",
"video",
"fan",
"foam",
"fairy",
"fool",
"veggie",
"fig",
"high-five",
"vibe",
"boss",
"bead",
"pony",
"puma",
"berry",
"bell",
"pouch",
"bike",
"beef",
"pipe",
]

mnemonic = ""

the_input = raw_input("Enter the number you'd like to memorise \n")

while len(the_input) > 1:

	next_number = int(the_input[0:2])
	
	next_image = pegs_list[next_number]
	
	the_input = the_input[2:]
	
	mnemonic += " " + next_image

if len(the_input) == 1:

	next_number = int(the_input[0:1])
	
	next_image = single_digit_peg_list[next_number]
	
	mnemonic += " " + next_image

else:

	pass

print mnemonic