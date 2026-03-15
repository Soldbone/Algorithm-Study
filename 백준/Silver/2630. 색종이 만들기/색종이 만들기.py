import sys

input = sys.stdin.readline
N = int(input())

entire_paper = [list(map(int, input().split())) for _ in range(N)]


blue_count = 0
white_count = 0


def make_paper(row_start, col_start, n):
    # end 구간은 반열림 구간으로 둬서 숫자가 1큼에 유의
    global blue_count
    global white_count

    row_end = row_start + n
    col_end = col_start + n
    color = entire_paper[row_start][col_start]
    if row_end - row_start == 1:
        if color == 0:
            white_count += 1
        else:
            blue_count += 1
        return

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if color != entire_paper[row][col]:
                # 왼쪽 위:      [0 ~ N//2][0 ~ N//2]
                make_paper(row_start, col_start, n // 2)
                # 오른쪽 위:    [0 ~ N//2][N//2 ~ N]
                make_paper(row_start, col_start + n // 2, n // 2)
                # 왼쪽 아래:    [N//2 ~ N][0 ~ N//2]
                make_paper(row_start + n // 2, col_start, n // 2)
                # 오른쪽 아래:  [N//2 ~ N][N//2 ~ N]
                make_paper(row_start + n // 2, col_start + n // 2, n // 2)
                return

    # 색이 모두 같으면 count하고 return
    if color == 0:
        white_count += 1
    else:
        blue_count += 1
    return


make_paper(0, 0, N)
print(white_count, blue_count, sep="\n")