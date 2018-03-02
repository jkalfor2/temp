Jeannelle Alford
jkalfor2
letterLangId.py:
	Functionality: Creates a dictionary of letter unigram counts and a
          dictionary of bigram letter counts for each language, using the
          training data. Tests each sentence in the test data against each
          model, using log probabilities.
	To run:
          Make sure python3 is in usr/bin.
          Run ./letterLangId.py
          Output in letterLangId.out

wordLangId.py:
	Functionality: Creates a dictionary of word unigram counts and a 
          dictionary of word bigram counts for each language, using the
          training data. Tests each sentence in the test data against each
          model, using log probabilities.
	To run:
          Make sure python3 is in usr/bin
          Run ./wordLangId.py
          Output in wordLangId.out

letterLangId.py correctly identified the language 299 times out of 300.
wordLangId.py also correctly identified the language 299 times out of 300.

Because the two models performed with the same accuracy on the given data,
it's hard to say which performs better overall. A more rigorous test with
more training data as well as more test data might provide an answer.

The advantage of the letter bigram model is that it does not require making
decisions about how to split up the words. You simply need to iterate over
every character, including spaces and punctuation. At least, that's what I
chose to do. I believe including the spaces and punctuation improves the model
because every language will differ in terms of which letters appear at word
boundaries or around symbols.
Another advantage of the letter model is that there will be far fewwer zero-
counts. In a large enough corpus, every letter of a language's alphabet will
be represented, so there's no need to do smoothing on the unigram counts.
