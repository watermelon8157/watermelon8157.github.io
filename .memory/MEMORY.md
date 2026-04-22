# Repository Memory

## Stable Context
- **Repository**: `watermelon8157/watermelon8157.github.io`  
- **記憶維護流程**  
  - 每日由 *issue agents* 讀取過去 30 天內的 GitHub Issue（含開啟與關閉）產出快照。  
  - 快照檔案位於 `.memory/daily/`，以 `YYYY-MM-DD.json` 命名。  
  - 產出的快照僅保留 **摘要**（跨 Issue 主題、決策、Open Loops、Top Labels），不會直接寫入原始 Issue 內容。  
  - `shared/manual.md` 為人工維護的長期記憶手冊，僅存放 **穩定規則、長期決策、常見限制、repo 習慣**，不會被自動覆寫。  
- **Agent 共識**  
  - 所有 agents 必須以 **GitHub Issue / comment** 為唯一事實來源。  
  - 任何新資訊若未在 Issue 中出現，皆視為 **未確定**，不會寫入 `Stable Context`。  
  - `compact‑memory` 工作流會讀取 `shared/manual.md`，但不會改寫它；因此手動筆記是唯一的 **長期、穩定** 記憶來源。  

## Recent Themes
> 目前的每日快照（2026‑04‑16 至 2026‑04‑22）皆顯示「本次整理視窗沒有可用 issue」，因此 **未偵測到任何跨 Issue 主題**、決策或重複出現的議題。  
- **無新主題**：每日皆回報「等待下一輪 issue 更新後再整理」。  
- **持續的空白狀態**：這本身是一個可觀察的模式——近期 repo 似乎缺乏活躍的 Issue。  

## Constraints
1. **資訊來源限制**  
   - 只能引用 GitHub Issue / comment 作為事實依據。  
   - `shared/manual.md` 只能作為 **手動維護的規則與限制**，不應直接搬入 Issue 文字。  
2. **記憶產出規則**  
   - `MEMORY.md` 必須是 **精煉、可重用** 的長期記憶，避免逐段複製原始日誌。  
   - 若資訊僅在單一天出現且未形成穩定事實，必須放入 **Open Loops** 或 **Recent Themes**，不可寫入 **Stable Context
