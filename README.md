What is the rough outline of what we're doing here:

The end result is: query a bunch of text and generate a prompt that returns paragraphs of text that are related to the query.

This requires the following:
1. Get a corpus to index.
2. Parse the text into chunks
3. Pass the text into openai ada embeddings and get a vector.
4. Write the embedding into a db with a mapping from embedding -> sentence chunk
5. Get a query string
6. Transform the query string into an embedding.
7. Run knn using the query embedding against the indexed data. 
8. Return top 5 sentence chunks.
9. Voila -> you have context for the query against the big boi LLM. 

Then you query the LLM with the following: Answer the follow query "<insert query text here>" given the following context { <sentence chunks from retrieval>}

## Implementation and Data

The implementation was based on following the instructions from [this comment on HN](https://news.ycombinator.com/item?id=36833618).

Data set is ronaneldan's [tiny stories dataset](https://huggingface.co/datasets/roneneldan/TinyStories) from HuggingFace.

## Outcome

And it sorta works! 

For the query "who went to the park?", you get the following output from the vector similarity search. 
```
Once upon a time, there was a little boy named Tim. Tim loved going to the park to play. One day, Tim went to the park with his mom and dad. He was very happy.
At the park, Tim saw a big tree. He wanted to give the tree a hug. So, he hugged the tree and felt good. Tim liked the tree a lot. He played with his ball, ran around, and had a lot of fun.
Tim had a successful day at the park. He played and laughed a lot. When it was time to go home, Tim felt tired but happy. He couldn't wait to come back to the park again.



Sue and Mike were planning a picnic in the park. They wanted to have the best time ever! Sue and Mike packed snacks for their picnic. They brought lots of different snacks, but their favorite was the beans.
When they arrived in the park, they spread out their blanket and started to get ready for the picnic. Suddenly, Sue noticed something strange – there was a deaf rabbit in the middle of the park.
Sue was excited. She called out to Mike, "Let's give him some beans!" Mike nodded with a smile and together they took out an extra portion of beans and placed it near the rabbit.
The rabbit hopped around the beans and started to eat. Sue and Mike were delighted to see the rabbit enjoying their snack. They had a wonderful picnic and plan to visit the park again soon.



Once there was a boy. His name was Tim. He was three years old and was very adventurous. One day he decided to go for a walk with his parents.
As they walked, they noticed something wonderful. There was a lake, with bright blue waters, and beautiful green trees surrounding it. 
The family couldn't help but add it to their list of favorite places. 
Tim was so excited, he said, "Can we go explore? I would love to see what's there!"
His parents replied, "Yes Tim! What an adventurous idea!"
They all went to explore. Tim discovered so many amazing things. He found colorful rocks, and new plants he'd never seen before. He even saw some animals stepping out of the water.
Tim added these sights to his memory, and felt a sense of wonder as he explored. He had a great day with his family and enjoyed their adventurous outing.
```

The output from ChatGPT using the above as context and the original query is:
 > Tim, Sue, and Mike went to the park.

 Pretty cool. 
