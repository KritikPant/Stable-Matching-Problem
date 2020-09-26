import collections
import copy
import sys
import random

#Gen list of preferences
def genPrefTables(n):
	values = [x for x in range(n)]
	for i in range(n):
		for j in range(n):
			selection = random.choice(values)			
			values.remove(selection)
			selection = "m" + str(selection+1)
			maleTable[i][j] = selection
		values = [x for x in range(n)]
	for i in range(n):
		for j in range(n):
			selection = random.choice(values)
			values.remove(selection)
			selection = "w" + str(selection+1)
			femaleTable[i][j] = selection
			
		values = [x for x in range(n)]

#Change list to dict for men
def genDictMen(prefTables, n):
	men = []
	for i in range (n):
		a = "m" + str(i+1)
		i += 1
		men.append(a)
	return dict( zip( men, prefTables))

#Change list to dict for women
def genDictWomen(prefTables, n):
	women = []
	for i in range (n):
		a = "w" + str(i+1)
		i += 1
		women.append(a)
	return dict( zip( women, prefTables))

#Not certain but this may end up as a couple
couples 	= [ ]

#Still does not have match
singleMen = [ ]

def createSingleMan():	
	for man in iter(menPref.keys()):
		singleMen.append(man)

def stableMatchingAlgorithm():
	while (len(singleMen) > 0): #Stop when no single men left
		for man in singleMen:
			match(man)


def match(man):
	print("DEALING WITH %s"%(man))
	for woman in menPref[man]:

		#Check if woman is in a couple already
		boolMatch = [couple for couple in couples if woman in couple]

		#If woman is single
		if (len(boolMatch) == 0):
			
			couples.append([man, woman])
			singleMen.remove(man)
			break
		
		#If woman is already in a relationship
		elif (len(boolMatch) > 0):
			#Check what number preference the current male is at
			womanCurrentMate = womenPref[woman].index(boolMatch[0][0])
			#Check what number preference the potential mate is at
			potentialMate = womenPref[woman].index(man)

			#If potential is better than current
			if (womanCurrentMate > potentialMate):
				#Remove potential from single men and pair them together
				singleMen.remove(man)
				#Append previous mate to single men
				singleMen.append(boolMatch[0][0])
				boolMatch[0][0] = man
				break
				

#### Main

#Generate Preferences
n = int(input("Enter the number of men/women: "))
#n=7
maleTable = [[0 for i in range(n)] for j in range(n)]
femaleTable = [[0 for i in range(n)] for j in range(n)]
genPrefTables(n)
menPref = genDictMen(femaleTable, n)
womenPref = genDictWomen(maleTable, n)
print (menPref)
print (womenPref)

#Solve Problem
createSingleMan()
stableMatchingAlgorithm()
print('Final Couples: %s'%(couples))
