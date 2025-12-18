# Coherence Paradigm – Double Slit Simulation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17011674.svg)](https://doi.org/10.5281/zenodo.17011674)



This repository explores the **double slit experiment** through the lens of a new **Coherence Paradigm**, where coherence is treated as the fundamental driver of physical phenomena.  

Instead of framing the double slit as a paradox of "wave vs particle," we treat **visibility of the interference fringes** as a direct measure of **system coherence**.  
This reframes the double slit not as a mystery, but as the *acid test* of coherence as a physical principle.

---

## 🌌 Key Ideas

- **Fringe contrast = coherence.**  
  Visibility of the interference pattern depends on the degree of coherence between the two paths.

- **Unification of photons & electrons.**  
  The same coherence-based visibility law applies to both photons and electrons, with wavelength given by  
  $$\[
  \lambda = \frac{h}{p}
  \]$$

- **Environment as decoherence channel.**  
  Which-path probes, thermal noise, or finite source size reduce fringe contrast exactly as predicted by a coherence parameter $$\( \gamma_{12} \)$$.

- **Paradigm shift.**  
  Matter is not sometimes “wave” and sometimes “particle” — instead, it always carries a coherence state, and visibility follows directly from that.

---

## 📂 Repository Structure

├── sim/
│ ├── sim_double_slit.py # Core simulation functions
│ ├── interactive_double_slit.ipynb # Jupyter notebook with sliders
├── results/
│ └── example_plots.png # Sample output plots
├── README.md # This file

---

## 🚀 Quickstart

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/coherence-double-slit.git
   cd coherence-double-slit
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Run a quick simulation:
   ```bash
   python sim/sim_double_slit.py
This will generate a sample double slit interference plot with given parameters.

📊 Interactive Notebook

To explore the experiment dynamically:

1. Launch Jupyter:
   ```bash
   jupyter lab
2. Open
   ```bash
   sim/interactive_double_slit.ipynb
3. Use sliders to vary
- **Electron energy** (\(eV\))  
- **Slit separation** (\(d\))  
- **Slit width** (\(a\))  
- **Coherence length** (\(L_c\))  

# 📖 Theory

The intensity at the screen is modeled as:

$$
I(\theta) \propto |A_1(\theta)|^2 + |A_2(\theta)|^2 + 2 \, \text{Re} \{ \gamma_{12} A_1(\theta) A_2^*(\theta) \}
$$

where:  

- $$\(A_1, A_2\)$$ are the amplitudes from slit 1 and slit 2.  
- $$\(\gamma_{12}\)$$ is the coherence factor $$(\(|\gamma| \le 1\))$$.

**Special cases:**

- If $$\(\gamma_{12} = 1\)$$ → perfect coherence, full interference pattern.  
- If $$\(\gamma_{12} = 0\)$$ → full decoherence, no fringes.

> This is the core visibility law — independent of whether the experiment uses photons or electrons.
🔭 Future Directions

Extend to multi-slit (N-slit interference with coherence matrix formalism).

Add decoherence models (thermal coupling, weak measurements).

Compare to experimental datasets.

Explore implications for coherence as a fundamental physical force.

✨ License

MIT License — free to use, adapt, and extend.



📬 Contributions

Pull requests, issues, and discussions are welcome.
This is an open-ended research project — feel free to build on it.
