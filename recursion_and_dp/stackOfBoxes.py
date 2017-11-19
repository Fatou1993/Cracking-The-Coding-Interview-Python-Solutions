from collections import namedtuple

def stackOfBoxes(boxes):
    def helper(bottom, top, h, num_boxes_left):
        if not top :
            return
        for i in range(num_boxes_left):
            box = top[i]
            if not bottom or (bottom[-1].w > box.w and bottom[-1].h > box.h and bottom[-1].d > box.d):
                bottom.append(box)
                h+=box.h
                res[0] = max(res[0], h)
                helper(bottom, top[:i]+top[i+1:], h, num_boxes_left-1)
                h-=box.h
                bottom.pop()

    res, bottom = [0], []
    n = len(boxes)
    helper(bottom, boxes, 0, n)
    return res[0]

if __name__ == "__main__":
    Box = namedtuple('box', ('w', 'h', 'd'))
    boxes = [Box(14,6,7), Box(15,22,3), Box(14,25,6), Box(10,12,32)]
    res = stackOfBoxes(boxes)
    print(res)
