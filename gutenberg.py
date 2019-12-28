import nltk                            
from nltk.corpus import gutenberg
gutenberg.fileids()
//OUTPUT-['austen-emma.txt',
          'austen-persuasion.txt',
          'austen-sense.txt',
          'bible-kjv.txt',
          'blake-poems.txt',
          'bryant-stories.txt',
          'burgess-busterbrown.txt',
          'carroll-alice.txt',
          'chesterton-ball.txt',
          'chesterton-brown.txt',
          'chesterton-thursday.txt',
          'edgeworth-parents.txt',
          'melville-moby_dick.txt',
          'milton-paradise.txt',
          'shakespeare-caesar.txt',
          'shakespeare-hamlet.txt',
          'shakespeare-macbeth.txt',
          'whitman-leaves.txt']
len(nltk.corpus.gutenberg.words('austen-emma.txt'))
//OUTPUT-192427

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))      
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
    print (int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid )
  
//OUTPUT-
4 24 26 austen-emma.txt
4 26 16 austen-persuasion.txt
4 28 22 austen-sense.txt
4 33 79 bible-kjv.txt
4 19 5 blake-poems.txt
4 19 14 bryant-stories.txt
4 17 12 burgess-busterbrown.txt
4 20 12 carroll-alice.txt
4 20 11 chesterton-ball.txt
4 22 11 chesterton-brown.txt
4 18 10 chesterton-thursday.txt
4 20 24 edgeworth-parents.txt
4 25 15 melville-moby_dick.txt
4 52 10 milton-paradise.txt
4 11 8 shakespeare-caesar.txt
4 12 7 shakespeare-hamlet.txt
4 12 6 shakespeare-macbeth.txt
4 36 12 whitman-leaves.txt

sent=gutenberg.sents('austen-emma.txt')
print(sent)
//OUTPUT-[['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']'], ['VOLUME', 'I'], ...]

sent[125]
//OUTPUT-['"',
          'I',
          'promise',
          'you',
          'to',
          'make',
          'none',
          'for',
          'myself',
          ',',
          'papa',
          ';',
          'but',
          'I',
          'must',
          ',',
          'indeed',
          ',',
          'for',
          'other',
          'people',
          '.']
 
max_len=max([len(s) for s in sent])
x=[s for s in sent if len(s)==max_len]
print(x)
//OUTPUT-[['While', 'he', 'lived', ',', 'it', 'must', 'be', 'only', 'an', 'engagement', ';', 'but', 'she', 'flattered', 'herself', ',', 'that', 'if', 'divested', 'of', 'the', 'danger', 'of', 'drawing', 'her', 'away', ',', 'it', 'might', 'become', 'an', 'increase', 'of', 'comfort', 'to', 'him', '.--', 'How', 'to', 'do', 'her', 'best', 'by', 'Harriet', ',', 'was', 'of', 'more', 'difficult', 'decision', ';--', 'how', 'to', 'spare', 'her', 'from', 'any', 'unnecessary', 'pain', ';', 'how', 'to', 'make', 'her', 'any', 'possible', 'atonement', ';', 'how', 'to', 'appear', 'least', 'her', 'enemy', '?--', 'On', 'these', 'subjects', ',', 'her', 'perplexity', 'and', 'distress', 'were', 'very', 'great', '--', 'and', 'her', 'mind', 'had', 'to', 'pass', 'again', 'and', 'again', 'through', 'every', 'bitter', 'reproach', 'and', 'sorrowful', 'regret', 'that', 'had', 'ever', 'surrounded', 'it', '.--', 'She', 'could', 'only', 'resolve', 'at', 'last', ',', 'that', 'she', 'would', 'still', 'avoid', 'a', 'meeting', 'with', 'her', ',', 'and', 'communicate', 'all', 'that', 'need', 'be', 'told', 'by', 'letter', ';', 'that', 'it', 'would', 'be', 'inexpressibly', 'desirable', 'to', 'have', 'her', 'removed', 'just', 'now', 'for', 'a', 'time', 'from', 'Highbury', ',', 'and', '--', 'indulging', 'in', 'one', 'scheme', 'more', '--', 'nearly', 'resolve', ',', 'that', 'it', 'might', 'be', 'practicable', 'to', 'get', 'an', 'invitation', 'for', 'her', 'to', 'Brunswick', 'Square', '.--', 'Isabella', 'had', 'been', 'pleased', 'with', 'Harriet', ';', 'and', 'a', 'few', 'weeks', 'spent', 'in', 'London', 'must', 'give', 'her', 'some', 'amusement', '.--', 'She', 'did', 'not', 'think', 'it', 'in', 'Harriet', "'", 's', 'nature', 'to', 'escape', 'being', 'benefited', 'by', 'novelty', 'and', 'variety', ',', 'by', 'the', 'streets', ',', 'the', 'shops', ',', 'and', 'the', 'children', '.--', 'At', 'any', 'rate', ',', 'it', 'would', 'be', 'a', 'proof', 'of', 'attention', 'and', 'kindness', 'in', 'herself', ',', 'from', 'whom', 'every', 'thing', 'was', 'due', ';', 'a', 'separation', 'for', 'the', 'present', ';', 'an', 'averting', 'of', 'the', 'evil', 'day', ',', 'when', 'they', 'must', 'all', 'be', 'together', 'again', '.']]
