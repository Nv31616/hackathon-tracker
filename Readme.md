## Hackathon Tracker

### Video Demo:

[Link to your YouTube or Streamable video here]

### Description:

This project gathers data about upcoming hackathons from **Unstop** and **Devfolio**. It is built on the principles of ethical web scraping. By using the Python `requests` library, the program interacts with public API endpoints to gather hackathon data in **JSON** (JavaScript Object Notation) format.

The core of the program lies in its ability to navigate complex, nested data structures. The `parse_json()` function extracts critical details such as the hackathon name, location, dates, and registration links. A primary focus of this tool is tracking the **registration deadline**, ensuring users never miss an opportunity due to timing.

---
### Installation & Usage:

1. Install the dependencies of `requirements.txt` using pip.
```Python
pip install -r requirements.txt
```

2. Run the project.py script
```Python
python project.py #For Linux/Mac
py project.py     #For Windows
```

3. Wait a few minutes for data extraction from the internet.
![[Pasted image 20260314014218.png]]
4. When prompted, enter the city name as a filter
![[Pasted image 20260314015319.png]]

5. The list of active hackathons in that city will be displayed.
 ![[Pasted image 20260314015447.png]]

---
### Libraries Used:

- `requests` - To send HTTP get requests and fetch data.
- `re` - For extracting `build_id` in the case of **Devfolio**.
- `tqdm` - To show a real-time progress bar on the terminal while the program is running, as scraping multiple pages of data can take a few minutes.
- `datetime` - To handle the ISO 8601 string format of time commonly used in JSON.
- `time` - To add a delay of a few seconds between the HTTP requests so that platform's servers don't crash.


### Key Functions:

- **`get_build_id()`** Since **Devfolio** utilizes a **Next.js** architecture, a unique `build_id` string is required to access their data endpoints. Because this string changes frequently with new deployments, this function uses **Regular Expressions (RegEx)** to dynamically extract the current `build_id` from the site's source code.
    
- **`calculate_pages()`** **Unstop** distributes its hackathon listings across multiple pages. This function queries the API to determine the `last_page` count, ensuring the scraper covers the entire database.
    
- **`get_data(build_id, total_pages)`** The main engine of the program. It iterates through the determined pages, sending requests and collecting raw JSON data into two primary lists: `unstop_json_list` and `devfolio_json_list`.
    
- **`parse_json()`** This function processes the complex  JSON data and organizes it into a clean **list of dictionaries**. Each  dictionary represents a hackathon and contains  keys: `name`, `start`, `link`, and `college`, making the data easy to manipulate.
    
- **`filter_hack_list()`** This function filters the aggregated lists based on a specific city (e.g., **Mumbai**) taken as an input from the user.
    
- **`display_hack_list()`** It formats the filtered data and displays it into a attractive, human-readable layout in the terminal using **f-strings** and visual separators for a clean user experience.
  
### Ethical Considerations: 

