from smarts import db
from smarts.models import Message
from pathlib import Path
import json
from datetime import datetime
from smarts.commands import db_manage_bp


@db_manage_bp.cli.group()
def db_manage():
    """ Database management commands """
    pass


@db_manage.command()
def add_data():
    """ Add sample data to database """

    try:
        messages_path = Path(__file__).parent.parent / 'samples' / 'messages.json'
        with open(messages_path) as file:
            data_json = json.load(file)
        for item in data_json:
            item['date'] = datetime.strptime(item['date'], '%d-%m-%Y').date()
            message = Message(**item)
            db.session.add(message)
        db.session.commit()
        print('Data has been successfully added to database')
    except Exception as exc:
        print(f'Unexpected error: {exc}')


@db_manage.command()
def remove_data():
    """ Remove all data from the database """

    try:
        db.session.execute('TRUNCATE TABLE messages')
        db.session.commit()
        print('Data has been successfully remove from database')
    except Exception as exc:
        print(f'Unexpected error: {exc}')
