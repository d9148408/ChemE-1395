# Unit10：經濟分析與評價

- **課程名稱**：化工程序模擬 (ChemE 1395)
- **單元主題**：Aspen Plus 內建經濟分析 × Aspen Process Economic - Analyzer (APEA)
- **課程製作**：逢甲大學 化工系 智慧程序系統工程實驗室 ｜ 授課教師：莊曜禎 助理教授
- **更新日期**：2026-06-26

---

## 📁 檔案清單

| 檔案 / 資料夾 | 類型 | 說明 |
|:---|:---:|:---|
| [`Unit10-1_Economics_Analysis.md`](Unit10-1_Economics_Analysis.md) | 講義 | 主講義：Aspen Plus 內建經濟分析（10.1 節），含完整結果討論與投資分析 |
| [`images/`](images/) | 圖片 | 講義對應截圖（fig_10_002 ～ fig_10_018） |


---

## 📖 學習內容概覽

### 第 10.1 節：Aspen Plus 內建經濟分析（`Unit10-1_Economics_Analysis.md`）

以 **環氧乙烷制乙二醇（EO → MEG/DEG/TEG）** 工業流程為範例，完整示範從工藝模擬到財務評估的全流程：

| 節次 | 主題 |
|:---:|:---|
| 章節概述 | Aspen Economic Evaluation 三款模組介紹（ACCE / AICE / APEA） |
| 核心工作流程 | Mapping → Sizing → Estimating 三步驟原理說明 |
| 乙二醇製程背景 | EO 水合反應化學、MEG 選擇性、工業意義、本例模擬規模 |
| 獲利核心概念 | 原料成本、操作成本與產品售價三者關係；P.O. Period 直觀理解 |
| 10.1.1–10.1.3 | 開啟範例檔、設定成本核算選項、輸入物流價格 |
| 10.1.4–10.1.6 | 啟用經濟估算、裝置 Mapping 與設備選型、刪除虛擬元件 |
| 10.1.7–10.1.8 | 檢視初步結果、處理警告與錯誤（EG-RCTR 高度超限 / PREHEAT 問題修復） |
| 10.1.9 | 新增公用工程（冷卻水 / 中壓蒸汽）並重新計算，含四頁結果深度討論 |
| 10.1.10 | 投資分析（IPEWB2.xlsx）：分析假設、資本成本結構、10 年現金流、7 項財務指標 |

**本單元核心教學重點**：
以 P.O. Period = 0（無法回收）為教學反例，深入剖析 EO-WATER 混合流股定價方式所隱含的 EO 成本高達 \$1,100/tonne（而 MEG 售價僅 \$600/tonne），說明正確定義原料流股價格對經濟分析結果的決定性影響。

---

## ⚗️ 製程背景：環氧乙烷制乙二醇

本單元範例基於 **EO 水合制乙二醇** 製程（Aspen Plus 內建 Bulk Chemical 示例）：

$$
\text{EO} + \text{H}_2\text{O} \longrightarrow \text{MEG} \quad (\text{選擇性} \approx 86.5\%)
$$

| 項目 | 本例數值 | 工業典型值 |
|:---|---:|---:|
| EO 進料量 | 55,000 kg/hr | 視廠規模 |
| 水/EO 莫耳比 | 2.44:1 | **≥ 20:1** |
| MEG 選擇性 | 86.5% | > 90% |
| MEG 年產量 | ~587,800 t/yr | 視廠規模 |
| 總資本成本（含修改後） | $19.84M USD | — |
| 年度原料成本 | $530M USD/yr | — |
| 年度產品收益 | $410M USD/yr | — |

> **注意**：本例水/EO 莫耳比偏低（2.44:1），導致 MEG 選擇性偏低（86.5%）且 DEG/TEG 副產物偏多。此設定為教學示例，目的在於展示完整分離流程（脫水塔、MEG 塔、DEG 塔、TEG 塔）的設計特性與建設成本，而非最優工業操作條件。

---

## 🖥️ 軟體需求

| 軟體 | 版本 | 用途 |
|:---|:---|:---|
| **Aspen Plus** | V12.2（建議） | 開啟 `.apwz`、`.bkp` 模擬檔，執行內建經濟分析 |
| **Aspen Process Economic Analyzer (APEA)** | V12.2（建議） | 開啟 `.apprj` 專案檔，執行獨立經濟分析 |
| **Microsoft Excel** | 2016 以上 | 檢視 `IPEWB2.xlsx` 投資分析結果 |

> Aspen Plus 與 APEA 均包含於 **AspenONE** 套裝軟體中。學校授權帳號可透過 AspenONE Exchange 下載安裝。

---

## 🚀 學習路徑建議

```
1. 閱讀「章節概述」與「核心工作流程」 → 建立 Mapping → Sizing → Estimating 概念框架
      ↓
2. 閱讀「乙二醇製程背景」與「獲利核心概念」 → 理解原料/操作成本/售價關係
      ↓
3. 開啟 Ethylene Glycol Plant Example.bkp → 跟隨 10.1.1–10.1.6 完成 Mapping
      ↓
4. 執行 10.1.7 取得初步結果 → 對照 10.1.8 修復錯誤（調整 EG-RCTR / 新增 PREHEAT2）
      ↓
5. 依 10.1.9 新增公用工程並重新評估 → 深度解讀四頁結果（流量平衡 / 成本 / 設備 / 收益）
      ↓
6. 執行 Investment Analysis → 開啟 IPEWB2.xlsx → 解讀 10 年現金流與 7 項財務指標
      ↓
7. 對照 pdf/Unit10-2_APEA.md → 使用獨立 APEA 軟體重新進行更完整的財務評估
```

---

**課程授權 [CC BY-NC-SA 4.0]**
本教材遵循 [創用CC 姓名標示-非商業性-相同方式分享 4.0 國際 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 授權。
