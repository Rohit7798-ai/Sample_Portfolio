# Interactive Doors Portfolio 🚪✨

A modern, responsive, high-performance portfolio website inspired by experiential creative development. Built with vanilla HTML5, CSS3, modern JavaScript, and Lenis smooth scrolling.

Features an interactive **"Magic happens behind the doors"** gallery where each door dynamically cracks open on hover, swings into perspective on click, and zooms the user seamlessly through the doorway into dedicated sub-galleries.

---

## 🌟 Key Features

- **3D Interactive Doors Gallery**:
  - Physics-based door swing perspective on hover and focus.
  - Seamless zoom-through transition directly into embedded project suites with instant exit animations ("Back to the doors").
  - Mobile swipe gestures with snap-to-door alignment and responsive viewport fitting.
- **Dedicated Project Showcase Rooms**:
  - **Web Development**: Interactive device preview cards with live scrolling simulations and video showcase previews.
  - **App Development**: iOS native mockups, custom interactions, and app previews.
  - **UI/UX Design**: Wireframes, design systems, and case studies.
  - **Graphic Design**: Horizontal brand galleries, posters, print creatives, and lightboxes.
  - **Photography**: Responsive photo walls and full-bleed image viewing.
- **Polished Micro-Interactions**:
  - Pull-cord dark/light theme switch with persistent preference.
  - Multi-step interactive client inquiry modal.
  - Momentum smooth scrolling powered by Lenis with automatic anchor offsets.
- **Zero Heavy Framework Overheads**:
  - Ultra-fast first contentful paint (FCP) and 60fps animations.
  - Zero framework dependencies; pure HTML5, CSS, and ES modules.

---

## 🚀 Quick Start (Local Development)

### Option 1: Python (Built-in Server)
```bash
python serve.py 8080
```
Then open [http://localhost:8080](http://localhost:8080) in your browser.

### Option 2: Node.js / NPX
```bash
npx serve .
```

---

## 📁 Repository Structure

```text
portfolio-website/
├── index.html            # Main home page with hero, interactive doors, story, & contact modal
├── serve.py              # Zero-dependency local dev server with correct MIME & route handling
├── package.json          # Node scripts for local serving
├── .gitignore            # Clean git configuration
├── web-developer/        # Web Development project suite
├── app-developer/        # App Development project suite
├── ui-ux-designer/       # UI/UX Design project suite
├── graphic-designer/     # Graphic Design & branding project suite
├── photographer/         # Photography gallery suite
├── legal/                # Privacy & legal terms
├── fonts/                # Custom Onest variable font files (.woff2)
├── card/                 # Project showcase screenshots & poster assets
├── ability-card/         # Ability icon assets
└── vendor/               # Bundled Lenis smooth-scroll library
```

---

## 🚢 Deployment

### GitHub Pages
1. Push this repository to GitHub.
2. In your repository settings, navigate to **Pages**.
3. Under **Build and deployment**, select **Source: Deploy from a branch** and choose the `main` branch (root `/`).
4. Save — your website will be live at `https://<username>.github.io/<repo-name>/`.

### Vercel / Netlify
- Simply import your GitHub repository into [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/).
- No build command is needed; output directory is root `/`.

---

## 📄 License
MIT License.
