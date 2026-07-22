'''
第一步：用二維列表（2D List）代表數獨
棋盤數獨是 $9 \times 9$ 的網格。
在 Python 中，我們可以用「列表中包含列表」來代表。0 代表空格。
'''
# 0 代表空格
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]



'''
第二步：寫一個「印出棋盤」的函式
直接印出列表很難看，我們寫一個漂亮的格式，
每 3 行/列加一條分隔線，並把 0 顯示成 .。
'''

def print_board(b):
    for i in range(9):
        # 每 3 列印出一條橫向分隔線
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
            
        for j in range(9):
            # 每 3 欄印出一條縱向分隔線
            if j % 3 == 0 and j != 0:
                print("| ", end="")
                
            # 如果是最後一欄，印出數字並換行；否則印完不換行
            cell = "." if b[i][j] == 0 else str(b[i][j])
            if j == 8:
                print(cell)
            else:
                print(cell + " ", end="")

# 測試看看
print_board(board)



'''
第三步：檢查填入的數字合不合法
數獨有三個基本規則：
同行不能重複。
同列不能重複。
同一個 3 X 3 九宮格不能重複。
'''

def is_valid(b, num, row, col):
    # 1. 檢查「列 (Row)」
    for j in range(9):
        if b[row][j] == num and col != j:
            return False

    # 2. 檢查「行 (Column)」
    for i in range(9):
        if b[i][col] == num and row != i:
            return False

    # 3. 檢查「3x3 九宮格」
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != (row, col):
                return False

    return True



'''
第四步：組合完整的玩家互動循環（完整的可執行程式）
把上面的部分整合在一起，加入 while 迴圈讓玩家可以一直填數字，
直到棋盤填滿或想退出。
'''

# 1. 初始化棋盤 (0 代表空格)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(b):
    print("\n  0 1 2   3 4 5   6 7 8 (欄)")
    print(" +------+-------+------+")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(" |------+-------+------|")
        
        row_str = f"{i}| "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            cell = "." if b[i][j] == 0 else str(b[i][j])
            row_str += cell + " "
        row_str += "|"
        print(row_str)
    print(" +------+-------+------+\n")

def is_valid(b, num, row, col):
    # 檢查列
    for j in range(9):
        if b[row][j] == num and col != j:
            return False
    # 檢查行
    for i in range(9):
        if b[i][col] == num and row != i:
            return False
    # 檢查 3x3
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != (row, col):
                return False
    return True

def is_full(b):
    for row in b:
        if 0 in row:
            return False
    return True

# --- 遊戲主流程 ---
print("=== 歡迎來到 Python 最簡數獨 ===")

while True:
    print_board(board)
    
    if is_full(board):
        print("🎉 恭喜你完成數獨！")
        break

    user_input = input("請輸入『列 欄 數字』(例：0 2 4，輸入 q 退出): ")
    if user_input.lower() == 'q':
        print("遊戲結束，下次再玩！")
        break

    try:
        r, c, num = map(int, user_input.split())
        
        # 檢查輸入範圍
        if not (0 <= r <= 8 and 0 <= c <= 8 and 1 <= num <= 9):
            print("⚠️ 輸入超出範圍！列與欄必須是 0-8，數字必須是 1-9。")
            continue
            
        # 檢查該位置是否合規
        if is_valid(board, num, r, c):
            board[r][c] = num
            print("✅ 填入成功！")
        else:
            print("❌ 違規！這個數字在同行、同列或 3x3 區塊內已存在！")
            
    except ValueError:
        print("⚠️ 輸入格式錯誤，請用空格分開三個數字，例如：0 2 4")