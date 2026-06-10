import json

def S(c, n, cr, cat):
    return {"course_code": c, "course_name": n, "credits": cr, "category": cat}
def SM(n, subs):
    return {"semester": n, "subjects": subs}
def C(i, n, d, y, cr, sems):
    return {"course_id": i, "course_name": n, "department": d,
            "duration_years": y, "total_credits": cr, "semesters": sems}

C1 = [S("21LEH101T","Professional English I",3,"HSMC"), S("21MAB101T","Calculus and Linear Algebra",4,"BSC"),
      S("21PYB101J","Engineering Physics",4,"BSC"), S("21CYB101J","Engineering Chemistry",4,"BSC"),
      S("21MES101L","Engineering Graphics and Design",3,"ESC"), S("21EES101J","Basic Electrical and Electronics Engineering",4,"ESC"),
      S("21CSC101J","Programming for Problem Solving",4,"ESC"), S("21PDM101L","Professional Skills and Practices",1,"MC"),
      S("21GNM101L","Physical and Mental Health using Yoga",1,"MC")]
C2 = [S("21LEH201T","Professional English II",3,"HSMC"), S("21MAB102T","Advanced Calculus and Complex Analysis",4,"BSC"),
      S("21PYB201J","Physics for Information Science",4,"BSC"), S("21MAB201T","Transforms and Boundary Value Problems",4,"BSC"),
      S("21MES102L","Engineering Mechanics",3,"ESC"), S("21MES103L","Engineering Practices Laboratory",2,"ESC"),
      S("21CSC102J","Object Oriented Programming using C++",4,"ESC"), S("21CYM101T","Environmental Science",2,"MC"),
      S("21LEM101T","Constitution of India",1,"MC")]
R1 = [S("21LEH101T","Professional English I",3,"HSMC"), S("21MAB101T","Calculus and Linear Algebra",4,"BSC"),
      S("21PYB101J","Engineering Physics",4,"BSC"), S("21CYB101J","Engineering Chemistry",4,"BSC"),
      S("21MES101L","Engineering Graphics and Design",3,"ESC"), S("21MEC101T","Basic Civil and Mechanical Engineering",3,"ESC"),
      S("21EES101J","Basic Electrical and Electronics Engineering",4,"ESC"), S("21PDM101L","Professional Skills and Practices",1,"MC"),
      S("21GNM101L","Physical and Mental Health using Yoga",1,"MC")]
R2 = [S("21LEH201T","Professional English II",3,"HSMC"), S("21MAB102T","Advanced Calculus and Complex Analysis",4,"BSC"),
      S("21MAB201T","Transforms and Partial Differential Equations",4,"BSC"), S("21PYB301T","Materials Science",3,"BSC"),
      S("21MES102L","Engineering Mechanics",3,"ESC"), S("21MES103L","Engineering Practices Laboratory",2,"ESC"),
      S("21MES104L","Basic Workshop Practice",2,"ESC"), S("21CYM101T","Environmental Science",2,"MC"),
      S("21LEM101T","Constitution of India",1,"MC")]
E1 = [S("21LEH101T","Professional English I",3,"HSMC"), S("21MAB101T","Calculus and Linear Algebra",4,"BSC"),
      S("21PYB101J","Engineering Physics",4,"BSC"), S("21CYB101J","Engineering Chemistry",4,"BSC"),
      S("21MES101L","Engineering Graphics and Design",3,"ESC"), S("21EES101J","Basic Electrical and Electronics Engineering",4,"ESC"),
      S("21EEC101T","Basic Electronics Engineering",3,"ESC"), S("21PDM101L","Professional Skills and Practices",1,"MC"),
      S("21GNM101L","Physical and Mental Health using Yoga",1,"MC")]
E2 = list(R2)
B1 = [S("21LEH101T","Professional English I",3,"HSMC"), S("21MAB101T","Calculus and Linear Algebra",4,"BSC"),
      S("21PYB101J","Engineering Physics",4,"BSC"), S("21CYB101J","Engineering Chemistry",4,"BSC"),
      S("21MES101L","Engineering Graphics and Design",3,"ESC"), S("21BIB101T","Basic Biology for Engineers",3,"BSC"),
      S("21EES101J","Basic Electrical and Electronics Engineering",3,"ESC"), S("21PDM101L","Professional Skills and Practices",1,"MC"),
      S("21GNM101L","Physical and Mental Health using Yoga",1,"MC")]
B2 = [S("21LEH201T","Professional English II",3,"HSMC"), S("21MAB102T","Advanced Calculus and Complex Analysis",4,"BSC"),
      S("21MAB201T","Transforms and Partial Differential Equations",4,"BSC"), S("21CYB301T","Chemistry of Materials",3,"BSC"),
      S("21MES102L","Engineering Mechanics",3,"ESC"), S("21MES103L","Engineering Practices Laboratory",2,"ESC"),
      S("21BIB102T","Biology for Engineers",2,"BSC"), S("21CYM101T","Environmental Science",2,"MC"),
      S("21LEM101T","Constitution of India",1,"MC")]

courses = []

courses.append(C("CSE","B.Tech Computer Science and Engineering","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CSC201J","Data Structures and Algorithms",4,"PCC"),S("21CSC202J","Operating Systems",4,"PCC"),S("21CSC203P","Advanced Programming Practice",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21PDM201L","Verbal Reasoning",1,"MC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CSC204J","Design and Analysis of Algorithms",4,"PCC"),S("21CSC205P","Database Management Systems",4,"PCC"),S("21CSC206T","Artificial Intelligence",3,"PCC"),S("21CSC301T","Formal Language and Automata",3,"PCC"),S("21CSC302J","Computer Networks",4,"PCC")]),
    SM(5,[S("21CSC303J","Software Engineering and Project Management",4,"PCC"),S("21CSC304J","Compiler Design",4,"PCC"),S("21CSC305P","Machine Learning",4,"PCC"),S("21CSE251T","Digital Image Processing",3,"PEC"),S("21CSO351T","Web Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CSE352T","Full Stack Web Development",3,"PEC"),S("21CSE354T","Augmented, Virtual and Mixed Reality",3,"PEC"),S("21CSE353T","Neuro Fuzzy and Genetic Programming",3,"PEC"),S("21CSO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CSP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CSE451T","Natural Language Processing",3,"PEC"),S("21CSE452T","Cloud Computing",3,"PEC"),S("21CSE453T","Cyber Security and Cryptography",3,"PEC"),S("21CSO353T","Mobile Application Development",3,"OEC"),S("21CSP701L","Major Project Phase I",4,"Project"),S("21CSI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CSE461T","Deep Learning",3,"PEC"),S("21CSE462T","Blockchain Technology",3,"PEC"),S("21CSP801L","Major Project Phase II",10,"Project"),S("21CSI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AIML","B.Tech CSE with Specialization in Artificial Intelligence and Machine Learning","Computational Intelligence",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AIC201J","Data Structures and Algorithms",4,"PCC"),S("21AIC202J","Operating Systems",4,"PCC"),S("21AIC203P","Python for Data Science",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21AIC204T","Foundations of Artificial Intelligence",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AIC205J","Design and Analysis of Algorithms",4,"PCC"),S("21AIC206P","Database Management Systems",4,"PCC"),S("21AIC207J","Machine Learning",4,"PCC"),S("21AIC301T","Computer Networks",3,"PCC"),S("21AIC208T","Data Visualization",3,"PCC")]),
    SM(5,[S("21AIC302J","Deep Learning",4,"PCC"),S("21AIC303J","Natural Language Processing",4,"PCC"),S("21AIE251T","Computer Vision",3,"PEC"),S("21AIE252T","Reinforcement Learning",3,"PEC"),S("21AIO351T","Introduction to Artificial Intelligence",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AIE351T","Generative AI",3,"PEC"),S("21AIE352T","Big Data Analytics",3,"PEC"),S("21AIE353T","Robotics and Automation",3,"PEC"),S("21AIO352T","Machine Learning for All",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AIE451T","Cognitive Computing",3,"PEC"),S("21AIE452T","Speech and Audio Processing",3,"PEC"),S("21AIE453T","Edge AI",3,"PEC"),S("21AIO353T","Soft Computing",3,"OEC"),S("21AIP701L","Major Project Phase I",4,"Project"),S("21AII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AIE461T","Explainable AI",3,"PEC"),S("21AIE462T","MLOps",3,"PEC"),S("21AIP801L","Major Project Phase II",10,"Project"),S("21AII801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("DS","B.Tech CSE with Specialization in Data Science","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21DSC201J","Data Structures and Algorithms",4,"PCC"),S("21DSC202J","Operating Systems",4,"PCC"),S("21DSC203P","Python for Data Analytics",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21DSC204T","Foundations of Data Science",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21DSC205J","Design and Analysis of Algorithms",4,"PCC"),S("21DSC206P","Database Management Systems",4,"PCC"),S("21DSC207J","Machine Learning",4,"PCC"),S("21DSC301T","Computer Networks",3,"PCC"),S("21DSC208T","Data Mining and Warehousing",3,"PCC")]),
    SM(5,[S("21DSC302J","Big Data Analytics",4,"PCC"),S("21DSE251T","Statistical Learning",3,"PEC"),S("21DSE252T","Data Visualization",3,"PEC"),S("21DSE253T","Time Series Analysis",3,"PEC"),S("21DSO351T","Data Analytics for All",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21DSE351T","Natural Language Processing",3,"PEC"),S("21DSE352T","Cloud Computing for Data Science",3,"PEC"),S("21DSE353T","Business Analytics",3,"PEC"),S("21DSO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21DSP601L","Minor Project",3,"Project")]),
    SM(7,[S("21DSE451T","Deep Learning",3,"PEC"),S("21DSE452T","Social Network Analysis",3,"PEC"),S("21DSE453T","Reinforcement Learning",3,"PEC"),S("21DSO353T","Convolutional Neural Networks Foundation",3,"OEC"),S("21DSP701L","Major Project Phase I",4,"Project"),S("21DSI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21DSE461T","MLOps and Model Deployment",3,"PEC"),S("21DSE462T","Data Engineering",3,"PEC"),S("21DSP801L","Major Project Phase II",10,"Project"),S("21DSI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("CSEC","B.Tech CSE with Specialization in Cyber Security","Networking and Communications",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21SCC201J","Data Structures and Algorithms",4,"PCC"),S("21SCC202J","Operating Systems",4,"PCC"),S("21SCC203P","Python for Security",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21SCC204T","Fundamentals of Cyber Security",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21SCC205J","Design and Analysis of Algorithms",4,"PCC"),S("21SCC206P","Database Management Systems",4,"PCC"),S("21SCC207J","Computer Networks",4,"PCC"),S("21SCC301T","Cryptography and Network Security",3,"PCC"),S("21SCC208T","Digital Forensics",3,"PCC")]),
    SM(5,[S("21SCC302J","Malware Analysis and Reverse Engineering",4,"PCC"),S("21SCE251T","Web Security",3,"PEC"),S("21SCE252T","Ethical Hacking",3,"PEC"),S("21SCE253T","Security Operations and SIEM",3,"PEC"),S("21CSO270T","Cyber Security",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21SCE351T","Cloud Security",3,"PEC"),S("21SCE352T","IoT Security",3,"PEC"),S("21SCE353T","Cyber Law and Ethics",3,"PEC"),S("21SCO351T","Network Security",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21SCP601L","Minor Project",3,"Project")]),
    SM(7,[S("21SCE451T","Application Security",3,"PEC"),S("21SCE452T","Blockchain Security",3,"PEC"),S("21SCE453T","AI for Cyber Security",3,"PEC"),S("21SCO352T","Fundamentals of Information System Security",3,"OEC"),S("21SCP701L","Major Project Phase I",4,"Project"),S("21SCI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21SCE461T","Cyber Threat Intelligence",3,"PEC"),S("21SCE462T","Penetration Testing",3,"PEC"),S("21SCP801L","Major Project Phase II",10,"Project"),S("21SCI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CC","B.Tech CSE with Specialization in Cloud Computing","Networking and Communications",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CCC201J","Data Structures and Algorithms",4,"PCC"),S("21CCC202J","Operating Systems",4,"PCC"),S("21CCC203P","Linux and Shell Programming",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21CCC204T","Fundamentals of Cloud Computing",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CCC205J","Design and Analysis of Algorithms",4,"PCC"),S("21CCC206P","Database Management Systems",4,"PCC"),S("21CCC207J","Computer Networks",4,"PCC"),S("21CCC301T","Cloud Architecture",3,"PCC"),S("21CCC208T","Virtualization Technologies",3,"PCC")]),
    SM(5,[S("21CCC302J","Cloud Security",4,"PCC"),S("21CCE251T","AWS Cloud Services",3,"PEC"),S("21CCE252T","Azure Cloud Services",3,"PEC"),S("21CCE253T","Docker and Kubernetes",3,"PEC"),S("21CCO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CCE351T","DevOps and CI/CD",3,"PEC"),S("21CCE352T","Cloud Native Application Development",3,"PEC"),S("21CCE353T","Multi-Cloud Management",3,"PEC"),S("21CCO352T","Data Analytics",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CCP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CCE451T","Cloud DevOps Engineering",3,"PEC"),S("21CCE452T","Serverless Computing",3,"PEC"),S("21CCE453T","Cloud Migration Strategies",3,"PEC"),S("21CCO353T","Machine Learning for All",3,"OEC"),S("21CCP701L","Major Project Phase I",4,"Project"),S("21CCI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CCE461T","Cloud Economics and Cost Management",3,"PEC"),S("21CCE462T","Edge and Fog Computing",3,"PEC"),S("21CCP801L","Major Project Phase II",10,"Project"),S("21CCI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IOT","B.Tech CSE with Specialization in Internet of Things","Networking and Communications",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IOC201J","Data Structures and Algorithms",4,"PCC"),S("21IOC202J","Operating Systems",4,"PCC"),S("21IOC203P","Embedded C Programming",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21IOC204T","Introduction to IoT",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21IOC205J","Design and Analysis of Algorithms",4,"PCC"),S("21IOC206P","Database Management Systems",4,"PCC"),S("21IOC207J","Computer Networks",4,"PCC"),S("21IOC301T","Wireless Sensor Networks",3,"PCC"),S("21IOC208T","Microcontrollers and Interfacing",3,"PCC")]),
    SM(5,[S("21IOC302J","IoT Security",4,"PCC"),S("21IOE251T","IoT Architecture and Protocols",3,"PEC"),S("21IOE252T","Cloud Computing for IoT",3,"PEC"),S("21IOE253T","RFID and NFC Technologies",3,"PEC"),S("21IOO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21IOE351T","Industrial IoT",3,"PEC"),S("21IOE352T","Smart City Applications",3,"PEC"),S("21IOE353T","Edge Computing",3,"PEC"),S("21IOO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21IOP601L","Minor Project",3,"Project")]),
    SM(7,[S("21IOE451T","IoT Data Analytics",3,"PEC"),S("21IOE452T","Mobile App Development for IoT",3,"PEC"),S("21IOE453T","AI for IoT",3,"PEC"),S("21IOO353T","Mobile Application Development",3,"OEC"),S("21IOP701L","Major Project Phase I",4,"Project"),S("21IOI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21IOE461T","IoT System Design",3,"PEC"),S("21IOE462T","Blockchain for IoT",3,"PEC"),S("21IOP801L","Major Project Phase II",10,"Project"),S("21IOI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IT","B.Tech Information Technology","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21ITC201J","Data Structures and Algorithms",4,"PCC"),S("21ITC202J","Operating Systems",4,"PCC"),S("21ITC203P","Java Programming",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21ITC204T","Web Technologies",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21ITC205J","Design and Analysis of Algorithms",4,"PCC"),S("21ITC206P","Database Management Systems",4,"PCC"),S("21ITC207J","Computer Networks",4,"PCC"),S("21ITC301T","Software Engineering",3,"PCC"),S("21ITC208T","UI/UX Design",3,"PCC")]),
    SM(5,[S("21ITC302J","Cloud Computing",4,"PCC"),S("21ITE251T","Cyber Security",3,"PEC"),S("21ITE252T","Data Mining",3,"PEC"),S("21ITE253T","Mobile Computing",3,"PEC"),S("21ITO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21ITE351T","Full Stack Web Development",3,"PEC"),S("21ITE352T","Big Data Analytics",3,"PEC"),S("21ITE353T","Information Security",3,"PEC"),S("21ITO352T","Machine Learning for All",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21ITP601L","Minor Project",3,"Project")]),
    SM(7,[S("21ITE451T","DevOps",3,"PEC"),S("21ITE452T","Blockchain Technology",3,"PEC"),S("21ITE453T","Artificial Intelligence",3,"PEC"),S("21ITO353T","Mobile Application Development",3,"OEC"),S("21ITP701L","Major Project Phase I",4,"Project"),S("21ITI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21ITE461T","Quantum Computing",3,"PEC"),S("21ITE462T","Digital Image Processing",3,"PEC"),S("21ITP801L","Major Project Phase II",10,"Project"),S("21ITI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("CSBS","B.Tech Computer Science and Business Systems","Computing Technologies",4,165,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CSC201J","Data Structures and Algorithms",4,"PCC"),S("21CSC202J","Operating Systems",4,"PCC"),S("21BSB201T","Principles of Management",3,"HSMC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21BSB202T","Business Communication",3,"HSMC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CSC205P","Database Management Systems",4,"PCC"),S("21BSB301T","Financial Management",3,"HSMC"),S("21BSB302T","Marketing Management",3,"HSMC"),S("21CSC301T","Formal Language and Automata",3,"PCC"),S("21CSC302J","Computer Networks",4,"PCC")]),
    SM(5,[S("21BSB401T","Human Resource Management",3,"HSMC"),S("21BSB402T","Business Analytics",3,"HSMC"),S("21BSB403T","Operations Management",3,"HSMC"),S("21CSC303J","Software Engineering and Project Management",4,"PCC"),S("21CSO351T","Web Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BSB451T","Enterprise Resource Planning",3,"HSMC"),S("21BSB452T","Strategic Management",3,"HSMC"),S("21BSB453T","Business Intelligence",3,"HSMC"),S("21CSO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BSP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BSB551T","Supply Chain Management",3,"HSMC"),S("21BSB552T","Digital Marketing",3,"HSMC"),S("21BSB553T","Data Visualization",3,"PCC"),S("21CSO353T","Mobile Application Development",3,"OEC"),S("21BSP701L","Major Project Phase I",4,"Project"),S("21BSI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BSB651T","Organizational Behaviour",3,"HSMC"),S("21BSB652T","E-Commerce",3,"HSMC"),S("21BSP801L","Major Project Phase II",10,"Project"),S("21BSI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CSE_NET","B.Tech CSE with Specialization in Computer Networking","Networking and Communications",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21NEC201J","Data Structures and Algorithms",4,"PCC"),S("21NEC202J","Operating Systems",4,"PCC"),S("21NEC203P","Network Programming with Python",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21NEC204T","Fundamentals of Computer Networks",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21NEC205J","Design and Analysis of Algorithms",4,"PCC"),S("21NEC206P","Database Management Systems",4,"PCC"),S("21NEC207J","Advanced Computer Networks",4,"PCC"),S("21NEC301T","Network Routing and Switching",3,"PCC"),S("21NEC208T","Network Security Fundamentals",3,"PCC")]),
    SM(5,[S("21NEC302J","Wireless and Mobile Networks",4,"PCC"),S("21NEE251T","Network Design and Implementation",3,"PEC"),S("21NEE252T","Software Defined Networking",3,"PEC"),S("21NEE253T","Network Management and Monitoring",3,"PEC"),S("21NEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21NEE351T","Cloud Networking",3,"PEC"),S("21NEE352T","Network Analytics",3,"PEC"),S("21NEE353T","IoT Networking",3,"PEC"),S("21NEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21NEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21NEE451T","Network Virtualization",3,"PEC"),S("21NEE452T","5G Networks",3,"PEC"),S("21NEE453T","Network Security Management",3,"PEC"),S("21NEO353T","Mobile Application Development",3,"OEC"),S("21NEP701L","Major Project Phase I",4,"Project"),S("21NEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21NEE461T","Data Center Networking",3,"PEC"),S("21NEE462T","Network Automation",3,"PEC"),S("21NEP801L","Major Project Phase II",10,"Project"),S("21NEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CSE_GAME","B.Tech CSE with Specialization in Gaming Technology","Computational Intelligence",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21GMC201J","Data Structures and Algorithms",4,"PCC"),S("21GMC202J","Operating Systems",4,"PCC"),S("21GMC203P","C++ for Game Development",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21GMC204T","Computer Graphics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21GMC205J","Design and Analysis of Algorithms",4,"PCC"),S("21GMC206P","Database Management Systems",4,"PCC"),S("21GMC207J","Computer Networks",4,"PCC"),S("21GMC301T","Game Design Fundamentals",3,"PCC"),S("21GMC208T","Mathematics for Game Development",3,"PCC")]),
    SM(5,[S("21GMC302J","Game Engine Architecture",4,"PCC"),S("21GME251T","2D Game Development",3,"PEC"),S("21GME252T","3D Modeling and Animation",3,"PEC"),S("21GME253T","Game Physics",3,"PEC"),S("21GMO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21GME351T","3D Game Development",3,"PEC"),S("21GME352T","Augmented and Virtual Reality",3,"PEC"),S("21GME353T","Game AI",3,"PEC"),S("21GMO352T","UI/UX Design",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21GMP601L","Minor Project",3,"Project")]),
    SM(7,[S("21GME451T","Multiplayer Game Development",3,"PEC"),S("21GME452T","Mobile Game Development",3,"PEC"),S("21GME453T","Game Testing and Quality Assurance",3,"PEC"),S("21GMO353T","Web Programming",3,"OEC"),S("21GMP701L","Major Project Phase I",4,"Project"),S("21GMI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21GME461T","Serious Games and Gamification",3,"PEC"),S("21GME462T","Game Audio and Sound Design",3,"PEC"),S("21GMP801L","Major Project Phase II",10,"Project"),S("21GMI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CSE_SE","B.Tech CSE with Specialization in Software Engineering","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21SEC201J","Data Structures and Algorithms",4,"PCC"),S("21SEC202J","Operating Systems",4,"PCC"),S("21SEC203P","Advanced Programming Practice",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21SEC204T","Software Engineering Fundamentals",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21SEC205J","Design and Analysis of Algorithms",4,"PCC"),S("21SEC206P","Database Management Systems",4,"PCC"),S("21SEC207J","Computer Networks",4,"PCC"),S("21SEC301T","Requirements Engineering",3,"PCC"),S("21SEC208T","Software Design and Architecture",3,"PCC")]),
    SM(5,[S("21SEC302J","Software Project Management",4,"PCC"),S("21SEE251T","Web Application Development",3,"PEC"),S("21SEE252T","Mobile Application Development",3,"PEC"),S("21SEE253T","Software Testing and Automation",3,"PEC"),S("21SEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21SEE351T","DevOps and Continuous Delivery",3,"PEC"),S("21SEE352T","Agile and Scrum Methodologies",3,"PEC"),S("21SEE353T","Cloud-Native Application Development",3,"PEC"),S("21SEO352T","UI/UX Design",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21SEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21SEE451T","Software Maintenance and Evolution",3,"PEC"),S("21SEE452T","Software Quality Management",3,"PEC"),S("21SEE453T","Secure Software Engineering",3,"PEC"),S("21SEO353T","Mobile Application Development",3,"OEC"),S("21SEP701L","Major Project Phase I",4,"Project"),S("21SEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21SEE461T","Software Analytics",3,"PEC"),S("21SEE462T","Software Entrepreneurship",3,"PEC"),S("21SEP801L","Major Project Phase II",10,"Project"),S("21SEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CSE_ITSPEC","B.Tech CSE with Specialization in Information Technology","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21ITC201J","Data Structures and Algorithms",4,"PCC"),S("21ITC202J","Operating Systems",4,"PCC"),S("21ITC203P","Java Programming",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21ITC204T","Web Technologies",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21ITC205J","Design and Analysis of Algorithms",4,"PCC"),S("21ITC206P","Database Management Systems",4,"PCC"),S("21ITC207J","Computer Networks",4,"PCC"),S("21ITC301T","Information Theory and Coding",3,"PCC"),S("21ITC208T","Data Mining",3,"PCC")]),
    SM(5,[S("21ITC302J","Cloud Computing",4,"PCC"),S("21ITE251T","Cyber Security",3,"PEC"),S("21ITE252T","Big Data Analytics",3,"PEC"),S("21ITE253T","Information Storage and Management",3,"PEC"),S("21ITO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21ITE351T","Enterprise Application Development",3,"PEC"),S("21ITE352T","IT Infrastructure Management",3,"PEC"),S("21ITE353T","Information Security Management",3,"PEC"),S("21ITO352T","Machine Learning for All",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21ITP601L","Minor Project",3,"Project")]),
    SM(7,[S("21ITE451T","IT Service Management",3,"PEC"),S("21ITE452T","Blockchain Technology",3,"PEC"),S("21ITE453T","Artificial Intelligence",3,"PEC"),S("21ITO353T","Mobile Application Development",3,"OEC"),S("21ITP701L","Major Project Phase I",4,"Project"),S("21ITI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21ITE461T","IT Governance and Compliance",3,"PEC"),S("21ITE462T","Digital Transformation",3,"PEC"),S("21ITP801L","Major Project Phase II",10,"Project"),S("21ITI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("CSE_BDA","B.Tech CSE with Specialization in Big Data Analytics","Computational Intelligence",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BDC201J","Data Structures and Algorithms",4,"PCC"),S("21BDC202J","Operating Systems",4,"PCC"),S("21BDC203P","Python for Data Analytics",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21BDC204T","Introduction to Big Data",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BDC205J","Design and Analysis of Algorithms",4,"PCC"),S("21BDC206P","Database Management Systems",4,"PCC"),S("21BDC207J","Computer Networks",4,"PCC"),S("21BDC301T","Data Warehousing and OLAP",3,"PCC"),S("21BDC208T","Data Mining Techniques",3,"PCC")]),
    SM(5,[S("21BDC302J","Hadoop and MapReduce",4,"PCC"),S("21BDE251T","Apache Spark",3,"PEC"),S("21BDE252T","NoSQL Databases",3,"PEC"),S("21BDE253T","Stream Data Processing",3,"PEC"),S("21BDO351T","Data Analytics for All",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BDE351T","Big Data Visualization",3,"PEC"),S("21BDE352T","Machine Learning for Big Data",3,"PEC"),S("21BDE353T","Cloud Computing for Big Data",3,"PEC"),S("21BDO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BDP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BDE451T","Big Data Security",3,"PEC"),S("21BDE452T","Deep Learning for Big Data",3,"PEC"),S("21BDE453T","Data Engineering and Pipelines",3,"PEC"),S("21BDO353T","Machine Learning for All",3,"OEC"),S("21BDP701L","Major Project Phase I",4,"Project"),S("21BDI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BDE461T","Big Data on Cloud",3,"PEC"),S("21BDE462T","DataOps",3,"PEC"),S("21BDP801L","Major Project Phase II",10,"Project"),S("21BDI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CSE_BC","B.Tech CSE with Specialization in Blockchain Technology","Computing Technologies",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BCC201J","Data Structures and Algorithms",4,"PCC"),S("21BCC202J","Operating Systems",4,"PCC"),S("21BCC203P","Python Programming",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21BCC204T","Fundamentals of Blockchain",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BCC205J","Design and Analysis of Algorithms",4,"PCC"),S("21BCC206P","Database Management Systems",4,"PCC"),S("21BCC207J","Computer Networks",4,"PCC"),S("21BCC301T","Cryptography and Consensus Algorithms",3,"PCC"),S("21BCC208T","Smart Contracts and Solidity",3,"PCC")]),
    SM(5,[S("21BCC302J","Decentralized Application Development",4,"PCC"),S("21BCE251T","Ethereum and Hyperledger",3,"PEC"),S("21BCE252T","Blockchain Security",3,"PEC"),S("21BCE253T","Token Economics",3,"PEC"),S("21BCO351T","Web Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BCE351T","Blockchain for Supply Chain",3,"PEC"),S("21BCE352T","Blockchain for Finance",3,"PEC"),S("21BCE353T","Decentralized Finance",3,"PEC"),S("21BCO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BCP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BCE451T","Blockchain Governance",3,"PEC"),S("21BCE452T","Blockchain Interoperability",3,"PEC"),S("21BCE453T","NFT and Metaverse",3,"PEC"),S("21BCO353T","Mobile Application Development",3,"OEC"),S("21BCP701L","Major Project Phase I",4,"Project"),S("21BCI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BCE461T","Zero Knowledge Proofs",3,"PEC"),S("21BCE462T","Blockchain Scalability",3,"PEC"),S("21BCP801L","Major Project Phase II",10,"Project"),S("21BCI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AI","B.Tech Artificial Intelligence","Computational Intelligence",4,162,[
    SM(1,C1),SM(2,C2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AIC201J","Data Structures and Algorithms",4,"PCC"),S("21AIC202J","Operating Systems",4,"PCC"),S("21AIC203P","Python for Data Science",3,"PCC"),S("21CSS201T","Computer Organization and Architecture",3,"ESC"),S("21AIC204T","Foundations of Artificial Intelligence",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AIC205J","Design and Analysis of Algorithms",4,"PCC"),S("21AIC206P","Database Management Systems",4,"PCC"),S("21AIC207J","Machine Learning",4,"PCC"),S("21AIC301T","Computer Networks",3,"PCC"),S("21AIC208T","Data Visualization",3,"PCC")]),
    SM(5,[S("21AIC302J","Deep Learning",4,"PCC"),S("21AIC303J","Natural Language Processing",4,"PCC"),S("21AIE251T","Computer Vision",3,"PEC"),S("21AIE252T","Reinforcement Learning",3,"PEC"),S("21AIO351T","Introduction to AI",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AIE351T","Generative AI",3,"PEC"),S("21AIE352T","Big Data Analytics",3,"PEC"),S("21AIE353T","Robotics and Automation",3,"PEC"),S("21AIO352T","Machine Learning for All",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AIE451T","Cognitive Computing",3,"PEC"),S("21AIE452T","Speech and Audio Processing",3,"PEC"),S("21AIE453T","Edge AI",3,"PEC"),S("21AIO353T","Soft Computing",3,"OEC"),S("21AIP701L","Major Project Phase I",4,"Project"),S("21AII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AIE461T","Explainable AI",3,"PEC"),S("21AIE462T","MLOps",3,"PEC"),S("21AIP801L","Major Project Phase II",10,"Project"),S("21AII801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE","B.Tech Electronics and Communication Engineering","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21ECC201T","Electronic Devices and Circuits",3,"PCC"),S("21ECC202J","Digital Logic Design",4,"PCC"),S("21ECC203P","Circuit Analysis and Simulation",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21ECC204T","Signals and Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21ECC205J","Analog Communication",4,"PCC"),S("21ECC206P","Microprocessors and Microcontrollers",4,"PCC"),S("21ECC207J","Analog and Digital Circuits Lab",4,"PCC"),S("21ECC301T","Electromagnetic Fields",3,"PCC"),S("21ECC208T","Digital Signal Processing",3,"PCC")]),
    SM(5,[S("21ECC302J","Digital Communication",4,"PCC"),S("21ECC303P","VLSI Design",4,"PCC"),S("21ECE251T","Antenna and Wave Propagation",3,"PEC"),S("21ECE252T","Embedded Systems",3,"PEC"),S("21ECO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21ECE351T","Wireless Communication",3,"PEC"),S("21ECE352T","Optical Communication",3,"PEC"),S("21ECE353T","IoT and Applications",3,"PEC"),S("21ECO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21ECP601L","Minor Project",3,"Project")]),
    SM(7,[S("21ECE451T","Microwave Engineering",3,"PEC"),S("21ECE452T","Radar and Navigation Systems",3,"PEC"),S("21ECE453T","Satellite Communication",3,"PEC"),S("21ECO353T","Machine Learning for All",3,"OEC"),S("21ECP701L","Major Project Phase I",4,"Project"),S("21ECI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21ECE461T","5G Communication Systems",3,"PEC"),S("21ECE462T","Cognitive Radio",3,"PEC"),S("21ECP801L","Major Project Phase II",10,"Project"),S("21ECI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE_DS","B.Tech ECE with Specialization in Data Sciences","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21EDS201J","Electronic Devices and Circuits",4,"PCC"),S("21EDS202J","Digital Logic Design",4,"PCC"),S("21EDS203P","Python for Data Analysis",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21EDS204T","Signals and Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21EDS205J","Database Management Systems",4,"PCC"),S("21EDS206P","Microprocessors and Microcontrollers",4,"PCC"),S("21EDS207J","Data Mining and Warehousing",4,"PCC"),S("21EDS301T","Digital Communication",3,"PCC"),S("21EDS208T","Machine Learning Fundamentals",3,"PCC")]),
    SM(5,[S("21EDS302J","Big Data Analytics",4,"PCC"),S("21EDE251T","Data Visualization",3,"PEC"),S("21EDE252T","Statistical Learning",3,"PEC"),S("21EDE253T","Time Series Analysis",3,"PEC"),S("21EDO351T","Web Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21EDE351T","Deep Learning",3,"PEC"),S("21EDE352T","Natural Language Processing",3,"PEC"),S("21EDE353T","Cloud Data Engineering",3,"PEC"),S("21EDO352T","Python Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21EDP601L","Minor Project",3,"Project")]),
    SM(7,[S("21EDE451T","Data Science for IoT",3,"PEC"),S("21EDE452T","Reinforcement Learning",3,"PEC"),S("21EDE453T","Computer Vision",3,"PEC"),S("21EDO353T","Machine Learning for All",3,"OEC"),S("21EDP701L","Major Project Phase I",4,"Project"),S("21EDI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21EDE461T","MLOps",3,"PEC"),S("21EDE462T","Data Engineering",3,"PEC"),S("21EDP801L","Major Project Phase II",10,"Project"),S("21EDI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE_CPS","B.Tech ECE with Specialization in Cyber-Physical Systems","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CPS201J","Electronic Devices and Circuits",4,"PCC"),S("21CPS202J","Digital Logic Design",4,"PCC"),S("21CPS203P","Embedded C Programming",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21CPS204T","Introduction to Cyber-Physical Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CPS205J","Microcontrollers and Interfacing",4,"PCC"),S("21CPS206P","Operating Systems",4,"PCC"),S("21CPS207J","Computer Networks",4,"PCC"),S("21CPS301T","Real-Time Systems",3,"PCC"),S("21CPS208T","Sensor Networks",3,"PCC")]),
    SM(5,[S("21CPS302J","Control Systems for CPS",4,"PCC"),S("21CPE251T","IoT Architecture and Design",3,"PEC"),S("21CPE252T","Cloud Computing for CPS",3,"PEC"),S("21CPE253T","CPS Security",3,"PEC"),S("21CPO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CPE351T","Edge Computing",3,"PEC"),S("21CPE352T","Machine Learning for CPS",3,"PEC"),S("21CPE353T","Digital Twin Technology",3,"PEC"),S("21CPO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CPP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CPE451T","Autonomous Systems",3,"PEC"),S("21CPE452T","CPS Data Analytics",3,"PEC"),S("21CPE453T","Industrial CPS",3,"PEC"),S("21CPO353T","Mobile Application Development",3,"OEC"),S("21CPP701L","Major Project Phase I",4,"Project"),S("21CPI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CPE461T","CPS Design and Verification",3,"PEC"),S("21CPE462T","Human-Cyber-Physical Systems",3,"PEC"),S("21CPP801L","Major Project Phase II",10,"Project"),S("21CPI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("ECE_VLSI","B.Tech Electronics Engineering VLSI Design and Technology","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21VLC201J","Electronic Devices and Circuits",4,"PCC"),S("21VLC202J","Digital Logic Design",4,"PCC"),S("21VLC203P","Circuit Simulation and Analysis",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21VLC204T","Semiconductor Physics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21VLC205J","Microprocessors and Microcontrollers",4,"PCC"),S("21VLC206P","Verilog and FPGA Design",4,"PCC"),S("21VLC207J","Analog Integrated Circuits",4,"PCC"),S("21VLC301T","Digital Signal Processing",3,"PCC"),S("21VLC208T","CMOS VLSI Design",3,"PCC")]),
    SM(5,[S("21VLC302J","VLSI Fabrication Technology",4,"PCC"),S("21VLE251T","ASIC Design",3,"PEC"),S("21VLE252T","Low Power VLSI Design",3,"PEC"),S("21VLE253T","VLSI Testing and Verification",3,"PEC"),S("21VLO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21VLE351T","Analog VLSI Design",3,"PEC"),S("21VLE352T","RF VLSI Design",3,"PEC"),S("21VLE353T","System on Chip Design",3,"PEC"),S("21VLO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21VLP601L","Minor Project",3,"Project")]),
    SM(7,[S("21VLE451T","Advanced VLSI Design",3,"PEC"),S("21VLE452T","Memory Design and Technology",3,"PEC"),S("21VLE453T","VLSI Signal Processing",3,"PEC"),S("21VLO353T","Machine Learning for All",3,"OEC"),S("21VLP701L","Major Project Phase I",4,"Project"),S("21VLI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21VLE461T","Mixed Signal VLSI Design",3,"PEC"),S("21VLE462T","Nanoelectronics",3,"PEC"),S("21VLP801L","Major Project Phase II",10,"Project"),S("21VLI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE_EMB","B.Tech Electronics and Computer Engineering","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21EMC201J","Electronic Devices and Circuits",4,"PCC"),S("21EMC202J","Digital Logic Design",4,"PCC"),S("21EMC203P","Programming for Problem Solving",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21EMC204T","Data Structures and Algorithms",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21EMC205J","Microprocessors and Microcontrollers",4,"PCC"),S("21EMC206P","Operating Systems",4,"PCC"),S("21EMC207J","Computer Organization and Architecture",4,"PCC"),S("21EMC301T","Embedded Systems",3,"PCC"),S("21EMC208T","Database Management Systems",3,"PCC")]),
    SM(5,[S("21EMC302J","Computer Networks",4,"PCC"),S("21EME251T","Embedded Linux",3,"PEC"),S("21EME252T","IoT and Edge Computing",3,"PEC"),S("21EME253T","Digital Signal Processing",3,"PEC"),S("21EMO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21EME351T","Real-Time Operating Systems",3,"PEC"),S("21EME352T","Embedded Machine Learning",3,"PEC"),S("21EME353T","Automotive Embedded Systems",3,"PEC"),S("21EMO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21EMP601L","Minor Project",3,"Project")]),
    SM(7,[S("21EME451T","Hardware-Software Co-Design",3,"PEC"),S("21EME452T","Embedded Security",3,"PEC"),S("21EME453T","Wireless Embedded Systems",3,"PEC"),S("21EMO353T","Mobile Application Development",3,"OEC"),S("21EMP701L","Major Project Phase I",4,"Project"),S("21EMI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21EME461T","Embedded AI",3,"PEC"),S("21EME462T","FPGA Based System Design",3,"PEC"),S("21EMP801L","Major Project Phase II",10,"Project"),S("21EMI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE_EIE","B.Tech Electronics and Instrumentation Engineering","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21EIC201J","Electronic Devices and Circuits",4,"PCC"),S("21EIC202J","Digital Logic Design",4,"PCC"),S("21EIC203P","Circuit Analysis and Simulation",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21EIC204T","Electrical Measurements",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21EIC205J","Transducers and Sensors",4,"PCC"),S("21EIC206P","Microprocessors and Microcontrollers",4,"PCC"),S("21EIC207J","Analog and Digital Instrumentation",4,"PCC"),S("21EIC301T","Control Systems",3,"PCC"),S("21EIC208T","Industrial Instrumentation",3,"PCC")]),
    SM(5,[S("21EIC302J","Biomedical Instrumentation",4,"PCC"),S("21EIE251T","Process Control",3,"PEC"),S("21EIE252T","Virtual Instrumentation",3,"PEC"),S("21EIE253T","Robotics and Automation",3,"PEC"),S("21EIO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21EIE351T","Smart Sensors and IoT",3,"PEC"),S("21EIE352T","Instrumentation System Design",3,"PEC"),S("21EIE353T","Data Acquisition Systems",3,"PEC"),S("21EIO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21EIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21EIE451T","Industrial IoT",3,"PEC"),S("21EIE452T","Machine Learning for Instrumentation",3,"PEC"),S("21EIE453T","Nano Instrumentation",3,"PEC"),S("21EIO353T","Mobile Application Development",3,"OEC"),S("21EIP701L","Major Project Phase I",4,"Project"),S("21EII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21EIE461T","Optical Instrumentation",3,"PEC"),S("21EIE462T","Aerospace Instrumentation",3,"PEC"),S("21EIP801L","Major Project Phase II",10,"Project"),S("21EII801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ECE_ECOMM","B.Tech Electronics Communication Engineering","Electronics and Communication Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21ECM201J","Electronic Devices and Circuits",4,"PCC"),S("21ECM202J","Digital Logic Design",4,"PCC"),S("21ECM203P","Circuit Analysis and Simulation",3,"PCC"),S("21ECS201T","Network Theory",3,"ESC"),S("21ECM204T","Signals and Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21ECM205J","Analog Communication",4,"PCC"),S("21ECM206P","Microprocessors and Microcontrollers",4,"PCC"),S("21ECM207J","Analog and Digital Circuits Lab",4,"PCC"),S("21ECM301T","Electromagnetic Fields",3,"PCC"),S("21ECM208T","Digital Signal Processing",3,"PCC")]),
    SM(5,[S("21ECM302J","Digital Communication",4,"PCC"),S("21ECM303P","Communication Networks",4,"PCC"),S("21ECM251T","Antenna and Wave Propagation",3,"PEC"),S("21ECM252T","RF and Microwave Engineering",3,"PEC"),S("21ECO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21ECM351T","Wireless Communication",3,"PEC"),S("21ECM352T","Optical Communication",3,"PEC"),S("21ECM353T","Satellite Communication",3,"PEC"),S("21ECO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21ECP601L","Minor Project",3,"Project")]),
    SM(7,[S("21ECM451T","Microwave Engineering",3,"PEC"),S("21ECM452T","Radar Systems",3,"PEC"),S("21ECM453T","Mobile Communication",3,"PEC"),S("21ECO353T","Machine Learning for All",3,"OEC"),S("21ECP701L","Major Project Phase I",4,"Project"),S("21ECI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21ECM461T","5G Communication Systems",3,"PEC"),S("21ECM462T","Cognitive Radio",3,"PEC"),S("21ECP801L","Major Project Phase II",10,"Project"),S("21ECI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("EEE","B.Tech Electrical and Electronics Engineering","Electrical and Electronics Engineering",4,165,[
    SM(1,E1),SM(2,E2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21EEC201J","Electric Circuit Analysis",4,"PCC"),S("21EEC202J","Electromagnetic Fields",4,"PCC"),S("21EEC203P","Electronic Devices and Circuits",3,"PCC"),S("21EES201T","Electrical Machines I",3,"ESC"),S("21EEC204T","Network Theory",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21EEC205J","Electrical Machines II",4,"PCC"),S("21EEC206P","Power Systems",4,"PCC"),S("21EEC207J","Power Electronics",4,"PCC"),S("21EEC301T","Control Systems",3,"PCC"),S("21EEC208T","Digital Logic and Microprocessors",3,"PCC")]),
    SM(5,[S("21EEC302J","Power System Analysis",4,"PCC"),S("21EEE251T","Renewable Energy Systems",3,"PEC"),S("21EEE252T","High Voltage Engineering",3,"PEC"),S("21EEE253T","Electrical Drives",3,"PEC"),S("21EEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21EEE351T","Smart Grid Technology",3,"PEC"),S("21EEE352T","Protection and Switchgear",3,"PEC"),S("21EEE353T","Electric Vehicle Technology",3,"PEC"),S("21EEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21EEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21EEE451T","Power Quality",3,"PEC"),S("21EEE452T","HVDC and FACTS",3,"PEC"),S("21EEE453T","Energy Management and Audit",3,"PEC"),S("21EEO353T","Machine Learning for All",3,"OEC"),S("21EEP701L","Major Project Phase I",4,"Project"),S("21EEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21EEE461T","Electrical Energy Conservation",3,"PEC"),S("21EEE462T","Advanced Power Electronics",3,"PEC"),S("21EEP801L","Major Project Phase II",10,"Project"),S("21EEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("EVT","B.Tech Electric Vehicle Technology","Automobile Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21EVC201J","Electric Circuit Analysis",4,"PCC"),S("21EVC202J","Automotive Systems",4,"PCC"),S("21EVC203P","Power Electronics Fundamentals",3,"PCC"),S("21EVS201T","Engineering Thermodynamics",3,"ESC"),S("21EVC204T","Electric Vehicle Architecture",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21EVC205J","Battery Management Systems",4,"PCC"),S("21EVC206P","Motor and Drive Systems",4,"PCC"),S("21EVC207J","Control Systems for EV",4,"PCC"),S("21EVC301T","EV Charging Infrastructure",3,"PCC"),S("21EVC208T","Embedded Systems for EV",3,"PCC")]),
    SM(5,[S("21EVC302J","Vehicle Dynamics",4,"PCC"),S("21EVE251T","Energy Storage Systems",3,"PEC"),S("21EVE252T","EV Power Electronics",3,"PEC"),S("21EVE253T","Automotive Control Systems",3,"PEC"),S("21EVO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21EVE351T","EV Design and Simulation",3,"PEC"),S("21EVE352T","EV Standards and Certification",3,"PEC"),S("21EVE353T","Connected EV Technology",3,"PEC"),S("21EVO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21EVP601L","Minor Project",3,"Project")]),
    SM(7,[S("21EVE451T","Autonomous Electric Vehicles",3,"PEC"),S("21EVE452T","EV Fleet Management",3,"PEC"),S("21EVE453T","Wireless Power Transfer",3,"PEC"),S("21EVO353T","Machine Learning for All",3,"OEC"),S("21EVP701L","Major Project Phase I",4,"Project"),S("21EVI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21EVE461T","EV System Integration",3,"PEC"),S("21EVE462T","Sustainable Mobility",3,"PEC"),S("21EVP801L","Major Project Phase II",10,"Project"),S("21EVI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("ME","B.Tech Mechanical Engineering","Mechanical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MEC201J","Engineering Mechanics",4,"PCC"),S("21MEC202J","Fluid Mechanics and Machinery",4,"PCC"),S("21MEC203P","Thermodynamics Lab",3,"PCC"),S("21MES201T","Materials Science and Engineering",3,"ESC"),S("21MEC204T","Machine Drawing",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MEC205J","Heat and Mass Transfer",4,"PCC"),S("21MEC206P","Manufacturing Technology",4,"PCC"),S("21MEC207J","Strength of Materials",4,"PCC"),S("21MEC301T","Theory of Machines",3,"PCC"),S("21MEC208T","CAD/CAM",3,"PCC")]),
    SM(5,[S("21MEC302J","Design of Machine Elements",4,"PCC"),S("21MEE251T","Robotics",3,"PEC"),S("21MEE252T","Automobile Engineering",3,"PEC"),S("21MEE253T","Power Plant Engineering",3,"PEC"),S("21MEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MEE351T","Computational Fluid Dynamics",3,"PEC"),S("21MEE352T","Finite Element Analysis",3,"PEC"),S("21MEE353T","Industrial Engineering and Management",3,"PEC"),S("21MEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MEE451T","Additive Manufacturing",3,"PEC"),S("21MEE452T","Refrigeration and Air Conditioning",3,"PEC"),S("21MEE453T","Renewable Energy Systems",3,"PEC"),S("21MEO353T","Machine Learning for All",3,"OEC"),S("21MEP701L","Major Project Phase I",4,"Project"),S("21MEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MEE461T","Design of Thermal Systems",3,"PEC"),S("21MEE462T","Mechatronics",3,"PEC"),S("21MEP801L","Major Project Phase II",10,"Project"),S("21MEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ME_AIML","B.Tech Mechanical Engineering with Specialization in AI and ML","Mechanical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MAM201J","Engineering Mechanics",4,"PCC"),S("21MAM202J","Fluid Mechanics and Machinery",4,"PCC"),S("21MAM203P","Python for Mechanical Engineers",3,"PCC"),S("21MES201T","Materials Science and Engineering",3,"ESC"),S("21MAM204T","Data Structures and Algorithms",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MAM205J","Heat and Mass Transfer",4,"PCC"),S("21MAM206P","Machine Learning",4,"PCC"),S("21MAM207J","Strength of Materials",4,"PCC"),S("21MAM301T","CAD/CAM",3,"PCC"),S("21MAM208T","Data Analytics",3,"PCC")]),
    SM(5,[S("21MAM302J","Deep Learning",4,"PCC"),S("21MAE251T","Computer Vision",3,"PEC"),S("21MAE252T","Robotics and Automation",3,"PEC"),S("21MAE253T","Digital Twin Technology",3,"PEC"),S("21MAO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MAE351T","Predictive Maintenance",3,"PEC"),S("21MAE352T","Smart Manufacturing",3,"PEC"),S("21MAE353T","IoT and Industry 4.0",3,"PEC"),S("21MAO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MAP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MAE451T","Reinforcement Learning",3,"PEC"),S("21MAE452T","Finite Element Analysis",3,"PEC"),S("21MAE453T","Computational Fluid Dynamics",3,"PEC"),S("21MAO353T","Machine Learning for All",3,"OEC"),S("21MAP701L","Major Project Phase I",4,"Project"),S("21MAI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MAE461T","Natural Language Processing",3,"PEC"),S("21MAE462T","Advanced Robotics",3,"PEC"),S("21MAP801L","Major Project Phase II",10,"Project"),S("21MAI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("ME_AR","B.Tech Mechanical Engineering with Specialization in Automotive Robotics","Mechanical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MAR201J","Engineering Mechanics",4,"PCC"),S("21MAR202J","Fluid Mechanics and Machinery",4,"PCC"),S("21MAR203P","Thermodynamics Lab",3,"PCC"),S("21MES201T","Materials Science and Engineering",3,"ESC"),S("21MAR204T","Introduction to Robotics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MAR205J","Heat and Mass Transfer",4,"PCC"),S("21MAR206P","Automotive Systems",4,"PCC"),S("21MAR207J","Strength of Materials",4,"PCC"),S("21MAR301T","Theory of Machines",3,"PCC"),S("21MAR208T","Robot Kinematics and Dynamics",3,"PCC")]),
    SM(5,[S("21MAR302J","Design of Machine Elements",4,"PCC"),S("21MAE251T","Industrial Robotics",3,"PEC"),S("21MAE252T","Automobile Engineering",3,"PEC"),S("21MAE253T","Robotic Vision",3,"PEC"),S("21MAO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MAE351T","Robot Programming and Control",3,"PEC"),S("21MAE352T","Collaborative Robots",3,"PEC"),S("21MAE353T","Additive Manufacturing",3,"PEC"),S("21MAO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MAP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MAE451T","Autonomous Vehicles",3,"PEC"),S("21MAE452T","Robot Operating System",3,"PEC"),S("21MAE453T","Swarm Robotics",3,"PEC"),S("21MAO353T","Machine Learning for All",3,"OEC"),S("21MAP701L","Major Project Phase I",4,"Project"),S("21MAI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MAE461T","Advanced Robotics",3,"PEC"),S("21MAE462T","Humanoid Robotics",3,"PEC"),S("21MAP801L","Major Project Phase II",10,"Project"),S("21MAI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AE","B.Tech Aerospace Engineering","Aerospace Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AEC201J","Aerodynamics I",4,"PCC"),S("21AEC202J","Aircraft Structures I",4,"PCC"),S("21AEC203P","Thermodynamics Lab",3,"PCC"),S("21AES201T","Engineering Mechanics",3,"ESC"),S("21AEC204T","Introduction to Aerospace Engineering",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AEC205J","Aerodynamics II",4,"PCC"),S("21AEC206P","Aircraft Structures II",4,"PCC"),S("21AEC207J","Propulsion I",4,"PCC"),S("21AEC301T","Flight Mechanics",3,"PCC"),S("21AEC208T","Aircraft Materials",3,"PCC")]),
    SM(5,[S("21AEC302J","Propulsion II",4,"PCC"),S("21AEE251T","Space Flight Mechanics",3,"PEC"),S("21AEE252T","Computational Fluid Dynamics",3,"PEC"),S("21AEE253T","Aircraft Design",3,"PEC"),S("21AEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AEE351T","Finite Element Methods",3,"PEC"),S("21AEE352T","Rocket and Missile Technology",3,"PEC"),S("21AEE353T","Wind Tunnel Testing",3,"PEC"),S("21AEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AEE451T","Satellite Technology",3,"PEC"),S("21AEE452T","Aircraft Stability and Control",3,"PEC"),S("21AEE453T","Hypersonic Aerodynamics",3,"PEC"),S("21AEO353T","Machine Learning for All",3,"OEC"),S("21AEP701L","Major Project Phase I",4,"Project"),S("21AEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AEE461T","Unmanned Aerial Vehicles",3,"PEC"),S("21AEE462T","Composite Materials for Aerospace",3,"PEC"),S("21AEP801L","Major Project Phase II",10,"Project"),S("21AEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AU","B.Tech Automobile Engineering","Automobile Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AUC201J","Engineering Mechanics",4,"PCC"),S("21AUC202J","Thermodynamics",4,"PCC"),S("21AUC203P","Fluid Mechanics Lab",3,"PCC"),S("21AUS201T","Materials Science",3,"ESC"),S("21AUC204T","Automotive Engines",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AUC205J","Automotive Chassis",4,"PCC"),S("21AUC206P","Vehicle Dynamics",4,"PCC"),S("21AUC207J","Heat and Mass Transfer",4,"PCC"),S("21AUC301T","Manufacturing Technology",3,"PCC"),S("21AUC208T","Automotive Electrical Systems",3,"PCC")]),
    SM(5,[S("21AUC302J","Design of Automotive Systems",4,"PCC"),S("21AUE251T","Automotive Transmission",3,"PEC"),S("21AUE252T","Vehicle Maintenance",3,"PEC"),S("21AUE253T","Two and Three Wheeler Technology",3,"PEC"),S("21AUO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AUE351T","Automotive Pollution and Control",3,"PEC"),S("21AUE352T","Alternative Fuels and Energy Systems",3,"PEC"),S("21AUE353T","Vehicle Safety and Ergonomics",3,"PEC"),S("21AUO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AUP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AUE451T","Electric and Hybrid Vehicles",3,"PEC"),S("21AUE452T","Automotive Testing",3,"PEC"),S("21AUE453T","Automotive NVH",3,"PEC"),S("21AUO353T","Machine Learning for All",3,"OEC"),S("21AUP701L","Major Project Phase I",4,"Project"),S("21AUI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AUE461T","Autonomous Vehicles",3,"PEC"),S("21AUE462T","Motor Vehicle Insurance and Accident Analysis",3,"PEC"),S("21AUP801L","Major Project Phase II",10,"Project"),S("21AUI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("AU_AE","B.Tech Automobile Engineering with Specialization in Automotive Electronics","Automobile Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AUA201J","Engineering Mechanics",4,"PCC"),S("21AUA202J","Thermodynamics",4,"PCC"),S("21AUA203P","Electronic Devices and Circuits",3,"PCC"),S("21AUS201T","Materials Science",3,"ESC"),S("21AUA204T","Automotive Electronics I",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AUA205J","Digital Electronics",4,"PCC"),S("21AUA206P","Microcontrollers",4,"PCC"),S("21AUA207J","Automotive Engines",4,"PCC"),S("21AUA301T","Automotive Electronics II",3,"PCC"),S("21AUA208T","Sensor and Actuator Systems",3,"PCC")]),
    SM(5,[S("21AUA302J","Embedded Systems for Automotive",4,"PCC"),S("21AUA251T","Automotive Control Systems",3,"PEC"),S("21AUA252T","Vehicle Diagnostics",3,"PEC"),S("21AUA253T","Automotive Networking",3,"PEC"),S("21AUO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AUA351T","ADAS",3,"PEC"),S("21AUA352T","Vehicle to Everything",3,"PEC"),S("21AUA353T","Electric Vehicle Electronics",3,"PEC"),S("21AUO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AUP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AUA451T","Autonomous Driving Systems",3,"PEC"),S("21AUA452T","Automotive Cybersecurity",3,"PEC"),S("21AUA453T","Automotive Software Engineering",3,"PEC"),S("21AUO353T","Machine Learning for All",3,"OEC"),S("21AUP701L","Major Project Phase I",4,"Project"),S("21AUI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AUA461T","Automotive IoV",3,"PEC"),S("21AUA462T","Functional Safety",3,"PEC"),S("21AUP801L","Major Project Phase II",10,"Project"),S("21AUI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AU_GARC","B.Tech Automobile Engineering with Specialization in Green and Automotive Research and Consulting","Automobile Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AUG201J","Engineering Mechanics",4,"PCC"),S("21AUG202J","Thermodynamics",4,"PCC"),S("21AUG203P","Fluid Mechanics Lab",3,"PCC"),S("21AUS201T","Materials Science",3,"ESC"),S("21AUG204T","Sustainable Automotive Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AUG205J","Automotive Engines",4,"PCC"),S("21AUG206P","Alternative Fuels Lab",4,"PCC"),S("21AUG207J","Heat and Mass Transfer",4,"PCC"),S("21AUG301T","Vehicle Dynamics",3,"PCC"),S("21AUG208T","Environmental Impact Assessment",3,"PCC")]),
    SM(5,[S("21AUG302J","Green Vehicle Design",4,"PCC"),S("21AUG251T","Carbon Footprint Analysis",3,"PEC"),S("21AUG252T","Energy Management and Audit",3,"PEC"),S("21AUG253T","Life Cycle Assessment",3,"PEC"),S("21AUO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AUG351T","Sustainable Supply Chain",3,"PEC"),S("21AUG352T","Circular Economy",3,"PEC"),S("21AUG353T","Green Manufacturing",3,"PEC"),S("21AUO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AUP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AUG451T","Emission Control Technologies",3,"PEC"),S("21AUG452T","Climate Change and Policy",3,"PEC"),S("21AUG453T","Renewable Energy Systems",3,"PEC"),S("21AUO353T","Machine Learning for All",3,"OEC"),S("21AUP701L","Major Project Phase I",4,"Project"),S("21AUI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AUG461T","Hydrogen Economy",3,"PEC"),S("21AUG462T","Sustainable Transportation",3,"PEC"),S("21AUP801L","Major Project Phase II",10,"Project"),S("21AUI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("AU_ARAI","B.Tech Automobile Engineering with Specialization in Automotive Research and AI","Automobile Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21AUR201J","Engineering Mechanics",4,"PCC"),S("21AUR202J","Thermodynamics",4,"PCC"),S("21AUR203P","Python for Automotive",3,"PCC"),S("21AUS201T","Materials Science",3,"ESC"),S("21AUR204T","Automotive Systems",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21AUR205J","Data Structures",4,"PCC"),S("21AUR206P","Machine Learning",4,"PCC"),S("21AUR207J","Automotive Engines",4,"PCC"),S("21AUR301T","Vehicle Dynamics",3,"PCC"),S("21AUR208T","Deep Learning",3,"PCC")]),
    SM(5,[S("21AUR302J","Computer Vision",4,"PCC"),S("21AUR251T","Natural Language Processing",3,"PEC"),S("21AUR252T","Reinforcement Learning",3,"PEC"),S("21AUR253T","Autonomous Vehicle Algorithms",3,"PEC"),S("21AUO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21AUR351T","Robotics and Automation",3,"PEC"),S("21AUR352T","Edge AI for Automotive",3,"PEC"),S("21AUR353T","Generative AI for Design",3,"PEC"),S("21AUO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21AUP601L","Minor Project",3,"Project")]),
    SM(7,[S("21AUR451T","Explainable AI",3,"PEC"),S("21AUR452T","MLOps",3,"PEC"),S("21AUR453T","Speech and Audio Processing",3,"PEC"),S("21AUO353T","Machine Learning for All",3,"OEC"),S("21AUP701L","Major Project Phase I",4,"Project"),S("21AUI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21AUR461T","Advanced Autonomous Driving",3,"PEC"),S("21AUR462T","AI in Motorsports",3,"PEC"),S("21AUP801L","Major Project Phase II",10,"Project"),S("21AUI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("MCT","B.Tech Mechatronics Engineering","Mechatronics Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MCT201J","Engineering Mechanics",4,"PCC"),S("21MCT202J","Thermodynamics",4,"PCC"),S("21MCT203P","Electronic Devices and Circuits",3,"PCC"),S("21MCT204T","Digital Logic Design",3,"PCC"),S("21MCT205T","Sensors and Transducers",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MCT206J","Microcontrollers and Embedded Systems",4,"PCC"),S("21MCT207P","Fluid Power Systems",4,"PCC"),S("21MCT208J","Control Systems",4,"PCC"),S("21MCT301T","Mechanical Design",3,"PCC"),S("21MCT209T","Robot Modeling",3,"PCC")]),
    SM(5,[S("21MCT302J","Industrial Robotics",4,"PCC"),S("21MCE251T","PLC and SCADA",3,"PEC"),S("21MCE252T","MEMS and Microsystems",3,"PEC"),S("21MCE253T","Computer Integrated Manufacturing",3,"PEC"),S("21MCO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MCE351T","Machine Vision",3,"PEC"),S("21MCE352T","Industrial IoT",3,"PEC"),S("21MCE353T","Additive Manufacturing",3,"PEC"),S("21MCO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MCP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MCE451T","Autonomous Systems",3,"PEC"),S("21MCE452T","Hydraulic and Pneumatic Systems",3,"PEC"),S("21MCE453T","Drives and Control",3,"PEC"),S("21MCO353T","Machine Learning for All",3,"OEC"),S("21MCP701L","Major Project Phase I",4,"Project"),S("21MCI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MCE461T","Advanced Robotics",3,"PEC"),S("21MCE462T","Smart Materials",3,"PEC"),S("21MCP801L","Major Project Phase II",10,"Project"),S("21MCI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("MCT_ROBO","B.Tech Mechatronics with Specialization in Robotics","Mechatronics Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MRB201J","Engineering Mechanics",4,"PCC"),S("21MRB202J","Thermodynamics",4,"PCC"),S("21MRB203P","Electronic Devices and Circuits",3,"PCC"),S("21MRB204T","Digital Logic Design",3,"PCC"),S("21MRB205T","Introduction to Robotics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MRB206J","Microcontrollers and Embedded Systems",4,"PCC"),S("21MRB207P","Robot Kinematics",4,"PCC"),S("21MRB208J","Control Systems",4,"PCC"),S("21MRB301T","Sensors and Actuators",3,"PCC"),S("21MRB209T","Manufacturing Technology",3,"PCC")]),
    SM(5,[S("21MRB302J","Robot Dynamics and Control",4,"PCC"),S("21MRE251T","Robot Operating System",3,"PEC"),S("21MRE252T","Machine Vision",3,"PEC"),S("21MRE253T","Industrial Robotics",3,"PEC"),S("21MRO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MRE351T","Collaborative Robots",3,"PEC"),S("21MRE352T","Mobile Robotics",3,"PEC"),S("21MRE353T","AI for Robotics",3,"PEC"),S("21MRO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MRP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MRE451T","Swarm Robotics",3,"PEC"),S("21MRE452T","Medical Robotics",3,"PEC"),S("21MRE453T","Underwater Robotics",3,"PEC"),S("21MRO353T","Machine Learning for All",3,"OEC"),S("21MRP701L","Major Project Phase I",4,"Project"),S("21MRI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MRE461T","Humanoid Robotics",3,"PEC"),S("21MRE462T","Space Robotics",3,"PEC"),S("21MRP801L","Major Project Phase II",10,"Project"),S("21MRI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("MCT_ADT","B.Tech Mechatronics with Specialization in Advanced Digital Twin","Mechatronics Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MAD201J","Engineering Mechanics",4,"PCC"),S("21MAD202J","Thermodynamics",4,"PCC"),S("21MAD203P","Python for Engineers",3,"PCC"),S("21MAD204T","Digital Logic Design",3,"PCC"),S("21MAD205T","Data Structures",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MAD206J","Microcontrollers and Embedded Systems",4,"PCC"),S("21MAD207P","CAD and 3D Modeling",4,"PCC"),S("21MAD208J","Control Systems",4,"PCC"),S("21MAD301T","IoT and Edge Computing",3,"PCC"),S("21MAD209T","Cloud Computing",3,"PCC")]),
    SM(5,[S("21MAD302J","Digital Twin Architecture",4,"PCC"),S("21MDE251T","Simulation and Modeling",3,"PEC"),S("21MDE252T","Data Analytics",3,"PEC"),S("21MDE253T","Machine Learning",3,"PEC"),S("21MDO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MDE351T","AR/VR for Digital Twin",3,"PEC"),S("21MDE352T","Predictive Maintenance",3,"PEC"),S("21MDE353T","Industrial IoT",3,"PEC"),S("21MDO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MDP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MDE451T","Smart Manufacturing",3,"PEC"),S("21MDE452T","Digital Twin for Energy",3,"PEC"),S("21MDE453T","Cyber-Physical Systems",3,"PEC"),S("21MDO353T","Machine Learning for All",3,"OEC"),S("21MDP701L","Major Project Phase I",4,"Project"),S("21MDI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MDE461T","Digital Twin for Healthcare",3,"PEC"),S("21MDE462T","Blockchain for Digital Twin",3,"PEC"),S("21MDP801L","Major Project Phase II",10,"Project"),S("21MDI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("MCT_IMT","B.Tech Mechatronics with Specialization in Industrial and Medical Technology","Mechatronics Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MIM201J","Engineering Mechanics",4,"PCC"),S("21MIM202J","Thermodynamics",4,"PCC"),S("21MIM203P","Electronic Devices and Circuits",3,"PCC"),S("21MIM204T","Digital Logic Design",3,"PCC"),S("21MIM205T","Biomedical Sensors",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MIM206J","Microcontrollers and Embedded Systems",4,"PCC"),S("21MIM207P","Fluid Power Systems",4,"PCC"),S("21MIM208J","Control Systems",4,"PCC"),S("21MIM301T","Medical Device Design",3,"PCC"),S("21MIM209T","Industrial Automation",3,"PCC")]),
    SM(5,[S("21MIM302J","Robotics in Healthcare",4,"PCC"),S("21MIE251T","Rehabilitation Engineering",3,"PEC"),S("21MIE252T","PLC and SCADA",3,"PEC"),S("21MIE253T","Medical Imaging",3,"PEC"),S("21MIO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MIE351T","Prosthetics and Orthotics",3,"PEC"),S("21MIE352T","Industrial IoT",3,"PEC"),S("21MIE353T","Machine Vision",3,"PEC"),S("21MIO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MIE451T","AI in Healthcare",3,"PEC"),S("21MIE452T","Smart Manufacturing",3,"PEC"),S("21MIE453T","Biomechatronics",3,"PEC"),S("21MIO353T","Machine Learning for All",3,"OEC"),S("21MIP701L","Major Project Phase I",4,"Project"),S("21MII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MIE461T","Surgical Robotics",3,"PEC"),S("21MIE462T","Industry 5.0",3,"PEC"),S("21MIP801L","Major Project Phase II",10,"Project"),S("21MII801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("MCT_IIOT","B.Tech Mechatronics with Specialization in Industrial IoT","Mechatronics Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21MIT201J","Engineering Mechanics",4,"PCC"),S("21MIT202J","Thermodynamics",4,"PCC"),S("21MIT203P","Python for IoT",3,"PCC"),S("21MIT204T","Digital Logic Design",3,"PCC"),S("21MIT205T","Introduction to IoT",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21MIT206J","Microcontrollers and Embedded Systems",4,"PCC"),S("21MIT207P","Sensor Networks",4,"PCC"),S("21MIT208J","Computer Networks",4,"PCC"),S("21MIT301T","Cloud Computing",3,"PCC"),S("21MIT209T","Wireless Communication",3,"PCC")]),
    SM(5,[S("21MIT302J","Industrial IoT Architecture",4,"PCC"),S("21MIE251T","Edge Computing",3,"PEC"),S("21MIE252T","IoT Security",3,"PEC"),S("21MIE253T","Data Analytics for IoT",3,"PEC"),S("21MIO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21MIE351T","PLC and SCADA",3,"PEC"),S("21MIE352T","Digital Twin",3,"PEC"),S("21MIE353T","Big Data Analytics",3,"PEC"),S("21MIO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21MIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21MIE451T","Industry 4.0",3,"PEC"),S("21MIE452T","Smart Grid Technology",3,"PEC"),S("21MIE453T","Machine Learning for IoT",3,"PEC"),S("21MIO353T","Machine Learning for All",3,"OEC"),S("21MIP701L","Major Project Phase I",4,"Project"),S("21MII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21MIE461T","5G for IoT",3,"PEC"),S("21MIE462T","Blockchain for IoT",3,"PEC"),S("21MIP801L","Major Project Phase II",10,"Project"),S("21MII801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CE","B.Tech Civil Engineering","Civil Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CEC201J","Mechanics of Solids",4,"PCC"),S("21CEC202J","Fluid Mechanics",4,"PCC"),S("21CEC203P","Building Materials Lab",3,"PCC"),S("21CES201T","Surveying",3,"ESC"),S("21CEC204T","Engineering Geology",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CEC205J","Structural Analysis I",4,"PCC"),S("21CEC206P","Concrete Technology",4,"PCC"),S("21CEC207J","Geotechnical Engineering",4,"PCC"),S("21CEC301T","Transportation Engineering",3,"PCC"),S("21CEC208T","Environmental Engineering I",3,"PCC")]),
    SM(5,[S("21CEC302J","Structural Analysis II",4,"PCC"),S("21CEE251T","Design of Steel Structures",3,"PEC"),S("21CEE252T","Water Resources Engineering",3,"PEC"),S("21CEE253T","Environmental Engineering II",3,"PEC"),S("21CEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CEE351T","Earthquake Engineering",3,"PEC"),S("21CEE352T","Foundation Engineering",3,"PEC"),S("21CEE353T","Construction Management",3,"PEC"),S("21CEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CEE451T","Prestressed Concrete",3,"PEC"),S("21CEE452T","Bridge Engineering",3,"PEC"),S("21CEE453T","Remote Sensing and GIS",3,"PEC"),S("21CEO353T","Machine Learning for All",3,"OEC"),S("21CEP701L","Major Project Phase I",4,"Project"),S("21CEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CEE461T","Finite Element Methods",3,"PEC"),S("21CEE462T","Smart Cities and Urban Planning",3,"PEC"),S("21CEP801L","Major Project Phase II",10,"Project"),S("21CEI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("CE_CA","B.Tech Civil Engineering with Specialization in Computer Applications","Civil Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CEC201J","Mechanics of Solids",4,"PCC"),S("21CEC202J","Fluid Mechanics",4,"PCC"),S("21CEC203P","Python for Civil Engineers",3,"PCC"),S("21CES201T","Surveying",3,"ESC"),S("21CEC204T","Data Structures",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CEC205J","Structural Analysis I",4,"PCC"),S("21CEC206P","Database Management Systems",4,"PCC"),S("21CEC207J","Geotechnical Engineering",4,"PCC"),S("21CEC301T","Transportation Engineering",3,"PCC"),S("21CEC208T","Concrete Technology",3,"PCC")]),
    SM(5,[S("21CEC302J","Structural Analysis II",4,"PCC"),S("21CEE251T","BIM and CAD",3,"PEC"),S("21CEE252T","Machine Learning for Civil",3,"PEC"),S("21CEE253T","Computer Networks",3,"PEC"),S("21CEO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CEE351T","Web Development for Engineering",3,"PEC"),S("21CEE352T","IoT in Construction",3,"PEC"),S("21CEE353T","Data Analytics",3,"PEC"),S("21CEO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CEP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CEE451T","Software Project Management",3,"PEC"),S("21CEE452T","GIS Programming",3,"PEC"),S("21CEE453T","Digital Twin for Infrastructure",3,"PEC"),S("21CEO353T","Machine Learning for All",3,"OEC"),S("21CEP701L","Major Project Phase I",4,"Project"),S("21CEI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CEE461T","Cloud Computing for Civil",3,"PEC"),S("21CEE462T","AI in Structural Engineering",3,"PEC"),S("21CEP801L","Major Project Phase II",10,"Project"),S("21CEI801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("CH","B.Tech Chemical Engineering","Chemical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21CHC201J","Chemical Process Calculations",4,"PCC"),S("21CHC202J","Fluid Mechanics",4,"PCC"),S("21CHC203P","Mechanical Operations",3,"PCC"),S("21CHS201T","Engineering Chemistry II",3,"ESC"),S("21CHC204T","Chemical Thermodynamics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21CHC205J","Heat Transfer",4,"PCC"),S("21CHC206P","Mass Transfer I",4,"PCC"),S("21CHC207J","Chemical Reaction Engineering I",4,"PCC"),S("21CHC301T","Process Instrumentation",3,"PCC"),S("21CHC208T","Material Science",3,"PCC")]),
    SM(5,[S("21CHC302J","Mass Transfer II",4,"PCC"),S("21CHE251T","Chemical Reaction Engineering II",3,"PEC"),S("21CHE252T","Process Dynamics and Control",3,"PEC"),S("21CHE253T","Transport Phenomena",3,"PEC"),S("21CHO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21CHE351T","Process Equipment Design",3,"PEC"),S("21CHE352T","Petroleum Refinery Engineering",3,"PEC"),S("21CHE353T","Environmental Engineering",3,"PEC"),S("21CHO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21CHP601L","Minor Project",3,"Project")]),
    SM(7,[S("21CHE451T","Process Plant Safety",3,"PEC"),S("21CHE452T","Biochemical Engineering",3,"PEC"),S("21CHE453T","Process Optimization",3,"PEC"),S("21CHO353T","Machine Learning for All",3,"OEC"),S("21CHP701L","Major Project Phase I",4,"Project"),S("21CHI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21CHE461T","Polymer Engineering",3,"PEC"),S("21CHE462T","Nano Technology",3,"PEC"),S("21CHP801L","Major Project Phase II",10,"Project"),S("21CHI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("BM","B.Tech Biomedical Engineering","Biomedical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BMC201J","Human Anatomy and Physiology",4,"PCC"),S("21BMC202J","Electronic Devices and Circuits",4,"PCC"),S("21BMC203P","Biomedical Instrumentation Lab",3,"PCC"),S("21BMS201T","Biochemistry",3,"ESC"),S("21BMC204T","Sensors and Measurements",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BMC205J","Digital Electronics",4,"PCC"),S("21BMC206P","Microcontrollers",4,"PCC"),S("21BMC207J","Biomaterials",4,"PCC"),S("21BMC301T","Medical Imaging",3,"PCC"),S("21BMC208T","Biomechanics",3,"PCC")]),
    SM(5,[S("21BMC302J","Biomedical Signal Processing",4,"PCC"),S("21BME251T","Medical Image Processing",3,"PEC"),S("21BME252T","Prosthetics and Orthotics",3,"PEC"),S("21BME253T","Physiological Modeling",3,"PEC"),S("21BMO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BME351T","AI in Healthcare",3,"PEC"),S("21BME352T","Rehabilitation Engineering",3,"PEC"),S("21BME353T","Biofluid Mechanics",3,"PEC"),S("21BMO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BMP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BME451T","Medical Device Design",3,"PEC"),S("21BME452T","Neural Engineering",3,"PEC"),S("21BME453T","Tissue Engineering",3,"PEC"),S("21BMO353T","Machine Learning for All",3,"OEC"),S("21BMP701L","Major Project Phase I",4,"Project"),S("21BMI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BME461T","Biophotonics",3,"PEC"),S("21BME462T","Robot-Assisted Surgery",3,"PEC"),S("21BMP801L","Major Project Phase II",10,"Project"),S("21BMI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("BM_MI","B.Tech Biomedical Engineering with Specialization in Medical Informatics","Biomedical Engineering",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BMI201J","Human Anatomy and Physiology",4,"PCC"),S("21BMI202J","Electronic Devices and Circuits",4,"PCC"),S("21BMI203P","Python for Biomedical",3,"PCC"),S("21BMS201T","Biochemistry",3,"ESC"),S("21BMI204T","Data Structures",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BMI205J","Database Management Systems",4,"PCC"),S("21BMI206P","Microcontrollers",4,"PCC"),S("21BMI207J","Medical Imaging",4,"PCC"),S("21BMI301T","Clinical Data Management",3,"PCC"),S("21BMI208T","Biomedical Instrumentation",3,"PCC")]),
    SM(5,[S("21BMI302J","Machine Learning for Healthcare",4,"PCC"),S("21BIE251T","Medical Image Analytics",3,"PEC"),S("21BIE252T","Health Informatics",3,"PEC"),S("21BIE253T","Bioinformatics",3,"PEC"),S("21BIO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BIE351T","Deep Learning in Healthcare",3,"PEC"),S("21BIE352T","Telemedicine Technology",3,"PEC"),S("21BIE353T","Natural Language Processing",3,"PEC"),S("21BIO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BIP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BIE451T","Predictive Healthcare Analytics",3,"PEC"),S("21BIE452T","Edge AI for Healthcare",3,"PEC"),S("21BIE453T","Wearable Technology",3,"PEC"),S("21BIO353T","Machine Learning for All",3,"OEC"),S("21BIP701L","Major Project Phase I",4,"Project"),S("21BII701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BIE461T","Clinical Decision Support",3,"PEC"),S("21BIE462T","Genomic Data Analysis",3,"PEC"),S("21BIP801L","Major Project Phase II",10,"Project"),S("21BII801L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("BT_CB","B.Tech Biotechnology with Specialization in Computational Biology","Bio Technology",4,165,[
    SM(1,B1),SM(2,B2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BTC201J","Cell Biology",4,"PCC"),S("21BTC202J","Biochemistry",4,"PCC"),S("21BTC203P","Bioinformatics Lab",3,"PCC"),S("21BTS201T","Genetics",3,"ESC"),S("21BTC204T","Introduction to Computational Biology",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BTC205J","Molecular Biology",4,"PCC"),S("21BTC206P","Data Structures and Algorithms",4,"PCC"),S("21BTC207J","Immunology",4,"PCC"),S("21BTC301T","Bioprocess Engineering",3,"PCC"),S("21BTC208T","Machine Learning for Biology",3,"PCC")]),
    SM(5,[S("21BTC302J","Genome Analysis",4,"PCC"),S("21BTE251T","Structural Bioinformatics",3,"PEC"),S("21BTE252T","Systems Biology",3,"PEC"),S("21BTE253T","Pharmacogenomics",3,"PEC"),S("21BTO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BTE351T","Deep Learning in Bioinformatics",3,"PEC"),S("21BTE352T","Proteomics",3,"PEC"),S("21BTE353T","Network Biology",3,"PEC"),S("21BTO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BTP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BTE451T","Drug Discovery and Design",3,"PEC"),S("21BTE452T","Metagenomics",3,"PEC"),S("21BTE453T","Cancer Informatics",3,"PEC"),S("21BTO353T","Machine Learning for All",3,"OEC"),S("21BTP701L","Major Project Phase I",4,"Project"),S("21BTI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BTE461T","Single Cell Analysis",3,"PEC"),S("21BTE462T","Ethical and Regulatory Affairs",3,"PEC"),S("21BTP801L","Major Project Phase II",10,"Project"),S("21BTI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("BT_FT","B.Tech Biotechnology with Specialization in Fermentation Technology","Bio Technology",4,165,[
    SM(1,B1),SM(2,B2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BTF201J","Cell Biology",4,"PCC"),S("21BTF202J","Biochemistry",4,"PCC"),S("21BTF203P","Microbiology Lab",3,"PCC"),S("21BTS201T","Genetics",3,"ESC"),S("21BTF204T","Industrial Microbiology",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BTF205J","Molecular Biology",4,"PCC"),S("21BTF206P","Bioprocess Engineering",4,"PCC"),S("21BTF207J","Immunology",4,"PCC"),S("21BTF301T","Fermentation Technology",3,"PCC"),S("21BTF208T","Enzyme Engineering",3,"PCC")]),
    SM(5,[S("21BTF302J","Downstream Processing",4,"PCC"),S("21BFE251T","Bioprocess Optimization",3,"PEC"),S("21BFE252T","Food Biotechnology",3,"PEC"),S("21BFE253T","Bioprocess Modeling",3,"PEC"),S("21BFO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BFE351T","Biofuel Technology",3,"PEC"),S("21BFE352T","Pharmaceutical Biotechnology",3,"PEC"),S("21BFE353T","Wastewater Treatment",3,"PEC"),S("21BFO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BFP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BFE451T","Bioreactor Design",3,"PEC"),S("21BFE452T","Metabolic Engineering",3,"PEC"),S("21BFE453T","Protein Engineering",3,"PEC"),S("21BFO353T","Machine Learning for All",3,"OEC"),S("21BFP701L","Major Project Phase I",4,"Project"),S("21BFI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BFE461T","Industrial Biotechnology",3,"PEC"),S("21BFE462T","Regulatory Affairs in Biotech",3,"PEC"),S("21BFP801L","Major Project Phase II",10,"Project"),S("21BFI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("BT_RM","B.Tech Biotechnology with Specialization in Regenerative Medicine","Bio Technology",4,165,[
    SM(1,B1),SM(2,B2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BTR201J","Cell Biology",4,"PCC"),S("21BTR202J","Biochemistry",4,"PCC"),S("21BTR203P","Histology Lab",3,"PCC"),S("21BTS201T","Genetics",3,"ESC"),S("21BTR204T","Introduction to Stem Cells",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BTR205J","Molecular Biology",4,"PCC"),S("21BTR206P","Cell Culture Technology",4,"PCC"),S("21BTR207J","Immunology",4,"PCC"),S("21BTR301T","Tissue Engineering",3,"PCC"),S("21BTR208T","Biomaterials",3,"PCC")]),
    SM(5,[S("21BTR302J","Stem Cell Biology",4,"PCC"),S("21BRE251T","Gene Therapy",3,"PEC"),S("21BRE252T","Developmental Biology",3,"PEC"),S("21BRE253T","Cancer Biology",3,"PEC"),S("21BRO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BRE351T","3D Bioprinting",3,"PEC"),S("21BRE352T","Clinical Trials and Regulations",3,"PEC"),S("21BRE353T","Organ on Chip",3,"PEC"),S("21BRO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BRP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BRE451T","Immunotherapy",3,"PEC"),S("21BRE452T","Translational Medicine",3,"PEC"),S("21BRE453T","Aging and Regeneration",3,"PEC"),S("21BRO353T","Machine Learning for All",3,"OEC"),S("21BRP701L","Major Project Phase I",4,"Project"),S("21BRI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BRE461T","Nanomedicine",3,"PEC"),S("21BRE462T","Ethical Issues in Regenerative Medicine",3,"PEC"),S("21BRP801L","Major Project Phase II",10,"Project"),S("21BRI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("BT_GE","B.Tech Biotechnology with Specialization in Genetic Engineering","Bio Technology",4,165,[
    SM(1,B1),SM(2,B2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21BTG201J","Cell Biology",4,"PCC"),S("21BTG202J","Biochemistry",4,"PCC"),S("21BTG203P","Genetics Lab",3,"PCC"),S("21BTS201T","Genetics",3,"ESC"),S("21BTG204T","Genetic Engineering I",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21BTG205J","Molecular Biology",4,"PCC"),S("21BTG206P","Bioinformatics",4,"PCC"),S("21BTG207J","Immunology",4,"PCC"),S("21BTG301T","Genetic Engineering II",3,"PCC"),S("21BTG208T","Genomics and Proteomics",3,"PCC")]),
    SM(5,[S("21BTG302J","Recombinant DNA Technology",4,"PCC"),S("21BGE251T","Plant Biotechnology",3,"PEC"),S("21BGE252T","Animal Biotechnology",3,"PEC"),S("21BGE253T","CRISPR and Gene Editing",3,"PEC"),S("21BGO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21BGE351T","Epigenetics",3,"PEC"),S("21BGE352T","Phage Biotechnology",3,"PEC"),S("21BGE353T","Bioprocess Engineering",3,"PEC"),S("21BGO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21BGP601L","Minor Project",3,"Project")]),
    SM(7,[S("21BGE451T","Metabolic Engineering",3,"PEC"),S("21BGE452T","Nanobiotechnology",3,"PEC"),S("21BGE453T","Forensic Biotechnology",3,"PEC"),S("21BGO353T","Machine Learning for All",3,"OEC"),S("21BGP701L","Major Project Phase I",4,"Project"),S("21BGI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21BGE461T","Evolutionary Biology",3,"PEC"),S("21BGE462T","Biosafety and IPR",3,"PEC"),S("21BGP801L","Major Project Phase II",10,"Project"),S("21BGI801L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("NANO","B.Tech Nanotechnology","Nano Technology",4,165,[
    SM(1,R1),SM(2,R2),
    SM(3,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21NAN201J","Physics of Nanomaterials",4,"PCC"),S("21NAN202J","Chemistry of Nanomaterials",4,"PCC"),S("21NAN203P","Nano Characterization Lab",3,"PCC"),S("21NAS201T","Solid State Physics",3,"ESC"),S("21NAN204T","Quantum Mechanics",3,"PCC"),S("21DCS201P","Design Thinking and Methodology",2,"ESC")]),
    SM(4,[S("21MAB401T","Probability and Statistics",4,"BSC"),S("21NAN205J","Synthesis of Nanomaterials",4,"PCC"),S("21NAN206P","Thin Film Technology",4,"PCC"),S("21NAN207J","Nanoelectronics",4,"PCC"),S("21NAN301T","Nanophotonics",3,"PCC"),S("21NAN208T","Nanobiotechnology",3,"PCC")]),
    SM(5,[S("21NAN302J","Nano Sensors",4,"PCC"),S("21NAE251T","Carbon Nanostructures",3,"PEC"),S("21NAE252T","Computational Nanotechnology",3,"PEC"),S("21NAE253T","Nanocomposites",3,"PEC"),S("21NAO351T","Python Programming",3,"OEC"),S("21IPR501J","Research Methodology",3,"PCC")]),
    SM(6,[S("21NAE351T","Nanomedicine",3,"PEC"),S("21NAE352T","Green Nanotechnology",3,"PEC"),S("21NAE353T","NEMS",3,"PEC"),S("21NAO352T","Web Programming",3,"OEC"),S("21MBC521T","Professional Ethics",2,"HSMC"),S("21NAP601L","Minor Project",3,"Project")]),
    SM(7,[S("21NAE451T","Nano Energy Systems",3,"PEC"),S("21NAE452T","Spintronics",3,"PEC"),S("21NAE453T","Nanotoxicology",3,"PEC"),S("21NAO353T","Machine Learning for All",3,"OEC"),S("21NAP701L","Major Project Phase I",4,"Project"),S("21NAI701L","Summer Internship",2,"Internship")]),
    SM(8,[S("21NAE461T","Advanced Characterization",3,"PEC"),S("21NAE462T","Nano Photovoltaics",3,"PEC"),S("21NAP801L","Major Project Phase II",10,"Project"),S("21NAI801L","Comprehensive Viva Voce",2,"Project")])
]))


# Integrated MTech courses (5-year programs, 10 semesters)
IM1 = [
    S("21ENG101T","English Communication",2,"HSMC"),
    S("21MAB101T","Calculus and Linear Algebra",4,"BSC"),
    S("21PYB101T","Engineering Physics",3,"BSC"),
    S("21CYB101T","Engineering Chemistry",3,"BSC"),
    S("21MES101T","Engineering Graphics and Design",3,"ESC"),
    S("21EES101T","Basic Electrical Engineering",3,"ESC"),
    S("21MES102P","Manufacturing Practices",2,"ESC"),
    S("21CSC101P","Problem Solving and Programming",3,"ESC")
]
IM2 = [
    S("21MAB201T","Advanced Calculus",4,"BSC"),
    S("21PYB201T","Materials Physics",3,"BSC"),
    S("21MAB202T","Complex Analysis",3,"BSC"),
    S("21CSC102J","Data Structures",4,"ESC"),
    S("21MEC102T","Engineering Mechanics",3,"ESC"),
    S("21CSC103T","Object Oriented Programming",3,"ESC"),
    S("21CSC104P","Web Programming Lab",2,"ESC"),
    S("21CSC105P","Digital Logic Lab",2,"ESC")
]

courses.append(C("IM_CSE","Integrated MTech Computer Science and Engineering","Computing Technologies",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMC301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMC302J","Operating Systems",4,"PCC"),S("21IMC303P","Database Management Systems",4,"PCC"),S("21IMC304J","Computer Networks",4,"PCC"),S("21IMC305T","Software Engineering",3,"PCC")]),
    SM(6,[S("21IMC306J","Machine Learning",4,"PCC"),S("21IMC307J","Artificial Intelligence",4,"PCC"),S("21IMC308P","Cloud Computing",4,"PCC"),S("21IME351T","Advanced Data Analytics",3,"PEC"),S("21IME352T","Big Data Technologies",3,"PEC"),S("21IMC309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMC401J","Deep Learning",4,"PCC"),S("21IMC402J","Natural Language Processing",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Advanced Computer Architecture",3,"PEC"),S("21IME453T","IoT and Edge Computing",3,"PEC"),S("21IMC403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMC404J","Computer Vision",4,"PCC"),S("21IME454T","Cyber Security",3,"PEC"),S("21IME455T","Blockchain Technology",3,"PEC"),S("21IME456T","Reinforcement Learning",3,"PEC"),S("21IMC405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMC501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Distributed Systems",3,"PEC"),S("21IME552T","Edge AI",3,"PEC"),S("21IME553T","Speech and Audio Processing",3,"PEC"),S("21IMC502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMC503P","Major Project Phase II",16,"Project"),S("21IMC504L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IM_AI","Integrated MTech Computer Science with Specialization in Artificial Intelligence","Computational Intelligence",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMA301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMA302J","Operating Systems",4,"PCC"),S("21IMA303P","Database Management Systems",4,"PCC"),S("21IMA304J","Computer Networks",4,"PCC"),S("21IMA305T","Introduction to AI",3,"PCC")]),
    SM(6,[S("21IMA306J","Machine Learning",4,"PCC"),S("21IMA307J","Deep Learning",4,"PCC"),S("21IMA308P","Data Visualization",4,"PCC"),S("21IME351T","Natural Language Processing",3,"PEC"),S("21IME352T","Big Data Analytics",3,"PEC"),S("21IMA309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMA401J","Computer Vision",4,"PCC"),S("21IMA402J","Reinforcement Learning",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Generative AI",3,"PEC"),S("21IME453T","Robotics",3,"PEC"),S("21IMA403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMA404J","Explainable AI",4,"PCC"),S("21IME454T","MLOps",3,"PEC"),S("21IME455T","Cognitive Computing",3,"PEC"),S("21IME456T","Edge AI",3,"PEC"),S("21IMA405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMA501J","MTech Seminar",4,"PCC"),S("21IME551T","Speech and Audio Processing",3,"PEC"),S("21IME552T","Quantum Machine Learning",3,"PEC"),S("21IME553T","AI for Healthcare",3,"PEC"),S("21IMA502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMA503P","Major Project Phase II",16,"Project"),S("21IMA504L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("IM_CSE_CSD","Integrated MTech CSE with Specialization in Cyber Security and Digital Forensics","Computing Technologies",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMD301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMD302J","Operating Systems",4,"PCC"),S("21IMD303P","Database Management Systems",4,"PCC"),S("21IMD304J","Computer Networks",4,"PCC"),S("21IMD305T","Cryptography Fundamentals",3,"PCC")]),
    SM(6,[S("21IMD306J","Network Security",4,"PCC"),S("21IMD307J","Digital Forensics",4,"PCC"),S("21IMD308P","Web Security",4,"PCC"),S("21IME351T","Ethical Hacking",3,"PEC"),S("21IME352T","Cyber Law and Compliance",3,"PEC"),S("21IMD309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMD401J","Malware Analysis",4,"PCC"),S("21IMD402J","Cloud Security",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","IoT Security",3,"PEC"),S("21IME453T","Blockchain Security",3,"PEC"),S("21IMD403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMD404J","AI for Cyber Security",4,"PCC"),S("21IME454T","Penetration Testing",3,"PEC"),S("21IME455T","Security Operations",3,"PEC"),S("21IME456T","Mobile Security",3,"PEC"),S("21IMD405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMD501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Cryptography",3,"PEC"),S("21IME552T","Cyber Threat Intelligence",3,"PEC"),S("21IME553T","Digital Watermarking",3,"PEC"),S("21IMD502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMD503P","Major Project Phase II",16,"Project"),S("21IMD504L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IM_CSE_DS","Integrated MTech CSE with Specialization in Data Science","Computing Technologies",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMS301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMS302J","Operating Systems",4,"PCC"),S("21IMS303P","Database Management Systems",4,"PCC"),S("21IMS304J","Computer Networks",4,"PCC"),S("21IMS305T","Data Mining",3,"PCC")]),
    SM(6,[S("21IMS306J","Machine Learning",4,"PCC"),S("21IMS307J","Big Data Analytics",4,"PCC"),S("21IMS308P","Data Warehousing",4,"PCC"),S("21IME351T","Apache Spark",3,"PEC"),S("21IME352T","NoSQL Databases",3,"PEC"),S("21IMS309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMS401J","Deep Learning",4,"PCC"),S("21IMS402J","Statistical Learning",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Stream Data Processing",3,"PEC"),S("21IME453T","Data Engineering",3,"PEC"),S("21IMS403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMS404J","Data Visualization",4,"PCC"),S("21IME454T","Cloud Data Platforms",3,"PEC"),S("21IME455T","MLOps",3,"PEC"),S("21IME456T","Time Series Analysis",3,"PEC"),S("21IMS405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMS501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Data Mining",3,"PEC"),S("21IME552T","Graph Analytics",3,"PEC"),S("21IME553T","Data Science at Scale",3,"PEC"),S("21IMS502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMS503P","Major Project Phase II",16,"Project"),S("21IMS504L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IM_CSE_MESD","Integrated MTech CSE with Specialization in Micro Electronics and System Design","Computing Technologies",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMM301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMM302J","Operating Systems",4,"PCC"),S("21IMM303P","Electronic Devices and Circuits",4,"PCC"),S("21IMM304J","Digital Logic Design",4,"PCC"),S("21IMM305T","Signals and Systems",3,"PCC")]),
    SM(6,[S("21IMM306J","Microprocessors and Microcontrollers",4,"PCC"),S("21IMM307J","VLSI Design",4,"PCC"),S("21IMM308P","Embedded Systems",4,"PCC"),S("21IME351T","Verilog and FPGA",3,"PEC"),S("21IME352T","CMOS Design",3,"PEC"),S("21IMM309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMM401J","System on Chip Design",4,"PCC"),S("21IMM402J","Low Power VLSI",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","ASIC Design",3,"PEC"),S("21IME453T","VLSI Testing",3,"PEC"),S("21IMM403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMM404J","Analog VLSI Design",4,"PCC"),S("21IME454T","RF VLSI Design",3,"PEC"),S("21IME455T","Memory Design",3,"PEC"),S("21IME456T","Mixed Signal Design",3,"PEC"),S("21IMM405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMM501J","MTech Seminar",4,"PCC"),S("21IME551T","Nanoelectronics",3,"PEC"),S("21IME552T","Advanced VLSI Design",3,"PEC"),S("21IME553T","VLSI Signal Processing",3,"PEC"),S("21IMM502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMM503P","Major Project Phase II",16,"Project"),S("21IMM504L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IM_CSE_COG","Integrated MTech CSE with Specialization in Cognitive Science","Computing Technologies",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,C1),SM(4,C2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMC301J","Design and Analysis of Algorithms",4,"PCC"),S("21IMC302J","Operating Systems",4,"PCC"),S("21IMC303P","Database Management Systems",4,"PCC"),S("21IMC304J","Computer Networks",4,"PCC"),S("21IMC305T","Cognitive Psychology",3,"PCC")]),
    SM(6,[S("21IMC306J","Machine Learning",4,"PCC"),S("21IMC307J","Neural Networks",4,"PCC"),S("21IMC308P","Cognitive Modeling",4,"PCC"),S("21IME351T","Natural Language Processing",3,"PEC"),S("21IME352T","Knowledge Representation",3,"PEC"),S("21IMC309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMC401J","Computational Neuroscience",4,"PCC"),S("21IMC402J","Cognitive Robotics",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Brain Computer Interface",3,"PEC"),S("21IME453T","Decision Making Systems",3,"PEC"),S("21IMC403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMC404J","AI and Consciousness",4,"PCC"),S("21IME454T","Neuroimaging",3,"PEC"),S("21IME455T","Affective Computing",3,"PEC"),S("21IME456T","Cognitive IoT",3,"PEC"),S("21IMC405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMC501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Cognitive Science",3,"PEC"),S("21IME552T","Human Robot Interaction",3,"PEC"),S("21IME553T","Computational Creativity",3,"PEC"),S("21IMC502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMC503P","Major Project Phase II",16,"Project"),S("21IMC504L","Comprehensive Viva Voce",2,"Project")])
]))


courses.append(C("IM_ME","Integrated MTech Mechanical Engineering","Mechanical Engineering",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,R1),SM(4,R2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMM301J","Engineering Mechanics",4,"PCC"),S("21IMM302J","Fluid Mechanics and Machinery",4,"PCC"),S("21IMM303P","Thermodynamics Lab",3,"PCC"),S("21IMM304J","Materials Science",4,"PCC"),S("21IMM305T","Machine Drawing",3,"PCC")]),
    SM(6,[S("21IMM306J","Heat and Mass Transfer",4,"PCC"),S("21IMM307J","Manufacturing Technology",4,"PCC"),S("21IMM308P","Strength of Materials",4,"PCC"),S("21IME351T","CAD/CAM",3,"PEC"),S("21IME352T","Theory of Machines",3,"PEC"),S("21IMM309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMM401J","Design of Machine Elements",4,"PCC"),S("21IMM402J","Robotics",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Finite Element Analysis",3,"PEC"),S("21IME453T","Computational Fluid Dynamics",3,"PEC"),S("21IMM403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMM404J","Additive Manufacturing",4,"PCC"),S("21IME454T","Industrial Engineering",3,"PEC"),S("21IME455T","Renewable Energy Systems",3,"PEC"),S("21IME456T","Automobile Engineering",3,"PEC"),S("21IMM405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMM501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Thermodynamics",3,"PEC"),S("21IME552T","Vibration Analysis",3,"PEC"),S("21IME553T","Smart Materials",3,"PEC"),S("21IMM502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMM503P","Major Project Phase II",16,"Project"),S("21IMM504L","Comprehensive Viva Voce",2,"Project")])
]))

courses.append(C("IM_MSE","Integrated MTech Materials Science and Engineering","Materials Science and Engineering",5,205,[
    SM(1,IM1),SM(2,IM2),
    SM(3,R1),SM(4,R2),
    SM(5,[S("21MAB301T","Discrete Mathematics",4,"BSC"),S("21IMS301J","Materials Science I",4,"PCC"),S("21IMS302J","Thermodynamics of Materials",4,"PCC"),S("21IMS303P","Materials Characterization",3,"PCC"),S("21IMS304J","Solid State Physics",4,"PCC"),S("21IMS305T","Phase Transformations",3,"PCC")]),
    SM(6,[S("21IMS306J","Materials Science II",4,"PCC"),S("21IMS307J","Mechanical Behavior of Materials",4,"PCC"),S("21IMS308P","Composite Materials",4,"PCC"),S("21IME351T","Nanomaterials",3,"PEC"),S("21IME352T","Surface Engineering",3,"PEC"),S("21IMS309P","Minor Project",3,"Project")]),
    SM(7,[S("21IMS401J","Electronic Materials",4,"PCC"),S("21IMS402J","Polymer Science",4,"PCC"),S("21IME451T","Research Methodology",3,"PCC"),S("21IME452T","Ceramic Materials",3,"PEC"),S("21IME453T","Thin Film Technology",3,"PEC"),S("21IMS403P","Summer Internship",2,"Internship")]),
    SM(8,[S("21IMS404J","Biomaterials",4,"PCC"),S("21IME454T","Corrosion Engineering",3,"PEC"),S("21IME455T","Energy Materials",3,"PEC"),S("21IME456T","Magnetic Materials",3,"PEC"),S("21IMS405P","Minor Project II",3,"Project")]),
    SM(9,[S("21IMS501J","MTech Seminar",4,"PCC"),S("21IME551T","Advanced Characterization",3,"PEC"),S("21IME552T","Computational Materials Science",3,"PEC"),S("21IME553T","Sustainable Materials",3,"PEC"),S("21IMS502P","Major Project Phase I",4,"Project")]),
    SM(10,[S("21IMS503P","Major Project Phase II",16,"Project"),S("21IMS504L","Comprehensive Viva Voce",2,"Project")])
]))


output = json.dumps({"university": "SRM Institute of Science and Technology",
                      "regulation": "2021",
                      "total_courses": len(courses),
                      "courses": courses}, indent=2)
with open("srm_university_54_courses.json", "w", encoding="utf-8") as fh:
    fh.write(output)
print(f"Generated {len(courses)} courses to srm_university_54_courses.json")
