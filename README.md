# 🏜️ The Most Barren GitHub Profile Function

## Why This Exists

Are you tired of having a GitHub profile that looks like a digital tumbleweed collection? Do your contribution graphs make the Sahara Desert look busy? Well, same here! After years of being a corporate code ninja, committing exclusively to private company repositories, my GitHub profile became the perfect metaphor for my social life during lockdown - absolutely empty.

## The Problem

```
recruiter_thought_process = {
    "sees_empty_github": "This dev probably just watches Netflix all day",
    "reality": "Been busy shipping features that paid for my Netflix subscription"
}
```

## The Solution

This revolutionary function lets you fill your contribution graph with commits, either for the past year or a custom date range!

### Features
- Exists ✨
- Makes my GitHub profile slightly less empty
- Proves I can create repositories
- Shows I have a sense of humor about my barren GitHub wasteland
- Flexible commit date ranges

## Installation

```bash
# There's nothing to install
# Just star this repo to make me feel better
```

## Files

- `yearly_commit.py`: Generate commits for the past year
- `range_commit.py`: Generate commits for a custom date range
- `main.py`: Entry point that runs today's commit

## Usage

### Option 1: Past Year Commits
In `yearly_commit.py`, customize your start date:
```python
# Change this line to set your desired start date
start_date = end_date - timedelta(days=365)  # Default: 1 year ago
# Example: start_date = datetime(2023, 1, 1)  # From January 1, 2023
```

### Option 2: Custom Date Range
In `range_commit.py`, set your desired date range:
```python
# Example usage:
start = datetime(2024, 3, 21)
end = datetime(2024, 4, 21)
perform_commits(start, end)
```

### Running the Script
```bash
# Option 1: Manual (for the dedicated clickers)
python main.py

# Option 2: Automated (for server owners)
# Add to crontab to run daily at midnight:
0 0 * * * cd /path/to/repo && python main.py
```

Watch as your contribution graph magically comes alive! 🌱

Pro tip: No server? No problem! Just remember to run it manually like your morning coffee routine. ☕

## Contributing

Why would you want to contribute to this? But if you insist, feel free to add more emptiness to this repository of emptiness.

## License

MIT License (Because that's what all the cool repos use)

## Author

A developer whose best work is hidden behind NDAs and private repositories. Like a ninja, but with more coffee and less throwing stars. 🥷☕

---
*This README is part of my "Make My GitHub Less Sad" initiative.*
