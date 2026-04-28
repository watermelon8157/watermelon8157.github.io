# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **Issue handling**: 每日快照會檢視過去 30 天內的所有 issue（上限 100），若無可用 issue，則保留既有記憶不做變更。  
- **Shared Manual Notes**（`shared/manual.md`）是唯一由人類手動維護、用來保存**穩定規則、長期決策、常見限制與 repo 習慣**的檔案。此檔案不會被自動覆寫，也不應直接複製 issue 原文。  
- **目前觀測期間（2026‑04‑22 ~ 2026‑04‑28）**，所有每日快照皆顯示「本次整理視窗沒有可用 issue」，代表在此段時間內 repository 沒有開啟或待處理的 issue。  
- **跨 issue 主題、決策與標籤**：在上述期間未偵測到任何跨 issue 主題、決策或常用標籤（`Top Labels: none`）。  

> **不確定性**：因為缺乏實際 issue 內容，我們無法從日誌中抽取具體的長期規則或工作流程。若未來出現 issue，請於 `shared/manual.md` 中補充相應的穩定規則與限制。

## Recent Themes
- **無活躍 issue**：連續七天的快照皆未捕捉到任何 issue，顯示近期工作狀態相對靜止。  
- **等待更新**：每日快照的「Open Loops」皆寫明「等待下一輪 issue 更新後再整理」，暗示目前的主要關注點是 **監測新 issue 的出現**。  

> 若在未來的日誌中出現新 issue，請留意是否出現重複出現的主題（例如部署、文件、功能需求等），以便將其升級至 **Stable Context** 或 **Open Loops**。

## Constraints
1. **手動筆記優先**：所有長期規則與限制必須寫入 `shared/manual.md`，自動化流程僅讀取不寫入。  
2. **Issue 數量上限**：每日快照僅檢視最多 100 個 issue，且僅限過去 30 天內的變動。  
3. **資料來源**：正式的原始資訊
