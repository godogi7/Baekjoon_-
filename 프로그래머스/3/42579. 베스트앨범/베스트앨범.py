# by 상혁
def solution(genres, plays):
    total_counts = {}
    for i in range(len(genres)): #01234
        if genres[i] in total_counts:
            total_counts[genres[i]].append((plays[i],i))
        else:
            total_counts[genres[i]]= [(plays[i],i)]
    print(total_counts)
    # 장르:plays 키로 만들었음
    # 각 장르별 plays sum으로 합산.-> 합산 딕셔너리로 만듦
    total = {key:sum(val[0] for val in value) for key,value in total_counts.items()}
    # value 값으로 key 값 정렬. 
    
    total = sorted(total.keys(), key = lambda x: total[x], reverse=True)
    print(total)
    answer = []
    for genre in total:
        total_counts[genre].sort(key = lambda x:(-x[0], x[1]))
        for i in range(min(len(total_counts[genre]), 2)):
            answer.append(total_counts[genre][i][1])
    
    return answer
    
    

# 장르별/장르별 최다재생노래2개
# 장르 전체 줄세우기
# 각 장르별 줄 세우기
# 두 개의 리스트 엮어서 dictionary 형태로
# 각 key별로의 합으로 장르 줄 세우기
# 각 Key 별로 2개의 index만 list에 넣기
# 1. 우선 장르별 총 재생횟수 딕셔너리 만들고
# 2. 2개 장르 뽑아서, 2개 장르의 인덱스와, 재생횟수 넣어줌
# 3. 정렬 -> 상위두개
# 4. answer에 추가
                                                                                                                                                                                                                                                   
total_counts = {}


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
genre_dict = {}

for i in range(len(genres)):

    if genres[i] in genre_dict:
        genre_dict[genres[i]] += plays[i]
    else:
        genre_dict[genres[i]] = plays[i]
        

#print(genre_dict)
