# Git Workflow for Error-Driven Plasticity Framework

## Academic Research Git Best Practices

This document outlines the Git workflow for maintaining the computational analysis supporting our Nature Neuroscience paper.

## Repository Structure and Branching Strategy

### Main Branches
- **`main`**: Production-ready code for paper submission
- **`develop`**: Integration branch for new analyses
- **`paper-revisions`**: Dedicated branch for reviewer responses

### Feature Branches
```
feature/statistical-validation
feature/allen-observatory-integration  
feature/bootstrap-analysis
feature/figure-generation
```

### Release Branches
```
release/v1.0-initial-submission
release/v1.1-reviewer-response
release/v1.2-final-submission
```

## Commit Message Standards

### Structure
```
[type](scope): description

Body explaining what and why, not how.
Reference relevant paper sections.

Paper-Section: Methods/Results/Discussion
Validation: [x] Tests pass [ ] Manual verification
```

### Types for Academic Code
- `analysis`: New statistical analysis or computation
- `data`: Parameter updates or dataset modifications
- `figure`: Visualization and plotting changes
- `paper`: Direct manuscript-related changes
- `repro`: Reproducibility improvements
- `valid`: Validation and verification updates

### Examples
```
analysis(correlation): add cross-scale error-plasticity analysis

Implements hierarchical mixed-effects model for testing error-
plasticity relationships across behavioral, network, and synaptic 
scales. Based on Bates et al. (2015) lme4 methodology.

Paper-Section: Methods, Results Figure 2
Validation: [x] Bootstrap validation passes
References: #12, addresses reviewer comment 3
```

## Development Workflow

### Starting New Analysis
```bash
# Update main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b analysis/spine-dynamics-validation

# Set up commit message template
git config commit.template .gitmessage

# Work on analysis
# ... make changes ...

# Commit with scientific context
git add -A
git commit  # Opens template for detailed message

# Push feature branch
git push -u origin analysis/spine-dynamics-validation
```

### Code Review Process
```bash
# Create pull request
gh pr create --title "Add spine dynamics validation" \
             --body "Comprehensive validation of spine formation..."

# Address review comments
git checkout analysis/spine-dynamics-validation
# ... make requested changes ...
git add -A
git commit -m "fix(validation): address reviewer statistical concerns"

# Update pull request
git push origin analysis/spine-dynamics-validation
```

### Preparing for Submission
```bash
# Create release branch
git checkout -b release/v1.2-nature-submission

# Final validation
python -m pytest tests/
python scripts/run_full_analysis.py --validate

# Update version numbers
git add -A
git commit -m "paper: prepare v1.2 for Nature Neuroscience submission"

# Tag release
git tag -a v1.2.0 -m "Nature Neuroscience submission ready
- Complete multi-scale analysis
- Statistical validation with bootstrap
- Publication-ready figures
- Comprehensive documentation"

# Merge to main
git checkout main
git merge release/v1.2-nature-submission
git push origin main --tags
```

## Repository Maintenance

### Regular Maintenance Tasks
```bash
# Weekly dependency updates
pip freeze > requirements.txt
git add requirements.txt
git commit -m "deps: update package versions for security"

# Monthly validation runs
python scripts/full_validation_suite.py
git add validation_reports/
git commit -m "valid: monthly reproducibility check"

# Archive old branches
git branch -d feature/completed-analysis
git push origin --delete feature/completed-analysis
```

### Backup and Archival
```bash
# Create manuscript submission archive
git archive --format=zip --prefix=error-plasticity-code/ \
            v1.2.0 > submission_archives/nature_neuroscience_v1.2.zip

# Document submission version
echo "v1.2.0 - Nature Neuroscience Submission $(date)" >> SUBMISSION_HISTORY.md
git add SUBMISSION_HISTORY.md
git commit -m "paper: document Nature Neuroscience submission"
```

## Collaboration Guidelines

### Academic Collaboration
- **Attribution**: Clear commit attribution for all contributors
- **Documentation**: Scientific rationale in commit messages
- **Validation**: Statistical validation before merging
- **Transparency**: Open development with public repository

### Code Review Standards
- **Scientific Accuracy**: Verify biological parameter realism
- **Statistical Validity**: Check analysis methodology
- **Reproducibility**: Ensure deterministic results
- **Documentation**: Clear scientific explanations

### Conflict Resolution
```bash
# Handle merge conflicts in analysis code
git checkout main
git pull origin main
git checkout feature/your-analysis
git rebase main

# Resolve conflicts prioritizing:
# 1. Statistical accuracy
# 2. Biological realism  
# 3. Reproducibility
# 4. Code clarity

git add resolved_files.py
git rebase --continue
```

## Integration with Paper Writing

### Linking Code to Manuscript
```bash
# Tag commits related to specific figures
git tag figure-2a-data commit_hash
git tag figure-2b-analysis commit_hash

# Reference commits in manuscript
# "Statistical analysis performed using validated code
#  (commit abc123f, tag v1.2.0)"
```

### Reviewer Response Workflow
```bash
# Create reviewer response branch
git checkout -b reviewer-response-round1

# Address specific comments
git commit -m "fix(stats): address reviewer concern about multiple comparisons

Implements Benjamini-Hochberg FDR correction as requested.
Maintains significance of primary findings (q<0.05).

Reviewer-Comment: #3 (statistical rigor)
Paper-Section: Methods, Results Table 1"

# Document response
echo "Response to Reviewer 3, Comment 3: $(git rev-parse HEAD)" >> REVIEWER_RESPONSES.md
```

## Quality Assurance

### Pre-Submission Checklist
- [ ] All analyses run successfully with fixed seeds
- [ ] Statistical results match manuscript values  
- [ ] Figure generation reproduces paper figures
- [ ] Documentation is comprehensive and accurate
- [ ] Dependencies are properly specified
- [ ] License and citation information is correct
- [ ] Repository follows academic standards

### Continuous Integration
```yaml
# .github/workflows/validate.yml
name: Scientific Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run analysis validation
      run: python scripts/validate_all_analyses.py
    - name: Check statistical reproducibility
      run: python scripts/check_reproducibility.py
```

This Git workflow ensures that our computational analysis maintains the highest standards of reproducibility and transparency required for Nature Neuroscience publication while facilitating collaborative scientific development.