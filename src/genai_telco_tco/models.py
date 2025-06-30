"""
Data models for telco TCO analysis
"""

from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field
from enum import Enum


class UserPlaneLocation(str, Enum):
    """User plane deployment location options"""
    REGION = "region"
    OUTPOSTS = "outposts"


class TrafficSplit(BaseModel):
    """Traffic distribution configuration"""
    direct_connect_percent: float = Field(default=80.0, ge=0, le=100)
    internet_gateway_percent: float = Field(default=20.0, ge=0, le=100)
    
    def __post_init__(self):
        if abs(self.direct_connect_percent + self.internet_gateway_percent - 100.0) > 0.01:
            raise ValueError("Traffic split percentages must sum to 100%")


class ComputeResources(BaseModel):
    """Compute resource requirements"""
    vcpu: int = Field(ge=1, description="Total vCPU cores required")
    memory: int = Field(ge=1, description="Total memory in GB")
    instance_types: Optional[List[str]] = Field(default=None, description="Preferred EC2 instance types")


class StorageResources(BaseModel):
    """Storage resource requirements"""
    ebs_storage: int = Field(ge=0, description="EBS storage in GB")
    efs_storage: int = Field(ge=0, description="EFS storage in GB")
    s3_storage: int = Field(default=0, ge=0, description="S3 storage in GB")


class NetworkResources(BaseModel):
    """Network resource requirements"""
    peak_bandwidth: float = Field(ge=0, description="Peak bandwidth in Gbps")
    monthly_tonnage: float = Field(ge=0, description="Monthly data transfer in TB")
    traffic_split: TrafficSplit = Field(default_factory=TrafficSplit)


class TelcoDeployment(BaseModel):
    """Complete telco deployment specification"""
    user_plane: UserPlaneLocation
    compute: ComputeResources
    storage: StorageResources
    network: NetworkResources
    eks_clusters: int = Field(ge=1, description="Number of EKS clusters")
    sites: int = Field(ge=1, description="Number of deployment sites")
    region: str = Field(default="us-east-1", description="AWS region")


class CostBreakdown(BaseModel):
    """Detailed cost breakdown by service"""
    compute_cost: float = Field(ge=0)
    storage_cost: float = Field(ge=0)
    network_cost: float = Field(ge=0)
    eks_cost: float = Field(ge=0)
    data_transfer_cost: float = Field(ge=0)
    total_monthly_cost: float = Field(ge=0)


class CostAnalysis(BaseModel):
    """Complete cost analysis results"""
    deployment: TelcoDeployment
    monthly_costs: CostBreakdown
    annual_costs: CostBreakdown
    three_year_tco: float = Field(ge=0)
    cost_per_site: float = Field(ge=0)
    recommendations: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    exclusions: List[str] = Field(default_factory=list)


class OptimizationRecommendation(BaseModel):
    """Cost optimization recommendation"""
    category: str
    description: str
    potential_savings: float = Field(ge=0)
    implementation_effort: str = Field(description="Low, Medium, High")
    priority: str = Field(description="High, Medium, Low")