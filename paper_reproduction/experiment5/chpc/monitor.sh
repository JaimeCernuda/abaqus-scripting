#!/usr/bin/env bash
# Monitor Experiment 5 topology optimization progress on CHPC.
#
# Usage:
#   bash chpc/monitor.sh          # One-shot status
#   bash chpc/monitor.sh --watch  # Refresh every 60s

set -euo pipefail

EXP5_DIR="$HOME/Abaqus/paper_reproduction/experiment5"
TOSCA_DIR="$EXP5_DIR/Experiment5_TO/TOSCA_POST"

print_status() {
    echo "========================================"
    echo "EXPERIMENT 5: STATUS"
    echo "Time: $(date)"
    echo "========================================"

    # SLURM jobs
    echo ""
    echo "--- SLURM Jobs ---"
    squeue -u "$USER" --format="%.10i %.20j %.8T %.10M %.6D %R" 2>/dev/null || echo "  No active jobs"

    # Optimization progress
    echo ""
    echo "--- Optimization Progress ---"
    if [ -d "$TOSCA_DIR" ]; then
        ODB_COUNT=$(ls "$TOSCA_DIR"/*.odb 2>/dev/null | wc -l)
        echo "  Design cycles: ${ODB_COUNT} / 50"

        LATEST_ODB=$(ls -t "$TOSCA_DIR"/*.odb 2>/dev/null | head -1)
        if [ -n "${LATEST_ODB:-}" ]; then
            echo "  Latest: $(basename "$LATEST_ODB")"
            echo "  Modified: $(stat -c '%y' "$LATEST_ODB" 2>/dev/null || stat -f '%Sm' "$LATEST_ODB" 2>/dev/null || echo 'unknown')"
        fi
    elif [ -d "$EXP5_DIR/TOSCA_POST" ]; then
        ODB_COUNT=$(ls "$EXP5_DIR/TOSCA_POST"/*.odb 2>/dev/null | wc -l)
        echo "  Design cycles: ${ODB_COUNT} / 50 (alt path)"
    else
        echo "  Not started (no TOSCA_POST directory)"
    fi

    # Recent log activity
    echo ""
    echo "--- Recent Log ---"
    LATEST_LOG=$(ls -t "$EXP5_DIR"/exp5_tosca_*.out "$EXP5_DIR"/exp5_validate_*.out 2>/dev/null | head -1)
    if [ -n "${LATEST_LOG:-}" ]; then
        echo "  File: $(basename "$LATEST_LOG")"
        tail -5 "$LATEST_LOG" 2>/dev/null | sed 's/^/    /'
    else
        echo "  No logs yet"
    fi

    # Errors
    LATEST_ERR=$(ls -t "$EXP5_DIR"/exp5_*.err 2>/dev/null | head -1)
    if [ -n "${LATEST_ERR:-}" ] && [ -s "$LATEST_ERR" ]; then
        echo ""
        echo "--- ERRORS ---"
        tail -5 "$LATEST_ERR" | sed 's/^/    /'
    fi

    # Disk usage
    echo ""
    echo "--- Disk Usage ---"
    du -sh "$EXP5_DIR" 2>/dev/null | sed 's/^/  /'

    # Output files
    echo ""
    echo "--- Output Files ---"
    for f in Experiment5_TO.cae optimization_summary.csv optimization_report.txt \
             convergence_history.csv validation_results.txt validation_comparison.csv; do
        if [ -f "$EXP5_DIR/$f" ]; then
            echo "  [OK] $f"
        else
            echo "  [  ] $f"
        fi
    done

    # Screenshots
    SCREENSHOT_COUNT=$(ls "$EXP5_DIR"/screenshots/*.png 2>/dev/null | wc -l)
    echo "  Screenshots: ${SCREENSHOT_COUNT} PNG files"

    # Validation ODBs
    echo ""
    echo "--- Validation ODBs ---"
    for kn in 20 60 100; do
        if [ -f "$EXP5_DIR/Validation_${kn}kN.odb" ]; then
            echo "  [OK] Validation_${kn}kN.odb"
        else
            echo "  [  ] Validation_${kn}kN.odb"
        fi
    done
    echo ""
}

if [ "${1:-}" = "--watch" ]; then
    while true; do
        clear
        print_status
        echo "Refreshing in 60s... (Ctrl+C to stop)"
        sleep 60
    done
else
    print_status
fi
