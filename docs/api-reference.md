# API Reference - GenAI Telco TCO Builder

## Core Classes

### TelcoDeployment

Represents a complete telco deployment specification.

```python
from genai_telco_tco.models import TelcoDeployment, ComputeResources, StorageResources, NetworkResources, UserPlaneLocation

deployment = TelcoDeployment(
    user_plane=UserPlaneLocation.REGION,
    compute=ComputeResources(vcpu=96, memory=384),
    storage=StorageResources(ebs_storage=1000, efs_storage=500),
    network=NetworkResources(peak_bandwidth=10.0, monthly_tonnage=1000.0),
    eks_clusters=2,
    sites=3,
    region="us-east-1"
)
```

**Fields:**
- `user_plane`: UserPlaneLocation (REGION or OUTPOSTS)
- `compute`: ComputeResources specification
- `storage`: StorageResources specification  
- `network`: NetworkResources specification
- `eks_clusters`: Number of EKS clusters (int)
- `sites`: Number of deployment sites (int)
- `region`: AWS region string

### CostOptimizer

Main class for performing TCO analysis.

```python
from genai_telco_tco.calculator import CostOptimizer

optimizer = CostOptimizer()
analysis = optimizer.analyze_deployment(deployment)
```

**Methods:**
- `analyze_deployment(deployment: TelcoDeployment) -> CostAnalysis`

### NetworkCalculator

Calculates network-related costs.

```python
from genai_telco_tco.calculator import NetworkCalculator

calc = NetworkCalculator(region="us-east-1")
transfer_costs = calc.calculate_data_transfer_costs(deployment)
bandwidth_costs = calc.calculate_bandwidth_costs(deployment)
```

**Methods:**
- `calculate_data_transfer_costs(deployment: TelcoDeployment) -> Dict[str, float]`
- `calculate_bandwidth_costs(deployment: TelcoDeployment) -> float`

### ComputeCalculator

Calculates compute-related costs and provides instance recommendations.

```python
from genai_telco_tco.calculator import ComputeCalculator

calc = ComputeCalculator(region="us-east-1")
recommendations = calc.recommend_instance_types(vcpu=96, memory=384)
costs = calc.calculate_compute_costs(deployment)
```

**Methods:**
- `recommend_instance_types(vcpu: int, memory: int) -> List[Dict[str, any]]`
- `calculate_compute_costs(deployment: TelcoDeployment) -> Dict[str, float]`

### ReportGenerator

Generates formatted reports from cost analysis.

```python
from genai_telco_tco.report_generator import ReportGenerator

generator = ReportGenerator()
markdown_report = generator.generate_markdown_report(analysis)
summary = generator.generate_executive_summary(analysis)
```

**Methods:**
- `generate_markdown_report(analysis: CostAnalysis) -> str`
- `generate_executive_summary(analysis: CostAnalysis) -> Dict[str, Any]`

## Data Models

### ComputeResources

```python
ComputeResources(
    vcpu=96,                    # Total vCPU cores (int)
    memory=384,                 # Total memory in GB (int)
    instance_types=None         # Optional preferred instance types (List[str])
)
```

### StorageResources

```python
StorageResources(
    ebs_storage=1000,          # EBS storage in GB (int)
    efs_storage=500,           # EFS storage in GB (int)
    s3_storage=0               # S3 storage in GB (int)
)
```

### NetworkResources

```python
NetworkResources(
    peak_bandwidth=10.0,       # Peak bandwidth in Gbps (float)
    monthly_tonnage=1000.0,    # Monthly data transfer in TB (float)
    traffic_split=TrafficSplit(
        direct_connect_percent=80.0,
        internet_gateway_percent=20.0
    )
)
```

### CostAnalysis

Result object containing complete TCO analysis.

**Fields:**
- `deployment`: Original TelcoDeployment specification
- `monthly_costs`: CostBreakdown for monthly costs
- `annual_costs`: CostBreakdown for annual costs
- `three_year_tco`: Total 3-year cost (float)
- `cost_per_site`: Monthly cost per site (float)
- `recommendations`: List of optimization recommendations
- `assumptions`: List of analysis assumptions
- `exclusions`: List of excluded costs

### CostBreakdown

Detailed cost breakdown by service category.

**Fields:**
- `compute_cost`: EC2 and compute costs (float)
- `storage_cost`: Storage service costs (float)
- `network_cost`: Network and bandwidth costs (float)
- `eks_cost`: EKS cluster management costs (float)
- `data_transfer_cost`: Data transfer costs (float)
- `total_monthly_cost`: Sum of all costs (float)

## Enums

### UserPlaneLocation

```python
from genai_telco_tco.models import UserPlaneLocation

UserPlaneLocation.REGION     # AWS Region deployment
UserPlaneLocation.OUTPOSTS   # AWS Outposts deployment
```

## Plugin Integration

### TelcoTCOPlugin

Amazon Q CLI plugin class.

```python
from genai_telco_tco.plugin import TelcoTCOPlugin

plugin = TelcoTCOPlugin()
result = plugin.execute_command("build-tco", parameters)
```

**Methods:**
- `get_plugin_info() -> Dict[str, Any]`
- `execute_command(command: str, parameters: Dict[str, Any]) -> Dict[str, Any]`
- `get_help(command: str = None) -> str`

## Error Handling

All classes use Pydantic for data validation and will raise `ValidationError` for invalid inputs.

```python
from pydantic import ValidationError

try:
    deployment = TelcoDeployment(
        user_plane="invalid",  # Will raise ValidationError
        compute=ComputeResources(vcpu=96, memory=384),
        # ... other fields
    )
except ValidationError as e:
    print(f"Validation error: {e}")
```

## Examples

### Basic Usage

```python
from genai_telco_tco import TelcoDeployment, CostOptimizer, ComputeResources, StorageResources, NetworkResources, UserPlaneLocation

# Define deployment
deployment = TelcoDeployment(
    user_plane=UserPlaneLocation.REGION,
    compute=ComputeResources(vcpu=96, memory=384),
    storage=StorageResources(ebs_storage=1000, efs_storage=500),
    network=NetworkResources(peak_bandwidth=10.0, monthly_tonnage=1000.0),
    eks_clusters=2,
    sites=3
)

# Analyze costs
optimizer = CostOptimizer()
analysis = optimizer.analyze_deployment(deployment)

# Print results
print(f"Monthly Cost: ${analysis.monthly_costs.total_monthly_cost:,.2f}")
print(f"3-Year TCO: ${analysis.three_year_tco:,.2f}")
```

### Comparison Analysis

```python
# Compare region vs outposts
region_deployment = TelcoDeployment(user_plane=UserPlaneLocation.REGION, ...)
outposts_deployment = TelcoDeployment(user_plane=UserPlaneLocation.OUTPOSTS, ...)

region_analysis = optimizer.analyze_deployment(region_deployment)
outposts_analysis = optimizer.analyze_deployment(outposts_deployment)

savings = region_analysis.monthly_costs.total_monthly_cost - outposts_analysis.monthly_costs.total_monthly_cost
print(f"Monthly Savings with Outposts: ${savings:,.2f}")
```