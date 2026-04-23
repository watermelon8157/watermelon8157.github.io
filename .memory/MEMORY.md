# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶管理流程**：每日由多個 issue agents 收集當天的 Issue 資訊，產生 snapshot，然後由龍蝦群蒸餾成長期記憶。  
- **資料來源**：所有原始資訊必須來自 GitHub Issue 或 Comment，`shared/manual.md` 為唯一手動維護的長期記憶檔案。  
- **更新頻率**：每日一次，若當天無可用 Issue，則保留既有記憶不做變更。  
- **記憶原則**：  
  1. 只保留**穩定規則**、**長期決策**、**常見限制**與**repo 習慣**。  
  2. 不直接複製 Issue 原文，避免冗餘。  
  3. `compact‑memory` 工作流會讀取本檔案但不會覆寫。  

## Recent Themes
> 目前在最近 30 天的 daily snapshots 中，未偵測到任何跨 Issue 的共同主題或重複出現的議題。  

## Constraints
- **資訊來源限制**：只能引用 Issue / Comment 作為事實依據，`shared/manual.md` 只能作為補充說明。  
- **寫作限制**：本檔案必須保持 **可讀性** 與 **工程友好**，避免冗長的日誌逐段複製。  
- **不確定性**：若某件事僅在單一天出現且未形成穩定事實，必須歸入「Open Loops」而非「Stable Context」。  

## Open Loops
- **待處理 Issue**：自 2026‑04‑17 起至今，所有每日 snapshot 均顯示「本次整理視窗沒有可用 issue」，因此目前沒有新資訊可加入長期記憶。  
- **未完成事項**：等待下一輪 Issue 更新後，重新評估是否有新主題、決策或限制需要納入。  

---  
*此檔案由一群勤奮的龍蝦負責保存主人在 `watermelon8157.github.io` 專案中的長期記憶，確保重要規則與限制永不遺忘。*
