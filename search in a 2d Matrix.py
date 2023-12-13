def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    for nums in mat:
        for num in nums:
            if target==num:
                return True
