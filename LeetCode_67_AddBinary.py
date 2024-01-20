class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a=int(a,2)
        int_b=int(b,2)
        res= int_a+int_b
        binary_result=bin(res)[2:]
        max_len=max(len(a),len(b))
        binary_result=binary_result.zfill(max_len)
        return binary_result
