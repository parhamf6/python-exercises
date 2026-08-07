def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        t = 1
        while h > window:
            h = h * bounce
            # print(h)
            if h > window:
                t+=2
        return t
    else:
        return -1