class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        split_word=[]
        if(len(strs)==1):
            return [strs]
        else:
            for s in strs:
                temp = "".join(sorted(list(s)))
                if temp not in dict:
                    dict[temp] = [s]
                else:   
                    dict[temp].append(s)
            #print(sorted(dict))        
            #result = []    
            # for value in dict.values():
            #     result +=[value]
            # return result       
            #print(split_word)
            #print(strs)
        
            
