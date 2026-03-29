# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶管理流程**  
  - 所有原始資訊皆來自 GitHub Issue / Comment。  
  - `shared/manual.md` 用於手動維護的長期規則、決策與限制，**不會被自動覆寫**。  
  - `daily/*.json` 為每日快照，由各 Issue Agent 彙整，僅供抽取跨 Issue 主題與決策。  
  - `compact‑memory workflow` 會讀取 `shared/manual.md` 作為穩定上下文，並將提煉後的資訊寫入 `MEMORY.md`。  
- **Agent 角色與慣例**  
  - 代理人以「西瓜蝦」系列命名（例：Lobster‑01），負責監控 Issue、產出快照、執行指令。  
  - 任何新角色或技能描述必須先以 Issue 形式提交，待確認後方可啟用。  
- **常見限制**  
  - 不得直接複製 Issue 原文至 `shared/manual.md` 或 `MEMORY.md`，只能抽象化為規則或事實。  
  - 只能在有可用 Issue 時更新記憶；若無 Issue，保留既有記憶不變。  

## Recent Themes
- **2026‑03‑24**：建立「西瓜蝦 agent」的角色與技能描述（已提交 Issue，尚未收到後續指令）。  
- **2026‑03‑25**：Lobster‑01 於 06:53 仍保持活躍，等待 **Telegram 需求的轉換**（尚未收到具體指令）。  
- **2026‑03‑26 ~ 2026‑03‑29**：每日快照皆顯示「本次整理視窗沒有可用 issue」，因此記憶未變動。  

## Constraints
1. **資料來源限制**  
   - 只能從 Issue / Comment 抽取事實；若快照顯示「無可用 Issue」，則不新增任何內容。  
2. **編寫規範**  
   - `MEMORY.md` 必須保持可讀性與工程友好，避免冗長的原文段落。  
   - 必須以繁體中文撰寫，語氣模擬「龍蝦」在協助主人記憶。  
3. **更新時機**
