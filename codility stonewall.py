print('hello and welcome to hangman!')


def solution1(H):
    arr= []
    blocks = 0
    start = 0
    end = 0
    zero = 1

    minus = min(H)
    H = [x-minus for x in H]
    blocks +=1
    while H:
        try:
            for x in H:
                if x == 0 and zero !=0:
                    start+=1
                    end+=1
                if x != 0:
                    zero = 0
                    end += 1
                    arr.append(x)
                if x == 0 and zero == 0:
                    end+1
                    break

            minus = min(arr)
            H[start:end] = [x-minus for x in arr]
            start = 0
            end = 0
            arr = []
            zero = 1
            blocks += 1
        except ValueError:
            break
    return blocks




def solution(H):
    stack = []
    block_count = 0    # The number of needing blocks
    for height in H:
        print(height)
        while len(stack) != 0 and height < stack[-1]:
            print(stack)
            # If the height of current block is less than
            #    the previous ones, the previous ones have
            #    to end before current point. They have no
            #    chance to exist in the remaining part.
            # So the previous blocks are completely finished.
            stack.pop()
            print(stack)
            block_count += 1
        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than
            #    the previous one, a new block is needed for
            #    current position.
            stack.append(height)
        # Else (the height of current block is same as that
        #    of previous one), they should be combined to
        #    one block.
    # Some blocks with different heights are still in the stack.
    block_count += len(stack)
    return block_count




print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
