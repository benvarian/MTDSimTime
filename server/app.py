import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify, url_for
from experiments.run import execute_simulation, create_experiment_snapshots
import matplotlib
matplotlib.use('Agg')  # Set the backend for writing to file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    # Collect data from the form
    network_size_list = [int(size) for size in request.form.get(
        'network_size_list').split(",")]
    start_time = int(request.form.get('start_time'))
    finish_time = int(request.form.get('finish_time'))
    mtd_interval = int(request.form.get('mtd_interval'))
    scheme = request.form.get('scheme')
    total_nodes = int(request.form.get('total_nodes'))

    # Process the simulation and snapshot creation
    create_experiment_snapshots(network_size_list)
    evaluation = execute_simulation(start_time=start_time, finish_time=finish_time,
                                    mtd_interval=mtd_interval, scheme=scheme, total_nodes=total_nodes)

    evaluation.get_network().draw()

    # Return a JSON response
    return jsonify({
        'image_url': url_for('static', filename='experimental_data/plots/network.png')
    })


if __name__ == '__main__':
    app.run(debug=True)
