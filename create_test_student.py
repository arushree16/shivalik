from app import app, db, Student

with app.app_context():
    # Create a test student
    student = Student(
        name='Test Student',
        class_name='8A',
        roll_no='101',
        admission_no='2024101',
        fathers_name='Test Father',
        english_pa=9,
        english_ma=8,
        english_portfolio=9,
        english_se=9,
        english_term=55,
        hindi_pa=8,
        hindi_ma=9,
        hindi_portfolio=8,
        hindi_se=9,
        hindi_term=52,
        maths_pa=10,
        maths_ma=9,
        maths_portfolio=9,
        maths_se=8,
        maths_term=58,
        science_pa=9,
        science_ma=8,
        science_portfolio=9,
        science_se=9,
        science_term=54,
        sst_pa=8,
        sst_ma=9,
        sst_portfolio=9,
        sst_se=8,
        sst_term=53,
        gk_grade='A',
        computer_grade='A',
        drawing_grade='A'
    )
    
    # Add and commit to database
    db.session.add(student)
    db.session.commit()
    print('Test student created with ID:', student.id)
