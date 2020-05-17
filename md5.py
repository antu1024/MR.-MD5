from pyfiglet import Figlet
import hashlib



custom_fig = Figlet(font='big')
print(custom_fig.renderText('MR. MD5'))
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("# DEVELOPER: ARMAN HOSSAIN ANTU // ANTU1024                    #")
print("# TWITTER  : https://twitter.com/antu1024                      #")
print("# ABOUT IT : MR. MD5 is a Free MD5 Encrypt & Decrypt Tools     #")
print("# VERSION  : @2.0                                              #")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("")

print("[||] 1// Encrypt")
print("[||] 2// Decrypt")
print("[||] 3// Quit")
selection=int(input("[#] Select your Mode (1,2,3):>> "))
if selection==1:
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("")
	hashvalue = input("## ENTER THE VALUE ::: ")	              
	print("")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")	    
	hashobj1 = hashlib.md5()
	hashobj1.update(hashvalue.encode())
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("")
	print ("##",hashvalue +"'s","MD5 VALUE is ::: ",hashobj1.hexdigest())
	print("")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("")
	print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024           ")
	print("")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
elif selection==2:
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("[||] 1// Dictionary Attack")
	print("[||] 2// Search the Website")
	print("[||] 3// Quit")
	selection=int(input("[#] Select your Option (1,2,3):>> "))
	if selection==1:
		def tryOpen (wordlist):
			global pass_file
			try:
				pass_file = open(wordlist,"r")
			except:
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("")
				print("## NO SUCH FILE AT THAT PATH !")
				print("")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("")
				print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
				print("")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				quit()
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		pass_hash = input ("## ENTER MD5 HASH VALUE: ")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		wordlist = input("## ENTER PATH TO THE HASH FILE (Type 'w.txt'): ")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		tryOpen(wordlist)

		for word in pass_file:
	
			enc_wrd = word.encode('utf=8')
			md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

			if md5digest == pass_hash:
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("")
				print("## HASH FOUND: " + word)
				print("")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				print("")
				print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
				print("")
				print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
				quit()	    
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## HASH NOT IN LIST")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

	elif selection==2:
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Please type this Command.< pyhton3 web-md5.py //MD5_Hash// >#")
		print("")  
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")


	elif selection==3:
 		exit()
	else:
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Invalid Option. Enter 1-3. :))                              #")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
elif selection==3:
	exit()
	
else:
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("")
	print("## Invalid Mode. Enter 1-3. :))                                #")
	print("")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
	print("")
	print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
	print("")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#") 
