# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **長期記憶手冊** (`shared/manual.md`) 為唯一目前可供參考的穩定規則與決策來源。  
  - 內容概述  
    - 只保留 **穩定規則、長期決策、常見限制、repo 習慣**。  
    - **不** 直接複製 GitHub Issue 或 comment 原文。  
    - `compact‑memory` 工作流程會讀取此手冊，但不會覆寫它。  
- **Issue 資料**：過去 30 天內的每日快照皆顯示「本次整理視窗沒有可用 issue」，因此目前 **沒有活躍的 issue、跨 Issue 主題或已形成的決策**。  
- **工作流程假設**  
  - 所有新資訊皆應先寫入 Issue，待 Issue 被 agents 處理後再匯入本記憶庫。  
  - 若無 Issue，則保留既有記憶，不產生新條目。

> **不確定性**：因缺乏任何 Issue 記錄，我們無法確認是否真的沒有待辦事項，或是資料收集機制暫時失效。若日後出現 Issue，請立即更新本節。

## Recent Themes
> 近期（過去 30 天）未偵測到任何可辨識的跨 Issue 主題或重複出現的討論。  
> 若未來出現持續出現的關鍵字、標籤或討論，將在此節匯總為「近期主題」。

## Constraints
1. **不複製原始 Issue 文字**：所有記錄必須以摘要或抽象方式呈現，避免直接搬錄。  
2. **手動筆記優先**：`shared/manual.md` 中的條目視為最高可信度的長期規則。  
3. **資料來源限制**：僅允許從 GitHub Issue / comment、每日快照 JSON、以及手動筆記三個來源抽取資訊。  
4. **更新頻率**：每日快照若持續顯示「無可用 Issue」，則視為「靜止狀態」，不必重複寫入相同訊息。  
5. **語氣要求**：所有條目以「龍蝦」的口吻撰寫，保持友善且具工程可讀性。

## Open Loops
- **等待 Issue 更新**：目前所有
