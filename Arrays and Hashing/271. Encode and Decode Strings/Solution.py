class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string+= i + "//$"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_arr = s.split("//$")
        decoded_arr.pop()
        return decoded_arr