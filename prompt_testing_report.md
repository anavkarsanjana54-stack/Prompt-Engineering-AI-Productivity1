# Prompt Testing Report

## Objective
Check whether reusable prompts produce outputs that are relevant, clear, correctly formatted and safe to use.

## Test cases

| Test | Input/task | Expected result | Status |
|---|---|---|---|
| T1 | Ask for a beginner explanation using a zero-shot prompt | Simple explanation, requested structure | Pass – template checked |
| T2 | Provide examples before a new classification request | Same label style as examples | Pass – demonstration checked |
| T3 | Ask for JSON with fixed keys | Valid JSON; missing values represented as null | Pass – Python JSON output validated |
| T4 | Summarize supplied text only | No unsupported extra facts | Review required for any real AI output |
| T5 | Ask AI to debug code | Explanation, corrected code and test | Manual verification required |
| T6 | Ask for an email draft | Polite, concise draft with no invented details | Manual review required |

## Evaluation criteria
Score each criterion from 1 (poor) to 5 (excellent):
1. Relevance – answers the requested task.
2. Clarity – easy to understand.
3. Format – follows the requested output format.
4. Completeness – includes all required information.
5. Reliability – avoids unsupported facts and flags uncertainty.

## Example evaluation
A prompt that asks for a JSON object with three named keys can be tested by parsing the result with Python's `json.loads()`. If parsing fails or a key is missing, the test fails.

## Findings
- Clear roles, context, tasks, formats and constraints make prompts easier to evaluate.
- Few-shot examples help demonstrate the expected response pattern.
- Structured output should be validated programmatically.
- AI-generated code and factual claims must be checked by a person.
- Reusable templates save time and improve consistency.

## Conclusion
The toolkit meets the learning objectives as a beginner demonstration. The sample functions are not a substitute for a live AI model. Real model outputs should be tested with the same checklist before practical use.
