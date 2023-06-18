# ResumeATS

ResumeATS is a project that aims to automate the scoring of resumes using machine learning techniques. It provides an end-to-end solution for parsing, analyzing, and scoring resumes based on predefined criteria.

## Features

- Resume parsing: Extracts information from resumes in various formats (e.g., PDF, Word) and converts it into structured data.
- Preprocessing: Applies preprocessing techniques to clean and standardize the extracted resume data.
- Scoring: Utilizes machine learning models to score resumes based on predefined criteria.
- User Interface: Provides a web-based interface built with Streamlit for easy interaction and visualization of the results.

## Installation

To install and set up the ResumeATS project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ajendrasharma/ResumeATS.git
   ```

2. Change into the project directory:
   ```bash
   cd ResumeATS
   ```

3. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the ResumeATS web interface.

3. Follow the instructions on the web interface to upload resumes and view the scoring results.

## Contributing

Contributions are welcome! If you'd like to contribute to ResumeATS, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your changes.
3. Make your modifications and commit them with descriptive messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).