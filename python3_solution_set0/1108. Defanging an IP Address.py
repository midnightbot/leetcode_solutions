class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".","[.]")
        return address
        
        
        
