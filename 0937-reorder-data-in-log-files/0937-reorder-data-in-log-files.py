class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, dig_log = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_log.append(log)
            else:
                dig_log.append(log)
        
        letter_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))
       
        return letter_log + dig_log