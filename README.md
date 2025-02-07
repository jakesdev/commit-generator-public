# 🏜️ Commit Generator

## Why This Exists

Are you tired of having a GitHub profile that looks like a digital tumbleweed collection? This tool helps fill your contribution graph with meaningful activity markers.

## The Problem

```
recruiter_thought_process = {
    "sees_empty_github": "This dev probably just watches Netflix all day",
    "reality": "Been busy shipping features that paid for my Netflix subscription"
}
```

## Quick Setup Guide

1. Create your private repository
   ```bash
   git init commit-generator
   cd commit-generator
   ```

2. Required Files Structure
   ```
   commit-generator/
   ├── range_commit.py    # Handles date range commits
   ├── daily_commit.py    # Entry point for daily execution
   └── daily_log.txt      # Auto-generated activity log
   ```

3. Configure Git
   ```bash
   git init
   git branch -M main
   git remote add origin YOUR_PRIVATE_REPO_URL
   ```

4. Run the Script
   ```bash
   python range_commit.py  # For bulk commits
   # OR
   python daily_commit.py  # For single day
   ```

5. Push Changes
   ```bash
   git push -u origin main
   ```

## Automation (Optional)
```bash
0 0 * * * cd /path/to/commit-generator && python daily_commit.py
```

## License

MIT License

---
*Part of the "Make My GitHub Less Sad" initiative.*
