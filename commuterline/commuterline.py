import os, random, sys, time

def warna(word, warna):
	return "\x1b[0m\x1b[1;%dm" % (warna) + word + "\x1b[0m"

def header():
	print warna("#"*80, 36)
	print warna("#", 36) + " "*78 + warna("#", 36)
	print warna("#", 36) + " "*18 + warna("=== Commuter Line Jakarta Kota - Bogor ===", 31) + " "*18 + warna("#", 36)
	print warna("#", 36) + " "*78 + warna("#", 36)
	print warna("#", 36) + " "*28 + warna("1. List of Stations", 37) + " "*31 + warna("#", 36)
	print warna("#", 36) + " "*28 + warna("2. Start the Challenge", 37) + " "*28 + warna("#", 36)
	print warna("#", 36) + " "*78 + warna("#", 36)
	print warna("#"*80, 36)
	print
	print "# Dalam challenge ini, kamu diberi 2 stasiun yang berbeda\n"
	print "# Kamu harus jawab challenge ini dengan menjawab jarak dari 2 stasiun tersebut\n"
	print "# Misal, diberikan stasiun " + warna("Jakarta Kota - Mangga Besar", 37) + ", maka jawabannya adalah:"
	print "  Jakarta Kota -> Jayakarta -> Mangga Besar = 1.487 + 1.020 = " + warna("2.507", 35) + " Km\n"
	print "# Kamu diberi waktu yang cukup singkat untuk menjawab setiap challengenya\n"
	print "# Silakan lihat daftar jarak antar stasiun dengan memilih angka 1\n"
	print "# Semoga beruntung! ^_^"

jarak = (
	7.518,
	4.331,
	5.197,
	5.084,
	1.741,
	2.570,
	1.109,
	2.264,
	1.029,
	2.460,
	3.031,
	1.695,
	1.509,
	1.475,
	1.301,
	2.610,
	1.606,
	1.699,
	2.198,
	0.707,
	1.171,
	1.020,
	1.487
)	
kereta = [
	"Bogor",
	"Cilebut",
	"Bojong Gede",
	"Citayam",
	"Depok",
	"Depok Baru",
	"Pondok Cina",
	"Univ Indonesia",
	"Univ Pancasila",
	"Lenteng Agung",
	"Tanjung Barat",
	"Pasar Minggu",
	"Pasar Minggu Baru",
	"Duren Kalibata",
	"Cawang",
	"Tebet",
	"Manggarai",
	"Cikini",
	"Gondangdia",
	"Juanda",
	"Sawah Besar",
	"Mangga Besar",
	"Jayakarta",
	"Jakarta Kota"
]

# gua nyusunnya kebalik
kereta = kereta[::-1]
jarak = jarak[::-1]

header()

print
pilihan = raw_input(" [" + warna("+", 37) + "] Pilihan : ")

if pilihan == "1":
	print

	for i in range(len(kereta)):
		coy = random.randint(34, 36)
		print warna(">", coy), warna(kereta[i], coy)
		
		if i != len(kereta)-1:
			for j in range(3):
				if j==1:
					print " "*4 + warna("|", 37) + " %.3f Km" % (jarak[i])
				else:
					print " "*4 + warna("|", 37)
	print				
	sys.exit(0)				

elif pilihan == "2":
	print

	time.sleep(0.5)
	correct = 0

	for c in range(50):
		x = random.randint(0, len(kereta)-1)
		y = random.randint(0, len(kereta)-1)
		while x==y:
			x = random.randint(0, len(kereta)-1)
			y = random.randint(0, len(kereta)-1)

		total = 0.000	
		temp = 0

		if x > y:
			temp = x
			x = y
			y = temp

		for i in range(x, y):
			total += jarak[i]	

		hasil = "%.3f" % (total)

		sys.stdout.write(" [>] ")
		sys.stdout.write(warna("Challenge %d/50: " % (c+1), 35))
		sys.stdout.write(warna("%s - %s"  % (kereta[x], kereta[y]), 37) + " (in Km)\n")
		sys.stdout.write(" [>] Your answer is: ")

		a = time.time()
		tebak = raw_input()
		b = time.time()
		
		time.sleep(0.5)

		if tebak==hasil:
			if correct<=3 and (b-a) < 20:
				print "\n [" + warna("+", 32) +"] Correct!\n"
				correct += 1
			elif (b-a) < 2:
				print "\n [" + warna("+", 32) +"] Correct!\n"
				correct += 1
				if correct == 50:
					print "Congrats! Here is your flag:"
					os.system("cat flag")
					sys.exit(0)	
			else:
				print "\n [" + warna("-", 31) +"] Waktu habis!\n"
				sys.exit(0)
		else:
			print "\n [" + warna("-", 31) +"] Wrong!\n"
			sys.exit(0)

	sys.exit(0)				

else:
	print
	sys.exit(0)			
