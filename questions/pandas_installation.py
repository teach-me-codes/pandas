questions = [
    {
        'Main question': 'What is Pandas and how is it used in data analysis?',
        'Explanation': 'The candidate should explain that Pandas is an open-source Python library used for data manipulation and analysis. It provides data structures like DataFrames to work with tabular data, supports reading and writing data from various file formats, and offers functionalities for data cleaning, transformation, and exploration.',
        'Follow-up questions': ['How does Pandas compare to NumPy in terms of data manipulation capabilities?', 'Can you explain the key components of a DataFrame in Pandas and their roles in data analysis?', 'In what scenarios would you choose Pandas over traditional data processing tools like Excel?']
    },
    {
        'Main question': 'What are the key data structures in Pandas and how are they used?',
        'Explanation': 'The candidate should discuss the primary data structures in Pandas, including Series and DataFrame, and their applications. Series represent one-dimensional labeled arrays, while DataFrames are two-dimensional data structures resembling tables that consist of rows and columns.',
        'Follow-up questions': ['How can you create a Series or DataFrame from existing data in Python?', 'What advantages do DataFrames offer over traditional spreadsheets for data analysis tasks?', 'Can you demonstrate how to access and manipulate specific elements within a DataFrame using Pandas?']
    },
    {
        'Main question': 'How can data be loaded into a Pandas DataFrame from different sources?',
        'Explanation': 'The candidate should explain the various methods available in Pandas to import data from sources such as CSV files, Excel spreadsheets, SQL databases, and web APIs. They should also mention the parameters and options that can be specified during the data loading process.',
        'Follow-up questions': ['What considerations should be taken into account when loading large datasets into a Pandas DataFrame?', 'Can you describe the differences between read_csv() and read_excel() functions in Pandas?', 'How can data cleansing techniques be applied after loading data into a DataFrame using Pandas?']
    },
    {
        'Main question': 'What are the common data manipulation tasks that can be performed using Pandas?',
        'Explanation': 'The candidate should elaborate on the data manipulation functionalities provided by Pandas, such as filtering rows, selecting columns, handling missing values, merging datasets, grouping data, and applying functions to data elements. They should also discuss the benefits of using these operations in data analysis workflows.',
        'Follow-up questions': ['How does the groupby() function in Pandas contribute to aggregating and analyzing data based on specific criteria?', 'What are the differences between merge() and join() operations in Pandas for combining datasets?', 'Can you explain the concept of method chaining in Pandas and its role in streamlining data manipulation processes?']
    },
    {
        'Main question': 'How does Pandas support data cleaning and preprocessing tasks?',
        'Explanation': 'The candidate should describe the tools and techniques in Pandas for data cleaning, including handling missing values, removing duplicates, converting data types, scaling or normalizing data, and encoding categorical variables. They should also discuss the importance of data preprocessing in improving model performance.',
        'Follow-up questions': ['What role does the fillna() function play in dealing with missing values in a DataFrame using Pandas?', 'How can outliers be identified and treated in a dataset using Pandas?', 'In what ways can feature scaling and normalization impact the training of machine learning models with Pandas?']
    },
    {
        'Main question': 'What are the capabilities of Pandas for data analysis and exploration?',
        'Explanation': 'The candidate should explain the functionalities in Pandas for performing descriptive statistics, data visualization, handling time series data, and executing complex data transformations. They should also discuss the benefits of using Pandas for exploratory data analysis and gaining insights from datasets.',
        'Follow-up questions': ['How can you generate summary statistics for numerical and categorical data columns in a DataFrame using Pandas?', 'What plotting libraries can be integrated with Pandas for data visualization tasks?', 'Can you demonstrate a practical example of using Pandas to analyze a time series dataset and extract meaningful information?']
    },
    {
        'Main question': 'How can data be exported from a Pandas DataFrame to different file formats?',
        'Explanation': 'The candidate should discuss the methods available in Pandas to export data from a DataFrame to formats like CSV, Excel, SQL databases, JSON, and HTML. They should also explain the parameters and options that can be used to customize the output file.',
        'Follow-up questions': ['What considerations should be made when exporting a large DataFrame to a CSV file in Pandas?', 'Can you illustrate the process of saving multiple DataFrame components into separate sheets in an Excel file using Pandas?', 'How does the to_sql() method in Pandas facilitate exporting data to a SQL database for further analysis?']
    },
    {
        'Main question': 'How does Pandas handle missing data and duplicates in a DataFrame?',
        'Explanation': 'The candidate should explain the methods offered by Pandas to detect and deal with missing values and duplicate rows in a DataFrame, such as isnull(), dropna(), fillna(), and drop_duplicates(). They should also emphasize the importance of data integrity and quality in data analysis.',
        'Follow-up questions': ['What are the potential risks and challenges associated with dropping rows containing missing values in a DataFrame using Pandas?', 'In what scenarios would you prioritize imputation over removal of missing values in a dataset with Pandas?', 'Can you discuss the impact of duplicate entries on statistical analysis and machine learning models when working with Pandas?']
    },
    {
        'Main question': 'How can you apply functions to elements within a DataFrame using Pandas?',
        'Explanation': 'The candidate should describe the methods for applying functions, lambda expressions, or custom operations to individual elements, rows, or columns within a DataFrame using Pandas. They should showcase how these techniques can facilitate complex data transformations and calculations.',
        'Follow-up questions': ['What are the advantages of using apply(), map(), and applymap() functions in Pandas for element-wise operations?', 'Can you explain the role of lambda functions in simplifying data manipulation tasks within a DataFrame?', 'How can custom functions be defined and applied to subsets of data in a DataFrame for specific analysis requirements with Pandas?']
    },
    {
        'Main question': 'What are the features and benefits of using Pandas for time series data analysis?',
        'Explanation': 'The candidate should highlight the specialized functionalities in Pandas for working with time series data, such as date/time indexing, resampling, shifting, rolling window operations, and time zone handling. They should explain how Pandas simplifies the manipulation and analysis of temporal data structures.',
        'Follow-up questions': ['How does the to_datetime() function in Pandas aid in converting string representations of dates into datetime objects?', 'What role does the dt accessor play in accessing and manipulating components of datetime-like Series in Pandas?', 'Can you demonstrate a practical example of performing rolling window calculations on time series data using Pandas?']
    },
    {
        'Main question': 'How can you combine and merge multiple DataFrames in Pandas?',
        'Explanation': 'The candidate should discuss the methods available in Pandas for combining DataFrames through concatenation, merging (joining) based on common columns or indices, and appending rows or columns. They should explain the parameters and options for customizing the merge operations in Pandas.',
        'Follow-up questions': ['What considerations should be taken into account when performing an inner, outer, left, or right merge on DataFrames in Pandas?', 'How can you handle overlapping column names in merged DataFrames to avoid conflicts or ambiguity?', 'In what scenarios would you use the concat() function versus the merge() function for combining datasets in Pandas?']
    }
]