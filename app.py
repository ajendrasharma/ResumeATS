import streamlit as st
from PyPDF2 import PdfReader

from docx import Document
from io import BytesIO

import spacy
from spacy.cli import download

def download_model(model_name):
    if not spacy.util.is_package(model_name):
        download(model_name)
    else:
        st.write(f"Model '{model_name}' is already installed.")

def load_model(model_name):
    try:
        return spacy.load(model_name)
    except OSError:
        st.write(f"Model '{model_name}' not found. Downloading...")
        download_model(model_name)
        return spacy.load(model_name)

# Load the 'en_core_web_sm' model
nlp = load_model("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from docx
def extract_text_from_docx(file):
    file.seek(0)  # Go to the beginning of the file
    doc = Document(BytesIO(file.read()))
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

# Function to extract named entities
def extract_named_entities(text):
    doc = nlp(text)
    entities = set([(ent.text.lower(), ent.label_) for ent in doc.ents])
    return entities

# Function to calculate matching score and extract matching text
def calculate_matching_score(job_description_entities, resume_entities):
    matching_entities = job_description_entities.intersection(resume_entities)
    score = len(matching_entities) / len(job_description_entities) * 100
    matching_text = [text for text, label in matching_entities]
    return score, matching_text

# Function to fetch job listings
def fetch_job_listings():
    # This function should fetch job listings from your data source
    # Replace this placeholder with your implementation
    job_listings = ["Job 1", "Job 2", "Job 3", "Job 4", "Job 5"]
    return job_listings

# Function to fetch matching resumes for a job listing
def fetch_matching_resumes(job):
    # This function should fetch resumes that match the given job
    # with a score greater than 40%
    # Replace this placeholder with your implementation
    matching_resumes = ["Resume 1", "Resume 2", "Resume 3"]
    return matching_resumes

def main():
    st.title("List of Matching Resumes")
    mode = st.sidebar.selectbox("Select Mode", ["Manual Selection", "All Jobs"])

    if mode == "All Jobs":
        st.header("All Jobs Matching list")

        # Select a job listing
        job_listings = fetch_job_listings()
        selected_job = st.selectbox("Select a Job Listing", job_listings)

        # Fetch and display matching resumes
        matching_resumes = fetch_matching_resumes(selected_job)
        st.subheader(f"Matching Resumes for {selected_job}")
        for resume in matching_resumes:
            st.text(resume)

    else:
        st.header("Manual Selection")

        # Upload resume
        st.subheader("Upload Resume")
        resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

        if resume_file is not None:
            file_details = {"FileName": resume_file.name, "FileType": resume_file.type, "FileSize": resume_file.size}
            st.write(file_details)

            # Read and print resume
            if file_details["FileType"] == "application/pdf":
                resume_text = extract_text_from_pdf(resume_file)
            elif file_details["FileType"] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                resume_text = extract_text_from_docx(resume_file)
            else:
                st.write("The file type is not supported. Please upload a pdf or docx file.")

            st.subheader("Resume Text")
            st.text(resume_text)

        if resume_file is not None:
            # Extract named entities from resume
            st.subheader("Important Keywords in Resume")
            resume_entities = extract_named_entities(resume_text)
            for entity, label in resume_entities:
                st.write(f"- {entity} ({label})")

            # Enter job description
            st.header("Enter Job Description")
            job_description = st.text_area("Enter the job description here")

            if st.button("Match"):
                # Extract named entities from job description
                job_description_entities = extract_named_entities(job_description)

                # Calculate matching score and extract matching text
                score, matching_text = calculate_matching_score(job_description_entities, resume_entities)

                # Display matching text
                st.subheader("Matching Text")
                for text in matching_text:
                    st.write(text)

                # Display matching score
                st.subheader("Matching Score")
                st.write(f"The resume matches the job description with a score of {score:.2f}%")

if __name__ == "__main__":
    main()
