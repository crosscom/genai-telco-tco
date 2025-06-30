# GenAI Telco TCO Examples

This directory contains example configurations for common telco deployment scenarios.

## Example Configurations

### 5G Core Network Deployments

- **`5g-core-region.yaml`** - 5G Core deployed in AWS Region
  - 96 vCPU, 384GB RAM across 3 sites
  - 80% Direct Connect, 20% Internet Gateway traffic
  - 1TB monthly data transfer

- **`5g-core-outposts.yaml`** - 5G Core deployed on AWS Outposts
  - Same compute/storage as region deployment
  - Zero user plane data transfer charges
  - Local processing for ultra-low latency

## Usage Examples

### CLI Usage

```bash
# Analyze region deployment
q telco build-tco \
  --vcpu 96 --memory 384 \
  --ebs-storage 1000 --efs-storage 500 \
  --eks-clusters 2 --sites 3 \
  --peak-bandwidth 10.0 --monthly-tonnage 1000 \
  --user-plane region

# Analyze outposts deployment
q telco build-tco \
  --vcpu 96 --memory 384 \
  --ebs-storage 1000 --efs-storage 500 \
  --eks-clusters 2 --sites 3 \
  --peak-bandwidth 10.0 --monthly-tonnage 1000 \
  --user-plane outposts

# Compare both deployments
q telco compare-deployments \
  --vcpu 96 --memory 384 \
  --monthly-tonnage 1000
```

### Configuration File Usage

```bash
# Analyze from configuration file
q telco analyze-config 5g-core-region.yaml --format markdown

# Generate detailed report
q telco analyze-config 5g-core-outposts.yaml \
  --output outposts-tco-report.md \
  --format markdown
```

## Expected Results

### Region Deployment
- **Monthly Cost**: ~$15,000-20,000
- **Primary Costs**: Compute (60%), Data Transfer (25%), Storage (15%)
- **3-Year TCO**: ~$540,000-720,000

### Outposts Deployment  
- **Monthly Cost**: ~$12,000-16,000
- **Primary Costs**: Compute (75%), Storage (20%), Network (5%)
- **3-Year TCO**: ~$432,000-576,000
- **Savings**: 20-25% vs Region deployment

## Customization

Modify the YAML files to match your specific requirements:

- Adjust compute resources based on workload
- Update storage requirements for your data needs
- Modify network parameters for your traffic patterns
- Change the number of sites and clusters as needed