# GetonDigitalJournal IQ 📰🤖

[![npm](https://img.shields.io/npm/v/@getondigitaljournal/iq)](https://npmjs.com/package/@getondigitaljournal/iq)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21401693.svg)](https://doi.org/10.5281/zenodo.21401693)

An AI-powered content intelligence platform that analyzes publication readiness, predicts AI visibility, and benchmarks successful Digital Journal articles to help improve content quality and discoverability. Built by [GetonDigitalJournal.com](https://getondigitaljournal.com).

## Features

- Publication Readiness Score — evaluates content structure, formatting, and editorial standards
- AI Visibility Prediction — estimates likelihood of being cited by ChatGPT, Perplexity, Google AI
- Content Quality Score — measures factual clarity, source authority, and writing depth
- Discoverability Score — evaluates headline strength, keyword density, and SEO alignment
- Benchmark Analysis — compares against successful Digital Journal articles
- Editorial Standards Score — checks compliance with Digital Journal submission guidelines
- CLI support in Node.js and Python
- Benchmark dataset included (20 Digital Journal article cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @getondigitaljournal/iq
npx getondigitaljournal-iq "my-article-title" 82 75 88 70 65 90
```

### Python

```bash
pip install getondigitaljournal-iq
python -m iq "my-article-title" 82 75 88 70 65 90
```

## Output

```
Article: my-article-title
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Publication Readiness Score:   82 / 100  [Healthy]
AI Visibility Score:           75 / 100  [Healthy]
Content Quality Score:         88 / 100  [Excellent]
Discoverability Score:         70 / 100  [Healthy]
Benchmark Score:               65 / 100  [Healthy]
Editorial Standards Score:     90 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall IQ Score:              78 / 100
Priority Action:               Benchmark (lowest — act first)

AI Platform Visibility:
  ChatGPT:              75 / 100
  Google AI Overviews:  71 / 100
  Perplexity AI:        77 / 100
  Gemini:               68 / 100
```

## Project Structure

```
GetonDigitalJournalIQ/
├── index.ts              # TypeScript IQ engine
├── iq.py                 # Python IQ engine
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── digitaljournal_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml     # Auto-commit daily
│   └── npm-publish.yml   # Auto-publish to NPM
├── README.md
└── LICENSE
```

## Content Intelligence Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Publication Readiness | Content structure, formatting, editorial standards | 0–100 |
| AI Visibility | Likelihood of AI platform citation and discovery | 0–100 |
| Content Quality | Factual clarity, source authority, writing depth | 0–100 |
| Discoverability | Headline strength, keywords, SEO alignment | 0–100 |
| Benchmark | Performance vs successful Digital Journal articles | 0–100 |
| Editorial Standards | Compliance with Digital Journal submission guidelines | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Major revision required |
| 31–60 | At Risk | Significant improvements needed |
| 61–80 | Healthy | Minor optimizations recommended |
| 81–100 | Excellent | Ready to publish |

## Keywords

Content Intelligence · Publication Readiness · AI Visibility · Digital Journal · Content Quality · Editorial Standards · Discoverability · AI Citation · BHMarketer

## Links

| Platform | URL |
|----------|-----|
| Website | https://getondigitaljournal.com |
| GitHub | https://github.com/getondigitaljournal/GetonDigitalJournalIQ |
| GitHub Pages | https://getondigitaljournal.github.io/GetonDigitalJournalIQ/ |
| NPM | https://npmjs.com/package/@getondigitaljournal/iq |
| Hugging Face | https://huggingface.co/datasets/getondigitaljournal/digitaljournal-iq-benchmarks |
| Kaggle | https://kaggle.com/datasets/getondigitaljournal/digitaljournal-iq-benchmarks |
| Zenodo | https://zenodo.org/records/21401693 |
| Docs | https://getondigitaljournal-iq.readthedocs.io |

## About GetonDigitalJournal.com

GetonDigitalJournal.com is an AI-powered content intelligence platform helping brands, PR professionals, and publishers analyze publication readiness, predict AI visibility, and benchmark content against successful Digital Journal articles.

## License

MIT — [GetonDigitalJournal.com](https://getondigitaljournal.com)
