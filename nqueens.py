def initialize(n,board):
	for key in['queen','row','col','nwtose','swtone']:
		board[key] = {}
	for i in range(n):
		board['queen'][i] = -1
		board['row'][i] = 0
		board['col'][i] = 0
	for i in range(-(n-1),n):
		board['nwtose'][i] = 0
	for i in range(2*n-1):
		board['swtone'][i] = 0



def printboard(board):
	l=[[" " for i in range(len(board['queen'].keys()))] for j in range(len(board['queen'].keys()))]
	for row in sorted(board['queen'].keys()):
		#print((row,board['queen'][row]))
		l[row][board['queen'][row]] = 'Q'
	for i in range(len(board['queen'].keys())):
		print('', end='|')
		for j in range(len(board['queen'].keys())):
			print(l[i][j], end='|')
		print('')
		
		



def free(i,j,board):
	return(board['row'][i] == 0 and board['col'][j] == 0 and
		board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)



def addqueen(i,j,board):
	board['queen'][i] = j
	board['row'][i] = 1
	board['col'][j] = 1
	board['nwtose'][j-i] = 1
	board['swtone'][j+i] = 1




def undoqueen(i,j,board):
	board['queen'][i] = -1
	board['row'][i] = 0
	board['col'][j] = 0
	board['nwtose'][j-i] = 0
	board['swtone'][j+i] = 0





def placequeen(i,board):
	n = len(board['queen'].keys())
	for j in range(n):
		if free(i,j,board):
			addqueen(i,j,board)
			if i == n-1:
				print(i)
				return(True)
			else:
				extendsoln = placequeen(i+1,board)
			if extendsoln:
				return(True)
			else:
				undoqueen(i,j,board)
	else:
		return(False)





board = {}
n = int(input("no. of queens"))
initialize(n,board)
placequeen(0,board)
printboard(board)

