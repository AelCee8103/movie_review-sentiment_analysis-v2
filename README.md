# movie_review-sentiment_analysis-v2

## Getting Started

### Requirements

- Python 3.8+
- Install dependencies:

  ```bash
    pip install -r requirements.txt
    ```

### Data

- Ensure your dataset (CSV or similar) is available in the project directory or update paths in the notebooks accordingly.

## How to Run

1. **Clone the repository** and navigate to the project folder.
2. **Install dependencies** as above.
3. **Run Jupyter Notebook**:

     ```bash
     jupyter notebook
    
     ```

4. Open the notebooks in your browser and run cells as needed.

## Notebooks Overview

- **model_creation.ipynb**  
    For building, training, and saving sentiment analysis models. Use this notebook to experiment with model architectures and preprocessing.

- **Models_Comparison.ipynb**  
    For comparing the performance of different trained models. Do not use `model_creation.ipynb` for comparison tasks; use this notebook to load, evaluate, and compare models.

## Notes

- Models and vectorizers are saved using `joblib` for reuse.
- Update file paths as needed for your environment.
- For questions or issues, please open an issue or contact the maintainer.
