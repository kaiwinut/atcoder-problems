s = int(input())

print(str(s//3600).zfill(2) + ':' + str((s - 3600 * (s//3600)) // 60).zfill(2) + ':' + str(s%60).zfill(2))