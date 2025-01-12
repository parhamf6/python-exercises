# باب و کلید تیلویزیون
# https://quera.org/problemset/14580
s = str(input()).split(" ")
n, x, k = int(s[0]), int(s[1])-1, int(s[2])
channels = []
for c in range(n):
    sc = str(input())
    channels.append(sc)
index_channel = [x]
for i in range(k):
    last_index = index_channel[-1]+1
    if last_index==n:
        index_channel.append(0)
    else:
        index_channel.append(last_index)
print(channels[index_channel[-1]])