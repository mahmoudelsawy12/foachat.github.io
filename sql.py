# -*- coding: utf-8 -*-

import sqlite3


def insert_multiple_responses(data):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """
    )

    cursor.executemany("INSERT INTO responses (question, answer) VALUES (?, ?)", data)

    conn.commit()
    conn.close()
    print(f"Inserted {len(data)} questions successfully.")


data = [
    (
        "ماهي رؤية القسم؟",
        "تقديم برنامج أكاديميى مميز فى مجال تكنولوجيا المعلومات وتطبيقاتها فى مجال المكتبات والمعلومات",
    ),
    (
        "What Department Vision?",
        "Offering a distinguished academic program in the field of information technology and its applications in libraries and information science",
    ),
    (
        "ماهو قسم تقنية المعلومات و المكتبات؟",
        "برنامج تقنية المعلومات و المكتبات برنامج اكاديمي متميز يهدف الى :- تأهيل كوادر مهنية في مجال تكنولوجيا المكتبات و المعلومات والتي تلبى احتياجات ومتطلبات سوق العمل - مواكبة التطورات و التحديثات المتسارعه في مجال تكنولوجيا المعلومات وتقييم وتبني المفيد منها مما يسهم في تطور مرافق المعلومات - اكساب الطلاب مهارات التعامل مع الميتاداتا وشبكات المعلومات وتصميم وانشاء مواقع على الانترنت وامن المعلومات وتجهيز ومعالجة المعلومات وتصميم وتحليل النظم الالية ......الخ - تمكين الطلاب من بناء وادارة وتنظيم المحتوى المعلوماتي الرقمي في مرافق المعلومات - اكساب الطلاب مهارات التعامل مع البيئة الرقمية واستخدامها في تنظيم وادارة المعلومات - الدرجة العلمية : يمنح البرنامج درجة الليسانس في تقنية المعلومات و المكتبات بنظام الساعات المعتمده - القيد و القبول : يستهدف البرنامج الطلاب الحاصلين على الثانوية العامة او ما يعادلها والذين تنطبق عليهم شروط الالتحاق بكلية الاداب - نظام الدراسة : للحصول على درجة الليسانس في تقنية المعلومات و المكتبات بنظام الساعات المعتمده يجب ان يجتاز الطالب 139 ساعة معتمده شاملة لمتطلبات الجامعة ومتطلبات الكلية ومتطلبات التخصص وفقا لنظام الفصول الدراسية - الفرص الوظيفية للخريجين : يمكن لخريجي البرنامج العمل في القطاع الحكومي و الخاص في الكثير من المجالات ومنها ادارة وتصميم و تحليل النظم الالية والتعامل مع شبكات المعلومات وتصميم وانشاء مواقع على الانترنت وامن المعلومات وتجهيز ومعالجة المعلومات و الميتاداتا ......الخ",
    ),
    (
        "What is the department of information technology and libraries?",
        "Information Technology and Libraries Program: Program Description: The Information Technology and Libraries Program is a distinguished academic program designed to: Develop qualified professionals in the field of library and information technology, meeting the demands of the modern job market - Keep pace with rapid advancements and updates in information technology, evaluating and adopting beneficial innovations to enhance information facilities - Equip students with skills in metadata management, information networks, website design and development, information security, information processing, and automated systems design and analysis among others - Enable students to navigate and utilize the digital environment for effective information management - Academic Degree: The Program grants a Bachelor's degree in information technology and libraries, based on a credit hour system - Admission Requirements: The Program targets students holding a general secondary education certificate or its equivalent who meet the admission criteria of the Faculty of Arts - Study System: To obtain the Bachelor's degree in information technology and libraries under the credit hour system, students must complete 139 credit hours, including university, faculty, and specialization requirements, according to the semester system - Career Opportunities for Graduates: Graduates of the program can pursue careers in both the public and private sectors in various fields, including: 1- Automated system management, design, and analysis 2- Information network management 3- Website design and development 4- Information security 5- Information processing and metadata management and many other related fields",
    ),
    (
        "ماهي رسالة القسم؟",
        "تأهيل كوادر مهنية في مجال المعلومات و تكنولوجياتها والتي تلبى احتياجات السوق",
    ),
    (
        "What is the mission of the department?",
        "To qualify professional cadres in the field of information and its technologies, meeting the needs of the labor market",
    ),
    (
        "ماهي اهداف البرنامج؟",
        "يهدف برنامج تقنية المعلومات والمكتبات الى /n: - تحقيق المعرفة العلمية في مجال نظم المعلومات و تكنولوجياتها التي تمكن الطلاب من المشاركة في التعلم مدى الحياة/n - تمكين الطلاب من التصرف كمهنيين محترفين مسؤولين ومواطنين مدركين للمسؤوليات الاخلاقية و المشكلات المجتمعية وآلية حلها /n- مواكبة التطورات و التحديثات المتسارعة في مجال تكنولوجيا المعلومات وتقييم وتبني المفيد منها مما يسهم في تطور مرافق المعلومات /n- /nتمكين الطلاب من بناء وادارة وتنظيم المحتوى المعلوماتي الرقمي في انظمة تكنولوجيا المعلومات المتوافرة في مرافق المعلومات/n -/n اكساب الطلاب المهارات اللازمة للتواصل مع الاخرين علي مستوى العلاقات الشخصية, او العامة, او المهنية",
    ),
    (
        "What are the program objectives?",
        "Objectives of the Information Technology and Libraries Program: 1- Achieve scientific knowledge in the field of information systems and technologies, enabling students to engage in lifelong learning 2- Empower students to act as responsible professionals and informed citizens, aware of ethical responsibilities, societal issues, and their resolution 3- Keep pace with rapid advancements and updates in information technology, evaluating and adopting beneficial innovations to enhance information facilities 4- Enable students to build, manage, and organize digital information content within information technology systems available in information facilities 5- Equip students with the necessary skills to communicate with others on personal, public, and professional levels",
    ),
    (
        "رابط النتيجة؟ ",
        "من خلال زيارة الرابط:https://tdb.tanta.edu.eg/regart",
    ),
    (
        "Results Link?",
        "By Visiting the link :https://tdb.tanta.edu.eg/regart",
    ),
    (
        "رابط القسم؟",
        "من خلال زيارة الرابط:https://prog.tanat.edu.eg/ar/prog/infolib",
    ),
    (
        "Department Link ?,",
        "By Visiting the link :https://prog.tanat.edu.eg/ar/prog/infolib",
    ),
    (
        " رابط صفحة الفيسبوك؟",
        " من خلال زيارة الرابط:https://www.facebook.com/share/156efzREMN/?mibextid=wwXlfr",
    ),
    (
        "Facebook Page ? ",
        "By Visiting the link :https://www.facebook.com/share/156efzREMN/?mibextid=wwXlfr",
    ),
    (
        "  شروط البرنامج",
        "يقبل البرنامج طلاب الثانوية العامة العلمي والادبي : - البرنامج ليس له شروط سوى ان يكون مجموع الطالب يقبل الالتحاق بكلية الاداب  - المصروفات :حوالي 7 الاف في السنة قابله للدفع على قسطين ترم اول و ترم ثاني  - طبيعة الدراة : 4 سنوات دراسية بنظام الساعات المعتمدة  - الدرجة العلمية : يحصل الطلاب على درجة الليسانس في تقنية المعلومات و المكتبات بنظام الساعات المعتمدة",
    ),
    (
        "What are the program requirements? ",
        "Program Requirements : Eligbility: The Program accepts students holding a general secondery education certificate (both science and arts divisions  - Tuition Fees : Approximately 7.000 EGP per academic year , payable in two installments (frist and second semesters)  - Study Duration : Four academic years , based on credit hour system  - Academic Dgree : Students Will receive Bachelors degree (licence) in information technology and libraries , based on a credit hour system)",
    ),
    (
        "  دكاترة البرنامج؟ ",
        "ثروت يوسف الغلبان   - احمد عباده جدوع العربي   - بدوية محمد البسيوني محمد البسيوني  - نادية سعد مرسي على  - هبه فتحي بسيوني دنيا  - هبه احمد محمد احمد المتبولي  - احمد رجب احمد شاهين  - عواطف علي علي المكاوي  - ميرفت فؤاد جرجس غبريال  - هبه صلاح الدين النمورى  - رضوى محمد جلال زكريا النوساني  - عبدالله فراج عبدالمجيد عامر  - غادة عزت محمود ابو زويد  - منى مصطفى ابراهيم مرسى  - منى فاروق عباس شهوان  - هند عبدالحفيظ عبدالله صالح السمدونى  عمرو الخولي  - السيد سلام  - تهاني علام  - هاني الغايش  - امنية البربري  - رضا البسيوني  - شيماء خاطر  - مصطفى العشري    - ابراهيم عبد العال    - رافت عبد الرزاق",
    ),
    (
        "Who are the program faculty members? ",
        "ثروت يوسف الغلبان   - احمد عباده جدوع العربي   - بدوية محمد البسيوني محمد البسيوني  - نادية سعد مرسي على  - هبه فتحي بسيوني دنيا  - هبه احمد محمد احمد المتبولي  - احمد رجب احمد شاهين  - عواطف علي علي المكاوي  - ميرفت فؤاد جرجس غبريال  - هبه صلاح الدين النمورى  - رضوى محمد جلال زكريا النوساني  - عبدالله فراج عبدالمجيد عامر  - غادة عزت محمود ابو زويد  - منى مصطفى ابراهيم مرسى  - منى فاروق عباس شهوان  - هند عبدالحفيظ عبدالله صالح السمدونى  عمرو الخولي  - السيد سلام  - تهاني علام  - هاني الغايش  - امنية البربري  - رضا البسيوني  - شيماء خاطر  - مصطفى العشري    - ابراهيم عبد العال    - رافت عبد الرزاق",
    ),
    (
        "من انت ؟",
        "FOA CHAT اول شات بوت خاص بكلية الاداب جامعة طنطا صنع على يد طلاب من قسم تقنية المعلومات و المكتبات لمساعدة الطلاب الجدد والاجابة على اسئلتهم فورا وبدون تعقيد",
    ),
    (
        "Who are you ? ",
        "FOA CHAT is the frist chatbot dedicated to the faculty of arts at tanta university . it was developed by students from the information technology department to assist new students and answer their questions instantly and without complications.",
    ),
    (
        " لائحة البرنامج؟",
        " من خلال زيارة الرابط: https://prog.tanta.edu.eg/ar/spage/29/1675/%D9%84%D8%A7%D8%A6%D8%AD%D8%A9%20%D8%A7%D9%84%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC",
    ),
    (
        "Program policy?",
        "By Visiting the link :https://prog.tanta.edu.eg/ar/spage/29/1675/%D9%84%D8%A7%D8%A6%D8%AD%D8%A9%20%D8%A7%D9%84%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC",
    ),
    (
        " المواد الاجبارية؟",
        "المدخل الى علم المعلومات  - مرافق المعلومات  - الانترنت في المكتبات  - مصادر المعلومات الرقمية  - اخلاقيات الملومات  - دراسات المستفيدين  - مقدمة في تقنية المعلومات  - خدمات المعلومات الرقمية  - تجهيز ومعالجة المعلومات  - المصادر المرجعية الرقمية  - المكتبات و المستودعات الرقمية  - شبكات المعلومات  - ادارة المكتبات و مراكز المعلومات  - الاحصاء الببليوجرافي  - الفهرسة الالية - النشر الالكتروني  - نصوص متخصصه باللغة الانجليزية  - قواعد البيانات الببليوجرافية  - التصنيف في البيئة الرقمية  -النظم الالية المتكاملة  - الكلمات المفتاحية  - تطبيقات الحوسبه السحابيه في المكتبات  - امن المعلومات  - الميتاداتا - نظم التكشيف الالية  - التطبيقات الذكية في المكتبات  - رقمنة مصادر المعلومات  - برمجة الويب  - الترتيب و الوصف الارشيفي  - تطبيقات الويب الدلالي في المكتبات  - سياسات المعلومات  - تطبيقات النظم الخبيرة في المكتبات -  اللغة الاجنبية الاولى  - بناء و ادارة مواقع المكتبات  - الارشفة الالكترونية  - قياسات الويب  - علم المكتبات المقارن  - الجود الشاملة في المكتبات  - مشروع التخرج  - التدريب الميداني ",
    ),
    (
        "What are the mandatory courses?   ",
        "المدخل الى علم المعلومات  - مرافق المعلومات  - الانترنت في المكتبات  - مصادر المعلومات الرقمية  - اخلاقيات الملومات  - دراسات المستفيدين  - مقدمة في تقنية المعلومات  - خدمات المعلومات الرقمية  - تجهيز ومعالجة المعلومات  - المصادر المرجعية الرقمية  - المكتبات و المستودعات الرقمية  - شبكات المعلومات  - ادارة المكتبات و مراكز المعلومات  - الاحصاء الببليوجرافي  - الفهرسة الالية - النشر الالكتروني  - نصوص متخصصه باللغة الانجليزية  - قواعد البيانات الببليوجرافية  - التصنيف في البيئة الرقمية  -النظم الالية المتكاملة  - الكلمات المفتاحية  - تطبيقات الحوسبه السحابيه في المكتبات  - امن المعلومات  - الميتاداتا - نظم التكشيف الالية  - التطبيقات الذكية في المكتبات  - رقمنة مصادر المعلومات  - برمجة الويب  - الترتيب و الوصف الارشيفي  - تطبيقات الويب الدلالي في المكتبات  - سياسات المعلومات  - تطبيقات النظم الخبيرة في المكتبات -  اللغة الاجنبية الاولى  - بناء و ادارة مواقع المكتبات  - الارشفة الالكترونية  - قياسات الويب  - علم المكتبات المقارن  - الجود الشاملة في المكتبات  - مشروع التخرج  - التدريب الميداني",
    ),
    (
        " المواد الاختيارية؟",
        "البرامج التعاونية في مؤسسات المعلومات  - الوعي المعلوماتي  - المعلوماتيه الصحية  - نظم المعلومات المتخصصة  - تسويق خدمات المعلومات  - معمارية المعلومات  - ادارة المجموعات الرقمية  - ادارة مشروعات تقنية المعلومات  - الارشيفات المتخصصة  - التراخيص الرقمية لمصادر المعلومات  - عمارة المكتبات في الاثار المصرية  - اثار مصر عبر العصور",
    ),
    (
        "What are the optional courses? ",
        "البرامج التعاونية في مؤسسات المعلومات  - الوعي المعلوماتي  - المعلوماتيه الصحية  - نظم المعلومات المتخصصة  - تسويق خدمات المعلومات  - معمارية المعلومات  - ادارة المجموعات الرقمية  - ادارة مشروعات تقنية المعلومات  - الارشيفات المتخصصة  - التراخيص الرقمية لمصادر المعلومات  - عمارة المكتبات في الاثار المصرية  - اثار مصر عبر العصور",
    ),
    (
        " كيف اقيم المقررات؟",
        " من خلال زيارة الرابط:https://prog.tanta.edu.eg/ar/spage/29/1677/%D8%A7%D8%B3%D8%AA%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA",
    ),
    (
        "Courses evaluation survey? ",
        "By Visiting the link :https://prog.tanta.edu.eg/ar/spage/29/1677/%D8%A7%D8%B3%D8%AA%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA",
    ),
    (
        "ماهي التدريبات المتوافرة؟",
        "توافر للقسم معمل آلي مخصص لتدريس مقررات القسم العلمية ويتوافر به 40 جهازا كما يمكن للطلاب الافادة من نادي تكنولوجياالمعلومات التابع للجامعة و الموجود بالكلية",
    ),
    (
        "What training is available? ",
        "The department has a dedicate computer lab for teaching its scientific courses , equipped with 40 devices . students can also benefit fro the university information technology club located within the college",
    ),
    (
        "لينك تسجيل المقررات؟ ",
        "من خلال زيارة الرابط:https://tdb.tanta.edu.eg",
    ),
    (
        "Course registration link?  ",
        "By Visiting the link :https://tdb.tanta.edu.eg",
    ),
    (
        " رابط جامعة طنطا؟",
        "من خلال زيارة الرابط:https://tanta.edu.eg/",
    ),
    (
        "Tanta University Link?",
        "By Visiting the link :https://tanta.edu.eg/",
    ),
    (
        "كيف اعرف ارقام الجلوس و اماكن اللجان؟  ",
        "من خلال زيارة الرابط:https://art.tanta.edu.eg/stu-sitting-num.aspx",
    ),
    (
        "How do i find my seat numbers and exam center location ? ",
        "By Visiting the link :https://art.tanta.edu.eg/stu-sitting-num.aspx",
    ),
    (
        "ماهي اجراءات الكشف الطبي؟",
        "التعليمات المنظمة للكشف الطبي في بداية العام الدراسي تشمل: 1- سداد المصروفات الدراسية من الطلاب الجدد. 2- تحديد أيام الكشف الطبي من إدارة الجامعة بناءً على تعليمات وزارة التعليم العالي للكشف على حوالي 20 ألف طالب وطالبة خلال شهر. 3- تقسيم الكليات حسب جدول معتمد، مع تخصيص أيام للبنين والبنات والكشف في تخصصات (الباطنة – الأنف والأذن – الجراحة العامة – الرمد – الأسنان – العظام). 4- تسليم استمارة الكشف الطبي لرعاية الشباب بعد اكتمال الإجراءات. 5- فحوصات خاصة لطلبة كلية التربية الرياضية تشمل تحليل المخدرات وفحص القلب. 6- توقيع الكشف الطبي الخاص بالمدن الجامعية شرط أساسي للالتحاق مع إحضار بطاقة تطعيم فيروس كورونا",
    ),
    (
        "What are the medical examination procedures?",
        "The regulations for the medical examination at the beginning of the academic year include: * Payment of tuition fees by new students. * Setting the medical examination days by the university administration based on the Ministry of Higher Education's instructions to examine approximately 20,000 students within a month. * Dividing colleges according to an approved schedule, with designated days for male and female students, and examinations in (internal medicine, ear, nose, and throat, general surgery, ophthalmology, dentistry, orthopedics). * Submitting the medical examination form to student welfare after completing the procedures. * Special examinations for students of the Faculty of Physical Education, including drug analysis and cardiac examination. * Signing the medical examination for university dormitories, a mandatory requirement for enrollment, with the student bringing the COVID-19 vaccination card.",
    ),
    (
        " رابط الكشف الطبي؟",
        " من خلال زيارة الرابط:https://tanta.edu.eg/stu/new-student.aspx",
    ),
    (
        "Medical Examiniation Link?",
        "By Visiting the link :https://tanta.edu.eg/stu/new-student.aspx",
    ),
    (
        "ماهي متطلبات التقديم للطلاب الجدد و القدامى ؟ ",
        "١- أصل شهادة الثانوية العامة ٢- شهادة ميلاد كمبيوتر مدون بها الرقم الثلاثى للطلاب الذكور ٣- صورة البطاقة الشخصية ٤- أصل إيصال سداد الرسوم وصورة منه ٥- استمارة الرغبات وعليها طوابع فئة ٥٠ جنيه من خزينة الكلية ٦- طلب الالتحاق وعليه طوابع فئة ٤٠ جنيه من خزينة الكلية ٧- عدد ٤ صور شخصية ٨- استمارة ٢ جند للطلاب الذكور ملحوظة: علي الطالب تصوير نسختين من شهادة الثانوية العامة وشهادة الميلاد والبطاقة الشخصية والاحتفاظ بنسخة من أوراقه قبل تسليم الملف.",
    ),
    (
        "What are the application requirments for new and returning students?",
        "1. Original High School Diploma 2. Computerized Birth Certificate with the triple identification number for male students 3. Copy of National ID Card 4. Original and copy of payment receipt for fees 5. Preference form with stamps worth 50 EGP from the college treasury 6. Enrollment application with stamps worth 40 EGP from the college treasury 7. Four personal photos 8. Form 2 Jund for male students Note: Students must make two copies of their High School Diploma, Birth Certificate, and National ID Card and keep a copy of their documents before submitting the file.",
    ),
    (
        "مصاريف القسم؟",
        "برنامج تقنية المعلومات والمكتبات: - المستوى الأول (الترم الأول 3600 جنيه) (الترم الثاني 3600 جنيه) - المستوى الثاني (الترم الأول 3600 جنيه) (الترم الثاني 3600 جنيه) - المستوى الثالث (الترم الأول 3150 جنيه) (الترم الثاني 2975 جنيه) - المستوى الرابع (الترم الأول 2975 جنيه) (الترم الثاني 2625 جنيه)",
    ),
    (
        "How Much are the department fees? ",
        "Information Technology and Libraries Program: * Level 1 (Semester 1: 3600 EGP) (Semester 2: 3600 EGP) * Level 2 (Semester 1: 3600 EGP) (Semester 2: 3600 EGP) * Level 3 (Semester 1: 3150 EGP) (Semester 2: 2975 EGP) * Level 4 (Semester 1: 2975 EGP) (Semester 2: 2625 EGP)",
    ),
    (
        " رابط التربية العسكرية؟",
        "من خلال زيارة الرابط :https://militaryedu.tanta.edu.eg/",
    ),
    (
        "Military education Link? ",
        "By Visiting the link :https://militaryedu.tanta.edu.eg/",
    ),
    (
        "لينك تحميل صورة الكارنية ؟ ",
        "من خلال زيارة الرابط:http://tdb.tanta.edu.eg/regart",
    ),
    (
        "Doenload link for id card photo?",
        "By Visiting the link :http://tdb.tanta.edu.eg/regart",
    ),
    (
        " رابط تقديم المدينة الجامعية؟",
        "من خلال زيارة الرابط :https://tdb.tanta.edu.eg/univhostel/",
    ),
    (
        "How to apply for university dormitories?",
        "By Visiting the link :https://tdb.tanta.edu.eg/univhostel/",
    ),
    (
        "رابط التشعيب ؟",
        "https://tdb2.tanta.edu.eg/branching_system/login.aspx?id=5",
    ),
    (
        "Branching Link?",
        "https://tdb2.tanta.edu.eg/branching_system/login.aspx?id=5",
    ),
    (
        "  فيديو للتعامل مع رابط التشعيب؟",
        "https://www.facebook.com/share/v/1JgXCiTaBs/?mibextid=wwXIfr",
    ),
    (
        " video on how to use the specialization link?",
        "https://www.facebook.com/share/v/1JgXCiTaBs/?mibextid=wwXIfr",
    ),
    (
        "رابط منصة التحصيل الالكتروني؟",
        "https://tdb2.tanta.edu.eg/paymentgateway/e_payment/",
    ),
    (
        "Electronic payment platform? ",
        "https://tdb2.tanta.edu.eg/paymentgateway/e_payment/",
    ),
    (
        " فيديو للتعامل مع منصة التحصيل الالكتروني ؟",
        "https://www.facebook.com/share/v/1EBLtxrusm/?mibextid=wwXIfr",
    ),
    (
        " Video on how to use the electronic payment platform?",
        "https://www.facebook.com/share/v/1EBLtxrusm/?mibextid=wwXIfr",
    ),
    (
        "رابط منصة الكتاب الالكتروني ؟",
        "https://tdb.tanta.edu.eg/ebooks/",
    ),
    (
        "Electronic book platform link?",
        "https://tdb.tanta.edu.eg/ebooks/",
    ),
    (
        " فيديو للتعامل مع منصة الكتاب الالكتروني؟",
        "https://tdb.tanta.edu.eg/ebooks/",
    ),
    (
        "Video on hoe to use the electronic book platform link?",
        "https://tdb.tanta.edu.eg/ebooks/",
    ),
    (
        "كيف اتواصل مع الدكتور ثروت يوسف الغلبان؟",
        "عن طريق رقم الهاتف : 01227315841 - او عن طريق الايميل الخاص به : tharout.elghalban@art.tanta.edu.eg",
    ),
    (
        "How can i contact to dr tharout youseef elghalban?",
        "Phone: 01227315841  -  Email:tharout.elghalban@art.tanta.edu.eg",
    ),
    (
        "ماهي وظيفة الدكتور ثروت يوسف الغلبان حاليا؟",
        "استاذ جامعي",
    ),
    (
        "What is dr Thatout youssef elghalban current job?",
        "Professor",
    ),
    (
        "ماهي انجازات الدكتور ثروت يوسف الغلبان؟",
        "لدكتوراه (مكتبات) - (جامعة طنطا) - عام 2000 - الماجستير (مكتبات) - (جامعة طنطا) - عام 1995 - الليسانس (مكتبات) - (جامعة طنطا) - بتقدير جيد جدًا - عام 1990 - أستاذ بقرار بتاريخ 01/10/2012 اعتبارًا من 01/10/2012 - أستاذ مساعد بقرار بتاريخ 06/07/2008 اعتبارًا من 30/06/2008 - مدرس بقرار بتاريخ 02/05/2000 اعتبارًا من 29/04/2000 - مدرس مساعد بقرار بتاريخ 21/01/1996 اعتبارًا من 21/01/1996 - معيد بقرار بتاريخ 07/08/1990 اعتبارًا من 07/08/1990 - رئيس قسم بتاريخ 13/08/2013 - رئيس قسم بتاريخ 21/07/2008",
    ),
    (
        "What are dr Throut youssef elghalban achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2000 * Master's (Libraries) - (Tanta University) - 1995 * Bachelor's (Libraries) - (Tanta University) - With Very Good Honors - 1990 * Professor - By Decision dated 01/10/2012, effective from 01/10/2012 * Associate Professor - By Decision dated 06/07/2008, effective from 30/06/2008 * Lecturer - By Decision dated 02/05/2000, effective from 29/04/2000 * Assistant Lecturer - By Decision dated 21/01/1996, effective from 21/01/1996 * Teaching Assistant - By Decision dated 07/08/1990, effective from 07/08/1990 * Head of Department - Dated 13/08/2013 * Head of Department - Dated 21/07/2008",
    ),
    (
        "كيف التواصل مع الدكتور احمد عبادة العربي؟",
        "عن طريق الايميل الخاص به : ahmed.ebada@art.tanta.edu.eg ",
    ),
    (
        "How can i contact to dr Ahmed ebada elarabi?",
        "Email: ahmed.ebada@art.tanta.edu.eg",
    ),
    (
        "ماهي وظيفة الدكتوراحمد عبادة العربي؟",
        "استاذ جامعي",
    ),
    (
        "What are dr ahmed ebada elarabi current job?",
        "Professor",
    ),
    (
        "ماهي انجازات الدكتور احمد عبادة العربي؟",
        "الدكتوراه (مكتبات) - (جامعة طنطا) - عام 2001; الماجستير (مكتبات) - (جامعة طنطا) - عام 1999; الليسانس (مكتبات) - (جامعة طنطا) - بتقدير امتياز - عام 1992; استاذ بقرار بتاريخ 02/09/2015 اعتبارا من 31/08/2015; استاذ مساعد بقرار بتاريخ 04/04/2010 اعتبارا من 30/03/2010; مدرس بقرار بتاريخ 14/02/2002 اعتبارا من 29/01/2002; مدرس مساعد بقرار بتاريخ 24/02/1999 اعتبارا من 24/02/1999; معيد بقرار بتاريخ 30/12/1992 اعتبارا من 02/01/1993; معيد بقرار بتاريخ 30/12/1992 اعتبارا من 30/12/1992; وكيل الكلية لشئون خدمة المجتمع وتنمية البيئة بتاريخ 01/06/2016; رئيس قسم بتاريخ 16/09/2015",
    ),
    (
        "What are dr ahmed ebada elarabi achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2001; * Master's (Libraries) - (Tanta University) - 1999; * Bachelor's (Libraries) - (Tanta University) - with Honors - 1992; * Professor by decision dated 09/02/2015 effective from 08/31/2015; * Associate Professor by decision dated 04/04/2010 effective from 03/30/2010; * Lecturer by decision dated 02/14/2002 effective from 01/29/2002; * Assistant Lecturer by decision dated 02/24/1999 effective from 02/24/1999; * Demonstrator by decision dated 12/30/1992 effective from 01/02/1993; * Demonstrator by decision dated 12/30/1992 effective from 12/30/1992; * Vice Dean of the College for Community Service and Environmental Development Affairs dated 06/01/2016; * Head of Department dated 09/16/2015",
    ),
    (
        "كيف اتواصل مع الدكتور بدوية محمد البسيوني؟",
        "عن طريق الايميل الخاص به : badawia.elbasuni@art.tanta.edu.eg",
    ),
    (
        "How can i contact to dr Badawia mohammed elbasuni?",
        "Email : badawia.elbasuni@art.tanta.edu.eg ",
    ),
    (
        "ماهي وظيفة الدكتور بدوية محمد البسيوني حاليا؟",
        "استاذ جامعي",
    ),
    (
        "What are dr Badawia mohmmed elbasuni current job?",
        "Professor",
    ),
    (
        "ماهي انجازات الدكتور بدوية محمد البسيوني؟",
        "الدكتوراه (مكتبات) - (جامعة طنطا) - عام 2005; الماجستير (مكتبات) - (جامعة طنطا) - عام 2002; الليسانس (مكتبات) - (جامعة طنطا) - بتقدير جيد جدا مع مرتبة الشرف - عام 1996; استاذ بقرار بتاريخ 06/12/2015 اعتبارا من 30/11/2015; استاذ مساعد بقرار بتاريخ 31/07/2010 اعتبارا من 27/07/2010; مدرس بقرار بتاريخ 03/04/2005 اعتبارا من 29/03/2005; مدرس مساعد بقرار بتاريخ 04/03/2002 اعتبارا من 04/03/2002; معيد بقرار بتاريخ 16/02/1997 اعتبارا من 18/02/1997; معيد بقرار بتاريخ 16/02/1997 اعتبارا من 16/02/1997; قائم باعمال رئاسة القسم بتاريخ 27/07/2016",
    ),
    (
        "What are dr Badawia mohmmed elbasuni achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2005; * Master's (Libraries) - (Tanta University) - 2002; * Bachelor's (Libraries) - (Tanta University) - Very Good with Honors - 1996; * Professor by decision dated 12/06/2015 effective from 11/30/2015; * Associate Professor by decision dated 07/31/2010 effective from 07/27/2010; * Lecturer by decision dated 04/03/2005 effective from 03/29/2005; * Assistant Lecturer by decision dated 03/04/2002 effective from 03/04/2002; * Demonstrator by decision dated 02/16/1997 effective from 02/18/1997; * Demonstrator by decision dated 02/16/1997 effective from 02/16/1997; * Acting Head of Department dated 07/27/2016",
    ),
    (
        "كيف اتواصل مع الدكتور نادية سعد مرسي علي؟",
        "عن طريق الهاتف : 01231231231  - عن طريق الايميل الخاص به : nadia.ali@art.tanta.edu.eg",
    ),
    (
        "How can i contact to dr Nadia saad ali?",
        "Phone : 01231231231  - Email : nadia.ali@art.tanta.edu.eg",
    ),
    (
        "ماهي وظيفة الدكتور نادية سعد مرسي علي حاليا؟",
        "استاذ مساعد",
    ),
    (
        "What are dr Nadia saad ali current job?",
        "Associate Professor",
    ),
    (
        "ماهي انجازات الدكتور نادية سعد مرسي علي؟",
        "الدكتوراه (مكتبات) - (جامعة طنطا) - عام 2005; الماجستير (مكتبات) - (جامعة طنطا) - عام 2002; الليسانس (مكتبات) - (جامعة طنطا) - بتقدير جيد جدا - عام 1996; استاذ مساعد بقرار بتاريخ 01/04/2019 اعتبارا من 30/03/2019; مدرس بقرار بتاريخ 02/10/2005 اعتبارا من 27/09/2005; مدرس مساعد بقرار بتاريخ 02/12/2002 اعتبارا من 02/12/2002; معيد بقرار بتاريخ 25/07/1996 اعتبارا من 25/07/1996; معيد بقرار بتاريخ 30/12/1992 اعتبارا من 02/01/1993",
    ),
    (
        "What are dr Nadia saad ali achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2005; * Master's (Libraries) - (Tanta University) - 2002; * Bachelor's (Libraries) - (Tanta University) - Very Good - 1996; * Associate Professor by decision dated 04/01/2019 effective from 03/30/2019; * Lecturer by decision dated 10/02/2005 effective from 09/27/2005; * Assistant Lecturer by decision dated 12/02/2002 effective from 12/02/2002; * Demonstrator by decision dated 07/25/1996 effective from 07/25/1996; * Demonstrator by decision dated 12/30/1992 effective from 01/02/1993",
    ),
    (
        "كيف اتواصل مع الدكتور هبه فتحي دنيا",
        "عن طريق الهاتف : 01004485934  - عن طريق الايميل الخاص به : heba.basuni@art.tanta.edu.eg",
    ),
    (
        "How can i contact to dr Heba Fathy donia?",
        "Phone : 01004485934  - Email :heba.basuni@art.tanta.edu.eg "
        "heba matboly phone number",
    ),
    (
        "ماهي وظيفة الدكتور هبه فتحي دنيا حاليا؟",
        "استاذ مساعد",
    ),
    (
        "What are dr Heba fathy donia current job?",
        "Associate Professor",
    ),
    (
        "ماهي انجازات الدكتور هبه فتحي دنيا؟",
        "الدكتوراه (مكتبات) - (جامعة طنطا) - عام 2008; الماجستير (مكتبات) - (جامعة طنطا) - عام 2004; الليسانس (مكتبات) - (جامعة طنطا) - بتقدير جيد جدا مع مرتبة الشرف - عام 1998; استاذ مساعد بقرار بتاريخ 06/01/2021 اعتبارا من 30/12/2020; مدرس بقرار بتاريخ 06/08/2008 اعتبارا من 31/07/2008; مدرس مساعد بقرار بتاريخ 31/10/2004 اعتبارا من 31/10/2004; معيد بقرار بتاريخ 26/11/2000 اعتبارا من 10/12/2000; معيد بقرار بتاريخ 26/11/2000 اعتبارا من 26/11/2000",
    ),
    (
        "What are dr Heba fathy donia achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2008; * Master's (Libraries) - (Tanta University) - 2004; * Bachelor's (Libraries) - (Tanta University) - Very Good with Honors - 1998; * Associate Professor by decision dated 01/06/2021 effective from 12/30/2020; * Lecturer by decision dated 08/06/2008 effective from 07/31/2008; * Assistant Lecturer by decision dated 10/31/2004 effective from 10/31/2004; * Demonstrator by decision dated 11/26/2000 effective from 12/10/2000; * Demonstrator by decision dated 11/26/2000 effective from 11/26/2000",
    ),
    (
        "كيف اتواصل مع الدكتور هبه احمد محمد المتبولي؟",
        "عن طريق الهاتف : 01065129397 - عن طريق الايميل الخاص به : heba.elmatboley@art.tanta.edu.eg",
    ),
    (
        "How can i contact to dr Heba ahmed elmatboley?",
        "Phone : 01065129397  - Email:heba.elmatboley@art.tanta.edu.eg ",
    ),
    (
        "ماهي وظيفة الدكتور هبه احمد محمد المتبولي؟",
        "استاذ مساعد",
    ),
    (
        "What are dr Heba ahmed elmatboley current job?",
        "Associate Professor",
    ),
    (
        "ماهي انجازات الدكتور هبه احمد محمد المتبولي؟",
        "الدكتوراه (مكتبات) - (جامعة طنطا) - عام 2015; الماجستير (مكتبات) - (جامعة طنطا) - عام 2011; الليسانس (مكتبات) - (جامعة طنطا) - بتقدير جيد جدا مع مرتبة الشرف - عام 2005; استاذ مساعد بقرار بتاريخ 07/05/2022 اعتبارا من 27/04/2022; مدرس بقرار بتاريخ 08/12/2015 اعتبارا من 31/08/2015; مدرس مساعد بقرار بتاريخ 08/08/2011 اعتبارا من 08/08/2011; معيد بقرار بتاريخ 18/07/2006 اعتبارا من 12/08/2006; معيد بقرار بتاريخ 18/07/2006 اعتبارا من 18/07/2006",
    ),
    (
        "What are dr Heba ahmed elmatboley achievements?",
        "* Doctorate (Libraries) - (Tanta University) - 2015; * Master's (Libraries) - (Tanta University) - 2011; * Bachelor's (Libraries) - (Tanta University) - Very Good with Honors - 2005; * Associate Professor by decision dated 05/07/2022 effective from 04/27/2022; * Lecturer by decision dated 12/08/2015 effective from 08/31/2015; * Assistant Lecturer by decision dated 08/08/2011 effective from 08/08/2011; * Demonstrator by decision dated 07/18/2006 effective from 08/12/2006; * Demonstrator by decision dated 07/18/2006 effective from 07/18/2006",
    ),
]


insert_multiple_responses(data)
