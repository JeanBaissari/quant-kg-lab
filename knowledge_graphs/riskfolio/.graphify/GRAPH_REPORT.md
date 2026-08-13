# Graph Report - knowledge_graphs/riskfolio/repo/riskfolio  (2026-08-13)

## Corpus Check
- 15 files · ~97,150 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 426 nodes · 599 edges · 26 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: calls: 187 · rationale_for: 180 · contains: 167 · method: 63 · inherits: 2


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 15 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `632a9e4`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Portfolio` - 50 edges
2. `Sharpe_Risk()` - 37 edges
3. `Risk_Margin()` - 37 edges
4. `Risk_Contribution()` - 36 edges
5. `HCPortfolio` - 19 edges
6. `denoiseCov()` - 8 edges
7. `CliqHierarchyTree2s()` - 8 edges
8. `EVaR_Hist()` - 8 edges
9. `RLVaR_Hist()` - 8 edges
10. `codep_dist()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Portfolio` --inherits--> `object`  [EXTRACTED]
  src/Portfolio.py →   _Bridges community 5 → community 9_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (88): ADD_Abs(), ADD_Rel(), BrinsonAttribution(), CDaR_Abs(), CDaR_Rel(), CVaR_Hist(), CVRG(), DaR_Abs() (+80 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (52): block_vec_pq(), codep_dist(), color_list(), corr2cov(), cov2corr(), cov_fix(), cov_returns(), dcorr() (+44 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (36): plot_bar(), plot_BrinsonAttribution(), plot_clusters(), plot_clusters_network(), plot_clusters_network_allocation(), plot_dendrogram(), plot_drawdown(), plot_factor_risk_con() (+28 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (30): cokurtosis_matrix(), commutation_matrix(), coskewness_matrix(), covariance_matrix(), d_corr(), d_corr_matrix(), duplication_elimination_matrix(), duplication_matrix() (+22 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (30): assets_clusters(), assets_constraints(), assets_views(), average_centrality(), centrality_vector(), clusters_matrix(), connected_assets(), connection_matrix() (+22 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (2): Portfolio, r"""     Class that creates a portfolio object with all properties needed to

### Community 6 - "Community 6"
Cohesion: 0.10
Nodes (28): augmented_black_litterman(), backward_regression(), black_litterman(), black_litterman_bayesian(), bootstrapping(), cokurt_matrix(), covar_matrix(), entropy_pooling() (+20 more)

### Community 7 - "Community 7"
Cohesion: 0.12
Nodes (27): AdjCliq(), breadth(), BubbleCluster8s(), BubbleHierarchy(), BubbleMember(), BuildHierarchy(), CliqHierarchyTree2s(), clique3() (+19 more)

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (22): owa_cvar(), owa_cvrg(), owa_gmd(), owa_l_moment(), owa_l_moment_crm(), owa_rg(), owa_tg(), owa_tgrg() (+14 more)

### Community 9 - "Community 9"
Cohesion: 0.15
Nodes (4): object, HCPortfolio, r"""     Class that creates a portfolio object with all properties needed to, r"""         This method calculates the optimal portfolio according to the

### Community 10 - "Community 10"
Cohesion: 0.25
Nodes (4): r"""         Reset all risk constraints., r"""         Reset all linear constraints., r"""         Reset all inputs parameters of optimization models., r"""         Reset portfolio object to defatult values.

### Community 11 - "Community 11"
Cohesion: 0.29
Nodes (6): gerber_cov_stat0(), gerber_cov_stat1(), gerber_cov_stat2(), r"""     Compute Gerber covariance Statistics 1 :cite:`d-Gerber2021`.      Param, r"""     Compute Gerber covariance Statistics 2 :cite:`d-Gerber2021`.      Param, r"""     Compute Gerber covariance Statistics 0 or original Gerber statistics

### Community 12 - "Community 12"
Cohesion: 0.40
Nodes (3): r"""         This method that calculates the optimal portfolio according to the, r"""         Method that calculates the minimum risk and maximum return portfoli, r"""         Method that calculates several portfolios in the efficient frontier

### Community 13 - "Community 13"
Cohesion: 0.40
Nodes (4): excel_report(), jupyter_report(), r"""     Create an Excel report (with formulas) with useful information to analy, r"""     Create a matplotlib report with useful information to analyze risk and

### Community 14 - "Community 14"
Cohesion: 1.00
Nodes (1): r"""         Calculate the inputs that will be used by the optimization method w

### Community 15 - "Community 15"
Cohesion: 1.00
Nodes (1): r"""         Calculate the inputs that will be used by the optimization method w

### Community 16 - "Community 16"
Cohesion: 1.00
Nodes (1): r"""         Calculate the inputs that will be used by the optimization method w

### Community 17 - "Community 17"
Cohesion: 1.00
Nodes (1): r"""         Estimate the optimal scenario weights and comoments parameters usin

### Community 18 - "Community 18"
Cohesion: 1.00
Nodes (1): r"""         Calculate the inputs that will be used by the optimization method w

### Community 19 - "Community 19"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the risk parity portfolio using the ris

### Community 20 - "Community 20"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the MVSK portfolio using a semidefinite

### Community 21 - "Community 21"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the owa optimal portfolio according to

### Community 22 - "Community 22"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the risk parity portfolio using the ris

### Community 23 - "Community 23"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the relaxed risk parity portfolio accor

### Community 24 - "Community 24"
Cohesion: 1.00
Nodes (1): r"""         This method that calculates the worst case mean variance portfolio

### Community 25 - "Community 25"
Cohesion: 1.00
Nodes (1): r"""         Calculate the inputs that will be used by the wc_optimization metho

## Knowledge Gaps
- **180 isolated node(s):** `r"""     Calculate duplication matrix of size "n" as shown in :cite:`d-Magnus198`, `r"""     Calculate duplication elimination matrix of size "n" as shown in :cite:`, `r"""     Calculate duplication summation matrix of size "n" as shown in :cite:`d`, `r"""     Calculate commutation matrix of size T x n.      Parameters     -------`, `r"""     Calculates covariance matrix as shown in :cite:`d-Cajas4` and with prob` (+175 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (2 nodes): `Portfolio`, `r"""     Class that creates a portfolio object with all properties needed to`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `r"""         Calculate the inputs that will be used by the optimization method w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `r"""         Calculate the inputs that will be used by the optimization method w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `r"""         Calculate the inputs that will be used by the optimization method w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `r"""         Estimate the optimal scenario weights and comoments parameters usin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `r"""         Calculate the inputs that will be used by the optimization method w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `r"""         This method that calculates the risk parity portfolio using the ris`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `r"""         This method that calculates the MVSK portfolio using a semidefinite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `r"""         This method that calculates the owa optimal portfolio according to`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `r"""         This method that calculates the risk parity portfolio using the ris`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `r"""         This method that calculates the relaxed risk parity portfolio accor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `r"""         This method that calculates the worst case mean variance portfolio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `r"""         Calculate the inputs that will be used by the wc_optimization metho`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Portfolio` connect `Community 5` to `Community 9`, `Community 14`, `Community 15`, `Community 16`, `Community 12`, `Community 17`, `Community 18`, `Community 19`, `Community 20`, `Community 21`, `Community 10`, `Community 22`, `Community 23`, `Community 24`, `Community 25`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **What connects `r"""     Calculate duplication matrix of size "n" as shown in :cite:`d-Magnus198`, `r"""     Calculate duplication elimination matrix of size "n" as shown in :cite:`, `r"""     Calculate duplication summation matrix of size "n" as shown in :cite:`d` to the rest of the system?**
  _180 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.050817160367722165 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05079825834542816 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.05405405405405406 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.06451612903225806 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.07526881720430108 - nodes in this community are weakly interconnected._