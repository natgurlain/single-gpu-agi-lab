# Paper Implementation Card

Paper: On the Measure of Intelligence

URL: https://arxiv.org/abs/1911.01547

Category: AGI measurement, ARC foundations, benchmark design.

Core mechanism: Define intelligence as skill-acquisition efficiency rather than task-specific skill.

Why it matters for model building: It discourages measuring systems only by final-task performance
when that performance may come from unlimited priors, training data, or benchmark overfitting. It
pushes this lab toward experiments that track adaptation, generalization difficulty, experience,
baselines, and reproducibility.

Why it matters for ARC / skill acquisition: The paper is the conceptual foundation for ARC. For this
lab, its main translation is: ARC-AGI-3 agents should be judged by how efficiently they acquire new
skills in novel environments, not by memorized public-game behavior.

Implementation level: L4, read-only/theory. No code implementation is required for this paper in
Milestone 0.

Minimal implementation: Write the lab thesis, ARC-AGI-3 constraints summary, and transfer table.

Dataset / environment: ARC and ARC-AGI-3 as benchmark families.

Baseline: Human first-time adaptation is the conceptual baseline; future ARC-AGI-3 runs should also
compare against random, action-cycling, and novelty-seeking agents.

Metric: For Milestone 0, the metric is documentary acceptance: thesis exists, ARC scoring summary
exists, and static-to-interactive transfer table exists. For later ARC work, use completion, actions,
RHAE/scorecard score, unique states, no-op rate, and replay-based failure analysis.

Expected failure: The lab may drift into either leaderboard hacking or disconnected paper tourism.

Kill criterion: If an idea from this paper cannot be converted into a measurement, benchmark
discipline, or ARC agent design requirement, keep it as background philosophy rather than active
implementation work.

Integration target: `docs/lab-thesis.md`, ARC run metrics, replay analysis, and future evaluation
gates.

Public artifact: Milestone 0 notes in the repo; later, a short public thread or blog post about the
lab thesis and ARC-AGI-3 measurement target.

Decision: integrate as the lab's measurement compass; no standalone implementation.

