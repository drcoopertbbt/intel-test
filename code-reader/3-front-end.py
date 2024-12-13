from flask import Flask, render_template_string, request
from datasets import load_from_disk
import os

app = Flask(__name__)

# Function to load dataset
def load_dataset(dataset_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, dataset_name)
    dataset = load_from_disk(dataset_path)
    return dataset.to_pandas()

# Load both datasets
datasets = {
    'training': 'nvd_training_data_10Dec24.hf',
    'testing': 'nvd_testing_data_10Dec24.hf'
}

# Initialize with testing dataset
current_df = load_dataset(datasets['testing'])

# HTML template with Tailwind CSS
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>CVE Dataset Viewer</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl">Page {{ current_page }} of {{ total_pages }}</h1>
            <div class="flex gap-4">
                <form method="GET" action="{{ url_for('switch_dataset') }}" class="flex items-center gap-2">
                    <select name="dataset" class="p-2 rounded border" onchange="this.form.submit()">
                        <option value="testing" {{ 'selected' if current_dataset == 'testing' else '' }}>Testing Dataset</option>
                        <option value="training" {{ 'selected' if current_dataset == 'training' else '' }}>Training Dataset</option>
                    </select>
                </form>
            </div>
        </div>
        
        {% for idx in range(start_idx, end_idx) %}
        <div class="bg-white p-6 rounded-lg shadow-md mb-4">
            <h2 class="text-lg font-bold mb-2">Record {{ idx + 1 }}</h2>
            <div class="mb-4">
                <h3 class="font-semibold">Description:</h3>
                <p class="text-gray-700 whitespace-pre-wrap">{{ df.iloc[idx]['description'] }}</p>
            </div>
            <div>
                <h3 class="font-semibold">Text:</h3>
                <p class="text-gray-700 whitespace-pre-wrap">{{ df.iloc[idx]['text'] }}</p>
            </div>
        </div>
        {% endfor %}

        <div class="flex justify-between mt-4 mb-8">
            <a href="{{ url_for('show_page', page=current_page-1, dataset=current_dataset) if current_page > 1 else '#' }}"
               class="px-4 py-2 bg-blue-500 text-white rounded {{ 'opacity-50 cursor-not-allowed' if current_page == 1 else '' }}">
                Previous
            </a>
            <a href="{{ url_for('show_page', page=current_page+1, dataset=current_dataset) if current_page < total_pages else '#' }}"
               class="px-4 py-2 bg-blue-500 text-white rounded {{ 'opacity-50 cursor-not-allowed' if current_page == total_pages else '' }}">
                Next
            </a>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return show_page(1)

@app.route('/switch')
def switch_dataset():
    dataset_name = request.args.get('dataset', 'testing')
    return show_page(1, dataset_name)

@app.route('/page/<int:page>')
def show_page(page, dataset_name=None):
    global current_df
    
    if dataset_name is None:
        dataset_name = request.args.get('dataset', 'testing')
    
    # Load the selected dataset if it's different from current
    if dataset_name in datasets:
        current_df = load_dataset(datasets[dataset_name])
    
    rows_per_page = 3
    total_pages = len(current_df) // rows_per_page + (1 if len(current_df) % rows_per_page else 0)
    
    # Ensure page is within valid range
    page = max(1, min(page, total_pages))
    
    start_idx = (page - 1) * rows_per_page
    end_idx = min(start_idx + rows_per_page, len(current_df))
    
    return render_template_string(
        HTML_TEMPLATE,
        df=current_df,
        current_page=page,
        total_pages=total_pages,
        start_idx=start_idx,
        end_idx=end_idx,
        current_dataset=dataset_name
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')