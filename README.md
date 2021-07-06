# TASPal
Project to train an AI to write TASes


## Memory Address References
### Star Wars - Episode III - GBA
Player positions is tracked at memory address 04120C. The first 4 digits is the Y value and the last 4 is the X value. For instance, if the value went from 00A30001 -> 00A300B4 the player would have traveled right but their Y value would not have changed. They would also be as far left as possible after a loading screen. 
