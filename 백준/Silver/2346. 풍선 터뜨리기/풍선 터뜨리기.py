n = int(input())
papers_in_balloons = list(enumerate(map(int, input().split()), start=1))
index = 0
results = []

while papers_in_balloons:
    original_index, number = papers_in_balloons[index]
    results.append(original_index)
    papers_in_balloons.pop(index)

    if not papers_in_balloons:
        break

    if number > 0:
        index = (index + number - 1) % len(papers_in_balloons)
    else:
        index = (index + number) % len(papers_in_balloons)

print(*results)
