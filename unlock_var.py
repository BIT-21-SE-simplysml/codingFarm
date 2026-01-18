n = 0
m = 0
while True:
	if n == 0:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
			m += 1
			if(m >= 3):
				m = 0
				n += 1
	if n == 1:
		if can_harvest():
			harvest()
			till()
			plant(Entities.Carrot)
			move(North)
			m += 1
			if(m >= 3):
				m = 0
				n += 1
	if n == 2:
		if can_harvest():
			harvest()
			move(North)
			m += 1
			if(m >= 3):
				m = 0
				n += 1
	
	
# '/Users/sml/Library/Application Support/com.TheFarmerWasReplaced.TheFarmerWasReplaced/Saves/Save0'