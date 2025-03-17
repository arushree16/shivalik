from app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        # Add attendance column
        try:
            with db.engine.connect() as conn:
                conn.execute(db.text('ALTER TABLE student ADD COLUMN attendance INTEGER DEFAULT 80'))
                conn.commit()
            print("Added attendance column")
        except Exception as e:
            print(f"Attendance column might already exist: {str(e)}")

        # Add new columns for co-curricular subjects
        columns = [
            'gk_pa', 'gk_ma', 'gk_portfolio', 'gk_se', 'gk_term',
            'computer_pa', 'computer_ma', 'computer_portfolio', 'computer_se', 'computer_term',
            'drawing_pa', 'drawing_ma', 'drawing_portfolio', 'drawing_se', 'drawing_term'
        ]
        
        for column in columns:
            try:
                with db.engine.connect() as conn:
                    conn.execute(db.text(f'ALTER TABLE student ADD COLUMN {column} INTEGER DEFAULT 0'))
                    conn.commit()
                print(f"Added column: {column}")
            except Exception as e:
                print(f"Column {column} might already exist: {str(e)}")
        
        print("Migration completed!")
