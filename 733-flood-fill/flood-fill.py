class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_col = image[sr][sc]
        if color == original_col:
            return image
        rows = len(image)
        cols = len(image[0])
        def dfs(row, col):
            image[row][col] = color
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for delta_row, delta_col in directions:
                new_row = row + delta_row
                new_col = col + delta_col
                if (0 <= new_row < rows and 0 <= new_col < cols and image[new_row][new_col] == original_col):
                    dfs(new_row, new_col)
        dfs(sr, sc)
        return image
            