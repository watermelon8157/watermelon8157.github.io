# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶架構**：  
  - 以 GitHub Issue 為主要的原始資料來源，所有長期記憶與決策皆應從 Issue / Comment 中抽取。  
  - `shared/manual.md` 為人工維護的長期記憶手冊，僅保存 **穩定規則、長期決策、常見限制、repo 習慣**，不會被自動流程覆寫。  
- **目前觀測**：自 2026‑04‑11 起的 7 天每日快照皆顯示「本次整理視窗沒有可用 issue」，代表在此期間 **沒有任何開放或已關閉的 Issue 被標記為需要記憶整理**。  
- **既有規則（從手冊推測）**：  
  1. **不直接複製 Issue 原文**，僅抽象化為可重用的上下文。  
  2. **compact‑memory workflow** 會讀取 `shared/manual.md`，但不會寫入或覆寫它。  
  3. **跨 Issue 主題與決策** 必須在有足夠資料時才形成，否則保持空白。  

> **不確定性**：因為缺乏實際 Issue 內容，無法確認任何具體的長期規則或決策是否已存在於 repo 中。

## Recent Themes
- **無可辨識的跨 Issue 主題**：過去一週的快照均未偵測到重複或相關的主題。  
- **無新決策**：每日快照皆報告「目前沒有新的跨 issue 決策」。  
- **Issue 活動缺乏**：每日皆顯示「本次整理視窗沒有可用 issue」，暗示近期工作可能集中於非 Issue 的任務（例如本地開發、文件撰寫）或尚未將任務以 Issue 形式提出。

## Constraints
1. **資料來源限制**  
   - 只能從 GitHub Issue / Comment 取得原始資訊。  
   - `shared/manual.md` 只作為手動補充，不能自動寫入。  
2. **記憶整理原則**  
   - 不直接搬錄原始 Issue 文字，必須蒸餾成「可重用的上下文」或「規則」形式。  
   - 若資訊僅在單一天出
