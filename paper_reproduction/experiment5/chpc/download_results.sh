#!/usr/bin/env bash
# Download Experiment 5 results from CHPC cluster to local machine.
# Usage: bash chpc/download_results.sh <uNID>

set -euo pipefail

UNID="${1:?Usage: $0 <uNID>}"
REMOTE_HOST="${UNID}@kingspeak1.chpc.utah.edu"
REMOTE_EXP5="~/Abaqus/paper_reproduction/experiment5"

# Resolve local results directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOCAL_RESULTS="${SCRIPT_DIR}/../results"

mkdir -p "$LOCAL_RESULTS/screenshots"

echo "============================================"
echo "Downloading Experiment 5 results"
echo "  From: ${REMOTE_HOST}"
echo "  To:   ${LOCAL_RESULTS}"
echo "============================================"

# CSV and text reports
echo ""
echo "[1/4] Reports and CSVs..."
for f in optimization_summary.csv optimization_report.txt \
         validation_results.txt validation_comparison.csv \
         convergence_history.csv; do
    scp "${REMOTE_HOST}:${REMOTE_EXP5}/${f}" "$LOCAL_RESULTS/" 2>/dev/null \
        && echo "  OK: ${f}" \
        || echo "  --: ${f} (not found)"
done

# Convergence plot
echo ""
echo "[2/4] Plots..."
scp "${REMOTE_HOST}:${REMOTE_EXP5}/convergence_plot.png" \
    "$LOCAL_RESULTS/" 2>/dev/null \
    && echo "  OK: convergence_plot.png" \
    || echo "  --: convergence_plot.png (not found)"

# Screenshots
echo ""
echo "[3/4] Screenshots..."
scp "${REMOTE_HOST}:${REMOTE_EXP5}/screenshots/*.png" \
    "$LOCAL_RESULTS/screenshots/" 2>/dev/null \
    && echo "  OK: screenshots/*.png" \
    || echo "  --: No screenshots found"

# SLURM logs
echo ""
echo "[4/4] SLURM logs..."
scp "${REMOTE_HOST}:${REMOTE_EXP5}/exp5_*.out" \
    "$LOCAL_RESULTS/" 2>/dev/null \
    && echo "  OK: SLURM output logs" \
    || echo "  --: No SLURM logs found"

echo ""
echo "============================================"
echo "Download complete."
echo "============================================"
echo ""
echo "Contents:"
ls -la "$LOCAL_RESULTS/" 2>/dev/null
echo ""
ls -la "$LOCAL_RESULTS/screenshots/" 2>/dev/null || true
