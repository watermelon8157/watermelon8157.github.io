# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶管理流程**  
  - 以 GitHub Issue / Comment 為唯一原始資料來源。  
  - `shared/manual.md` 為人工維護的長期記憶檔，僅存放 **穩定規則、長期決策、常見限制、repo 習慣**，不會被自動覆寫。  
  - 每日快照只會檢視最近 **30 天**、最多 **100 個** Issue。  
- **Agent 系統**  
  - 主要執行者為 **Lobster‑01（西瓜蝦）**，於 2026‑03‑24 建立了「西瓜蝦 agent」的角色與技能描述。  
  - Agent 會在有新 Issue 或 Telegram 需求時自動切換至 **活躍** 狀態，等待指令。  
- **工作慣例**  
  - 任何跨 Issue 的決策或主題必須在 Issue 中明確記錄，才能被快照辨識。  
  - 若快照期間無可用 Issue，系統會保留既有記憶，不會自行產生新內容。

## Recent Themes
- **缺乏可用 Issue**：連續四天（2026‑03‑24 ~ 2026‑03‑27）快照皆未偵測到可處理的 Issue，導致「無跨 Issue 主題」與「無新決策」的結果。  
- **Agent 活躍狀態**：2026‑03‑25 快照顯示 Lobster‑01 在 06:53 仍保持活躍，主要在等待 **Telegram 需求的轉換**。  
- **等待指令**：自 2026‑03‑24 角色建立以來，尚未收到具體指令或任務分派。  

## Constraints
- **資料範圍限制**：每日快照僅檢視最近 30 天內、最多 100 個 Issue。超出此範圍的資訊不會自動納入記憶。  
- **來源唯一性**：只能從 GitHub Issue / Comment 取得資訊，任何非 Issue 的討論（如聊天記錄、外部文件）不會被自動納入。  
- **手動筆記保護**：`shared/manual.md` 的內容不會被自動覆寫，必須由人類手動編輯以加入或更新穩定規
