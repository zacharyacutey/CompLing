from nltk.corpus import cmudict
cmu=cmudict.dict()
def num(c):
  return c in '0123456789'
def remove_numbers(s):
  if s=="AH0":
    return "AX"
  r=""
  i=0
  while i!=len(s):
    r+=s[i] if not num(s[i]) else ""
    i+=1
  return r
def stressless(arg):
  t= [remove_numbers(i) for i in cmu[arg][0]]
  r=[]
  i=0
  while i!=len(t):
    if t[i]!='':
      r.append(t[i])
    i+=1
  return r
def vowel(arg):
  return arg in [
    'AA',
    'AE',
    'AH',
    'AO',
    'AW',
    'AX'
    'AY',
    'EH',
    'ER',
    'EY',
    'HH',
    'IH',
    'IY',
    'OW',
    'OY',
    'UH',
    'UW'
  ]

def end(arr):
  i=-1
  while not vowel(arr[i]):
    i-=1
  return arr[i:]

def rhyme(word1,word2):
  return end(stressless(word1))==end(stressless(word2))
