for tps in "♥♦♣♠":
    coast = iter([2,3,4,11])
    for c in (1,2,3,4,5,6,7,8,9,10,'V','D','K','T'):
        if str(c) in "VDKT":
            print (c,tps,next(coast),"  ",end = "")
        else:
            print (c,tps,c,"  ",end = "")
    print("\n")