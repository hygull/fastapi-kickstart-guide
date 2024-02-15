## What are the steps for DB migrations using alembic?

Yes, you're correct. After defining the SQLAlchemy models, it's essential to perform database migrations to create the corresponding tables in the database. This step ensures that the database schema matches the defined models.

To perform database migrations with SQLAlchemy, you typically use a migration tool like Alembic. Alembic allows you to generate migration scripts based on changes to your models and apply those changes to the database.

Here's a general outline of the steps to perform migrations with Alembic:

**Install Alembic:** If you haven't already, install Alembic using pip:

```bash
pip install alembic
```

**Set up Alembic:** Initialize Alembic in your project directory by running:

```bash
alembic init alembic
```

**Configure Alembic:** Edit the **alembic.ini** file to configure the database connection URL.

**Define the Migration Script:** After defining your SQLAlchemy models, generate a migration script with Alembic by running:

```bash
alembic revision --autogenerate -m "Initial migration"
```

**Apply Migrations:** Apply the generated migration script to the database to create the tables:

```bash
alembic upgrade head
```

**Verify:** Verify that the tables have been created in the database.

By following these steps, you ensure that your SQLAlchemy models are synchronized with the database schema. After any subsequent changes to your models, you can generate new migration scripts and apply them to update the database schema accordingly