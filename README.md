# RASAN-ANKALAN
This project aims to develop a machine learning model for predicting the toxicity of compounds based on their chemical formulas. Toxicity prediction plays a crucial role in various fields, including drug discovery, environmental risk assessment, and chemical safety evaluation. By leveraging a large dataset of compounds with known toxicity levels, we extract relevant features from their chemical formulas and build a predictive model using different machine learning algorithms.

Features
Dataset: The project utilizes a carefully curated dataset consisting of over 1,000,000 compounds, each accompanied by their respective chemical formulas and toxicity scores. This diverse dataset provides a comprehensive representation of compound structures and toxicity levels.

Feature Extraction: We extract several informative features from the chemical formulas, including molecular weight, the number of atoms, the number of heavy atoms, and the number of rotatable bonds. These features capture important structural properties of the compounds and serve as inputs to the predictive model.

Machine Learning Algorithms: The project employs various regression and classification algorithms, including XGBoost Regression, Polynomial Regression, Ridge Regression, Lasso Regression, Elastic Net Regression, Logistic Regression, Decision Tree Classifier, Random Forest Classifier, K-Nearest Neighbors (KNN), and Support Vector Machine (SVM). Each algorithm is trained and evaluated to determine its effectiveness in predicting compound toxicity.

Performance Evaluation: The performance of the developed models is assessed using appropriate evaluation metrics. For regression models, metrics such as R2 score, mean absolute error, mean squared error, and root mean squared error are calculated. For classification models, accuracy and the confusion matrix are used to measure the model's classification performance.

Usage
To use this project, follow these steps:

Install the necessary dependencies by running pip install -r requirements.txt.

Prepare your dataset by ensuring it has the required columns, including chemical formulas and toxicity scores.

Execute the Jupyter Notebook or Python script that corresponds to the desired machine learning algorithm. This will train the model on your dataset and generate predictions.

Evaluate the model's performance using the provided evaluation metrics to assess its accuracy in predicting compound toxicity.

Customize and fine-tune the model by adjusting hyperparameters, exploring different feature sets, or employing advanced techniques such as data augmentation.

Use the trained model to make toxicity predictions on new compounds by providing their chemical formulas as input.

Contributions
Contributions to this project are welcome. If you encounter any issues, have suggestions for improvements, or would like to contribute new features or algorithms, please submit a pull request. Let's collaborate to enhance the accuracy and effectiveness of compound toxicity prediction.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
We acknowledge the support and guidance of our mentors and advisors throughout the development of this project. Additionally, we extend our gratitude to the creators and contributors of the libraries and frameworks used in this project for their valuable tools and resources.

Contact
For any inquiries or further information, please feel free to contact us at aditgaur7809@gmail.com. We would be happy to answer any questions or discuss potential collaborations related to compound toxicity prediction.
