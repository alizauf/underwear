def underwear():
	
	def update_num():
		underwear_str = str(underwear_num)
		how_much = "You should bring " + underwear_str + " pairs of underwear."
		print how_much
	
#basic n+1 underwear rule	
	print "How many days long is your trip?"
	answer = raw_input()
	underwear_num = int(answer) + 1
	print "It's always good to bring an extra pair."
	update_num()
	print "But that is really just the basics. Let's dig a little deeper here."
	

	
#Swimming
	print "Will you be swimming or spending time in a hot tub on this trip?"
	answer = raw_input()
	if "y" not in answer:	
		print "But isn't the whole point of travel to spend some time in a crappy hotel pool? No? Okay, moving on."
	else:
		print "How many days will you be swimming?"
		answer = raw_input()
		underwear_num = underwear_num + int(answer)
		print "So here is my theory on how swimming affects the underwear count. For any given day that you'll be swimming, you should bring an extra pair of underwear. You'll end up taking more showers, or maybe forget your swim suit and need to swim in your underwear. It just gets complicated. So..."
		update_num()

#Working out
	print "Will you be working out while on your trip?"
	answer = raw_input()
	if "y" not in answer:
		print "Good. Relax. Enjoy."
	else:
		print "Do you typically change your underwear before working out? (I'm gonna assume you do afterward.)"
		answer = raw_input()
		if "y" not in answer:
			print "Okay, then this doesn't affect your underwear count."
		else:
			print "Okay, so how many days do you think you'll work out on this trip? Be real."
			answer = raw_input()
			if int(answer) == 0:
				print "Ah, I thought you said you were going to work out. That's okay though"
			else:
				underwear_num = underwear_num + int(answer)
				print "Well let's make sure you're prepared for " + answer + " days of sweatin' in your workout underwear." 
				update_num()

#Special underwear

		
	print "Do you need to bring any special underwear? (i.e. Spanx for a dress or somethin' sexy?)"
	answer = raw_input()
	if "y" not in answer:
		print "Well maybe next time..."
	else:
		def update_num():
			underwear_str = str(underwear_num)
			if int(total_special) > 1:
				how_much = "You should bring " + underwear_str + " regular pairs of underwear and " + total_special + " pairs of special underwear."
			elif int(total_special) == 1:
				how_much = "You should bring " + underwear_str + " regular pairs of underwear and " + total_special + " pair of special underwear."
			else:
				how_much = "You should bring " + underwear_str + " regular pairs of underwear."
			print how_much
		
		print "How many special pairs of underwear do you need?"
		answer = raw_input()
		total_special = answer
		print "And of those " + answer + " special undies, how many will you wear for an entire day?"
		answer = raw_input()
		underwear_num = underwear_num - int(answer)
		update_num()
		
	#washing machine access	
##add something about sexy underwear
	print "And finally, will you have easy access to a washing machine on your trip?"
	answer = raw_input()
	if "y" in answer:
		print "And do you actually want to do laundry on your trip?"
		answer = raw_input()
		if "y" in answer:
		#figure out how frequently they want to do laundry
			underwear_num = int(underwear_num * .7)
			print "Cool. So let's cut down your regular underwear a bit. But it's annoying to wash special underwear, so we're not going to touch that number and you can clean it when you get home." 
			
		else: 
			print "Agreed. Not a great use of time."
	else:
		print "That's okay, I don't even have easy access to laundry at home."
	
	print "And that takes us to the end of our little underwear adventure. In summary:"
	update_num()

underwear()
	

	