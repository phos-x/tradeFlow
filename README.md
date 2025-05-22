# 📊 TradeData Analysis Tool

Welcome to the **TradeData Analysis Tool**! This Python-based application allows you to fetch trading data from the [MarketStack API](https://marketstack.com/) and save it to a CSV file for further analysis. 🚀

---

## 📝 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

The **TradeData Analysis Tool** is designed to simplify the process of fetching and saving trading data. It provides an interactive command-line interface to select API functions, input parameters, and retrieve data seamlessly.

---

## ✨ Features

- Fetch trading data from the MarketStack API.
- Save data to a CSV file for analysis.
- Interactive command-line interface for ease of use.
- Customizable API functions and parameters.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher 🐍
- An API key from [MarketStack](https://marketstack.com/) 🔑

### Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/TradeData.git
     cd TradeData
     ```

2. Install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. Set up your API key:
     - Create a `.env` file in the project root.
     - Add the following line to the `.env` file:
         ```env
         ACCESS_KEY=your_marketstack_api_key
         ```

---

## 🛠️ Usage

1. Run the application:
     ```bash
     python main.py
     ```

2. Follow the prompts to:
     - Select an API function.
     - Enter required parameters.
     - Fetch and save the data.

3. The data will be saved to a file named `trading_data.csv` in the project directory.

---

## 📂 File Structure