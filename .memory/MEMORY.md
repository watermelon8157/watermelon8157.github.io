# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **主要角色**:  
  - **西瓜蝦 (Lobster‑01)**：負責監控 issue、整理每日快照、等待外部指令（如 Telegram 需求）。  
- **工作流程**:  
  1. 每日由 agents 讀取 GitHub Issue 列表（上限 100，回溯 30 天）。  
  2. 依據 issue 狀態產生 **Daily Snapshot**，彙整跨 issue 主題、決策與 open loops。  
  3. 若無可用 issue，保留既有記憶，等待下一輪更新。  
- **手動筆記 (`shared/manual.md`)** 的定位：保存 **穩定規則、長期決策、常見限制與 repo 習慣**，不會被自動流程覆寫。  
- **資料來源**：所有原始資訊皆來自 GitHub Issue / comment；本文件僅為萃取與整理後的長期記憶。

> **不確定性**：目前未在快照中觀測到其他 agents、額外的 issue 類別或特定的 repo 規範，故上述內容為已確認的核心資訊。

## Recent Themes
| 日期 | 觀測重點 | 說明 |
|------|----------|------|
| 2026‑03‑25 | **Lobster‑01 活躍** | 06:53 起持續活躍，等待 Telegram 需求的轉換。 |
| 2026‑03‑24 | **建立「西瓜蝦 agent」角色與技能描述** | 角色與技能於 2026‑03‑24 建立，尚未收到具體指令。 |
| 2026‑03‑26 ~ 2026‑03‑28 | **無可用 issue** | 每日快照皆顯示「本次整理視窗沒有可用 issue」，因此僅保留既有記憶。 |

- **跨 issue 主題**：連續多日皆未偵測到可辨識的跨 issue 主題。  
- **決策**：近期未產生新的跨 issue 決策。  

## Constraints
- **資料限制**：  
  - 只會從 **GitHub Issue / comment** 抽取資訊；若 Issue 未被建立或未被標記，系統無法產生相應快照。  
  - `shared/manual.md` 僅作為手動維護的長期記憶，不會自動同步或
