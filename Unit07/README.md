# Unit07：吸收與萃取操作 + 多級逆流萃取進階

> **課程名稱**：化工程序模擬 (ChemE 1395)
> **單元主題**：氣體吸收（Absorption）、液液萃取（Extraction）及多級逆流萃取（MSCCE）
> **課程製作**：逢甲大學 化工系 智慧程序系統工程實驗室 ｜ 授課教師：莊曜禎 助理教授
> **更新日期**：2026-06-12

---

## 📁 檔案清單

| 檔案 / 資料夾 | 類型 | 說明 |
|:---|:---:|:---|
| [`Unit07_AbsExtract.md`](Unit07_AbsExtract.md) | 講義 | Unit07 主講義：氣體吸收與液液萃取基礎（NRTL、EXTRACT 模塊） |
| [`Unit07_MSCCE.md`](Unit07_MSCCE.md) | 講義 | Unit07 進階講義：多級逆流萃取理論、Kremser 公式、Aspen Plus 模擬 |
| [`MSCCE_Interactive.html`](MSCCE_Interactive.html) | 互動網頁 | 4 頁籤 HTML 互動教學工具（**需下載至本機以瀏覽器開啟**，詳見下方說明） |


---

## 📖 學習內容概覽

### Unit07 主講義（`Unit07_AbsExtract.md`）

涵蓋吸收與萃取操作的核心 Aspen Plus 模擬技術：

- **氣體吸收**：RateFrac 模組、傳質效率（Murphree Efficiency）、Kremser 法求理論板數
- **液液萃取**：EXTRACT 模組設定、NRTL-LLE 參數選用、KLL 分配係數計算
- **典型例題**：CO₂ 吸收（Unit07 例 7-1）、苯酚廢水萃取（Unit07 例 7-3、7-2）

### Unit07 進階講義（`Unit07_MSCCE.md`）

多級逆流萃取（MSCCE）完整教學鏈：

| 章節 | 主題 |
|:---:|:---|
| MSCCE.1 | 萃取操作模式比較（單級 / 錯流 / 逆流）、實驗室常見設備 |
| MSCCE.2 | 逆流理論：操作線、Y-X 圖、McCabe-Thiele 法、Kremser 公式、最小溶劑量 $S'_{\min}$ |
| MSCCE.3 | Aspen Plus EXTRACT 模塊設定（NRTL-LLE、板號方向、KLL 計算） |
| 例 MSCCE-1 | 乙酸乙酯-丙酮-水體系：4 方案比較（Decanter 單級、錯流、逆流 + EXTRACT 模塊） |

**核心教學重點**：本案例以高濃度（丙酮 30 wt%）進料示範「稀溶液 Kremser 公式在高濃度體系的嚴重失效」——稀溶液預測回收率 89.4%，Aspen 嚴格計算實際僅 57.2%，有效 $KLL$ 從稀溶液極限 1.2 降至操作濃度下的 0.19。

---

## 🎮 互動教學網頁使用說明

### `MSCCE_Interactive.html`（4 頁籤 HTML 互動工具）

| 頁籤 | 功能 | 對應章節 |
|:---:|:---|:---:|
| ① 操作模式比較 | 滑桿即時比較單級 / 錯流 / 逆流回收率；流程示意圖 | §MSCCE.1.4 |
| ② Y-X 圖解互動 | McCabe-Thiele 逐板階梯動畫；夾緊點視覺化 | §MSCCE.2.5 |
| ③ Kremser 計算器 | 理論板數、 $S'_{\min}$ 、 $E_{\min}$ 即時計算；敏感度曲線 | §MSCCE.2.7 |
| ④ 逐板濃度動畫 | 各板 X/Y 濃度動態分布；塔板傳質梯度視覺化 | §MSCCE.3 |

### ⚠️ 下載使用（重要）

> **在 GitHub 上直接點擊 `MSCCE_Interactive.html` 連結只會顯示 HTML 原始碼，無法執行互動功能。**

請依以下任一方式取得並使用：

**方法 1（推薦）：Clone 整個 Repository**
```bash
git clone https://github.com/<username>/ChemE-1395.git
cd ChemE-1395/Unit07
# 以瀏覽器開啟
start MSCCE_Interactive.html      # Windows
open MSCCE_Interactive.html       # macOS
```

**方法 2：單獨下載 HTML 檔**

1. 在 GitHub 上開啟 `MSCCE_Interactive.html`
2. 點擊右上角 **Raw** 按鈕
3. 在瀏覽器中按 `Ctrl+S`（Windows）或 `Cmd+S`（macOS）另存新檔
4. 以瀏覽器（Chrome / Edge / Firefox）開啟儲存的 `.html` 檔

> 本網頁為純靜態 HTML + JavaScript，**無需安裝任何套件或伺服器**，使用現代瀏覽器即可正常執行所有互動功能。MathJax 公式渲染需要網際網路連線。

---

## 📝 版本記錄

| 日期 | 更新內容 |
|:---|:---|
| 2026-06-12 | 新增 MSCCE 進階講義（全文）；MSCCE_Interactive.html 4 頁籤互動工具；gen_MSCCE_figs.py；高濃度非線性效應深度分析 |
| 2026-06-11 | 重構例 MSCCE-1 為 4 方案教學流程；新增實驗室設備章節（MSCCE.1.2） |
| 2026-05-01 | Unit07 主講義（吸收與萃取基礎）初稿 |

---

**課程授權 [CC BY-NC-SA 4.0]**
本教材遵循 [創用CC 姓名標示-非商業性-相同方式分享 4.0 國際](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 授權。
