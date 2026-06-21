# Project Brief: AI Classification System Design and Evaluation

- [Project Brief: AI Classification System Design and Evaluation](#project-brief-ai-classification-system-design-and-evaluation)
	- [Course Context](#course-context)
	- [Core Requirements](#core-requirements)
	- [Key Skills They'll Develop](#key-skills-theyll-develop)
	- [Deployment Architecture](#deployment-architecture)
	- [Five to Ten Project Ideas](#five-to-ten-project-ideas)
		- [Project One: Sentiment Analysis for Review Classification](#project-one-sentiment-analysis-for-review-classification)
		- [Project Two: Content Moderation for Social Media](#project-two-content-moderation-for-social-media)
		- [Project Three: Product Category Classification for E-Commerce](#project-three-product-category-classification-for-e-commerce)
		- [Project Four: Audio Genre Classification](#project-four-audio-genre-classification)
		- [Project Five: Image-Based Plant Disease Detection](#project-five-image-based-plant-disease-detection)
		- [Project Six: Intent Classification for Customer Support Automation](#project-six-intent-classification-for-customer-support-automation)
		- [Project Seven: Hate Speech and Bias Detection](#project-seven-hate-speech-and-bias-detection)
		- [Project Eight: Email Spam Detection and Classification](#project-eight-email-spam-detection-and-classification)
		- [Project Nine: Resume Screening and Job Match Classification](#project-nine-resume-screening-and-job-match-classification)
		- [Project Ten: Sentiment Analysis for Social Media Monitoring](#project-ten-sentiment-analysis-for-social-media-monitoring)
	- [Evaluation Framework for All Projects](#evaluation-framework-for-all-projects)
	- [Grading Rubric](#grading-rubric)


## Course Context

Twenty-eight business school students, minimal technical background, five three-hour sessions, one month to complete. The goal is for them to prototype a real classification system using Hugging Face models and APIs, deploy it with an external interface, and genuinely understand how to evaluate AI systems.

## Core Requirements

Each group of three to four students will build a classification system. They must research and select an appropriate Hugging Face model for their chosen use case, document why they selected it, design evaluation metrics before testing, create a simple public interface using tools like Telegram, a form, or Lovable, and generate evaluation data to test their system's performance.

## Key Skills They'll Develop

Model selection and motivation, evaluation design and metrics, deployment using free cloud APIs, and genuine AI literacy around model limitations.

## Deployment Architecture

Students use Replicate API or Together AI for Hugging Face model inference, OpenRouter or Anthropic API for any LLM responses, and a simple front-end like Telegram bot, Google Form with automated response, or Lovable website. Everything is deployed and publicly accessible so you can interact with it as a teacher.

## Five to Ten Project Ideas

### Project One: Sentiment Analysis for Review Classification

Students analyse customer reviews and classify them as positive, negative, or neutral. They use a text classification model like DistilBERT fine-tuned for sentiment. Evaluation metrics are precision and recall per class, tested on a curated set of fifty reviews you provide plus twenty synthetic reviews they generate. Their motivation should cover why they chose this model over other text classifiers and how accuracy differs across product domains. The interface accepts review text and returns sentiment plus confidence score.


### Project Two: Content Moderation for Social Media

They build a system that flags potentially harmful or inappropriate text. They research models trained on toxicity detection and classify whether text violates content policies. Evaluation involves testing on mixed datasets—some clearly safe, some clearly harmful, some ambiguous edge cases. They document what they consider a true positive versus a false positive and why that trade-off matters for their use case. The system runs through a Telegram bot where users submit text and get a classification with explanation.


### Project Three: Product Category Classification for E-Commerce

Given product descriptions or titles, classify them into predefined categories like electronics, clothing, home goods, sports. They research Hugging Face multi-class text classifiers and justify their choice. Evaluation uses a test set of product descriptions you provide plus confusion matrices showing which categories they confuse. They explain why certain categories are harder to distinguish and propose how they'd improve. Deployed as a form where merchants paste product descriptions.

### Project Four: Audio Genre Classification

They classify audio clips into genres like speech, music, ambient, or noise. They research audio classification models on Hugging Face, explain computational and accuracy trade-offs, and create evaluation data from diverse audio samples. Metrics include per-class accuracy and handling of borderline cases. The interface accepts audio uploads and returns the predicted genre with confidence. This shows them multimodal AI beyond text.

### Project Five: Image-Based Plant Disease Detection

Given plant leaf images, classify whether the plant is healthy or has a specific disease. They use a vision model from Hugging Face, document why they chose it, and test on a dataset of images. Evaluation covers sensitivity to lighting conditions, image quality, and leaf variety. They discuss why certain diseases are harder to detect and propose data collection strategies. Users upload photos and get disease classification plus suggested remedies via an LLM API call.

### Project Six: Intent Classification for Customer Support Automation

They classify customer support queries into intents like billing, technical support, returns, or general inquiry. They use intent classification models and test on customer service transcripts. Evaluation measures how well intent detection works on edge cases—queries that blend multiple intents. They document when human review is necessary and why. Deployed as a Telegram bot for internal team use.

### Project Seven: Hate Speech and Bias Detection

They build a classifier that detects potentially hateful or biased language in text. This involves researching models trained on diverse language datasets and understanding their limitations across different populations. Evaluation is nuanced—they test on curated examples and document false positives and false negatives critically. They discuss why perfect accuracy is impossible and propose mitigation strategies. Accessible through a form interface.

### Project Eight: Email Spam Detection and Classification

Given email subject lines or full emails, classify as spam or legitimate, and further classify legitimate emails by type—promotions, important, social. They research appropriate models and explain trade-offs between recall and precision—missing important emails versus flagging legitimate ones. They test on real-world email datasets. Users submit email text and get classification with explanation.

### Project Nine: Resume Screening and Job Match Classification

They classify whether a resume matches a specific job description. This involves creating evaluation datasets of resumes paired with job descriptions and testing how well their model scores compatibility. They discuss ethical implications, potential biases, and what evaluation metrics actually matter for hiring. Deployed so you can upload a resume and get a match score against a sample job description.

### Project Ten: Sentiment Analysis for Social Media Monitoring

Similar to Project One but focused on monitoring brand mentions on social media. They classify brand sentiment in tweets or posts, use emotion classification models, and test across different contexts. Evaluation includes handling sarcasm, context-dependent sentiment, and domain shifts. They document where their system struggles and why. Deployed through a form where marketing teams can submit social media snippets.

## Evaluation Framework for All Projects

Each group documents three things: the evaluation dataset they created or curated, including how many samples and how they selected them; the metrics they chose and why, such as accuracy, precision, recall, or confusion matrices; and honest analysis of their model's performance, including what it does well, what it struggles with, and why.

They must also justify their model choice in writing—why this specific Hugging Face model over alternatives, what trade-offs they're making, and what would improve their system.

## Grading Rubric

**Model selection and justification**: Are they choosing thoughtfully or just picking the first model they find? Do they understand the trade-offs? 

**Evaluation design**: Have they thought deeply about what constitutes success? Do their metrics align with their use case? 

**Honest assessment**: Can they articulate what their system gets wrong and why? 

**Deployment and interface**: Is it actually accessible and usable? Does it work? 

**Presentation**: Can they explain their choices clearly in five minutes?
