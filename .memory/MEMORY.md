# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **主要記憶來源**  
  - GitHub Issue / Comment 為原始事實資料。  
  - `shared/manual.md` 為人工維護的長期記憶，僅存放 **穩定規則、長期決策、常見限制與 repo 習慣**，不會被自動流程覆寫。  
- **Agent 基本資訊**  
  - **Lobster‑01**（別名「西瓜蝦」）於 **2026‑03‑24** 建立角色與技能描述，仍處於 **活躍** 狀態。  
  - 目前唯一已知任務是 **等待 Telegram 需求的轉換**，尚未收到具體指令。  
- **工作流程**  
  - 每日快照會從過去 30 天內的 Issue 中抽取資訊，若無可用 Issue，則保留既有記憶。  
  - `compact‑memory` 工作流會讀取 `shared/manual.md` 作為長期上下文，**不會自動修改** 該檔案。  

> **不確定性**：目前沒有其他穩定規則或長期決策被記錄，若未來有新增，需手動寫入 `shared/manual.md`。

## Recent Themes
- **無跨 Issue 主題**：最近三天的快照皆未偵測到可辨識的跨 Issue 主題或重複議題。  
- **Agent 活動**：唯一重複出現的資訊是 Lobster‑01 的持續活躍與等待 Telegram 任務。  

## Constraints
1. **不複製完整 Issue 內容**：所有長期記憶必須以摘要或抽象形式呈現，避免直接搬錄原文。  
2. **手動筆記的角色**：`shared/manual.md` 只作為 **長期、穩定** 記憶的容器，任何自動化流程（如 daily snapshot、compact‑memory）**不會覆寫** 該檔。  
3. **Issue 為唯一事實來源**：所有可驗證的事實必須能追溯至 Issue 或 Comment。  
4. **每日快照範圍**：僅檢視
