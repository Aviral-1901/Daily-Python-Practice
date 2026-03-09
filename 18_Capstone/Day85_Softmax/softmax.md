Sigmoid = 1 output(yes/no)
Softmax = N outputs (cat/dog/bird)

Softmax uses e^x to turn negative scores to positive and then divides that by sum to ensure all outputs = 100% in total.
Categorial Cross-Entropy is used for this. It looks at the probability of correct answer and takes the -log() 
Temperature: Dividing the raw score before softmax.Big T somewhat creates uniform scores while small T creates fix high score (confident).

To get N outputs from the dense layer, the final layer should now have N neurons instead of previous 1.

Temperature is very important in LLMs.If the temperature is high, the probabilities gets to somewhat uniform distribution. AI becomes uncertain which is what we may call creative.
If temperature is low, the probabilites don't get uniformly distributed and the winner approaches 99%. So the AI becomes rigid and deterministic.