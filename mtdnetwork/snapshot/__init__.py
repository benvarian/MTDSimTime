import os

# Get the current directory where the script is run from
current_directory = os.path.dirname(os.path.abspath(__file__))


class Snapshot:
    def __init__(self):
        if not os.path.exists(current_directory + '/snapshots'):
            os.makedirs(current_directory + '/snapshots')

    @staticmethod
    def get_file_by_suffix(file_name: str, suffix: str):
        return os.path.join(current_directory + '/snapshots', f'{file_name}_{suffix}.pkl')
