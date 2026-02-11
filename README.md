# Personal Data Analytics CLI 📊

A command-line productivity tracking application that helps you monitor your study hours, physical activity, mood, and correlations between them.

## Features ✨

- **📝 Add Entries**: Log daily productivity data (study hours, sport hours, mood level, notes)
- **👀 View Data**: Display all recorded entries with complete information
- **✏️  Update Entries**: Modify existing entries by ID
- **🗑️ Delete Entries**: Remove specific entries or entire database
- **📈 Analytics**: View comprehensive statistics including:
  - Total and average study hours
  - Best study day
  - Average mood rating
  - Correlation between study hours and mood
- **📊 Visualization**: Generate scatter plots showing the relationship between study hours and mood
- **🛡️ Data Validation**: Input validation for dates, hours, and mood ratings

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Personal-Data-Analytics-CLI.git
cd Personal-Data-Analytics-CLI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

Run the application:
```bash
python main.py
```

### Menu Options

1. **Add New Entry** - Record your daily productivity data
   - Date (YYYY-MM-DD format)
   - Study hours (0-24)
   - Sport hours (0-24)
   - Mood rating (1-10)
   - Optional note

2. **View All Entries** - Display all recorded data

3. **Update Existing Entry** - Modify an entry by ID

4. **Delete Entry** - Remove a specific entry

5. **View Statistics** - See analytics and visualizations
   - Total study time
   - Average study hours
   - Best study day
   - Average mood
   - Study-Mood correlation analysis
   - Scatter plot visualization

6. **Delete Database** - Remove all data (requires confirmation)

0. **Exit Application** - Close the program

## Data Format

### Date Input
- Format: `YYYY-MM-DD` (e.g., 2026-02-11)
- Validated to ensure correct format

### Hours Input
- Range: 0-24 (decimal values allowed, e.g., 2.5)
- Both study and sport hours are validated

### Mood Rating
- Range: 1-10 (integer only)
- 1 = Very bad, 10 = Excellent

## Database

Data is stored in `productivity.db` (SQLite database) in the application directory.

Database schema:
```
productivity table:
- id (INTEGER PRIMARY KEY)
- date (TEXT NOT NULL)
- study_hours (REAL 0-24)
- sport_hours (REAL 0-24)
- mood (INTEGER 1-10)
- note (TEXT optional)
```

## Project Structure

```
Personal Data Analytics CLI/
├── main.py           # Main application and CLI menu
├── database.py       # SQLite database operations
├── analytics.py      # Data analysis functions
├── visualization.py  # Matplotlib chart generation
├── productivity.db   # SQLite database (created on first run)
├── requirements.txt  # Project dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Features Details

### Analytics Functions
- **Correlation Analysis**: Calculates Pearson correlation between study hours and mood
- **Trend Detection**: Identifies your best study days and average performance
- **Motivation Insights**: Shows how your mood correlates with productivity

### Validation
- Date format validation (YYYY-MM-DD)
- Range validation for hours (0-24)
- Range validation for mood (1-10)
- Secure SQL queries (parameterized queries prevent SQL injection)

## Error Handling

The application includes comprehensive error handling for:
- Invalid input formats
- Database errors
- File operations
- Missing data scenarios

## Future Enhancements 🔮

- [ ] Export data to CSV
- [ ] Weekly/monthly reports
- [ ] Multiple visualization types
- [ ] Goal setting and tracking
- [ ] Data filtering by date range
- [ ] Performance metrics dashboard
- [ ] Unit tests
- [ ] Configuration file support

## Requirements

See [requirements.txt](requirements.txt)
- matplotlib>=3.5.0

## Author
Makhmud Barakhoev
Created as a personal productivity tracking project.

## Contributing

Feel free to fork this project and submit pull requests with improvements!

---

**Happy tracking! 📈**

