#!/usr/bin/env bash
# Deploy Experiment 5 code to CHPC kingspeak cluster.
# Usage: bash chpc/deploy.sh <uNID>
#
# Prerequisites: VPN connected, SSH key configured for CHPC

set -euo pipefail

UNID="${1:?Usage: $0 <uNID>}"
REMOTE_HOST="${UNID}@kingspeak1.chpc.utah.edu"
REMOTE_DIR="~/Abaqus"

# Resolve repo root (deploy.sh lives in experiment5/chpc/)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "============================================"
echo "Deploying to ${REMOTE_HOST}:${REMOTE_DIR}"
echo "  Source: ${REPO_ROOT}"
echo "============================================"

# Create remote directory structure
echo ""
echo "[1/4] Creating remote directories..."
ssh "$REMOTE_HOST" "mkdir -p ${REMOTE_DIR}/paper_reproduction/experiment5/{scripts,chpc,screenshots}"
ssh "$REMOTE_HOST" "mkdir -p ${REMOTE_DIR}/paper_reproduction/experiment4/scripts"

# Sync experiment 5 scripts
echo "[2/4] Syncing experiment 5 scripts..."
rsync -avz --delete \
    "${REPO_ROOT}/paper_reproduction/experiment5/scripts/" \
    "${REMOTE_HOST}:${REMOTE_DIR}/paper_reproduction/experiment5/scripts/"

# Sync experiment 5 CHPC/SLURM files
echo "[3/4] Syncing SLURM scripts..."
rsync -avz --delete \
    "${REPO_ROOT}/paper_reproduction/experiment5/chpc/" \
    "${REMOTE_HOST}:${REMOTE_DIR}/paper_reproduction/experiment5/chpc/"

# Sync experiment 4 scripts (needed for baseline comparison in validation)
echo "[4/4] Syncing experiment 4 scripts..."
rsync -avz --delete \
    "${REPO_ROOT}/paper_reproduction/experiment4/scripts/" \
    "${REMOTE_HOST}:${REMOTE_DIR}/paper_reproduction/experiment4/scripts/"

# Make SLURM scripts executable
ssh "$REMOTE_HOST" "chmod +x ${REMOTE_DIR}/paper_reproduction/experiment5/chpc/*.slurm ${REMOTE_DIR}/paper_reproduction/experiment5/chpc/*.sh 2>/dev/null || true"

echo ""
echo "============================================"
echo "Deploy complete."
echo "============================================"
echo ""
echo "Next steps:"
echo "  ssh ${REMOTE_HOST}"
echo "  cd ${REMOTE_DIR}/paper_reproduction/experiment5"
echo "  sbatch chpc/test_slurm.slurm   # Stage 0: smoke test"
