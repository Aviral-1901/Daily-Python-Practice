Self-Attention is permutation invariant means the order doesn't matter.
Man Bites Dog is the same as Dog Bites Man.
So we need something so that the order of words make sense.


For this we generate sine/cosine waves of different frequencies.
Sine/Cosine values are bounded (remain between -1 and 1) preventing exploding gradients.
By using different frequencies, we create a unique signature for every position that never repeats even in long books.
The Positional Vector must have the same dimension as the Word Embedding (e.g., 512). This allows us to perform element-wise addition.
Now every word gets its own positional vector.
We add this positional vector to the word embeddings.
Addition preserves the original meaning while tinting it with position. While multiplication is destructive, if the wave is at 0 it would multiply the word by 0 and erase it from the memory.


Positional Encoding is not stored in the Master Embedding Matrix. It is calculated and added on-the-fly every time a sentence is processed. This keeps the "Pure Meaning" in the dictionary separate from the "Position" of the word in a specific sentence.