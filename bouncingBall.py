def bouncing_ball(h, bounce, window):
    if h <= 0 or 0 > bounce or bounce >= 1 or window >= h:
        return -1
    else:
        count = 1
        h = h*bounce
        while window < h:
            count+=2
            h = h*bounce
        return count

print(bouncing_ball(h = 3,bounce = 0.66,window = 1.5))