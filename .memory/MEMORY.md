# Repository Memory

## Stable Context
- **資料來源**：所有長期記憶皆以 GitHub Issue / Comment 為原始依據，手動維護的 `shared/manual.md` 只作為摘要與規則的存放，不會被自動覆寫。  
- **工作流程**：  
  1. **Issue 收集**：每日快照會從過去 30 天內的 Issue 中抽取資訊。  
  2. **蒸餾**：重複出現的事實或規則會被抽取到此長期記憶；一次性、尚未驗證的資訊則放入「Open Loops」或「Recent Themes」。  
  3. **同步**：若快照期間無可用 Issue，則保留既有記憶，不會自行產生新條目。  
- **目前狀態**：截至 2026‑04‑15，倉庫 `watermelon8157/watermelon8157.github.io` 在過去 30 天內 **沒有任何可用 Issue**，因此沒有新資訊可加入穩定上下文。  
- **Repo 習慣**（根據手動筆記的指引）：  
  - 所有長期規則、決策與限制必須寫在 `shared/manual.md` 中。  
  - 任何自動化流程（如 compact‑memory）只會 **讀取** 而不會 **覆寫** 手動筆記。  

## Recent Themes
- **無可辨識跨 Issue 主題**：連續 7 天的每日快照皆未偵測到共通主題或重複議題。  
- **等待 Issue 更新**：每日快照的「Open Loops」皆顯示「等待下一輪 issue 更新後再整理」，顯示目前的工作焦點是 **監控新 Issue 的產生**。  

## Constraints
- **資訊來源限制**：只能從 Issue / Comment 抽取事實，手動筆記僅作為輔助說明，不能直接作為事實依據。  
- **覆寫限制**：自動化記憶蒸餾流程不會改寫 `shared/manual.md`，避免手動維護的長期規則被意外覆蓋。  
- **資料新鮮度**：若 30 天內無 Issue，系統將保持現有記憶不變，避免產生虛假或過時的規則。  

## Open Loops
- **Issue 待補**：目前缺乏任何 Issue 作為新資訊的來源，需等待開發者或協作者在倉庫中建立或更新 Issue
