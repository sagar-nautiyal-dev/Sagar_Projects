from __future__ import annotations

import json
from pathlib import Path


project = Path(__file__).resolve().parents[1]
notebook_path = project / "notebooks" / "retail_trade_forecasting.ipynb"
notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
cells = notebook.get("cells", [])
markdown_count = sum(cell.get("cell_type") == "markdown" for cell in cells)
code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
errors = [
    output
    for cell in code_cells
    for output in cell.get("outputs", [])
    if output.get("output_type") == "error"
]
unexecuted = [cell for cell in code_cells if cell.get("execution_count") is None]

assert markdown_count >= 8, f"Expected at least 8 Markdown cells, found {markdown_count}"
assert not errors, f"Notebook contains {len(errors)} error outputs"
assert not unexecuted, f"Notebook contains {len(unexecuted)} unexecuted code cells"

expected = [
    project / "figures" / "coverage.png",
    project / "figures" / "model_comparison.png",
    project / "figures" / "test_predictions.png",
    project / "results" / "model_metrics.csv",
    project / "results" / "country_metrics.csv",
]
missing = [str(path.relative_to(project)) for path in expected if not path.exists()]
assert not missing, f"Missing generated outputs: {missing}"

print(f"Notebook validation passed: {markdown_count} Markdown cells, {len(code_cells)} executed code cells.")
