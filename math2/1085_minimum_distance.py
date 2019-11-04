x, y, w, h = map(int, input().split(' '))
choeso = []

choeso.append(x)
choeso.append(y)
choeso.append(w-x)
choeso.append(h-y)

print(min(choeso))