import matplotlib
matplotlib.use('Agg')  # Set the backend to non-interactive
import matplotlib.pyplot as plt
import numpy as np
import os

def create_tam_sam_som_chart(tam, sam, som):
    # Create figure and axis with smaller size
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Colors for each circle
    colors = ['#2b87f9', '#4299e1', '#93C5FD']
    
    # Create the three nested circles
    tam_circle = plt.Circle((0.5, 0.5), 0.35, color=colors[0])
    sam_circle = plt.Circle((0.5, 0.5), 0.25, color=colors[1])
    som_circle = plt.Circle((0.5, 0.5), 0.15, color=colors[2])
    
    # Add circles to plot
    ax.add_patch(tam_circle)
    ax.add_patch(sam_circle)
    ax.add_patch(som_circle)
    
    # Format numbers for display
    def format_number(num):
        if num >= 1e9:
            return f"${num/1e9:.1f}B"
        return f"${num/1e6:.0f}M"
    
    # Add text labels with formatted values
    plt.text(0.5, 0.7, f'TAM\n{format_number(tam)}', ha='center', va='center', 
             color='white', fontsize=10, fontweight='bold')
    plt.text(0.5, 0.5, f'SAM\n{format_number(sam)}', ha='center', va='center', 
             color='white', fontsize=10, fontweight='bold')
    plt.text(0.5, 0.35, f'SOM\n{format_number(som)}', ha='center', va='center', 
             color='white', fontsize=10, fontweight='bold')
    
    # Set aspect ratio and remove axes
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set the plot limits for proper centering
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Save the plot with transparent background
    plt.savefig('static/tam_sam_som.png', 
                bbox_inches='tight', 
                dpi=150,
                transparent=True,
                pad_inches=0.05)
    plt.close()