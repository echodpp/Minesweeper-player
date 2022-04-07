# Minesweeper-player

1. Background:  

We design and implement an algorithm to play minesweeper automatically. The rule of the game is shown as follows:  

1.1 The game is played on a board containing **nxn** cells, each cell as a possibility of being a mine or a safe block.  

1.2 All the blocks are covered initallily, every time the player should select a block to be revealed.  
 
1.3 If it is a mine, the mine goes off and the player gets no points; if it is not mine, it would tell the player how many mines are there in its neighbors.  

1.4 The player can also declare a block to contain a mine, if success, the player can win one points.  
 
1.5 The player should try to get as many points as possible. That is to say, the player should try to identity the blocks with mines with the information he has and avoid stepping on them.  

 **1.6 There is a little different rule, the game can continue even a mine goes off. Which would enable us to evaluate the performance of our algorithm by counting the final points it earns.** 
 
2. Baseline:  
For the baseline strategy that just uses single clues and local information around one cell, we implemented it by using a queue to store all the squares which are identified as safe for checking if we can use them to infer more information. First, we keep track of the state(a mine, safe or currently covered) for each cell and create the queue we mentioned above. Second, for a given cell(the node in the queue), if we can deduce from the clue of the cell that every hidden neighbor is safe(or mine), put all the neighbors in the queue(or mark them as mine). At last, if there are no nodes in the queue which means no hidden cell can be conclusively identified as a mine or safe, pick a cell to reveal at random.

3.Milestone:
- project approval
- figure out the list of questions
- complete the sub-questions in the issues
- test & evaluation
- final application
 
4.Questions:
- If no hidden cell can be conclusively identified as a mine or safe by using the baseline strategy, how can we can  gain more information?
- When we collect a new clue, how do you model / process / compute the information we gain from it? 
- How does our program decide which cell to search next? If all the strategies above fails to work.
- Are there any points where our program makes a decision that we don't agree with?
 

