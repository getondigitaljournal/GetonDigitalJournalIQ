#!/usr/bin/env node

interface IQInput {
  article: string;
  publicationReadiness: number;
  aiVisibility: number;
  contentQuality: number;
  discoverability: number;
  benchmark: number;
  editorialStandards: number;
}

interface IQOutput {
  article: string;
  publicationReadinessScore: number;
  aiVisibilityScore: number;
  contentQualityScore: number;
  discoverabilityScore: number;
  benchmarkScore: number;
  editorialStandardsScore: number;
  overallIQScore: number;
  priorityAction: string;
  aiPlatformVisibility: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    publicationReadiness: "Publication Readiness",
    aiVisibility: "AI Visibility",
    contentQuality: "Content Quality",
    discoverability: "Discoverability",
    benchmark: "Benchmark",
    editorialStandards: "Editorial Standards",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getAIPlatformVisibility(aiVisibility: number): Record<string, number> {
  return {
    "ChatGPT": Math.min(100, Math.round(aiVisibility * 1.0)),
    "Google AI Overviews": Math.min(100, Math.round(aiVisibility * 0.95)),
    "Perplexity AI": Math.min(100, Math.round(aiVisibility * 1.03)),
    "Gemini": Math.min(100, Math.round(aiVisibility * 0.91)),
  };
}

export function analyzeIQ(input: IQInput): IQOutput {
  const scores = {
    publicationReadiness: input.publicationReadiness,
    aiVisibility: input.aiVisibility,
    contentQuality: input.contentQuality,
    discoverability: input.discoverability,
    benchmark: input.benchmark,
    editorialStandards: input.editorialStandards,
  };
  const overallIQScore = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    article: input.article,
    publicationReadinessScore: input.publicationReadiness,
    aiVisibilityScore: input.aiVisibility,
    contentQualityScore: input.contentQuality,
    discoverabilityScore: input.discoverability,
    benchmarkScore: input.benchmark,
    editorialStandardsScore: input.editorialStandards,
    overallIQScore,
    priorityAction: getPriorityAction(scores),
    aiPlatformVisibility: getAIPlatformVisibility(input.aiVisibility),
  };
}

const args = process.argv.slice(2);
const article = args[0] || "article-title";
const publicationReadiness = parseInt(args[1]) || 82;
const aiVisibility = parseInt(args[2]) || 75;
const contentQuality = parseInt(args[3]) || 88;
const discoverability = parseInt(args[4]) || 70;
const benchmark = parseInt(args[5]) || 65;
const editorialStandards = parseInt(args[6]) || 90;

const result = analyzeIQ({
  article, publicationReadiness, aiVisibility, contentQuality,
  discoverability, benchmark, editorialStandards,
});

console.log(`Article: ${result.article}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Publication Readiness Score:   ${result.publicationReadinessScore}/100  [${getStatus(result.publicationReadinessScore)}]`);
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Content Quality Score:         ${result.contentQualityScore}/100  [${getStatus(result.contentQualityScore)}]`);
console.log(`Discoverability Score:         ${result.discoverabilityScore}/100  [${getStatus(result.discoverabilityScore)}]`);
console.log(`Benchmark Score:               ${result.benchmarkScore}/100  [${getStatus(result.benchmarkScore)}]`);
console.log(`Editorial Standards Score:     ${result.editorialStandardsScore}/100  [${getStatus(result.editorialStandardsScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall IQ Score:              ${result.overallIQScore}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nAI Platform Visibility:");
Object.entries(result.aiPlatformVisibility).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(22)} ${score}/100`);
});
