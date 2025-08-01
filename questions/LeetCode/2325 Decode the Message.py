class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string=""
        for i in key:
            if i==" ":
                continue
            if i not in string:
                string+=i
        dictionary=dict(zip(list(string), list(alphabets)))
        res=""
        for i in message:
            if i==" ":
                res+=" "
                continue
            res+=dictionary[i]
        return res