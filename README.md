# Stock Market Screener Project

## Overview
This project is designed to fetch and process financial market data to facilitate the screening of stocks across various market capitalizations. The project aims to categorize stocks into Micro-Cap, Small-Cap, Mid-Cap, Large-Cap, and Mega-Cap groups based on their market capitalization.

## Features
- Fetch market capitalization data in batches for efficiency.
- Categorize stocks into predefined market cap groups.
- Create a DataFrame to count the occurrences of each market cap type.
- Implement a progress bar for batch processing to monitor API data fetching.

## In Progress
This project is currently a work in progress. Future updates aim to enhance functionality, improve efficiency, and refine data analysis.

## Usage
The code is structured to run in a batch processing mode to efficiently handle large volumes of data from the [IEX Cloud API](https://iexcloud.io/).

### Setting Up
1. Obtain an API key from IEX Cloud.
2. Install the required Python libraries: `pandas`, `requests`, and `math`.

### Running the Script
1. Define the list of symbols or use the provided function to fetch them.
2. Set the `iex_key` variable to your IEX Cloud API key.
3. Run the script to process the data and view the results.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is open-sourced under the [MIT license](LICENSE.txt).

## Contact
For any queries or assistance, feel free to contact the project maintainers.

---

**Note**: This README is in progress and will be updated with more detailed information and instructions as the project evolves.
