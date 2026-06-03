#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ ! -d task_manager ]]; then
  echo "Creating task_manager directory..."
  mkdir -p task_manager
else
  echo "task_manager directory already exists."
fi

for FILE in validation.py task_utils.py; do
  if [[ -f "$FILE" ]]; then
    if [[ -f "task_manager/$FILE" ]]; then
      echo "Skipping $FILE: already exists in task_manager/."
    else
      echo "Moving $FILE into task_manager/"
      mv "$FILE" "task_manager/"
    fi
  else
    echo "Root file $FILE not found; no action taken."
  fi
done

echo "Done."
