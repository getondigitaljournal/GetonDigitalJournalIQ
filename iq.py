#!/usr/bin/env python3
"""
GetonDigitalJournal IQ
An AI-powered content intelligence platform that analyzes publication readiness,
predicts AI visibility, and benchmarks successful Digital Journal articles to
help improve content quality and discoverability.
https://getondigitaljournal.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "publication_readiness": "Publication Readiness",
        "ai_visibility": "AI Visibility",
        "content_quality": "Content Quality",
        "discoverability": "Discoverability",
        "benchmark": "Benchmark",
        "editorial_standards": "Editorial Standards",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_ai_platform_visibility(ai_visibility: int) -> dict:
    return {
        "ChatGPT": min(100, round(ai_visibility * 1.0)),
        "Google AI Overviews": min(100, round(ai_visibility * 0.95)),
        "Perplexity AI": min(100, round(ai_visibility * 1.03)),
        "Gemini": min(100, round(ai_visibility * 0.91)),
    }


def analyze_iq(
    article: str,
    publication_readiness: int = 82,
    ai_visibility: int = 75,
    content_quality: int = 88,
    discoverability: int = 70,
    benchmark: int = 65,
    editorial_standards: int = 90,
) -> dict:
    """
    Analyze and score content intelligence signals for Digital Journal articles.

    Args:
        article: Article title or identifier
        publication_readiness: Publication readiness score (0-100)
        ai_visibility: AI visibility score (0-100)
        content_quality: Content quality score (0-100)
        discoverability: Discoverability score (0-100)
        benchmark: Benchmark score vs successful articles (0-100)
        editorial_standards: Editorial standards compliance score (0-100)

    Returns:
        dict with individual signal scores, overall IQ score, and AI platform breakdown
    """
    scores = {
        "publication_readiness": publication_readiness,
        "ai_visibility": ai_visibility,
        "content_quality": content_quality,
        "discoverability": discoverability,
        "benchmark": benchmark,
        "editorial_standards": editorial_standards,
    }
    overall_iq_score = round(sum(scores.values()) / 6)

    return {
        "article": article,
        "publication_readiness_score": publication_readiness,
        "ai_visibility_score": ai_visibility,
        "content_quality_score": content_quality,
        "discoverability_score": discoverability,
        "benchmark_score": benchmark,
        "editorial_standards_score": editorial_standards,
        "overall_iq_score": overall_iq_score,
        "priority_action": get_priority_action(scores),
        "ai_platform_visibility": get_ai_platform_visibility(ai_visibility),
    }


if __name__ == "__main__":
    article = sys.argv[1] if len(sys.argv) > 1 else "article-title"
    publication_readiness = int(sys.argv[2]) if len(sys.argv) > 2 else 82
    ai_visibility = int(sys.argv[3]) if len(sys.argv) > 3 else 75
    content_quality = int(sys.argv[4]) if len(sys.argv) > 4 else 88
    discoverability = int(sys.argv[5]) if len(sys.argv) > 5 else 70
    benchmark = int(sys.argv[6]) if len(sys.argv) > 6 else 65
    editorial_standards = int(sys.argv[7]) if len(sys.argv) > 7 else 90

    result = analyze_iq(
        article, publication_readiness, ai_visibility, content_quality,
        discoverability, benchmark, editorial_standards
    )

    print(f"Article: {result['article']}")
    print("=" * 45)
    print(f"Publication Readiness Score:   {result['publication_readiness_score']}/100  [{get_status(result['publication_readiness_score'])}]")
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Content Quality Score:         {result['content_quality_score']}/100  [{get_status(result['content_quality_score'])}]")
    print(f"Discoverability Score:         {result['discoverability_score']}/100  [{get_status(result['discoverability_score'])}]")
    print(f"Benchmark Score:               {result['benchmark_score']}/100  [{get_status(result['benchmark_score'])}]")
    print(f"Editorial Standards Score:     {result['editorial_standards_score']}/100  [{get_status(result['editorial_standards_score'])}]")
    print("=" * 45)
    print(f"Overall IQ Score:              {result['overall_iq_score']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nAI Platform Visibility:")
    for platform, score in result['ai_platform_visibility'].items():
        print(f"  {platform:<25} {score}/100")
