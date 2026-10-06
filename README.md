Markdown# Planetary One Health & Macro-Economic Pandemic Defense Engine

> **A White-Box Multi-Scale Mathematical Simulation & Policy Optimization Platform for Global Public Health & Socio-Economic Resilience.**

---

## 🌍 Overview (プロジェクト概要)
現代のパンデミック危機や感染症の脅威において、政策決定者は「生命の安全（医療崩壊の回避）」と「社会経済活動の継続」という究極のトレードオフに直面します。
本システムは、ブラックボックスな経験則に頼るのではなく、**常微分方程式（ODE）をベースにした完全なホワイトボックス・マルチスケールモデル**により、発生源から国家マクロ経済、そして地球規模の国際協調に至るまでのダイナミクスを統合・シミュレートし、パレート最適な政策介入強度を導き出すオープンソースのデジタルツイン・エンジンです。

---

## 🏛️ Architecture (4層マルチスケール構造)

本シミュレータは、以下の4つのレイヤーを数理的に完全結合させています：

1. **Layer 1: Spillover & Cellular Dynamics**
   * 野生動物リザーバーからの人獣共通感染症の流出（スピルオーバー）と、ヒト標的細胞における野生株・変異株の感染・適応進化ダイナミクス。
2. **Layer 2: Adaptive Immunity & Inflammatory Control**
   * 免疫エフェクター細胞の立ち上がりと、致死的なサイトカインストーム（免疫暴走）の発生・抑制メカニズム。
3. **Layer 3: Metapopulation & International Supply Chain**
   * 都市間ネットワークの波及効果と、国際医療サプライチェーン（ワクチン・医薬品備蓄）の動的流通。
4. **Layer 4: Socio-Economic Pareto Optimization**
   * 医療リソース（ICU負荷）の限界制約を遵守しつつ、過剰な行動制限による経済損失と医療崩壊ペナルティを最小化する国家・国際戦略のパレート最適化。

---

## 🛠️ Requirements & Installation

Python 3.8以上と、以下の科学計算・可視化ライブラリが必要です。

```bash
# 必要なパッケージのインストール
pip install numpy scipy matplotlib
🚀 Quick Start (実行方法)リポジトリをクローンまたはダウンロードし、以下のコマンドを実行してください。Bash# 統合シミュレータスクリプトの実行
py planetary_health_complete_simulator.py
実行すると、各レイヤーのダイナミクス（感染動態、サプライチェーン備蓄、ICU負荷、経済健全度）を描示した4段構成の高度なダッシュボードが自動でレンダリングされます。📊 Core Mathematical Framework (抜粋)システムは以下の連立常微分方程式群をベースに駆動します：$$\begin{aligned}
\frac{dZ}{dt} &= r_z Z \left(1 - \frac{Z}{K_z}\right) - \gamma_{prev} Z \\
\frac{dT_c}{dt} &= \lambda - \beta V_{total} T_c - d_T T_c \\
\frac{dI_{total}}{dt} &= \text{Spillover}(Z) + \beta V_{total} T_c - \delta I_{total} \\
\frac{d\text{ICU}}{dt} &= \alpha I_{total} - \mu \text{ICU}
\end{aligned}$$📄 LicenseThis project is open-source under the MIT License.