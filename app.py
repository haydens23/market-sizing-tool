from flask import Flask, render_template, request
from dotenv import load_dotenv
from marketSizingTool.gemini_summary import generate_summary
from marketSizingTool.visualization import create_tam_sam_som_chart
import os

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    chart_created = False
    market_sizes = None
    
    if request.method == 'POST':
        business_summary = request.form.get('business_summary', '')
        geography = request.form.get('geography', '')
        trend = request.form.get('trend', '')
        traits = request.form.get('traits', '')
        
        summary = generate_summary(business_summary, geography, trend, traits)
        if summary is None:
            return render_template('index.html', 
                                error="Failed to generate market size analysis. Please try again.")
        
        try:
            # Extract TAM value and calculate SAM and SOM
            tam_text = summary['TAM']
            tam_value = float(''.join(filter(str.isdigit, tam_text)))
            sam_value = tam_value * 0.4
            som_value = sam_value * 0.2
            
            # Format numbers with shorter representation
            def format_number(num):
                if num >= 1e9:
                    return f"${num/1e9:.1f}B"
                return f"${num/1e6:.0f}M"
            
            # Create market sizes dictionary with formatted values
            market_sizes = {
                'tam': format_number(tam_value),
                'sam': format_number(sam_value),
                'som': format_number(som_value)
            }
            
            # Generate visualization
            create_tam_sam_som_chart(tam_value, sam_value, som_value)
            chart_created = True
            
        except Exception as e:
            print(f"Error creating visualization: {e}")
            chart_created = False
            market_sizes = None
    
    return render_template('index.html', 
                         summary=summary, 
                         chart_created=chart_created,
                         market_sizes=market_sizes)

if __name__ == '__main__':
    app.run(debug=True)