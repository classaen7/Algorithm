
def solution(book_time):
    def time_to_min(t):
        h,m = map(int, t.split(':'))
        return h*60 + m
    
    answer = 0
    book_time.sort()
    
    for i,time in enumerate(book_time):
        book_time[i] = [ time_to_min(time[0]), time_to_min(time[1]) ]
        book_time[i].append('X')
    
    
    for i in range(len(book_time)):
        if book_time[i][2] == 'X':
            answer += 1
            book_time[i][2] = 'O'
            end = book_time[i][1] + 10
            
            
            for j in range(i+1, len(book_time)):
                if book_time[j][2] == 'X' and end <= book_time[j][0]:
                    end = book_time[j][1] + 10
                    book_time[j][2] = 'O'
   

    return answer