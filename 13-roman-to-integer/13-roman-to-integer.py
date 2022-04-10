class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_index = 0
        sum = 0
        while current_index != len(s):
            if current_index == len(s) - 1:
                if s[current_index] == 'I':
                    sum += 1
                    current_index += 1
                elif s[current_index] == 'V':
                    sum += 5
                    current_index += 1
                elif s[current_index] == 'X':
                    sum += 10
                    current_index += 1
                elif s[current_index] == 'L':
                    sum += 50
                    current_index += 1
                elif s[current_index] == 'C':
                    sum += 100
                    current_index += 1
                elif s[current_index] == 'D':
                    sum += 500
                    current_index += 1
                else:
                    sum += 1000
                    current_index += 1
            else:
                if s[current_index] == 'V' or s[current_index] == 'L' or s[current_index] == 'D':
                    if s[current_index] == 'V':
                        sum += 5
                    elif s[current_index] == 'L':
                        sum += 50
                    else:
                        sum += 500
                    current_index += 1
                else:
                    if s[current_index] == 'I':
                        if s[current_index + 1] == 'V':
                            sum += 4
                            current_index += 2
                        elif s[current_index + 1] == 'X':
                            sum += 9
                            current_index += 2
                        else:
                            sum += 1
                            current_index += 1
                    elif s[current_index] == 'X':
                        if s[current_index + 1] == 'L':
                            sum += 40
                            current_index += 2
                        elif s[current_index + 1] == 'C':
                            sum += 90
                            current_index += 2
                        else:
                            sum += 10
                            current_index += 1
                    elif s[current_index] == 'C':
                        if s[current_index + 1] == 'D':
                            sum += 400
                            current_index += 2
                        elif s[current_index + 1] == 'M':
                            sum += 900
                            current_index += 2
                        else:
                            sum += 100
                            current_index += 1
                    else:
                        sum += 1000
                        current_index += 1
        return sum
            
                    
                            
                
                
                
        