# Repository Memory

## Stable Context
- **Repo 文化**  
  - 只以 GitHub Issue / Comment 為原始事實來源，任何記錄皆須可追溯回 Issue。  
  - `compact-memory` 工作流程會讀取本手動筆記，**不會**覆寫它；因此本檔案僅作為長期摘要，絕不直接複製 Issue 內容。  
  - 所有 agents 必須遵守上述規則，並在完成任務後於 Issue 留下明確的完成標記。

- **Agent 身分**  
  - 目前活躍的主要 agent 為 **西瓜蝦 (Lobster‑01)**，負責監控 Telegram 需求的轉換與日常 Issue 整理。  
  - 其他 agent 仍在觀察或待命狀態，未見具體任務分配。

- **技術限制**  
  - 每次記憶快照僅檢索最近 30 天、最多 100 個 Issue。  
  - 若 Issue 數量或時間範圍超出此限制，將不會出現在快照中，需另行查詢。

## Recent Themes
- **缺乏跨 Issue 主題**  
  - 連續兩天的快照皆未偵測到可辨識的跨 Issue 主題或共通決策，顯示近期工作較為分散或尚未形成明顯的議題聚焦。

- **Agent 活動監測**  
  - 2026‑03‑24 建立了「西瓜蝦 agent」的角色與技能描述，之後持續保持活躍等待指令。  
  - 2026‑03‑25 仍在等待 Telegram 需求的轉換指示，未見新任務產生。

## Constraints
1. **資料來源限制**  
   - 只能以 Issue / Comment 為事實依據，任何推論必須標註「不確定」或「待驗證」。
2. **記憶容量**
