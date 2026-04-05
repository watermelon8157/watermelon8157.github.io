# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`（個人網站的 GitHub Pages 專案）。  
- **記憶管理流程**  
  1. **Issue Agents** 每日掃描所有開放與已關閉的 Issue（上限 100）並產出 *daily snapshot*。  
  2. **Shared Manual Notes** (`shared/manual.md`) 用於手動維護長期穩定規則、決策與限制，**不會**被自動流程覆寫。  
  3. **Compact‑Memory Workflow** 會讀取 `shared/manual.md` 以及最近的 daily snapshots，將資訊蒸餾成本檔 `MEMORY.md`。  
- **Repo 習慣**  
  - 所有工作項目、待辦與討論必須以 GitHub Issue 形式記錄。  
  - Issue 標籤（labels）用於快速分類；目前每日快照未偵測到任何標籤。  
  - 每日快照若未偵測到可用 Issue，會保留既有記憶並在下一輪更新。  
- **穩定規則（從手動筆記推測）**  
  - **不複製原始 Issue 文字**：只保留概念與決策，避免冗長。  
  - **資訊層級**：先蒸餾成「長期規則」→「近期主題」→「限制」→「未完成事項」。  
  - **不確定資訊** 必須標註為 *不確定*，避免誤導。  

## Recent Themes
> 目前的 daily snapshots（2026‑03‑30 至 2026‑04‑05）皆顯示 **「本次整理視窗沒有可用 issue」**，因此在最近兩週內未出現可辨識的跨 Issue 主題、決策或重複出現的工作模式。  
- **缺乏 Issue 活動**：這可能代表專案暫時處於維護或靜止狀態，亦或是 Issue 被外部系統（如 PR）取代。  
- **無標籤統計**：`Top Labels` 為 *none*，顯示目前沒有分類需求。  

## Constraints
| 類別 | 具體限制 |
|------|----------
