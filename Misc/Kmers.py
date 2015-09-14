__author__ = 'shearora'

text = "abcdeabcdbcdebcde"
k = 4
list = dict()

def findKmers(text, k):
    for i in range(0,len(text)):

        tx = text[i:i+k]
        if(tx in list):

            val = list.get(tx)
            val +=1
            list.update({tx:val})
        else:

            list.update({tx:1})

        if(i+k==len(text)):
            return
        i +=1

def findTopKmer(d):
    max = 0;
    mer = "";
    for key in d:
        val = d.get(key)
        if(val > max):
            max = val
            mer = key
    return mer

findKmers(text,k)
print(findTopKmer(list))
print(list)