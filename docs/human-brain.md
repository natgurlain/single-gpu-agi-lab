## Executive conclusion

A **multilayer perceptron is not a valid biological representation of a neuron** if by “neuron” you mean an actual cortical cell. It is a useful mathematical abstraction: weighted inputs, nonlinear output, trainable connection strengths. But a biological neuron is closer to a **small, dynamic, chemically modulated, spiking, compartmental computer** than to a dot product plus activation function. In fact, work on cortical pyramidal neurons suggests that a single biological neuron’s input-output behavior can require a deep network-like approximation, partly because dendrites perform nonlinear computations before the soma ever “decides” to spike. ([PubMed][1])

The bigger lesson for building an artificial mind is this: **human-like fast learning probably will not come from copying only the neuron.** It will come from copying the *stack*: structured priors, embodiment, active exploration, predictive world models, episodic memory, replay, compositional reasoning, neuromodulated learning, local plasticity, sparsity, recurrent control, and social/instruction learning. The neuron matters, but the architecture and learning ecology matter more.

---

# 1. What the human brain is, in hard data

The adult human brain contains about **86 billion neurons** and roughly a similar number of non-neuronal cells, including glia. That old “100 billion neurons and 10× more glia” story is not the best current estimate. ([PubMed][2])

The complexity is not just the number of neurons. A 2024 nanoscale reconstruction of roughly **1 cubic millimeter of human temporal cortex** contained about **57,000 cells, 230 mm of blood vessels, 150 million synapses, and 1.4 petabytes of data**. That is a tiny brain fragment, smaller than a grain of rice. ([science.org][3])

Recent connectomics is starting to combine structure and function. The 2025 MICrONS mouse visual cortex dataset paired activity from around **75,000 neurons** with electron-microscopy reconstruction containing **more than 200,000 cells and 0.5 billion synapses**. This matters because a static wiring diagram alone is not enough; you need to know what the cells do while the animal sees and acts. ([Nature][4])

Cell identity is also far richer than “neuron vs. glia.” A 2024 Brain Cell Atlas integrated single-cell data from **70 human studies** and **103 mouse studies**, including **11.3 million human cells or nuclei** across major brain regions. This reinforces an important point for AI: the brain is not one uniform neural network. It is a heterogeneous system of many cell types, circuits, chemicals, and learning regimes. ([Nature][5])

And the brain does this on an absurdly low energy budget. The human brain runs around the scale of **20 watts**, while supporting perception, action, memory, planning, language, imagination, emotion, and self-maintenance. ([PMC][6])

---

# 2. A useful model of “how the mind works”

The mind is not located in one place. It is not a little commander inside the skull. A better working model is:

> The mind is an embodied, recurrent control system that builds predictive models of the world and body, uses memory to simulate possible futures, assigns value through needs and goals, and selects actions that reduce uncertainty or improve expected outcomes.

Different sciences describe different layers of this system. David Marr’s classic framing is still useful: understand cognition at the **computational level** — what problem is being solved; the **algorithmic level** — what representation and procedure solve it; and the **implementation level** — how neurons, synapses, glia, oscillations, and chemicals physically implement it. ([sites.socsci.uci.edu][7])

A modern synthesis looks like this:

| Layer            | Biological version                                     | AI lesson                                                                                 |
| ---------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Body/homeostasis | hunger, pain, arousal, hormones, interoception         | an artificial mind needs drives, priorities, and state variables, not just loss functions |
| Perception       | hierarchical recurrent sensory systems                 | perception is active inference, not passive labeling                                      |
| Memory           | hippocampal episodic memory + cortical semantic memory | separate fast memory from slow abstraction                                                |
| Value/action     | basal ganglia, dopamine, reward, habit, planning       | combine model-based and model-free reinforcement learning                                 |
| Control          | prefrontal cortex, working memory, attention           | build a controller that allocates computation and selects goals                           |
| Social/language  | instruction, imitation, culture                        | fast human learning is often socially transmitted                                         |
| Conscious access | global broadcasting / recurrent integration theories   | build a workspace where selected information becomes globally usable                      |

No single theory fully explains mind or consciousness. Predictive coding and active inference are promising frameworks, but a 2024 review judged the evidence for predictive coding as “modest” and argued that active inference still needs stronger empirical validation against alternatives. That is important: these ideas are useful, but they are not finished science. ([ScienceDirect][8])

For consciousness specifically, global neuronal workspace theory, integrated information theory, recurrent processing, and predictive-processing views are all active contenders. A 2025 adversarial collaboration directly tested global neuronal workspace theory against integrated information theory, which shows the field is moving from philosophy-heavy debate toward sharper empirical comparison. ([Nature][9])

---

# 3. How neurons compute

The simplified textbook neuron says: dendrites receive input, soma integrates it, axon sends a spike, synapse passes signal onward. That is true, but too simple.

A biological neuron has:

* **Dendrites** that can perform local nonlinear computations.
* **Synapses** with different receptor types, time constants, strengths, and plasticity rules.
* **Ion channels** that make the cell dynamic, excitable, and history-dependent.
* **Spikes** that encode timing, synchrony, bursts, and rate.
* **Neuromodulatory state** that changes whether the same input is ignored, learned, or acted on.
* **Morphology** that determines which inputs interact with which other inputs.
* **Glial interactions** that regulate neurotransmitter clearance, plasticity, metabolism, and pruning.

This is why the artificial neuron in an MLP is only a very rough abstraction.

The strongest reason is dendrites. A 2025 Nature Communications paper argues that current artificial neuron design is outdated relative to what is known about dendritic computation, and showed that dendrite-inspired artificial networks could match or outperform traditional ANNs on image classification while using fewer trainable parameters and reducing overfitting. ([Nature][10])

A biological pyramidal neuron is not merely “one node.” It has something like internal subunits. A more biologically inspired artificial neuron might look like this:

```
$y = f_\text{soma}\left(\sum_j c_j \cdot f_{\text{dendrite},j}\left(\sum_i w_{ij}x_i + b_j\right)\right)$
```

That is already closer to a tiny multilayer network inside each neuron: synapses feed dendritic compartments, dendrites compute nonlinear sub-results, and the soma integrates those sub-results into spiking output.

---

# 4. How neurons connect, and why

Neurons connect for two broad reasons:

First, **development builds rough circuit structure**. Genetic programs, chemical gradients, axon guidance cues, cell adhesion molecules, and molecular recognition systems help axons find broad target regions and form specific classes of synapses. The function of the brain depends on highly specific connection patterns between neuronal populations, and synaptic specificity arises from coordinated molecular signals during development. ([PMC][11])

Second, **activity refines the circuit**. The brain overproduces some connections, then stabilizes useful ones and eliminates weaker or poorly correlated ones. Activity-dependent synapse refinement includes elimination of inactive synapses and stabilization of active ones. ([PMC][12])

Learning then modifies this structure at multiple timescales:

| Timescale       | Mechanism                                 | AI analogue                                             |
| --------------- | ----------------------------------------- | ------------------------------------------------------- |
| milliseconds    | spikes, inhibition, oscillations          | dynamic routing, attention, recurrent state             |
| seconds-minutes | eligibility traces, short-term plasticity | temporary memory, context adaptation                    |
| minutes-hours   | synaptic strengthening/weakening          | online learning                                         |
| hours-days      | replay, consolidation, sleep              | offline distillation, replay buffers                    |
| months-years    | pruning, myelination, structural changes  | architecture search, parameter freezing, modularization |

The classic Hebbian idea is “cells that fire together wire together,” but real learning is more nuanced. A 2023 Nature Neuroscience paper showed that combining Hebbian plasticity with predictive plasticity can produce invariant representations in deep sensory-network models and can account for observed properties such as metaplasticity and spike-timing-dependent plasticity. ([Nature][13])

Glia also matter. Astrocytes are increasingly recognized as active regulators of excitability, transmission, axonal conduction, and plasticity, not just passive support cells. Microglia and astrocytes help coordinate neurogenesis, synapse elimination, inflammatory state, and circuit remodeling. ([Frontiers][14])

---

# 5. Why humans learn so quickly

Humans do **not** learn from scratch. This is the key mistake many AI comparisons make.

A child who learns a new word or concept quickly already has:

* millions of years of evolved priors,
* months or years of sensorimotor experience,
* object permanence,
* intuitive physics,
* social attention,
* imitation ability,
* language,
* episodic memory,
* reward and curiosity systems,
* rich multimodal grounding,
* a body that actively samples useful data.

Fast human learning is usually **fast adaptation on top of massive prior structure**.

This is why few-shot and one-shot learning are not magic. Humans can learn quickly because they compress the new thing into an existing world model. In AI terms, the human brain is doing something like meta-learning, retrieval, compositional recombination, and active inference all at once.

Compositionality is central. Humans can learn “jump,” “twice,” and “around the cone,” then combine them immediately. A 2023 Nature paper showed that neural networks can achieve more human-like systematic generalization when trained through meta-learning for compositionality, suggesting that the missing ingredient is not necessarily symbolic machinery alone, but the right training regime and inductive bias. ([Nature][15])

Memory replay is another key. Hippocampal replay is widely studied as a candidate mechanism for consolidation, especially during sleep, and newer work also emphasizes awake replay for decision-making and planning. ([PMC][16])

Dopamine is also important, but not in the simplistic “pleasure chemical” way. The influential view is that phasic dopamine reports reward prediction errors, but current work argues that this is too simple and that dopamine also relates to sensory/motor features, action selection, ramping toward goals, and more general prediction-error-like functions. 

---

# 6. What this means for creating an artificial mind

To build an artificial mind that learns closer to human speed, I would not start with “make a bigger MLP.” I would build a **multi-system architecture**.

A plausible blueprint:

| Brain-inspired component   | Artificial implementation                                                   |
| -------------------------- | --------------------------------------------------------------------------- |
| Sensory cortex             | multimodal self-supervised encoder                                          |
| Hippocampus                | fast episodic key-value memory with pattern completion                      |
| Neocortex                  | slow world model trained by prediction and abstraction                      |
| Prefrontal cortex          | recurrent planning and working-memory controller                            |
| Basal ganglia              | action selection, gating, habit learning, reinforcement learning            |
| Dopamine / neuromodulators | global signals for surprise, reward, uncertainty, novelty, arousal          |
| Dendrites                  | compartmental units, sparse conditional computation, context-gated subunits |
| Sleep/replay               | offline consolidation, generative replay, memory compression                |
| Social learning            | instruction following, imitation, language-grounded learning                |
| Body/interoception         | internal state, needs, drives, energy, risk, survival variables             |

The artificial system should learn through at least four loops:

1. **Self-supervised prediction**: predict next sensory state, missing modalities, action consequences, and hidden causes.
2. **Episodic one-shot storage**: store important events immediately without overwriting old knowledge.
3. **Replay and consolidation**: replay selected memories to train slower general models.
4. **Active exploration**: choose actions that reduce uncertainty or improve expected value.

This matters because most current neural networks are still trained too passively. They consume huge datasets, optimize a global loss, and then largely freeze. Humans constantly choose what to observe, what to ask, what to rehearse, and what to ignore.

---

# 7. Is an MLP a valid representation of a neuron?

## The direct answer

**A single MLP unit is a crude abstraction of one aspect of a neuron, not a faithful representation of a biological neuron.**

It captures:

| MLP neuron captures  | Biological analogue               |
| -------------------- | --------------------------------- |
| weighted inputs      | synaptic strengths                |
| summation            | some somatic integration          |
| nonlinear activation | threshold-like firing behavior    |
| trainable weights    | synaptic plasticity, very roughly |
| distributed networks | population-level representation   |

But it misses:

| MLP neuron misses       | Why it matters                                                                  |
| ----------------------- | ------------------------------------------------------------------------------- |
| spikes and timing       | brains compute with temporal structure, synchrony, bursts, delays               |
| dendritic compartments  | dendrites do local nonlinear computation                                        |
| local learning rules    | biology does not use ordinary global backprop in the obvious MLP way            |
| neuromodulation         | dopamine, acetylcholine, serotonin, noradrenaline change learning and attention |
| inhibitory interneurons | inhibition shapes timing, gain, competition, stability                          |
| recurrence              | cortex is massively recurrent, not simple feedforward layers                    |
| structural plasticity   | brains grow, prune, and rewire connections                                      |
| glia                    | astrocytes and microglia regulate synapses and learning                         |
| cell-type diversity     | “neuron” is not one uniform component                                           |
| embodiment              | biological learning is tied to action, body state, and survival                 |

So the MLP neuron is useful the way a stick-figure is useful for drawing a person: it gives you the rough arrangement, but almost none of the machinery.

A deeper issue is that **MLP layers are not cortical layers**. Cortical layers contain recurrent loops, inhibitory circuits, top-down feedback, neuromodulation, dendritic targeting, and different cell types. A feedforward MLP can model functions, but it should not be mistaken for a literal model of cortical tissue.

---

# 8. What a better artificial neuron might include

A more brain-inspired artificial neuron would include:

1. **Compartmental dendrites**
   Each neuron has several dendritic branches, each with local nonlinear integration.

2. **Sparse connectivity**
   Biological networks are not dense all-to-all matrices. Sparse structured connectivity can improve efficiency and reduce overfitting, as dendrite-inspired ANN work suggests. ([Nature][10])

3. **Spiking or temporal state**
   Not every AI system needs literal spikes, but fast learning and control benefit from time-sensitive state.

4. **Local plasticity plus global modulators**
   Synapses should update from local pre/post activity, gated by reward, novelty, uncertainty, or surprise.

5. **Eligibility traces**
   The system should remember which synapses were recently responsible when delayed feedback arrives.

6. **Structural plasticity**
   Some connections should be created, pruned, consolidated, or frozen over time.

7. **Cell-type specialization**
   Excitatory, inhibitory, memory, gating, prediction-error, and modulatory units should not all be identical.

This does not mean every AI model must become a biophysical simulation. That would be expensive and probably unnecessary. The point is to steal the **computational principles**, not blindly copy every molecule.

---

# 9. The key AI design principles from neuroscience

## 1. Use fast and slow learning together

Humans have fast episodic learning and slower statistical abstraction. AI systems need both. A model that updates everything slowly will not learn like a human. A model that stores everything episodically will not generalize well.

## 2. Separate memory from weights

Human knowledge is not only in synaptic weights. Episodic memory allows immediate storage and later consolidation. Artificial minds need external or internal memory systems that can retrieve, bind, and replay experiences.

## 3. Build world models, not just classifiers

The brain predicts consequences. It does not merely label inputs. A human-like learner should ask: “What will happen if I do this?” not only “What class is this image?”

## 4. Use active learning

Humans gather data intelligently. A child pokes, asks, imitates, repeats, and tests. Passive dataset training wastes enormous samples.

## 5. Use compositionality

Human intelligence is powerful because it recombines parts: objects, relations, actions, words, rules. This is why meta-learning for compositionality is so relevant. ([Nature][15])

## 6. Use neuromodulated learning rates

The brain does not learn everything equally. Surprise, reward, threat, novelty, confidence, fatigue, and social relevance change plasticity. AI systems should dynamically adjust when and where they learn.

## 7. Use replay

Replay is one of the strongest bridges between neuroscience and machine learning. It helps with consolidation, planning, and avoiding catastrophic forgetting.

## 8. Use sparse modularity

The whole brain does not activate uniformly for every task. Sparse modular systems are more energy-efficient, more interpretable, and often better at transfer.

## 9. Include embodiment or at least action-grounding

A disembodied text model can learn language patterns, but much of human intelligence is grounded in perception, movement, pain, effort, time, and social feedback.

## 10. Do not copy biology at the wrong level

A perfect ion-channel simulator is not automatically intelligent. A transformer is not automatically mind-like. The right target is the **algorithmic organization**: prediction, control, memory, attention, action, value, and self-maintenance.

---

# 10. A practical research roadmap

If your goal is an artificial mind that learns closer to human speed, I would pursue this order:

**Stage 1: Build a predictive embodied agent.**
Give it vision, action, proprioceptive-like state, and a self-supervised world model. Train it to predict future states under actions.

**Stage 2: Add hippocampal-style episodic memory.**
The system should store a single event and later retrieve it by partial cue. This is essential for one-shot learning.

**Stage 3: Add replay and consolidation.**
During offline periods, replay important episodes into the slow world model. Use prioritization: surprising, useful, emotionally/goal-relevant, and uncertain events replay more.

**Stage 4: Add neuromodulated plasticity.**
Use local learning rules gated by global signals: reward, prediction error, uncertainty, novelty, arousal.

**Stage 5: Add compositional meta-learning.**
Train across tasks where rules must be inferred from few examples and recombined. This targets human-like systematic generalization.

**Stage 6: Replace point neurons where useful.**
Use dendritic units, sparse mixture-of-experts, local receptive fields, compartmental routing, or spiking units. Do not do this everywhere blindly; benchmark whether it improves sample efficiency, robustness, continual learning, or energy.

**Stage 7: Add cognitive control.**
Create a prefrontal-like controller that decides what to attend to, what to retrieve, what to rehearse, when to explore, and when to exploit.

**Stage 8: Test against human-like benchmarks.**
Do not only test ImageNet or static classification. Test few-shot learning, causal reasoning, compositional generalization, continual learning, active exploration, instruction following, transfer, memory retention, and energy per learned skill.

Neuromorphic computing may become important for efficiency because it uses sparse event-based communication and brain-inspired hardware. Recent reviews argue that gradient-trained spiking networks and neuromorphic applications are becoming more practical, but this is an engineering path, not a guaranteed path to mind by itself. ([Nature][17])

---

# 11. Final answer to your core question

An MLP is **not wrong** as a mathematical tool. It is wrong only when people treat it as a realistic neuron model.

A biological neuron is not:

[
y = f(w \cdot x + b)
]

That is just the simplest abstraction.

A better mental model is:

> A biological neuron is a living, adaptive, spiking, chemically modulated, multi-compartment processor embedded in a recurrent circuit, whose connections are shaped by genetics, activity, body state, reward, prediction, and experience.

For artificial minds, the big opportunity is not to make every artificial neuron biologically realistic. The big opportunity is to import the principles that make biological intelligence so sample-efficient: **structured priors, active learning, fast memory, replay, local plasticity, dendritic computation, recurrence, modularity, embodiment, and social instruction.**

That is where the path toward human-speed learning is most likely to be.

[1]: https://pubmed.ncbi.nlm.nih.gov/34380016/?utm_source=chatgpt.com "Single cortical neurons as deep artificial neural networks"
[2]: https://pubmed.ncbi.nlm.nih.gov/19226510/?utm_source=chatgpt.com "Equal numbers of neuronal and nonneuronal cells make ..."
[3]: https://www.science.org/doi/10.1126/science.adk4858?utm_source=chatgpt.com "A petavoxel fragment of human cerebral cortex ..."
[4]: https://www.nature.com/articles/s41586-025-08790-w "Functional connectomics spanning multiple areas of mouse visual cortex | Nature"
[5]: https://www.nature.com/articles/s41591-024-03150-z "A brain cell atlas integrating single-cell transcriptomes across human brain regions | Nature Medicine"
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8364152/?utm_source=chatgpt.com "Brain power - PMC - NIH"
[7]: https://sites.socsci.uci.edu/~lpearl/courses/readings/Love2015_AlgorithmicLevel.pdf?utm_source=chatgpt.com "The Algorithmic Level Is the Bridge Between Computation ..."
[8]: https://www.sciencedirect.com/science/article/abs/pii/S0149763423004426 "The empirical status of predictive coding and active inference - ScienceDirect"
[9]: https://www.nature.com/articles/s41586-025-08888-1?utm_source=chatgpt.com "Adversarial testing of global neuronal workspace and ..."
[10]: https://www.nature.com/articles/s41467-025-56297-9 "Dendrites endow artificial neural networks with accurate, robust and parameter-efficient learning | Nature Communications"
[11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3327884/?utm_source=chatgpt.com "Molecular Mechanisms of Synaptic Specificity in Developing ..."
[12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11584027/?utm_source=chatgpt.com "Activity-dependent synapse refinement: From mechanisms to ..."
[13]: https://www.nature.com/articles/s41593-023-01460-y "The combination of Hebbian and predictive plasticity learns invariant object representations in deep sensory networks | Nature Neuroscience"
[14]: https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2024.1477985/full?utm_source=chatgpt.com "The role of astrocytes from synaptic to non-synaptic plasticity"
[15]: https://www.nature.com/articles/s41586-023-06668-3 "Human-like systematic generalization through a meta-learning neural network | Nature"
[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12107872/?utm_source=chatgpt.com "Sleep micro-structure organizes memory replay - PMC - NIH"
[17]: https://www.nature.com/articles/s41467-025-57352-1?utm_source=chatgpt.com "The road to commercial success for neuromorphic ..."
