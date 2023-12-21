def solution(k,score):
  answer = []
  for i in range(len(score)):
    partial_score = score[0:i+1]
    partial_score.sort()
    if len(partial_score) < k+1: # 1,2,3
      answer.append(partial_score[0])
    else:                      # 4, ...
      answer.append(partial_score[-k])

  return(answer)