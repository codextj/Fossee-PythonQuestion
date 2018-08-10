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
def num2words(number):
        number = str(number)
        length = len(number)     
        inWords =''  
        if length>4:
            if number[:2] in numInWordsDict:
                inWords +=numInWordsDict[number[:2]]  +'thousand '
            else:
                inWords +=numInWordsDict[number[0]+'0'] + numInWordsDict[number[1]] +'thousand '
                
              
        inWords += numInWordsDict[number[length-4]]+'thousand ' if length== 4 and number[length-4] != '0' else ''

        inWords += numInWordsDict[number[length-3]]+'hundred ' if length > 2 and number[length-3] != '0' else ''

        lastTwoDigits = 0
        if length > 1:
            lastTwoDigits = int(number[-2]+'0')  
            lastTwoDigits += int(number[-1])
            if lastTwoDigits > 9 and lastTwoDigits < 20:
                inWords += numInWordsDict[str(lastTwoDigits)] #direct key exist # 19
            else:
                inWords += numInWordsDict[number[-2]+'0'] + numInWordsDict[number[-1]] # 20 + 3
            
        else:
            inWords = numInWordsDict[number[0]]
            inWords = inWords.rstrip()


        return(inWords) # inWords.title()

    return(in_wds)
  
for i in range(10):
    number = input()
    print(number,'\n',num2words(number))
       
    pwd = ''
    for w in inWords.split(' '):
        pwd+=str(len(w))
    print('secret-code',pwd)
