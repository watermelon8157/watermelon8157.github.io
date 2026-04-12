# Repository Memory

## Stable Context
- **手動長期記憶檔案**：`shared/manual.md` 內保留 **穩定規則、長期決策、常見限制、repo 習慣**，此檔案僅供閱讀，不會被 agents 覆寫。  
- **資料來源原則**：所有原始資訊皆來自 GitHub **issue / comment**；agents 只會根據這些資料產生每日快照，並以 `compact‑memory` 工作流程讀取 `shared/manual.md`。  
- **記憶更新機制**：若當日無可用 issue，agents 會 **保留既有記憶**，不會自行創建或推測新規則。  
- **避免重複**：`MEMORY.md` 必須是 **精煉、可重用** 的長期記憶，絕不直接複製原始 issue 內容或標題。

## Recent Themes
- **2026‑04‑06 ~ 2026‑04‑12**：每日快照皆顯示「本次整理視窗沒有可用 issue」，因此 **未偵測到任何跨 issue 主題或重複出現的議題**。  
- **無新決策**：期間內未產生跨 issue 的決策或共識。

## Constraints
1. **不複製原始 issue 文字**：`MEMORY.md` 只能呈現概念性、抽象化的
