"""
GenAI Telco TCO Builder - Amazon Q CLI Plugin
Comprehensive Total Cost of Ownership analysis for telco infrastructure on AWS
"""

__version__ = "1.0.0"
__author__ = "AWS Labs"
__email__ = "aws-labs@amazon.com"

from .plugin import TelcoTCOPlugin
from .calculator import NetworkCalculator, CostOptimizer
from .models import TelcoDeployment, CostAnalysis

__all__ = [
    "TelcoTCOPlugin",
    "NetworkCalculator", 
    "CostOptimizer",
    "TelcoDeployment",
    "CostAnalysis",
]