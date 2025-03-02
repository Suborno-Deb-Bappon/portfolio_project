from django.shortcuts import render

def index(request):
    context = {
        'name': 'Suborno Deb Bappon',
        'summary': 'Computer Science graduate student with strong academic credentials and hands-on experience in software development and AI.',
        'contact': {
            'address': '103 Cumberland Avenue South, S7N 1L6, Saskatoon, SK, Canada',
            'phone': '639-916-1871',
            'email': 'subornodebbappon20@gmail.com',
            'linkedin': 'https://linkedin.com/in/suborno-deb-bappon',
            'github': 'https://github.com/Suborno-Deb-Bappon'
        }
    }
    return render(request, 'portfolio/index.html', context)

def about(request):
    context = {
        'summary': (
            'I am a Computer Science graduate student with a strong academic track record and hands-on experience in software development and AI. '
            'I am proficient in Python and passionate about solving complex problems with innovative solutions.'
        ),
        'technical_skills': ['Python', 'C++', 'C', 'PostgreSQL', 'HTML', 'CSS', 'JavaScript'],
        'technologies': ['scikit-learn', 'PyTorch', 'TensorFlow', 'Django', 'Flask', 'NumPy', 'Pandas', 'Git'],
        'tools': ['Microsoft VS Code', 'Jupyter Lab/Notebook', 'Spyder', 'Microsoft Power BI'],
        'research_interests': ['Machine Learning', 'Natural Language Processing', 'Software Engineering']
    }
    return render(request, 'portfolio/about.html', context)

def experience(request):
    context = {
        'experiences': [
            {
                'position': 'Graduate Research and Teaching Assistant',
                'company': 'Software Research Lab, University of Saskatchewan',
                'duration': 'Sept. 2023 – Aug. 2025 (Tentative)',
                'location': 'Saskatoon, SK',
                'details': []
            },
            {
                'position': 'Lecturer - Computer Science and Engineering',
                'company': 'Eastern University',
                'duration': 'Feb. 2023 – July 2023',
                'location': 'Dhaka, Bangladesh',
                'details': [
                    'Courses Instructed: Structured Programming, Data Structures, Database Management, Machine Learning, Web Programming'
                ]
            },
            {
                'position': 'Software Developer Intern',
                'company': 'Extreme Solutions Ltd.',
                'duration': 'Jan. 2022 – Feb. 2022',
                'location': 'Chattogram, Bangladesh',
                'details': [
                    'Assisted in software development and research using Agile methodologies.',
                    'Developed and optimized machine learning models using scikit-learn and Python for predictive analytics and automation.'
                ]
            }
        ]
    }
    return render(request, 'portfolio/experience.html', context)

def education(request):
    context = {
        'education': [
            {
                'degree': 'Master of Science Candidate - Computer Science',
                'institution': 'University of Saskatchewan',
                'duration': 'Sept. 2023 – Aug. 2025 (Tentative)',
                'grade': '89.5%',
                'details': 'Research Areas: Software Engineering, Generative AI. \n Thesis: Leveraging Context-Aware Large Language Models to Enhance the Quality and Usability of Technical Question-Answering Forums. \n Advisors: Dr. Kevin Schneider and Dr. Chanchal K. Roy.'
            },
            {
                'degree': 'Bachelor of Science - Computer Science and Engineering',
                'institution': 'Chittagong University of Engineering and Technology (CUET)',
                'duration': 'Feb. 2017 – Sept. 2022',
                'grade': '3.76/4.00 (Top 2% in the class)',
                'details': 'Thesis: Sentiment Analysis from Bengali Tech-Gadget Reviews Text using Deep Learning. \n Advisor: Dr. Muhammad Ibrahim Khan.'
            }
        ]
    }
    return render(request, 'portfolio/education.html', context)

def projects(request):
    context = {
        'projects': [
            # {
            #     'title': 'Browser Plugin for Enhanced Stack Overflow Answers',
            #     'description': 'Leveraging LLMs to integrate contextually relevant comment suggestions.',
            #     'tech_stack': 'Python, Flask, HTML, CSS, JavaScript'
            # },
            {
                'title': 'Context-Aware Inline Comments Plugin',
                'description': 'Built to generate inline comments for code snippets on Q&A platforms.',
                'tech_stack': 'Python, Flask, HTML, CSS, JavaScript'
            },
            {
                'title': 'Technical Debt Identification Plugin',
                'description': 'Utilized a transformer-based hybrid DeBERTa-CodeBERT model to identify code optimization-related technical debt discussions.',
                'tech_stack': 'PyTorch, Python, HTML, CSS, JavaScript'
            },
            {
                'title': 'ChatGPT Prompt Optimization Analysis',
                'description': 'Analyzed developer interactions to optimize multi-prompt cases for better response efficiency.',
                'tech_stack': 'Python libraries'
            },
            {
                'title': 'Deep Learning Framework for Sentiment Analysis',
                'description': 'Developed a CNN-BiLSTM model for sentiment analysis of Bengali tech-gadget reviews.',
                'tech_stack': 'TensorFlow, Python libraries'
            },
            {
                'title': 'Traffic Accident Prediction Framework',
                'description': 'Predicted accident frequency and peak hours, integrating Explainable AI for feature insights.',
                'tech_stack': 'scikit-learn, Python libraries'
            },
            {
                'title': 'E-library Application',
                'description': 'Allows users to search, borrow, and return e-books with catalogue filters and reviews.',
                'tech_stack': 'HTML, CSS, JavaScript, Django, SQLite'
            },
            {
                'title': 'Weather Dashboard',
                'description': 'Displays real-time weather data with API integration and dynamic visuals.',
                'tech_stack': 'HTML, CSS, JavaScript, Django, SQLite, Weather API'
            }
        ]
    }
    return render(request, 'portfolio/projects.html', context)

def publications(request):
    context = {
        'publications': [
            {
                'title': 'AUTOGENICS: Automated Generation of Context-Aware Inline Comments for Code Snippets on Programming Q&A Sites Using LLM',
                'details': 'IEEE SCAM 2024, pp. 24-35. \n Authors: Suborno Deb Bappon, Saikat Mondal, Banani Roy',
                'link': 'https://www.computer.org/csdl/proceedings-article/scam/2024/285000a024/22NQVK0OBiw'
            },
            {
                'title': 'Enhancing User Interaction in ChatGPT: Characterizing and Consolidating Multiple Prompts for Issue Resolution',
                'details': 'IEEE/ACM MSR 2024, pp. 222-226. \n Authors: Saikat Mondal, Suborno Deb Bappon, Chanchal K. Roy',
                'link': 'https://dl.acm.org/doi/10.1145/3643991.3645085'
            },
            {
                'title': 'Integrating CNNs for Microscopic Image Analysis in Leukemia Classification',
                'details': 'Systems and Soft Computing (2024), 6, 200121. \n Authors: Md. Samiul Alim, Suborno Deb Bappon, Shahriar Mahmud Sabuj, Md Jayedul Islam, Muhammad Masud Tarek, Md. Shafiul Azam, Md. Monirul Islam',
                'link': 'https://www.sciencedirect.com/science/article/pii/S2772941924000504'
            },
            {
                'title': 'Explainable Machine Learning for Drug Classification',
                'details': 'In 2023 International Conference on Electrical and Electronics Engineering, pp. 673-683. \n Authors: Krishna Mridha, Suborno Deb Bappon, Shahriar Mahmud Sabuj, Tasnim Sarker, Ankush Ghosh',
                'link': 'https://link.springer.com/chapter/10.1007/978-981-99-8661-3_48'
            },
            {
                'title': 'Attention U-Net: A Deep Learning Approach for Breast Cancer Segmentation',
                'details': 'In 2023 International Conference on Quantum Technologies (iQ-CCHESS), pp. 1-6. \n Authors: Krishna Mridha, Tasnim Sarker, Suborno Deb Bappon, Shahriar Mahmud Sabuj',
                'link': 'https://ieeexplore.ieee.org/abstract/document/10391674'
            },
            {
                'title': 'Classification of Tourism Reviews from Bengali Texts using Multinomial Naïve Bayes',
                'details': 'In 2022 25th International Conference on Computer and Information Technology (ICCIT), pp. 270-275. \n Authors: Suborno Deb Bappon, Asif Iqbal',
                'link': 'https://ieeexplore.ieee.org/abstract/document/10055560'
            },
            {
                'title': 'Sentiment Analysis of Bengali Texts on Tech Gadget Reviews using Machine Learning',
                'details': 'In 2022 25th ICCIT, pp. 324-329. \n Authors: Suborno Deb Bappon, Golam Sarwar Md. Mursalin, Muhammad Ibrahim Khan',
                'link': 'https://ieeexplore.ieee.org/abstract/document/10055639'
            },
            {
                'title': 'Toward a Machine Learning Approach to Predict the CO2 Rating of Fuel-Consuming Vehicles in Canada',
                'details': 'In 2022 25th ICCIT, pp. 384-389. \n Authors: Suborno Deb Bappon, Ashim Dey, Shahriar Mahmud Sabuj, Annesha Das',
                'link': 'https://ieeexplore.ieee.org/abstract/document/10054732'
            },
            {
                'title': 'A Deep Learning Approach for Recognizing Textual Emotion from Bengali-English Code-Mixed Data',
                'details': 'In 2022 25th ICCIT, pp. 330-335. \n Authors: Golam Sarwar Md Mursalin, Suborno Deb Bappon, Muhammad Ibrahim Khan',
                'link': 'https://ieeexplore.ieee.org/abstract/document/10054872'
            }
        ]
    }
    return render(request, 'portfolio/publications.html', context)

def certifications(request):
    context = {
        'certifications': [
            {
                'text': 'What is Data Science? (IBM)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/JNTMMY6M3AJB'
            },
            {
                'text': 'Data Analysis with Python (IBM)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/LP6JKEYBET4Y'
            },
            {
                'text': 'Machine Learning with Python (IBM)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/KHQDFVKE33X9'
            },
            {
                'text': 'Structuring Machine Learning Projects (DeepLearning.AI)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/X7X85463N656'
            },
            {
                'text': 'Introduction to Deep Learning & Neural Networks with Keras (IBM)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/RJXZR6TEZQRF'
            },
            {
                'text': 'Neural Networks & Deep Learning (DeepLearning.AI)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/LQJKNYGXW9UC'
            },
            {
                'text': 'Improving Deep Neural Networks: Hyperparameter Tuning, Regularization & Optimization (DeepLearning.AI)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/LMSPJ9VB9QYB'
            },
            {
                'text': 'Natural Language Processing with Classification & Vector Spaces (DeepLearning.AI)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/V4WSRZ9V74UJ'
            },
            {
                'text': 'Natural Language Processing with TensorFlow (DeepLearning.AI)',
                'link': 'https://www.coursera.org/account/accomplishments/certificate/LMG2VPLSBPMN'
            }
        ]
    }
    return render(request, 'portfolio/certifications.html', context)

def awards(request):
    context = {
        'awards': [
            'Nominee, Geddes Graduate Scholarship in Computer Science, University of Saskatchewan (Fall 2024)',
            'Best Research Award, CMPT 854: Human-Centric Software Renovation, University of Saskatchewan (Spring 2024)',
            '75th Anniversary Recruitment Scholarship, CGPS, University of Saskatchewan (Awarded for two years of Master’s program)',
            'Dean’s Award, Faculty of Electrical and Computer Engineering, CUET',
            'Merit Distinction: Topper for three consecutive semesters during junior and senior undergrad years, CUET'
        ]
    }
    return render(request, 'portfolio/awards.html', context)

def extracurricular(request):
    context = {
        'activities': [
            'Vice President Internal, Computer Science Graduate Council, University of Saskatchewan (Sept. 2024 – Present)',
            'Mentor, Eastern University Computing Club (May 2023 – July 2023)',
            'Finance Secretary, Notredamian Association, CUET (Aug. 2021 – Aug. 2022)',
            'Volunteer, ACM-ICPC Bangladesh CUET NCPC Provincial Programming Contest (March 2017)',
            'IT Secretary, Notre Dame Eco and Space Club (July 2015 – July 2016)',
            'Volunteer, Bangladesh Red Crescent Society, Mymensingh (Jan. 2011 – Jan. 2013)'
        ]
    }
    return render(request, 'portfolio/extracurricular.html', context)

def contact(request):
    context = {
        'contact': {
            'address': '103 Cumberland Avenue South, S7N 1L6, Saskatoon, SK, Canada',
            'phone': '639-916-1871',
            'email': 'subornodebbappon20@gmail.com',
            'linkedin': 'https://linkedin.com/in/suborno-deb-bappon',
            'github': 'https://github.com/Suborno-Deb-Bappon'
        }
    }
    return render(request, 'portfolio/contact.html', context)
