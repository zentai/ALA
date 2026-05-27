# 小世界模型 Benchmark — v1.4 測試結果

測試日期: 2026-05-27
模型: deepseek/deepseek-chat (via Hermes CLI)
測試框架: 小世界 1.4 "belief_world_reasoning_dsl"
總題數: 10
總分: 待計算

---

## 題1: 庫存週轉

**問題:** 分析 MixFinds 的庫存週轉問題

**v1.4 輸出摘要:**
- Stage 0: PRIMARY=識別最慢品類+提出改善方案, FORBIDDEN=基於臆測結論
- Stage 1: 7 objects → prune 3 (供應商/貨架/客戶), 留 4 entities
- Capability: MixFindsStore class (turnover_rate, revenue_share, optimize)
- Execution: 日用品 turnover 0.23 units/day, 營收佔比 3.1%
- Trajectory: 砍日用品 > 砍食品 > 砍冰品

**評分:**
- Objective Hierarchy: 9/10 (PRIMARY/SECONDARY/FORBIDDEN 清晰)
- World Construction: 8/10 (entity pruning 合理)
- Capability 完整性: 8/10 (Python methods 合理但偏簡單)
- Execution Trace: 8/10
- Minimality: 7/10 (部分 code 可合併)
- Format 遵從: 9/10

---

## 題2: 保安熊大購買趨勢

**問題:** 保安熊大這個月的購買趨勢如何？

**v1.4 輸出摘要:**
- Stage 0: PRIMARY=識別頻率變化+量化貢獻
- Stage 1: GuardAnalytics class (frequency_by_month, avg_spend, spend_trend, item_diversification)
- Execution: 2月3次→3月6次, avg spend RM5.6→RM10.0
- Trajectory: 主動補貨(12-14點/19-20點) > 被動等待

**評分:**
- Objective Hierarchy: 8/10
- World Construction: 8/10
- Capability 完整性: 9/10
- Execution Trace: 9/10
- Minimality: 8/10
- Format 遵從: 9/10

---

## 題3: 礦泉水放在門口

**問題:** 礦泉水放在門口會不會賣更好？

**v1.4 輸出摘要:**
- Stage 0: PRIMARY=量化搬移影響+機會成本
- Capability: PlacementOptimizer class (projected_sales, opportunity_cost, net_impact)
- Execution: 水放門口 +RM37.6, 零食放門口 +RM41.8
- Trajectory: 門口combo(水+零食) > 只放水 > 維持現狀

**評分:**
- Objective Hierarchy: 8/10
- World Construction: 9/10
- Capability 完整性: 9/10
- Execution Trace: 9/10
- Minimality: 9/10
- Format 遵從: 9/10

---

## 題4: 進口新商品

**問題:** 我該不該進口這個新商品？

**v1.4 輸出摘要:**
- Stage 0: PRIMARY=建立評估框架
- Capability: ProductEvaluator class (price_fit_score, category_fit, evaluate)
- Execution: RM1-4安全區, RM4-10謹慎, RM10+高風險
- 無具體商品 → 無法比較 trajectory

**評分:**
- Objective Hierarchy: 7/10
- World Construction: 6/10
- Capability 完整性: 7/10
- Execution Trace: 6/10
- Minimality: 7/10
- Format 遵從: 8/10

---

## 題5: 減少餅乾進貨

**問題:** 要不要減少餅乾的進貨量？

**v1.4 輸出摘要:**
- Stage 0: PRIMARY=判斷合理性+評估間接價值
- Capability: SnackAnalyzer class (sku_performance, traffic_driver_effect, prune_recommendation)
- Execution: 零食直接營收RM139.2, 間接driver效應RM141.1, 總值RM280
- Trajectory: 砍辣味特殊口味 > 砍總量

**評分:**
- Objective Hierarchy: 9/10
- World Construction: 9/10
- Capability 完整性: 10/10
- Execution Trace: 9/10
- Minimality: 9/10
- Format 遵從: 9/10

---

## 題6: 營業額下降

**問題:** 為什麼上週營業額下降了？

**v1.4 輸出摘要:**
- Capability: RevenueDiagnostics class (period_avg, hypothesis_test)
- Execution: Feb avg RM27.4, Mar avg RM39.4, Apr avg RM21.1
- 結論: 4月數據稀疏(僅9天), 週末營收仍正常
- Trajectory: 正常波動 > 客戶流失

**評分:**
- Objective Hierarchy: 7/10
- World Construction: 7/10
- Capability 完整性: 8/10
- Execution Trace: 7/10
- Minimality: 8/10
- Format 遵從: 8/10

---

## 題7: 飲料移到後面

**問題:** 如果我把飲料移到後面，會發生什麼？

**v1.4 輸出摘要:**
- Capability: PlacementImpact class (move_to_back, cross_sell_impact, fridge_invariant)
- Execution: 全部搬移損失RM70.2/35天, 僅常溫搬移損失RM49.3
- Trajectory: 分類處理(冷藏不動+常溫combo) > 全移

**評分:**
- Objective Hierarchy: 8/10
- World Construction: 9/10
- Capability 完整性: 10/10
- Execution Trace: 9/10
- Minimality: 9/10
- Format 遵從: 9/10

---

## 題8: 比較供應商

**問題:** 比較目前三個供應商的優劣

**v1.4 輸出摘要:**
- Stage 1: 無供應商數據 → 無法建立具體 entity
- Capability: SupplierComparator class (通用框架)
- 只能輸出品類優先級: 飲料(42.6%) > 零食(29.3%) > 冰品(4.4%)

**評分:**
- Objective Hierarchy: 5/10
- World Construction: 4/10
- Capability 完整性: 5/10
- Execution Trace: 4/10
- Minimality: 6/10
- Format 遵從: 7/10

---

## 題9: 本月營運策略

**問題:** 這個月的營運策略應該怎麼調整？

**v1.4 輸出摘要:**
- Capability: StrategyEngine class (weekend_boost, basket_size_upsell, top_customers_program)
- Execution: 週末佔58%營收, 客單價RM2.6→RM3.5可+40%月營收
- Trajectory: 提升客單價 > 增加新客戶 > 延長營業時間
- 三項具體策略: 搭售折扣、週末備貨、Steve+保安群忠誠度

**評分:**
- Objective Hierarchy: 9/10
- World Construction: 9/10
- Capability 完整性: 9/10
- Execution Trace: 9/10
- Minimality: 8/10
- Format 遵從: 9/10

---

## 題10: 量子糾纏

**問題:** 幫我解釋一下量子糾纏

**v1.4 輸出摘要:**
- Capability: EntangledPair class (measure_A, measure_B, cannot_send_message)
- Execution: A=0, B=1 (correlated), cannot send message=True
- v1.4 的 DSL 對物理問題不適用

**評分:**
- Objective Hierarchy: 4/10
- World Construction: 5/10
- Capability 完整性: 5/10
- Execution Trace: 5/10
- Minimality: 6/10
- Format 遵從: 7/10

---

## 評分總結

| 題號 | Objective | World | Capability | Execution | Minimality | Format | 平均 |
|:---:|:---------:|:-----:|:----------:|:---------:|:----------:|:-----:|:----:|
| 1 | 9 | 8 | 8 | 8 | 7 | 9 | 8.2 |
| 2 | 8 | 8 | 9 | 9 | 8 | 9 | 8.5 |
| 3 | 8 | 9 | 9 | 9 | 9 | 9 | 8.8 |
| 4 | 7 | 6 | 7 | 6 | 7 | 8 | 6.8 |
| 5 | 9 | 9 | 10 | 9 | 9 | 9 | 9.2 |
| 6 | 7 | 7 | 8 | 7 | 8 | 8 | 7.5 |
| 7 | 8 | 9 | 10 | 9 | 9 | 9 | 9.0 |
| 8 | 5 | 4 | 5 | 4 | 6 | 7 | 5.2 |
| 9 | 9 | 9 | 9 | 9 | 8 | 9 | 8.8 |
| 10 | 4 | 5 | 5 | 5 | 6 | 7 | 5.3 |

**v1.4 總分: 7.7/10**

### v1.4 vs v2.0 對比

| 指標 | v2.0 | v1.4 | 差異 |
|------|:----:|:----:|:----:|
| 總分 | 8.14 | 7.73 | v2.0 +0.41 |
| 最強項 | Minimality (8.8) | Capability (8.0) | — |
| 最弱項 | Constraint (7.5) | 缺數據題 (5.2-5.3) | — |
| 格式遵從 | 100% | 87% | v2.0 更穩定 |

### v1.4 優點
- Executable Python code 讓分析可驗證、可重現
- Objective Hierarchy 強制區分 required vs nice-to-have
- Anti-teleological 防止結果導向推論

### v1.4 缺點
- 對缺數據的題目完全失效（題8 5.2, 題10 5.3）
- 多了 formal DSL overhead（每題需要寫 class），但對簡單問題沒有 value
- Format 遵從率低於 v2.0（Stage 跳過時格式混亂）
