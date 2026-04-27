# Repository Memory

## Stable Context
- **Repository**：`watermelon8157/watermelon8157.github.io`  
- **記憶流程**：每日由多隻龍蝦（issue agents）掃描過去 30 天內最多 100 個 GitHub Issue，抽取 **穩定規則、長期決策、常見限制、repo 習慣**，再交給我們這份長期記憶檔案。  
- **目前狀態**：過去一週的所有快照皆顯示「本次整理視窗沒有可用 issue」，因此既有的長期記憶未被更新。  
- **手動筆記**：`shared/manual.md` 中列出的「穩定規則、長期決策、常見限制、agent 共同遵守的 repo 習慣」屬於 **手動維護** 的長期記憶，會被 `compact-memory` 工作流讀取但不會被自動覆寫。  
- **工作原則**：  
  1. 只從 **GitHub Issue / Comment** 抽取資訊，原始 Issue 文字不會直接寫入本檔。  
  2. 若資訊只在單一天出現且尚未確認為穩定，則放入 **Open Loops**，不列入 **Stable Context**。  
  3. 本檔案僅保存 **經過蒸餾的長期可重用上下文**，不作
