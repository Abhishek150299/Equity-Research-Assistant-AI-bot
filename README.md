# Equity-Research-Assistant-AI-bot
The Equity Research Assistant AI bot, built with OpenAI, Langchain, FAISS, and Streamlit, analyzes equity research articles by processing URLs. It extracts insights from the content, allowing users to ask questions and receive relevant answers with sources, enabling quick and efficient research analysis.

# Steps to use the AI-bot
Open the App:
 - Launch the Streamlit app where the Equity Research Assistant is hosted.
Provide URLs:
 - In the sidebar, you’ll see fields to enter up to three URLs of equity research articles. Copy and paste the URLs of the research articles you want to analyze.
Click "Analyze Articles":
 - Once you’ve entered the URLs, click the “Analyze Articles!!” button in the sidebar. This will trigger the data loading and processing steps.
Wait for Data Processing:
 - The bot will start by loading the data from the provided URLs and split it into smaller, manageable chunks. You’ll see status messages indicating the progress.
Vector Store Creation:
 - The bot will create embeddings for the text data and store them in a vector store (FAISS). This step might take a few moments, depending on the content.
Ask Your Question:
 - Once the processing is complete, you’ll see a text input box where you can ask any question related to the articles you uploaded.
Get Answer:
 - After entering your question, the bot will search for the most relevant information from the research articles and display the answer.
View Sources:
 - If available, the bot will also show the sources from which it retrieved the answer, providing transparency on the origin of the information.
Repeat the Process:
 - You can continue to ask more questions or upload different URLs for analysis as needed.
