import enum


class RoleType(enum.Enum):
    admin = 'admin',
    student = 'student',
    consultor = 'consultor',


class State(enum.Enum):
    pending = 'Pending',
    in_progress = 'In Progress',
    terminated = 'Terminated'

class Category(enum.Enum):
    final_work = 'Final Work',
    inscriptions = 'Inscriptions',
    income_25 = 'Income Older Than 25 Years',
    others = 'Others',