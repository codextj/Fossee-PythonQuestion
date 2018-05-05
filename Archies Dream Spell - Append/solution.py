numInWordsDict = {
  '0': '',
  '1': 'one ',
  '2': 'two ',
  '3': 'three ',
  '4': 'four ',
  '5': 'five ',
  '6': 'six ',
  '7': 'seven ',
  '8': 'eight ',
  '9': 'nine ',

  '00': '',
  '10': 'ten ',
  '20': 'twenty ',
  '30': 'thirty ',
  '40': 'forty ',
  '50': 'fifty ',
  '60': 'sixty ',
  '70': 'seventy ',
  '80': 'eighty ',
  '90': 'ninety ',

  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '14': 'fourteen',
  '15': 'fifteen',
  '16': 'sixteen',
  '17': 'seventeen',
  '18': 'eighteen',
  '19': 'nineteen'
}

for i in range(10):
    number = input()
    print(number)
            
    length = len(number)     
    inWords =''  
    inWords += numInWordsDict[number[length-4]]+'thousand ' if length>3 and number[length-4] != '0' else ''
    inWords += numInWordsDict[number[length-3]]+'hundred ' if length >2 and number[length-3] != '0' else ''
    
    lastTwoDigits = int(number[length-2]+'0') + int(number[length-1])
    
    if lastTwoDigits > 10 and lastTwoDigits <20 and length >1:
        inWords += numInWordsDict[str(lastTwoDigits)]
    else:
        inWords += numInWordsDict[number[length-2]+'0']
        inWords += numInWordsDict[number[length-1]]
        inWords = inWords.rstrip()
    print(inWords)
    
    pwd = ''
    for w in inWords.split(' '):
        pwd+=str(len(w))
    print('secret-code',pwd)
