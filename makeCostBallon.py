T=int(input())
#loop through each test case
for _ in range(T):
	#read the cost of balloon
	cost_green,cost_purple = map(int ,input().split())
	
	# read the number of participants
	n=int(input())
	
	#start counter
	problem1_solved=0
	problem2_solved=0
	
	#reading participant's status
	for _ in range(n):
		p1,p2 = map(int,input().split())
		problem1_solved+=p1
		problem2_solved+=p2
	#calculatee for strategy1 and strategy2
	method_1=problem1_solved*cost_green+problem2_solved*cost_purple
	method_2=problem1_solved*cost_purple+problem2_solved*cost_green
	print(min(method_1, method_2))1 
