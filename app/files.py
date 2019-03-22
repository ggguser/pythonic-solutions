from pathlib import Path


def relative_to_absolute(relative_path, filename):
    """
    Example:
    relative_path = '../data'
    filename = 'filename.txt'
    relative_to_absolute('01_own_apps', '07_relative_to_absolute_path.py')
    Result:
    C:\LagunovProjects\Playground\01_own_apps\01_own_apps\07_relative_to_absolute_path.py
    """
    work_dir = Path(__file__).parent
    return (work_dir / relative_path / filename).resolve()
