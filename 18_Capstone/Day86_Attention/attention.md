Self attention allows every word to look at every other word in the sentence simultaneously.

Attention mainly revolves around three things Q(query), K(key) and V(value).
Query: Every word asks a question about what it needs to clariy its meaning.
Key: Every word provides a label describing what it is.
Value: The information the word carries.

Math : Q = X * Wq, K = X * Wk, V = X * Wv
We multiply the input words(X) by three different weight matrices to project them into different spaces for searching, labeling and meaning.


Old AI : squashes whole sentences into a single vector. This caused AI to forget the beginning of long sentences.
Attention's Solution: It keeps words separate. It can dynamically connect to each other regardless of distance.

Attention Matrix: Softmax(Q * K) * V
Complexity : O(N^2) - memory cost grows quadritically with sentence length