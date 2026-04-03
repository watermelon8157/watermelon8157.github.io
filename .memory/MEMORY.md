# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶管理流程**  
  - 由每日快照（daily snapshots）彙整當天活躍的 Issue agents。  
  - `shared/manual.md` 用於手動維護長期記憶，僅保存**穩定規則、長期決策、常見限制與 repo 習慣**，不會被自動覆寫。  
- **目前觀測**  
  - 最近 30 天內的所有快照皆未偵測到可用 Issue，故無新資訊可加入長期記憶。  
  - 系統仍保留先前已建立的記憶（若有），但在本資料集中未顯示。

## Recent Themes
- **無可辨識跨 Issue 主題**（2023‑03‑28 至 2026‑04‑03 的所有快照皆未出現）。  
- **無新決策**：每日快照皆報告「目前沒有新的跨 issue 決策」。

## Constraints
- **Issue 必須存在**：記憶抽取依賴 Issue / Comment 作為原始資料來源，若缺乏 Issue，記憶更新將停留在「保留既有記憶」的狀態。  
- **手動筆記不可被自動覆寫**：`shared/manual.md` 只作為人類編輯的長期記憶來源，系統不會自動寫入或刪除其內容。  
- **資訊完整性**：若資訊不足或相互矛盾，必須在此文件中明確標示不確定性（目前屬於資訊缺乏的情形）。

## Open Loops
- **等待 Issue 更新**：所有快照皆顯示「等待下一輪 issue 更新後再整理」，因此以下項目仍未解決：  
  1. 何時會有可用 Issue 供系統彙整？  
  2. 是否需要主動建立 Issue 以啟動記憶更新流程？  
  3. 目前缺乏任何跨 Issue 主題或決策的追蹤。  

> **註**：若未來出現新的 Issue、跨 Issue 主題或決策，請於 `shared/manual.md` 中加入相應的穩定規則或長期決策，並在每日快照中觀測其演變。
