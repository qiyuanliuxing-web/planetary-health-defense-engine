import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class CompletePlanetaryHealthDefenseEngine:
    """
    [Complete Planetary One Health & Macro-Economic Pandemic Simulator]
    - Layer 1: 野生動物リザーバーからのスピルオーバー（人獣共通感染症の流出）
    - Layer 2: ヒト集団における感染・免疫・変異ウイルスのダイナミクス
    - Layer 3: 国際医療サプライチェーン（医薬品・ワクチン備蓄の動的流通）
    - Layer 4: 地球規模の医療崩壊制約と経済健全度のパレート最適化
    """
    def __init__(self, initial_state):
        # 状態変数ベクトル (y):
        # y[0]: Z (野生動物のウイルス保有負荷 - スピルオーバー源)
        # y[1]: T_c (ヒト標的細胞)
        # y[2]: I_total (ヒト感染者総数)
        # y[3]: V_total (グローバルウイルス量)
        # y[4]: ICU_global (世界平均ICU負荷)
        # y[5]: Vaccine_Stock (国際医療サプライチェーン・備蓄量)
        # y[6]: Global_Eco_Index (グローバル経済健全度・復興インデックス)
        self.state = initial_state

    def master_planetary_ode(self, y, t, u_global_policy):
        Z, T_c, I_total, V_total, ICU_global, Vaccine_Stock, Global_Eco_Index = y
        
        # 国際協調・政策介入パラメータ (u_global_policy: 0.0=無策, 5.0=強力な地球規模介入)
        prevention_eff = 0.55 * u_global_policy  # 生態系モニタリング・発生源封鎖
        supply_boost = 0.45 * u_global_policy    # サプライチェーン増産・国際分配
        lockdown_drag = 0.12 * u_global_policy   # 過度な移動制限による経済摩擦
        
        # 1. スピルオーバー動態（生態系からのウイルス流入）
        spillover_rate = 0.0008 * Z * np.exp(-prevention_eff)
        dZ_dt = 0.1 * Z * (1.0 - Z / 10.0) - 0.06 * prevention_eff * Z
        
        # 2. ヒト免疫・感染動態
        lam = 1.2
        beta = 0.002
        d_T = 0.04
        delta = 0.012
        p = 2.0
        c = 1.0
        
        dT_dt = lam - beta * V_total * T_c - d_T * T_c
        dI_total_dt = spillover_rate + beta * V_total * T_c - delta * I_total
        
        # サプライチェーンによる治療・予防効果がウイルスを抑制
        effective_antiviral = 0.35 * min(Vaccine_Stock, 6.0)
        dV_total_dt = p * I_total - c * V_total - effective_antiviral * V_total
        
        # 3. 国際医療リソース（ICU）負荷
        dICU_global_dt = 0.12 * I_total - 0.09 * ICU_global
        
        # 4. サプライチェーン備蓄量の動態
        dVaccine_Stock_dt = supply_boost - 0.08 * I_total - 0.04 * Vaccine_Stock
        
        # 5. 地球規模経済健全度の動態（医療崩壊ペナルティ ＋ 行動制限摩擦）
        collapse_penalty = max(0.0, ICU_global - 3.0)**2
        dGlobal_Eco_Index_dt = 0.22 * (1.0 - Global_Eco_Index) - collapse_penalty - lockdown_drag * 0.4
        
        return [dZ_dt, dT_dt, dI_total_dt, dV_total_dt, dICU_global_dt, dVaccine_Stock_dt, dGlobal_Eco_Index_dt]

    def simulate(self, t_span, u_global_policy):
        return odeint(self.master_planetary_ode, self.state, t_span, args=(u_global_policy,))

    def optimize_planetary_strategy(self, t_span, max_icu_limit):
        """
        地球規模の医療崩壊を防ぎつつ、経済復興を最大化する
        パレート最適国際協調ポリシー (u) を全探索する
        """
        best_u = 0.0
        max_eco_score = -float('inf')

        for u_candidate in np.linspace(0.0, 4.5, 45):
            traj = self.simulate(t_span, u_candidate)
            max_icu = np.max(traj[:, 4])
            final_eco_health = traj[-1, 6]
            
            # 制約条件: 世界平均ICU負荷が限界を超えないこと
            if max_icu <= max_icu_limit:
                if final_eco_health > max_eco_score:
                    max_eco_score = final_eco_health
                    best_u = u_candidate

        return best_u, max_eco_score

if __name__ == "__main__":
    # 初期状態設定:
    # [Z(5.0), T_c(10.0), I_total(0.05), V_total(0.5), ICU_global(0.1), Vaccine_Stock(2.0), Global_Eco_Index(0.9)]
    initial_state = [5.0, 10.0, 0.05, 0.5, 0.1, 2.0, 0.9]
    t_span = np.linspace(0, 50, 500)
    
    icu_global_limit = 3.2
    
    # 地球規模最適化AIエンジンの起動
    engine = CompletePlanetaryHealthDefenseEngine(initial_state)
    optimal_u, optimal_eco_score = engine.optimize_planetary_strategy(t_span, icu_global_limit)
    
    print("=================================================================")
    print(" [Complete Planetary One Health & Defense AI Engine Active] ")
    print("=================================================================")
    print(f"Optimal Planetary Coordination Policy Intensity (u): {optimal_u:.4f}")
    print(f"Maximized Planetary Economic Health Score: {optimal_eco_score:.4f}")
    
    # 最適政策でのシミュレーション実行
    trajectory = engine.simulate(t_span, optimal_u)
    
    # 4段構成の地球規模ダッシュボード描画
    fig, axes = plt.subplots(4, 1, figsize=(12, 13), sharex=True)
    
    # 1. 野生動物スピルオーバー & ヒト感染動態
    axes[0].plot(t_span, trajectory[:, 0], label='Wildlife Reservoir ($Z$)', color='saddlebrown', linewidth=2)
    axes[0].plot(t_span, trajectory[:, 2], label='Global Infected ($I_{total}$)', color='crimson', linewidth=1.8)
    axes[0].set_title('Layer 1: Wildlife Spillover & Global Infection Dynamics', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Population', fontsize=9)
    axes[0].legend(loc='upper right', fontsize=8)
    axes[0].grid(True, linestyle='--', alpha=0.5)
    
    # 2. 国際サプライチェーン備蓄量
    axes[1].plot(t_span, trajectory[:, 5], label='Medical Supply Stock ($S_{med}$)', color='forestgreen', linewidth=2.0)
    axes[1].set_title('Layer 3: International Supply Chain & Vaccine Buffer', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Stock Index', fontsize=9)
    axes[1].legend(loc='upper right', fontsize=8)
    axes[1].grid(True, linestyle='--', alpha=0.5)
    
    # 3. グローバル医療リソース (ICU) 負荷
    axes[2].plot(t_span, trajectory[:, 4], label='Global ICU Strain', color='darkred', linewidth=2.2)
    axes[2].axhline(y=icu_global_limit, color='black', linestyle=':', label='ICU Capacity Limit')
    axes[2].set_title(f'Layer 4: Global Hospital Strain & Capacity Limit (Optimal u = {optimal_u:.2f})', fontsize=11, fontweight='bold')
    axes[2].set_ylabel('Strain Index', fontsize=9)
    axes[2].legend(loc='upper right', fontsize=8)
    axes[2].grid(True, linestyle='--', alpha=0.5)
    
    # 4. 地球規模経済健全度
    axes[3].plot(t_span, trajectory[:, 6], label='Planetary Economic Health Index', color='midnightblue', linewidth=2.2)
    axes[3].set_title('Global Economic Recovery & Resilience Trade-off', fontsize=11, fontweight='bold')
    axes[3].set_xlabel('Time (Days)', fontsize=9)
    axes[3].set_ylabel('Economic Health', fontsize=9)
    axes[3].legend(loc='upper right', fontsize=8)
    axes[3].grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()