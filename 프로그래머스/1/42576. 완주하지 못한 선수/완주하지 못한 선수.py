def solution(participant, completion):
  participant.sort()
  completion.sort()
  while True:
    if len(completion)==0:
      return participant[-1]
      
    elif participant[-1] != completion[-1]:
        return participant[-1]

    elif participant[-1] == completion[-1]:
        participant.pop()
        completion.pop()