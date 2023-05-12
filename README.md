# pinecone-demo
A Very Simple Colour Matching App Using Pinecone

This repository provides an implementation of a colour search engine using Pinecone. The script connects to a Pinecone service, creates a 3-dimensional index, and allows for searching similar colours based on a given colour. This project utilises the Pinecone vector database service for finding similar vectors (colours).

This project is a simple example of how to use Pinecone for similarity searches. It is not designed for large-scale or real-world applications.

## Setup and Installation
To set up and run the example, follow these steps:

1. Clone this repository: git clone https://github.com/adiekaye/pinecone-demo.git
2. Navigate to the project directory: cd pinecone-demo
3. Create a virtual environment: for Python 3.6 and above: `python -m venv venv`
4. Activate the virtual environment:
- For Windows: venv\Scripts\activate
- For macOS/Linux: source venv/bin/activate
5. Install the required libraries: `pip install -r requirements.txt`
6. Run the script to see the colour search engine in action: `python main.py`
7. To exit the virtual environment, type deactivate in the terminal.

Note: The virtual environment and requirements installation steps are optional but recommended to ensure compatibility and avoid conflicts with other Python packages you may have installed.

## Contents
- main.py: Main script implementing the Pinecone colour search engine
- colour_data.py: Contains colour data used for this project
- colour.py: Contains the Colour class and a function to plot colours
- requirements.txt: Lists the required libraries for this project
- README.md: Provides instructions for setting up and running the example, and explains the contents of the repository
- .gitignore: A simple Git configuration file to ignore the virtual environment directory

## Usage
Replace <YOUR_PINECONE_API_KEY> with your actual Pinecone API key in the main.py file.

The script will create a 3-dimensional index in Pinecone, upsert vectors (colours), and perform a query to find similar colours. The results will be plotted for visual comparison.

## License
This project is licensed under the MIT License.
