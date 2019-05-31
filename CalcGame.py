import random
'''
Solution finder for the 'Calculator: The Game'
'''
class Problem():
	def __init__(self, numbsOps, goal, startingNum, numMoves):
		self.numbsOps = numbsOps
		self.goal = goal
		self.startingNum = startingNum
		self.numMoves = numMoves

	def situation(self):
		print(f"Goal: {self.goal}")
		print(f"Starting Number: {self.startingNum}")
		print(f"Numbers and Operators: {self.numbsOps}")
		print(f"Number of Moves: {self.numMoves}")

def selectMoves(problemIn):
	#selects a random list of moves to execute later on
	global moveScript
	moveScript = []
	t = len(problemIn.numbsOps)
	for x in range(problemIn.numMoves):
		#makes sense not to call len() multiple times, just grab it once and use that value throughout
		moveScript.append(problemIn.numbsOps[random.randint(0,t-1)])

def availableFunc(currNum, func):
	funcNum = int(func[1::])
	#print(f'{currNum}')
	#turns functions from string to operations
	if(func[0] == 's'):
		return currNum - funcNum
	if(func[0] == 'd'):
		return currNum / funcNum
	if(func[0] == 'a'):
		return currNum + funcNum
	if(func[0] == 'm'):
		return currNum * funcNum
	if(func[0] == 'r'):
		#must check if number is a fraction or not
		#must also check if number is 2 digits (removing a digit from 1 digit number results in error; could use try catch here as well)
		if(currNum%1 == 0 and currNum > 9):
			currNum = int(currNum)
			currNum = str(currNum)
			currNum = currNum[:-1]
		return float(currNum)

def execute(problem, script):
	#executes the given script
	global solution, solutions
	currNum = problem.startingNum

	solution = ''
	for i in range (0, len(script)):
		solution += str(script[i])
		#print(f'BEFORE FUNCTION: {currNum}')
		currNum = availableFunc(currNum, script[i])
		#print(f'AFTER FUNCTION: {currNum}')
	#print('-------------------------------')
	#print(solution)
	if(currNum%1 == 0):
		if(int(currNum) == problem.goal):
			#stores a possible solution in a list
			solutions.append(solution)

def getMultipleScripts(numCycles, problem):
	global moveScript, moveScriptList
	for i in range(0, numCycles):
		selectMoves(problem)
		moveScriptList.append(tuple(moveScript))

solution = ''
solutions = []
moveScript = ()
moveScriptList = []

#goal, starting number, number of moves
problem1 = Problem(('r1', 's8', 'm11'), 100, 99, 3)

getMultipleScripts(10000, problem1)
moveScriptUnique = list(set(moveScriptList))
#print(f'{moveScriptUnique}')

print(f'Removed {len(moveScriptList) - len(moveScriptUnique)} elements \nmoveScriptList:',\
 f'{len(moveScriptList)} elements\nmoveScriptUnique: {len(moveScriptUnique)} elements')

for i in range(0, len(moveScriptUnique)):
	execute(problem1, moveScriptUnique[i])

print('-------------------------SOLUTION-------------------------')
for i in range(0, len(solutions)):
	print(f'A possible soluton is: {solutions[i]}')

# #Check if a solution exists (it should)

# for i in range(0, len(moveScriptUnique)):
# 	if (moveScriptUnique[i][0] == 'a4' and moveScriptUnique[i][1] == 'm9' and moveScriptUnique[i][2] == 'r1'):
# 		print(moveScriptUnique[i])