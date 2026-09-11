# Project Report
## Sentiment Analysis of Student Feedback for Course Improvement

### Abstract
Student feedback can reveal opinions about teaching, materials, assignments and learning experiences. This project develops a Python application that classifies feedback as Positive, Neutral or Negative and summarizes multiple comments.

### Objectives
1. Accept student feedback.
2. Detect positive and negative language.
3. Classify sentiment.
4. Provide score and confidence.
5. Analyze CSV feedback.
6. Export results.

### Technologies
Python, Streamlit, Pandas, Regular Expressions and rule-based NLP.

### Methodology
Text is tokenized into words. Positive and negative vocabulary is counted, with simple handling for nearby negation words. A score is calculated from positive minus negative signals and thresholds assign the final class.

### Workflow
Input → Tokenization → Sentiment word matching → Negation handling → Score → Classification → Visualization/Export.

### Modules
**Single Feedback:** analyzes one comment.
**CSV Analysis:** analyzes every row with a `feedback` column, shows a table and chart, and exports CSV.

### Use Case
A department can analyze anonymous course comments and identify areas that may need improvement.

### Limitations
This is a lightweight prototype. Sarcasm, spelling mistakes, mixed sentiment and complex context may be misclassified. It is not intended for high-stakes decisions.

### Future Enhancements
Use labeled data with TF-IDF and machine-learning classifiers, multilingual models, topic extraction, trend dashboards and anonymized historical analysis.

### Conclusion
The project demonstrates practical NLP concepts through a simple Streamlit interface for student-feedback analysis.
