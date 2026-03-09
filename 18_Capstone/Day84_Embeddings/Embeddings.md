AI cannot process raw text or audio.
Embedding is a vector that maps a discrete object into a continuous mathematical space.

what we do in embedding is take a word and map it. Like if we do direct mapping then apple and banana would look totally different although they are fruits. So in embedding we map them closer so we know they are related.

In embedded space, geometric relationships mirror logical relationships.
Like : King - Man + Woman = Queen

The feauture extractor which outputs 488 floats is also an embedding.
The word "Yes" and "Yeah" would stay relatively closer than "NO".

Some calculation or example which I learned:
King: [0.99, -0.99]
Man: [0.01, -0.99]
Woman: [0.01, 0.99]
Math: King - Man + Woman = Queen
    [0.99, -0.99] - [0.01, -0.99] + [0.01, 0.99]
Result: [0.99, 0.99]