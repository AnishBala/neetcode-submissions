class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    

        

# Decode plan:
# 1. Initialize result list and pointer i = 0
# 2. While i < len(s):
#      - find the next '#' starting from i -> gives position of delimiter
#      - digits between i and that position = the length (convert to int)
#      - string body starts right after '#' and spans `length` characters -> slice it out
#      - append that string to result
#      - move i forward to right after the string body (start of next length-prefix)
# 3. Return result
    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0

        #iterate throuhg string until delimiter, convert string containing
        #numbers into integer
        
        while i < len(s): #current tarcked string doesn't include "#"
            currpos = s.find("#", i) # find delim
            length = int(s[i:currpos]) # cast int for string up to delim
            start = currpos + 1 # define start of word
            word = s[start:start+length] #word is within start point plus length of itself
            result.append(word)               #append word to result
            i = start + length #begin next
    

        return result




            

            

        

        

        #store length, delim, string within loop











