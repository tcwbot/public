# Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Software%20Engineering-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-ML%20%7C%20Agents%20%7C%20Automation-orange?style=for-the-badge" />
</p>

<p align="center">
  Building practical systems across machine learning, agentic frameworks, automation tooling, and data-focused software engineering.
</p>

---

## Quick Navigation
- [Skills & Tools](#skills--tools)
- [Featured Project](#featured-project)
- [Projects & Contributions](#projects--contributions)
- [Machine Learning Experiments](#machine-learning-experiments)
- [Data Visualization](#data-visualization)
- [Presentations & Tutorials](#presentations--tutorials)
- [Logos](#logos)
- [Progress](#progress)
- [Resources](#resources)

> `*` indicates request-access content (not publicly available).

## Skills & Tools

<table>
<tr>
  <td width="25%"><b>Languages</b></td>
  <td>Python, Java, SQL</td>
</tr>
<tr>
  <td><b>Cloud & DevOps</b></td>
  <td>Google Cloud, Microsoft Azure, Docker, Linux, Git, Heroku</td>
</tr>
<tr>
  <td><b>Frameworks & Libraries</b></td>
  <td>Flask, JavaFX, Bootstrap, RabbitMQ</td>
</tr>
<tr>
  <td><b>Technical Domains</b></td>
  <td>Machine Learning, OCR (Tesseract), Robot Simulation (Webots), Database Design</td>
</tr>
</table>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Tesseract-OCR-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Webots-Robot_Simulator-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

## Featured Project

### Near-Earth Object ML Recommender
Automated threat detection and tracking for near-Earth asteroids.

**Abstract:** This project analyzes and tracks near-Earth asteroids during close approaches to Earth. It applies SVM and K-fold machine learning methods on a large, evolving dataset, and produces recommendations using correlation-matrix-based weight indexing. Existing approaches often depend on manual domain expertise, require time-consuming review, and are not always adaptive as data volume grows. This work addresses that gap by helping astronomers, astrophysicists, and researchers focus on the objects that merit deeper investigation.

<table>
<tr>
  <td width="50%" valign="top">
    <b>Project Snapshot</b>
    <ul>
      <li><b>Objective:</b> Replace manual expert labeling with adaptive ML recommendations.</li>
      <li><b>Methodology:</b> SVM + K-fold validation + correlation-based weighting.</li>
      <li><b>Model:</b> MySQL + RabbitMQ (job runner)</li>
      <li><b>View:</b> Bootstrap</li>
      <li><b>Controller:</b> Flask</li>
      <li><b>CI/CD:</b> Heroku</li>
    </ul>
  </td>
  <td width="50%" valign="top">
    <img src="https://github.com/tcwbot/public/blob/main/images/neor-data.png" width="210"/><br/>
    <img src="https://github.com/tcwbot/public/blob/main/images/neor-jobrunner.png" width="210"/><br/>
    <img src="https://github.com/tcwbot/public/blob/main/images/system-diagram.png" width="210"/>
  </td>
</tr>
</table>

## Projects & Contributions

### AI & Agentic Systems
- [Simple LLM Agent](https://github.com/tcwbot/simpleagent): Lightweight local AI agent powered by Ollama using a ReAct loop for web and filesystem actions.
- [AgenticOS](https://github.com/tcwbot/agenticos): Governed Python-first agent framework for safe recursive self-improvement with strict verification gates.
- [ProbCR](https://github.com/aaronbrick/probcr): OCR enhancement work using corpus linguistics and probabilistic scoring to improve Tesseract output. Academic collaboration under Prof. Aaron Brick.

<p align="left">
  <img src="https://github.com/tcwbot/simpleagent/blob/main/docs/images/tui-screenshot.png" width="640"/>
</p>

### Utilities & Frameworks
- RetroConvert: JavaFX visualization framework for converting high-bit graphics into editable pixel-grid renders.
- [logger4py](https://github.com/tcwbot/logger4): Security-conscious Python logging framework inspired by Log4Shell lessons.
- [create_flask_app](https://github.com/tcwbot/public/tree/main/scripts/create_flask_app): CLI scaffolder for bootstrapping Flask applications with consistent structure.
- [Scripts & Utilities](https://github.com/tcwbot/public/tree/main/scripts): Practical automation scripts and CLI tools.
- [Web Scraper](https://github.com/tcwbot/public/tree/main/scripts/python231): Multi-threaded scraper for CCSF certifications.
- [CIDR Calculator](https://github.com/tcwbot/public/blob/main/scripts/cidr.py): Flask-based subnet calculator.
- [interrupt_driven](https://github.com/tcwbot/public/tree/main/scripts/interrupt_driven): Kanban-style priority manager inspired by interrupt-driven scheduling.

## Machine Learning Experiments

### Generative Adversarial Networks (GANs)
Exploration of GAN structure and training using PyTorch and NumPy.

<img src="https://github.com/tcwbot/public/blob/main/images/gan-model.png" width="360"/>

### Perceptron Study
Early experiments in binary classification and perceptron learning.

<table>
<tr>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/simple_classification_01.png" width="180"/></td>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/simple_classification_02.png" width="180"/></td>
</tr>
</table>

## Data Visualization
<table>
<tr>
  <td><img src="https://github.com/tcwbot/public/blob/main/images/visual-analysis1.png" width="240"/></td>
  <td><img src="https://github.com/tcwbot/public/blob/main/images/visual-analysis2.png" width="240"/></td>
</tr>
</table>

## Presentations & Tutorials
Items marked with `*` require access approval.

### Research & Analytics
- [Supervised Learning for Marketing Analytics - Presentation](https://www.youtube.com/watch?v=7WtoGeQmB0w) *
- [Relational Database Design - Presentation](https://www.youtube.com/watch?v=QxE2QbB2YTM) *
- [Data Science as a Field - Presentation](https://www.youtube.com/watch?v=uiD9XutppVQ) *
- [Deep Learning - GANs Introduction](https://www.youtube.com/watch?v=8LWD8VtZRe0) *
- [Robotics (Odometry, Lidar, and Line Following)](https://www.youtube.com/watch?v=V10tFtglBeQ)

### Technical Tutorials
- [CS 231 - VIM and Command Line Tutorial](https://www.youtube.com/watch?v=RCx34TPTjsg)
- [CS 231 - VIM and TAB Tutorial](https://www.youtube.com/watch?v=PhcTrkfMIS4)

## Logos
<table>
<tr>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/logo_01.png" height="100"/></td>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/logo_02.png" height="100"/></td>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/logo_03.png" height="75"/></td>
</tr>
<tr>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/sag_logo.jpg" height="75"/></td>
  <td><img src="https://raw.githubusercontent.com/tcwbot/public/main/images/ibm_logo.jpg" height="75"/></td>
</tr>
</table>

## Progress
[Accolades](https://github.com/tcwbot/public/blob/main/accolades.md)

## Resources
- [An Introduction to Statistical Learning](https://www.statlearning.com/)
- [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)
- [Probability!](https://bookdown.org/probability/beta/)
