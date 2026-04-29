# Repository Memory  

## Stable Context  
- **Repository**：`watermelon8157/watermelon8157.github.io` 為本記憶庫的唯一目標。  
- **Issue 為唯一事實來源**：所有可追溯的資訊必須來自 GitHub Issue 或其評論，手動筆記僅作為輔助摘要，絕不直接取代原始 Issue 內容。  
- **每日快照流程**：  
  1. 每日由各 Issue Agent 讀取最近 30 天內的 Issue（上限 100 件）。  
  2. 若當天無可用 Issue，則保留先前已建立的長期記憶，不產生新條目。  
  3. 產出 `daily/YYYY-MM-DD.json`，其中包含 **Agent Activity、Cross‑Issue Themes、Decisions、Open Loops、Top Labels**。  
- **手動筆記 (`shared/manual.md`) 的角色**：  
  - 用於保存 **穩定規則、長期決策、常見限制、repo 習慣**。  
  - 只作為 *compact‑memory* 工作流的參考，不會被自動覆寫。  
- **跨 Issue 主題與決策**：截至目前（2026‑04‑29）尚未偵測到任何跨 Issue 主題或跨 Issue 決策。  

## Recent Themes  
- **無可用 Issue**：連續七天（2026‑04‑23 至 2026‑04‑29）每日快照皆報告「本次整理視窗沒有可用 issue」，顯示近期工作區域缺乏新 Issue 或已全部關閉。  
- **等待更新**：每日快照的 **Open Loops** 均指向「等待下一輪 issue 更新後再整理」，形成一個持續的待辦循環。  

## Constraints  
1. **資訊來源限制**：只能引用 Issue / Comment，任何未在 Issue 中出現的資訊皆視為不確定或需另行驗證。  
2. **手動筆記不可覆寫**：自動化流程不會修改 `shared/manual.md`，因此任何新規則必須由人類手動加入。  
3. **每日快照上限**：每次僅檢視最近 30 天、最多 100 件 Issue，超出範圍的資訊不會自動納入本記憶。  
4. **語言與格式**：所有記憶必須以繁體中文撰寫，並保持 Markdown 可讀性，以供後續 Agent 解析。  

## Open Loops  
- **缺乏新 Issue**：目前無任何新 Issue 可供分析，需等待開發者或協作者提交新 Issue。  
- **跨 Issue 主題尚未形成**：若未來出現多個相關 Issue，需重新評估是否存在跨 Issue 主題或決策。
