# Architecture - AI Pipeline Log Summarizer

## Flow

1. Data pipeline fails in tools like Databricks, ADF, Airflow, or AWS Glue.
2. Raw error logs and job metadata are collected.
3. The log parser extracts important details such as error message, failed task, timestamp, and source system.
4. A prompt builder creates structured context for the LLM.
5. The AI summarizer generates:
   - failure summary
   - likely root cause
   - business impact
   - recommended actions
   - severity
6. The final summary can be shared with Data Engineering, DevOps, or incident teams.

## High-Level Architecture

```text
Pipeline Failure
      |
      v
Raw Logs / Job Metadata
      |
      v
Log Parser
      |
      v
Prompt Builder
      |
      v
LLM Summarizer
      |
      v
Structured Incident Summary
      |
      v
Engineer / Jira / Teams / Slack
