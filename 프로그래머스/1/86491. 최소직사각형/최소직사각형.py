def solution(sizes):
    max_width = 0
    max_height = 0
    
    for width, height in sizes:
        if width < height:
            width, height = height, width

        max_width = max(width, max_width)
        max_height = max(height, max_height)

    return max_width * max_height
        