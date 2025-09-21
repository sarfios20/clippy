# CLIPPY
This is a small learning project in a "back to basics" kind of deal. NO AI.

The objective is to transform from csv to json.

I will be adding new features and improving documentation and code quality.

This is the first stage of the project with a simple working utility but still many things to improve.

## ROADMAP
## Core
- [ ] **Robust CSV parsing:** support for quotes, delimiters, line breaks, Byte Ordere Mark.
- [ ] **Valid JSON:** escaping of special characters.
- [ ] **Header and misaligned rows hgandling:** policies of fails, pad or truncate.
- [ ] **Streaming read/write:** avoid loading the entire file in memory.
- [ ] **Avoid looped string concatenation:** improve performance with better logic.

## Functionality
- [ ] **JSONL/NDJSON support:** alternative to JSON array.
- [ ] **Configurable buffering:** parametrized output chunk size.
- [ ] **Basic flags:** delimiter, quotechar, escapechar, encoding.
- [ ] **STDIN/STDOUT:** allow for use to pipes.
- [ ] **Configurable error handling policy:** skip, warn and fail.
- [ ] **Column typing:** field casting.
- [ ] **Pretty vs compact:** toggle between human-readable and minified output.

## UX
- [ ] **Clear error messages:** inform row number and cause of error.
- [ ] **Stats:** show rows read and written, columns and nulls.
- [ ] **allow verbose and quiet flags:** control loggin levels.
- [ ] **Meaningful exit codes**
- [ ] **Auto delimiter detection**
- [ ] **Path validation:** avoid accidental overwrites.
- [ ] **--help:** show usage and examples.

## Quality
- [ ] **Golden tests:** edge cases like quotes, commas, empty lines, BOM and misaligments.
- [ ] **Performance tests:** for ease of benchmarking.
- [ ] **Layered or modular separation:** less bugs, easier improvements down the line.
- [ ] **Documentation**