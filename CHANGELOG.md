# 🧩 網頁數獨小遊戲 (Sudoku Web Game) - 開發與優化日誌

> **開發目標**：將基礎 Python/HTML 數獨專案，逐步優化為符合現代 UI/UX 標準、流暢無障礙的原生 App 體驗[cite: 1]。

---

## 💡 關於版本控制：什麼是 Git Commit Message？

在每次修改完 `index.html` 後執行的三行指令中，第二行：
`git commit -m "這裡填寫修改備註"`[cite: 1]

這個 `-m` 後面的文字稱為 **Commit Message（版本提交備註）**[cite: 1]。
- **程式碼註解**：解釋「這行 Code 在做什麼」[cite: 1]。
- **Commit Message**：上記 "這一版跟上一版相比改了什麼"[cite: 1]。

它是專案成長日記的標題，能讓開發者清晰追蹤每個版本的修改紀錄[cite: 1]。

---

## 📅 版本演進歷程與 Commit 歷史紀錄 (Version History)

### 🗓️ 2026-07-22 (初期建構與基礎優化)

#### 🚀 V1.0.0 - 基礎功能建立 (Initial Setup)
- **Commit Message**: `Initial commit`[cite: 1]
- **初始狀態**：具備 basic 9x9 數獨棋盤，可使用鍵盤填寫數字、計算通關用時與基本違規判定[cite: 1]。

#### 🎨 V1.1.0 - 點擊體驗與游標優化
- **Commit Message**: `Fix input cursor visibility and add cell selection style`[cite: 1]
- **問題痛點**：點擊 `<input>` 格子時會出現閃爍的文字游標（`I`），且選中樣式不明顯[cite: 1]。
- **修改亮點**：
  1. CSS 加入 `caret-color: transparent` 徹底隱藏閃爍游標[cite: 1]。
  2. 加入 `.selected` 樣式，點擊格子時背景呈現柔和淡藍高亮（`#bbdefb`）[cite: 1]。

#### 📐 V1.2.0 - 棋盤格線與同數字高亮 (Grid & Highlight Optimization)
- **Commit Message**: `Layout side numpad, add same number highlight and expert mode`[cite: 1]
- **問題痛點**：邊框重複疊加導致九宮格線條粗細不一；玩家很難一眼找到盤面上相同的數字[cite: 1]。
- **修改亮點**：
  1. **重構 CSS 格線**：採用獨立 `gap: 1px` 與灰色背景形成清晰 1px 細線，精準繪製 $3\times3$ 九宮格黑粗框[cite: 1]。
  2. **同數字全盤高亮**：點擊預設或已填數字時，全盤所有相同數字同步套用淡黃色背景（`#fff9c4`）[cite: 1]。
  3. **新增超困難 (Expert) 難度**：選單新增第 4 種高難度題庫[cite: 1]。

#### 📱 V1.3.0 - 排版重構與遊戲流程控管 (Layout & Game Flow)
- **Commit Message**: `Fix grid borders, side numpad layout, pause feature and start screen flow`[cite: 1]
- **問題痛點**：按鈕擺在棋盤下方導致頁面過長需要拉滾輪；開啟網頁就直接計時不夠人性化[cite: 1]。
- **修改亮點**：
  1. **左右橫向並排**：將 1~9 數字鍵盤移至棋盤右側（1欄9列單直欄排列），免滾輪[cite: 1]。
  2. **開始畫面流程**：預設隱藏棋盤，強迫玩家先輸入「姓名」與「難度」，按下 `▶ 開始遊戲` 後才展開棋盤與啟動計時[cite: 1]。
  3. **開始後自動隱藏設定欄**：點擊開始後隱藏頂部輸入框，讓介面保持極簡專注[cite: 1]。
  4. **右側新增功能鍵**：新增 `⏸️ 暫停`（含半透明遮罩）與 `🔄 重來` 功能[cite: 1]。

#### 🏳️ V1.4.0 - 選單體驗、放棄功能與通關自動重置 (UI Polish & Home Flow)
- **Commit Message 歷史**：
  - `Move pause and reset buttons to right side, hide controls on game start, restore full inline comments`[cite: 1]
  - `Add give up button, require difficulty selection, and restore inline comments`[cite: 1]
  - `Clean UI layout without static row green background, restore complete comments`[cite: 1]
  - `Return to start menu after clicking OK on win alert`[cite: 1]
- **問題痛點**：全盤綠色塊容易導致視覺疲勞；完成遊戲或想中途退出時無法直接返回選單[cite: 1]。
- **修改亮點**：
  1. **功能按鈕擺放**：將 `暫停`、`重來` 與新增的 `🏳️ 放棄` 按鈕移至 1-9 數字鍵右側，視覺比例更對稱[cite: 1]。
  2. **強迫選難度**：下拉選單預設為 `-- 請選擇難度 --`，防止玩家未選擇就直接開始[cite: 1]。
  3. **通關自動返回**：跳出「🎉 恭喜通關」彈窗後，點擊「確定」自動重置並優雅返回主選單[cite: 1]。
  4. **極簡視覺風**：移除大面積常駐綠色區塊，棋盤保持白底乾淨質感，全靠右側按鈕鎖定提示進度[cite: 1]。
  5. **程式碼全註解**：補齊 HTML / CSS / JavaScript 核心邏輯逐行中文備註[cite: 1]。

---

### 🗓️ 2026-07-23 (RWD 手機適配、智慧復原、無限隨機題庫與一鍵手動切換)

#### 📱🌐 V5.0.0 至 V7.0.0 - 行動體驗、題庫生成與版面自由切換重大升級
- **Commit Message 歷史**：
  - `Fix modal tabs logic to remember played difficulty and restyle modal buttons into rounded pills`[cite: 1]
  - `Fix undo logic to fully clear cell values and add comprehensive line-by-line comments`[cite: 1]
  - `Implement randomized board permutations and fix desktop/mobile RWD dual layout`[cite: 1]
  - `Add manual view mode toggle button and restore horizontal numpad layout for desktop`
- **問題痛點**：舊版寬螢幕會把 1-9 數字鍵變成方塊矩陣讓人不習慣，且受限於自動偵測寬度切換版面會比較死板。
- **修改亮點**：
  1. **難度記憶連動**：通關或打開英雄榜時，會自動切換並對齊玩家剛剛挑戰的難度頁籤[cite: 1]。
  2. **彈窗按鈕美化**：將按鈕改為現代感十足的圓角膠囊造型[cite: 1]。
  3. **完美復原功能 (Undo)**：修復復原邏輯，不僅清除紅字衝突，更能精準將格子數字回溯清空並更新 1-9 按鈕狀態[cite: 1]。
  4. **無限隨機母題變形**：導入智慧數字映射與鏡射翻轉演算法，每次點擊開始遊戲都能動態生成全新排列組合的數獨局[cite: 1]。
  5. **右上角一鍵手動切換版面**：新增「自動適配 / 強制電腦版 / 強制手機版」懸浮切換按鈕，讓電腦版數字鍵恢復舒適漂亮的橫向一整排佈局，版面想怎麼切就怎麼切！

---

💡 *本紀錄檔由 Git 版本控制備份，作為 Web 前端開發學習之里程碑紀錄[cite: 1]。*