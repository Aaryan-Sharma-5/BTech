import subprocess
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline_execution.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Pipeline configuration
SCRIPTS_DIR = Path('scripts')
DATA_DIR = Path('data')
OUTPUTS_DIR = Path('outputs')
VISUALIZATIONS_DIR = OUTPUTS_DIR / 'visualizations'
METRICS_DIR = OUTPUTS_DIR / 'metrics'

PIPELINE_STEPS = [
    {
        'name': 'Data Collection',
        'script': SCRIPTS_DIR / '1)dataset.py',
        'description': 'Fetching humidity data from Open-Meteo API',
        'required_output': DATA_DIR / 'ghatkopar_humidity_2023_2024.csv'
    },
    {
        'name': 'Data Preprocessing',
        'script': SCRIPTS_DIR / '2)data_processing.py',
        'description': 'Cleaning and validating data',
        'required_output': DATA_DIR / 'cleaned_humidity.csv'
    },
    {
        'name': 'Exploratory Data Analysis',
        'script': SCRIPTS_DIR / '3)EDA.py',
        'description': 'Analyzing trends and patterns',
        'required_output': VISUALIZATIONS_DIR / 'humidity_trend.png'
    },
    {
        'name': 'ARIMA Modeling',
        'script': SCRIPTS_DIR / '4)forecasting_with_arima.py',
        'description': 'Building ARIMA forecast model',
        'required_output': DATA_DIR / 'forecast_results.csv'
    },
    {
        'name': 'ARIMA Evaluation',
        'script': SCRIPTS_DIR / '5)model_evaluation.py',
        'description': 'Evaluating ARIMA performance',
        'required_output': METRICS_DIR / 'arima_evaluation_metrics.csv'
    },
    {
        'name': 'SARIMA Modeling',
        'script': SCRIPTS_DIR / '6)forecasting_with_sarima.py',
        'description': 'Building SARIMA forecast model',
        'required_output': DATA_DIR / 'forecast_results_sarima.csv'
    },
    {
        'name': 'Model Comparison',
        'script': SCRIPTS_DIR / '7)model_evaluation_sarima.py',
        'description': 'Comparing ARIMA vs SARIMA',
        'required_output': METRICS_DIR / 'model_comparison_metrics.csv'
    }
]

def check_dependencies():
    """Check if required packages are installed"""
    logger.info("Checking dependencies...")
    
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 
        'statsmodels', 'sklearn', 'scipy', 'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            logger.info(f"{package} is installed")
        except ImportError:
            missing_packages.append(package)
            logger.error(f"{package} is NOT installed")
    
    if missing_packages:
        logger.error("\nMissing packages detected!")
        logger.error("Install them using: pip install -r requirements.txt")
        return False
    
    logger.info("All dependencies are satisfied\n")
    return True

def run_script(script_name, step_name, description):
    """Run a script as a subprocess and log its output"""
    logger.info("="*70)
    logger.info(f"STEP: {step_name}")
    logger.info(f"Script: {script_name}")
    logger.info(f"Description: {description}")
    logger.info("="*70)
    
    try:
        # Run the script from project root (scripts use relative paths from their location)
        result = subprocess.run(
            [sys.executable, str(script_name)],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=Path.cwd()  # Run from project root
        )
        
        # Log output
        if result.stdout:
            print(result.stdout)
        
        if result.stderr and result.returncode != 0:
            logger.error(f"Error output:\n{result.stderr}")
        
        if result.returncode == 0:
            logger.info(f"{step_name} completed successfully\n")
            return True
        else:
            logger.error(f"{step_name} failed with return code {result.returncode}\n")
            return False
            
    except subprocess.TimeoutExpired:
        logger.error(f"{step_name} timed out after 5 minutes\n")
        return False
    except Exception as e:
        logger.error(f"{step_name} failed with error: {e}\n")
        return False

def verify_output(output_file):
    """Verify that expected output file was created"""
    if Path(output_file).exists():
        logger.info(f"Output verified: {output_file}")
        return True
    else:
        logger.warning(f"Output file not found: {output_file}")
        return False

def main():
    """Main pipeline execution"""
    logger.info("\n" + "="*70)
    logger.info("HUMIDITY PREDICTION PIPELINE - STARTING")
    logger.info("="*70 + "\n")
    
    # Check dependencies
    if not check_dependencies():
        logger.error("Pipeline aborted due to missing dependencies")
        return False
    
    # Track execution
    completed_steps = []
    failed_steps = []
    
    # Execute each step
    for i, step in enumerate(PIPELINE_STEPS, 1):
        logger.info(f"\n{'='*70}")
        logger.info(f"Executing Step {i}/{len(PIPELINE_STEPS)}")
        logger.info(f"{'='*70}\n")
        
        success = run_script(
            step['script'],
            step['name'],
            step['description']
        )
        
        if success:
            completed_steps.append(step['name'])
            # Verify output was created
            verify_output(step['required_output'])
        else:
            failed_steps.append(step['name'])
            logger.error(f"\nStep failed: {step['name']}")
            
            # Ask user if they want to continue
            user_input = input("\nContinue with next step? (y/n): ").strip().lower()
            if user_input != 'y':
                logger.info("Pipeline execution aborted by user")
                break
    
    # Final summary
    logger.info("\n" + "="*70)
    logger.info("PIPELINE EXECUTION SUMMARY")
    logger.info("="*70)
    logger.info(f"Total Steps: {len(PIPELINE_STEPS)}")
    logger.info(f"Completed: {len(completed_steps)}")
    logger.info(f"Failed: {len(failed_steps)}")
    
    if completed_steps:
        logger.info("\nCompleted Steps:")
        for step in completed_steps:
            logger.info(f"   • {step}")
    
    if failed_steps:
        logger.info("\nFailed Steps:")
        for step in failed_steps:
            logger.info(f"   • {step}")
    
    logger.info("="*70)
    
    # Check if all steps completed
    if len(completed_steps) == len(PIPELINE_STEPS):
        logger.info("\nSUCCESS! All pipeline steps completed successfully!")
        logger.info("\nGenerated Files:")
        logger.info("   • ghatkopar_humidity_2023_2024.csv - Raw data")
        logger.info("   • cleaned_humidity.csv - Processed data")
        logger.info("   • Multiple visualization PNG files")
        logger.info("   • forecast_results.csv - ARIMA predictions")
        logger.info("   • forecast_results_sarima.csv - SARIMA predictions")
        logger.info("   • model_comparison_metrics.csv - Final comparison")
        logger.info("\nCheck README.md for detailed documentation")
        return True
    else:
        logger.warning("\nPipeline completed with some failures")
        logger.warning("Check pipeline_execution.log for details")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("\n\nPipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"\n\nPipeline failed with unexpected error: {e}")
        sys.exit(1)
