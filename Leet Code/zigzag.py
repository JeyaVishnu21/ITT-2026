#To convert a string into a zigzag pattern
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or more than the string length, no zigzag is needed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of empty strings to represent each row.
        rows = [''] * numRows
        current_row = 0
        direction = -1 # Initial direction can be -1, it will be flipped to 1 (down) in the first iteration

        # Iterate through each character in the input string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char

            # Check if we are at the top or bottom row to reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            
            # Move to the next row in the current direction
            current_row += direction

        # Concatenate all rows to form the final string
        return "".join(rows)


        
