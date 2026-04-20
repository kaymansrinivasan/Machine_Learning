# Notebook completion and quality audit

Generated on: 2026-04-20 (UTC)

## Method used
I reviewed every `.ipynb` file in this repo and scored them with simple, objective signals:

- **Completeness signals**: unexecuted code cells, empty code cells, and cells ending in runtime errors.
- **Quality signals**: presence of markdown explanations and obvious notebook hygiene issues.

> Note: "unexecuted" here means `execution_count` is `null`; some teams intentionally clear outputs before committing.

## Highest-priority incomplete notebooks

1. **`Time_Series_Code_30_March_2026.ipynb`**
   - 69/69 code cells unexecuted.
   - 1 empty code cell.
   - Contains TODO-like markers.
2. **`TimeSeriesHandsOnMarch.ipynb`**
   - 46/46 code cells unexecuted.
   - 1 empty code cell.
3. **`.ipynb/Time Series_1.ipynb`**
   - Contains an error output (`KeyError: 'Sales'`).
   - 1 unexecuted code cell.
   - 1 empty code cell.
4. **`.ipynb/TNL6323 - Lab01 (Introduction to NLTK).ipynb`**
   - Contains an error output (`AttributeError: 'Text' object has no attribute 'cont'`).
   - 7 empty code cells, 5 unexecuted code cells.
5. **`.ipynb/PCA!.ipynb`**
   - Contains an error output (`ValueError: DataFrame constructor not properly called!`).

## Notebooks that look weakly documented / "not done well"

These are likely harder to maintain or review because they have little-to-no markdown context:

- `.ipynb/census.ipynb` (0 markdown cells)
- `.ipynb/Employee Data – Exploratory Data Analysis (EDA) with Pandas-checkpoint.ipynb` (0 markdown cells)
- `.ipynb/HousePrice_Prediction_LR3.ipynb` (0 markdown cells)
- `.ipynb/Insurance_charges_prediction.ipynb` (0 markdown cells)
- `.ipynb/K-means.ipynb` (0 markdown cells)
- `.ipynb/LR_2.ipynb` (0 markdown cells)
- `.ipynb/Student_Performance_LR3.ipynb` (0 markdown cells)

## Full metrics snapshot

| Notebook | Total cells | Code | Markdown | Empty code | Unexecuted code | Error outputs |
|---|---:|---:|---:|---:|---:|---:|
| .ipynb/Airlines Sentiment Analysis (NLP).ipynb | 37 | 27 | 10 | 1 | 0 | 0 |
| .ipynb/census.ipynb | 20 | 20 | 0 | 1 | 1 | 0 |
| .ipynb/Employee Data – Exploratory Data Analysis (EDA) with Pandas-checkpoint.ipynb | 8 | 8 | 0 | 0 | 1 | 0 |
| .ipynb/Heart.ipynb | 9 | 8 | 1 | 1 | 1 | 0 |
| .ipynb/HousePrice_Prediction_LR3.ipynb | 7 | 7 | 0 | 0 | 0 | 0 |
| .ipynb/Insurance_charges_prediction.ipynb | 18 | 18 | 0 | 1 | 1 | 0 |
| .ipynb/K-means.ipynb | 21 | 21 | 0 | 0 | 0 | 0 |
| .ipynb/LR_2.ipynb | 13 | 13 | 0 | 1 | 1 | 0 |
| .ipynb/PCA (Computer Vision).ipynb | 26 | 23 | 3 | 1 | 1 | 0 |
| .ipynb/PCA!.ipynb | 4 | 4 | 0 | 0 | 0 | 1 |
| .ipynb/PCA(Iris).ipynb | 11 | 10 | 1 | 1 | 1 | 0 |
| .ipynb/Student_Performance_LR3.ipynb | 9 | 9 | 0 | 1 | 1 | 0 |
| .ipynb/student_placement_prediction.ipynb | 68 | 53 | 15 | 2 | 2 | 0 |
| .ipynb/Time Series_1.ipynb | 53 | 39 | 14 | 1 | 1 | 1 |
| .ipynb/TNL6323 - Lab01 (Introduction to NLTK).ipynb | 45 | 20 | 25 | 7 | 5 | 1 |
| Time_Series_Code_30_March_2026.ipynb | 128 | 69 | 59 | 1 | 69 | 0 |
| TimeSeriesHandsOnMarch.ipynb | 59 | 46 | 13 | 1 | 46 | 0 |

## Suggested cleanup order

1. Fix all notebooks with recorded error outputs.
2. Re-run and save clean execution order for the two time-series notebooks where all code is unexecuted.
3. Add short markdown section headers/objectives to notebooks with zero markdown.
4. Remove empty code cells across the repo.
