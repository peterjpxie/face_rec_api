import math

def get_lip_height(lip):
    sum=0
    for i in [2,3,4]:
        # distance between two near points up and down
        distance = math.sqrt( (lip[i][0] - lip[12-i][0])**2 +
                              (lip[i][1] - lip[12-i][1])**2   )
        sum += distance
    return sum / 3

def get_mouth_height(top_lip, bottom_lip):
    sum=0
    for i in [8,9,10]:
        # distance between two near points up and down
        distance = math.sqrt( (top_lip[i][0] - bottom_lip[18-i][0])**2 + 
                              (top_lip[i][1] - bottom_lip[18-i][1])**2   )
        sum += distance
    return sum / 3

def check_mouth_open(top_lip, bottom_lip):
    top_lip_height =    get_lip_height(top_lip)
    bottom_lip_height = get_lip_height(bottom_lip)
    mouth_height =      get_mouth_height(top_lip, bottom_lip)

    # if mouth is open more than lip height * ratio, return true.
    ratio = 0.5
    if mouth_height > min(top_lip_height, bottom_lip_height) * ratio:
        return True
    else:
        return False

def test():
    # obama open mouth
    top_lip = [(181, 359), (192, 339), (211, 332), (225, 336), (243, 333), (271, 342), (291, 364), (282, 363), (242, 346), (225, 347), (211, 345), (188, 358)]
    bottom_lip = [(291, 364), (270, 389), (243, 401), (223, 403), (207, 399), (190, 383), (181, 359), (188, 358), (210, 377), (225, 381), (243, 380), (282, 363)]

    # close mouth
    # top_lip = [(151, 127), (157, 126), (163, 126), (168, 127), (172, 127), (178, 127), (185, 129), (182, 129), (172, 130), (167, 130), (163, 129), (153, 127)]
    # bottom_lip = [(185, 129), (177, 133), (171, 135), (166, 135), (161, 134), (156, 132), (151, 127), (153, 127), (162, 129), (167, 130), (171, 130), (182, 129)]

    print('top_lip height:', get_lip_height(top_lip))
    print('bottom_lip height:', get_lip_height(bottom_lip))
    print('mouth height:', get_mouth_height(top_lip,bottom_lip))
    print()

if __name__ == '__main__':
    test()
