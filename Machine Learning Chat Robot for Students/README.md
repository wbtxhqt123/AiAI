# MLGPT-C: Machine Learning Generative Pre-trained Transformer Chatbot

This repository contains the code and resources for the MLGPT-C (Machine Learning Generative Pre-trained Transformer Chatbot) project, which was developed as part of a research endeavor to create an efficient and specialized chatbot for machine learning education and query resolution.

## Project Overview

The MLGPT-C project aims to address the limitations of existing question-answering language models in specialized domains, such as machine learning, by developing a novel transformer-based model trained on a curated dataset of machine learning questions and answers. The project comprises several key components:

1. **MLQA Dataset**: A comprehensive dataset containing 26,550 pairs of machine learning questions and answers, carefully curated and cleaned.

2. **MLGPT Model**: A custom transformer-based neural network model designed specifically for understanding and generating natural language responses related to machine learning concepts.

3. **MLGPT-C Chatbot**: An interactive chatbot interface built using Flask, integrating the MLGPT model to facilitate conversational interactions with users through text and voice input/output.

## Installation

1. Clone the repository: `git clone https://github.com/shengjie94/MLGPT-C.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download the pre-trained MLGPT model weights from the releases section.

## Usage

1. Run the Flask application: `python app.py`
2. Access the chatbot interface by navigating to `http://localhost:5000` in your web browser.
3. Type or speak your machine learning-related queries, and the chatbot will provide relevant responses.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to express our gratitude to the open-source community for providing valuable resources and libraries that facilitated the development of this project.
