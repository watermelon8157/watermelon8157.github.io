# Repository Memory

## Stable Context
- 本倉庫的長期記憶由 **龍蝦團隊**（issue agents）每日從 GitHub Issue 中抽取資訊，彙整成快照（`daily/*.json`），再由我們整理成可重用的長期上下文。  
- **Shared Manual Notes (`shared/manual.md`)** 為人工維護的核心檔案，專門保存：
  - 穩定規則
  - 長期決策
  - 常見限制
  - Repo 內部的協作慣例  
  此檔案 **不會被自動覆寫**，僅供 `compact‑memory` 工作流讀取。
- 快照產生的基本參數（從所有快照可觀察到）：
  - 只檢視過去 **30 天** 內的 Issue  
  - 每次最多 **100** 筆 Issue  
  - 以 **deterministic** 演算法產出摘要  
- 目前的 Issue 狀態在最近 7 天內皆為 **「無可用 Issue」**，因此每日快照皆只保留既有記憶，未產生新主題或決策。

> **不確定性**：因為缺乏實際 Issue 內容，我們無法從快照中抽取具體的業務規則、工作流程或專案目標。上述「穩定規則」僅限於系統層面的運作方式。

## Recent Themes
- **無跨 Issue 主題**：過去一週的所有快照皆顯示「目前沒有可辨識的跨 issue 主題」。
- **無新決策**：同樣地，沒有任何跨 Issue 的決策被記錄。

> **不確定性**：若在未來的 Issue 中出現新主題，需重新評估此區塊。

## Constraints
1. **手動筆記優先**  
   - `shared/manual.md` 為唯一的手動長期記憶來源，任何自動化流程（如 `compact‑memory`）**不會覆寫**此檔案。  
2. **Issue 為唯一事實來源**  
   - 所有可追溯的事實、決策與任務必須來自 GitHub Issue / Comment。  
3. **快照範圍限制**  
   - 只考慮最近 30 天內、最多 100 筆 Issue。超出範圍的資訊不會出現在每日快照。
