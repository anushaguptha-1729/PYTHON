class Solution:
    def defangIPaddr(self, address: str) -> str:
        O=""
        for i in address:
            if i==".":
                O+="[.]"
            else:
                O+=i
        return O