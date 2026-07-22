# 🧩 網頁數獨小遊戲 (Sudoku Web Game) - 開發與優化日誌

> **開發目標**：將基礎 Python/HTML 數獨專案，逐步優化為符合現代 UI/UX 標準、流暢無障礙的原生 App 體驗。

---

## 💡 關於版本控制：什麼是 Git Commit Message？

在每次修改完 `index.html` 後執行的三行指令中，第二行：
`git commit -m "這裡填寫修改備註"`

這個 `-m` 後面的文字稱為 **Commit Message（版本提交備註）**。
- **程式碼註解**：解釋「這行 Code 在做什麼」。
- **Commit Message**：上記「這一版跟上一版相比改了什麼」。

它是專案成長日記的標題，能讓開發者清晰追蹤每個版本的修改紀錄。

---

## 📅 版本演進歷程與 Commit 歷史紀錄 (Version History)

### 🚀 V1.0.0 - 基礎功能建立 (Initial Setup)
- ** Commit Message**: `Initial commit`
- **初始狀態**：具備 basic 9x9 數獨棋盤，可使用鍵盤填寫數字、計算通關用時與基本違規判定。

---

### 🎨 V1.1.0 - 點擊體驗與游標優化
- ** Commit Message**: `Fix input cursor visibility and add cell selection style`
- **問題痛點**：點擊 `<input>` 格子時會出現閃爍的文字游標（`I`），且選中樣式不明顯。
- **修改亮點**：
  1. CSS 加入 `caret-color: transparent` 徹底隱藏閃爍游標。
  2. 加入 `.selected` 樣式，點擊格子時背景呈現柔和淡藍高亮（`#bbdefb`）。

---

### 📐 V1.2.0 - 棋盤格線與同數字高亮 (Grid & Highlight Optimization)
- ** Commit Message**: `Layout side numpad, add same number highlight and expert mode`
- **問題痛點**：邊框重複疊加導致九宮格線條粗細不一；玩家很難一眼找到盤面上相同的數字。
- **修改亮點**：
  1. **重構 CSS 格線**：採用獨立 `gap: 1px` 與灰色背景形成清晰 1px 細線，精準繪製 $3\times3$ 九宮格黑粗框。
  2. **同數字全盤高亮**：點擊預設或已填數字時，全盤所有相同數字同步套用淡黃色背景（`#fff9c4`）。
  3. **新增超困難 (Expert) 難度**：選單新增第 4 種高難度題庫。

---

### 📱 V1.3.0 - 排版重構與遊戲流程控管 (Layout & Game Flow)
- ** Commit Message**: `Fix grid borders, side numpad layout, pause feature and start screen flow`
- **問題痛點**：按鈕擺在棋盤下方導致頁面過長需要拉滾輪；開啟網頁就直接計時不夠人性化。
- **修改亮點**：
  1. **左右橫向並排**：將 1~9 數字鍵盤移至棋盤右側（1欄9列單直欄排列），免滾輪。
  2. **開始畫面流程**：預設隱藏棋盤，強迫玩家先輸入「姓名」與「難度」，按下 `▶ 開始遊戲` 後才展開棋盤與啟動計時。
  3. **開始後自動隱藏設定欄**：點擊開始後隱藏頂部輸入框，讓介面保持極簡專注。
  4. **右側新增功能鍵**：新增 `⏸️ 暫停`（含半透明遮罩）與 `🔄 重來` 功能。

---

### 🏳️ V1.4.0 - 選單體驗、放棄功能與通關自動重置 (UI Polish & Home Flow)
- ** Commit Message 歷史**:
  - `Move pause and reset buttons to right side, hide controls on game start, restore full inline comments`
  - `Add give up button, require difficulty selection, and restore inline comments`
  - `Clean UI layout without static row green background, restore complete comments`
  - `Return to start menu after clicking OK on win alert`
- **問題痛點**：全盤綠色塊容易導致視覺疲勞；完成遊戲或想中途退出時無法直接返回選單。
- **修改亮點**：
  1. **功能按鈕擺放**：將 `暫停`、`重來` 與新增的 `🏳️ 放棄` 按鈕移至 1-9 數字鍵右側，視覺比例更對稱。
  2. **強迫選難度**：下拉選單預設為 `-- 請選擇難度 --`，防止玩家未選擇就直接開始。
  3. **通關自動返回**：跳出「🎉 恭喜通關」彈窗後，點擊「確定」自動重置並優雅返回主選單。
  4. **極簡視覺風**：移除大面積常駐綠色區塊，棋盤保持白底乾淨質感，全靠右側按鈕鎖定提示進度。
  5. **程式碼全註解**：補齊 HTML / CSS / JavaScript 核心邏輯逐行中文備註。

---

💡 *本紀錄檔由 Git 版本控制備份，作為 Web 前端開發學習之里程碑紀錄。*
