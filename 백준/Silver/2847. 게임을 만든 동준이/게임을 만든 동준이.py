n = int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))

scores.reverse()
before = scores[0]
answer = 0

for level in range(1, n):
    if scores[level] >= before:
        new_score = before - 1
        answer += scores[level] - new_score
        scores[level] = new_score

    before = scores[level]

print(answer)