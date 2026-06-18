# Project 3: Universal Interactive AI Recommendation Engine

## Author

**Alishba Ghulam Rasool**
AI Intern – DecodeLabs Batch 2026

---

## Project Overview

The Universal Interactive AI Recommendation Engine is a Python-based recommendation system that suggests relevant items based on user interests.

The system takes user preferences as input, compares them with available items in a database, calculates similarity scores, and recommends the most relevant options.

This project demonstrates the basic concepts of Artificial Intelligence, recommendation systems, vector representation, and similarity matching.

---

## Objectives

* Accept user interests as input.
* Match user preferences with stored items.
* Calculate similarity scores using AI-based logic.
* Recommend the most relevant items.
* Display recommendations in ranked order.

---

## Technologies Used

* Python
* NumPy
* Jaccard Similarity Algorithm

---

## Features

### 1. User Interest Input

Users can enter one or more interests separated by commas.

Example:

Python, Data Science, Algorithms

### 2. Universal Vocabulary

The system contains interests from multiple domains:

* Technology
* Medical Science
* Physics & Astronomy
* Cooking
* Gardening
* Fashion

### 3. Vector-Based Processing

User interests and item tags are converted into numerical vectors for comparison.

### 4. Jaccard Similarity Matching

The recommendation engine calculates similarity using:

J(A,B) = |A ∩ B| / |A ∪ B|

Where:

* A = User Interests
* B = Item Tags

### 5. Ranked Recommendations

Recommendations are sorted from highest match score to lowest match score.

### 6. Best Recommendation

The system highlights the most suitable recommendation for the user.

### 7. Explainable Recommendations

The system shows which interests matched with each recommendation.

---

## Database Structure

Each item contains:

* ID
* Title
* Category
* Tags

Example:

Title: DecodeLabs AI Predictive Algorithm Bootcamp

Category: Technology

Tags:

* Python
* Algorithms
* Data Science

---

## Working Process

Step 1:
User enters interests.

Step 2:
System converts interests into vectors.

Step 3:
Each database item is converted into a vector.

Step 4:
Jaccard Similarity is calculated.

Step 5:
Items are ranked according to similarity score.

Step 6:
Best matching recommendations are displayed.

---

## Sample Input

Python, Data Science

---

## Sample Output

BEST RECOMMENDATION

Title:
DecodeLabs AI Predictive Algorithm Bootcamp

Category:
Technology

Score:
66.67%

Recommended Because:

* Python
* Data Science

---

## AI Concepts Used

* Recommendation Systems
* Pattern Matching
* Vector Representation
* Similarity Measurement
* Explainable AI

---

## Learning Outcomes

Through this project, I learned:

* How recommendation systems work.
* How user preferences can be represented numerically.
* How similarity algorithms are used in AI applications.
* How NumPy can be used for vector operations.
* How AI can provide personalized recommendations.

---

## Conclusion

This project successfully demonstrates a simple AI-powered recommendation engine that accepts user preferences, calculates similarity scores, and generates personalized recommendations. The project provides a practical introduction to recommendation systems and fundamental AI concepts.
