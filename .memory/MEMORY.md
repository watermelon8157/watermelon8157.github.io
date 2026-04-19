# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶管理流程**  
  - 每日由多個 *issue agents* 產出 **daily snapshot**，彙整當天活躍的 Issue。  
  - 這些 snapshot 只在有可用 Issue 時才會產生具體內容，否則保留既有記憶。  
  - 長期記憶的核心來源是 **GitHub Issue / Comment**，而非手動筆記或其他檔案。  
- **手動筆記 (`shared/manual.md`)**  
  - 用於保存 **穩定規則、長期決策、常見限制、repo 習慣**。  
  - 內容不會被自動流程覆寫，僅供 agents 參考。  
- **repo 習慣**（從手動筆記推測）  
  1. **不直接複製 Issue 原文**：只抽取關鍵資訊，避免冗長。  
  2. **compact‑memory workflow** 會讀取 `shared/manual.md`，但不會寫回。  
  3. **每日快照** 只保留「跨 Issue 主題」與「決策」等高層摘要，細節留在 Issue 本身。  

> **不確定性**：目前未在 Issue 中觀測到任何具體任務、決策或跨 Issue 主題，故上述「repo 習慣」僅根據手動筆記的說明推測，未經實際驗證。

## Recent Themes
- **無可辨識的跨 Issue 主題**（2026‑04‑13 至 2026‑04‑19）  
  - 每日快照皆顯示「目前沒有可辨識的跨 issue 主題」以及「沒有新的跨 issue 決策」。  
- **持續缺乏可用 Issue**  
  - 連續七天（2026‑04‑13 ~ 2026‑04‑19）皆報告「本次整理視窗沒有可用 issue」，表示近期 repo 內未產生或未被 agents 標記為活躍的 Issue。  

## Constraints
1. **資訊來源限制**  
   - 只能從 **GitHub Issue / Comment** 取得原始資料；手動筆記僅作為輔助。  
2. **內容呈現規則**  
   - 不得完整複製 Issue 原文；需以 **精煉、可
