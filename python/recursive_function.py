# Explain why below code does't print expected count down from 10 to 1

def count_down(start):
    print(start)
    while start > 1:
        start-=1
        count_down(start)

