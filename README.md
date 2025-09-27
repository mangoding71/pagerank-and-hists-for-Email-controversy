# Hillary Email Network Analysis (PageRank & HITS)

This repository contains an analysis of the **Hillary Clinton Email Scandal** dataset using two classic link analysis algorithms: **PageRank** and **HITS**.
The goal of this project is to uncover the importance of individuals and email interactions by modeling them as a graph network.

---

## 📊 Project Overview

* Construct a directed graph from Hillary Clinton’s released emails dataset.
* Apply **PageRank** to measure the global influence of nodes (persons).
* Apply **HITS (Hyperlink-Induced Topic Search)** to evaluate **hubs** and **authorities** in the network.
* Compare and interpret the results to better understand communication patterns.

---

## 📁 Dataset Files

The repository includes several preprocessed CSV files for building the email graph:

* **Aliases.csv**
  Contains alias mappings to unify different names/identities of the same person.

* **Persons.csv**
  List of individuals identified in the dataset.

* **Emails.csv**
  Records of emails, including sender, receiver(s), and timestamp.

* **EmailReceivers.csv**
  Mapping between email IDs and their recipients (one-to-many relationship).

---

## ⚙️ Code Files

* **pagerank.py**
  Implements the PageRank algorithm on the email communication graph.

* **hits.py**
  Implements the HITS algorithm to compute hub and authority scores.

---

## ▶️ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/mangoding71/pagerank-and-hists-for-Email-controversy.git
   cd pagerank-and-hists-for-Email-controversy
   ```

2. Ensure you have Python 3 installed with dependencies (e.g., `networkx`, `pandas`).

3. Run PageRank analysis:

   ```bash
   python pagerank.py
   ```

4. Run HITS analysis:

   ```bash
   python hits.py
   ```

---

## 📈 Output

* PageRank results: Ranked list of the most influential individuals in the email network.
* HITS results: Separate rankings for **hubs** (information spreaders) and **authorities** (information sources).

Both results provide insights into the structure and hierarchy of communication.

---

## 📝 Notes

* This project focuses on network analysis methods rather than political interpretation.
* The dataset is preprocessed for educational and research purposes.


