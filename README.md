# Minesweeper-player
We design and implement an algorithm to play minesweeper automatically. The rule of the game is shown as follows:  

1.The game is played on a board containing **nxn** cells, each cell as a possibility of being a mine or a safe block.  

2. All the blocks are covered initallily, every time the player should select a block to be revealed.  
 
3. If it is a mine, the mine goes off and the player gets no points; if it is not mine, it would tell the player how many mines are there in its neighbors.  

4. The player can also declare a block to contain a mine, if success, the player can win one points.  
 
5. The player should try to get as many points as possible. That is to say, the player should try to identity the blocks with mines with the information he has and avoid stepping on them.  

**6. There is a little different rule, the game can continue even a mine goes off. Which would enable us to evaluate the performance of our algorithm by counting the final points it earns.** 
