# 🚀 GenAI Telco TCO Builder

An Amazon Q CLI plugin for comprehensive Total Cost of Ownership (TCO) analysis of telco infrastructure deployments on AWS, with specialized support for 5G Core network architectures.

## 🎯 Overview

This plugin provides intelligent cost analysis for telco workloads with two primary deployment scenarios:
- **User Plane on AWS Region**: 80% traffic via Direct Connect, 20% via Internet Gateway
- **User Plane on AWS Outposts**: No user traffic charges, only control plane costs (~5%)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                Amazon Q CLI Framework                       │
├─────────────────────────────────────────────────────────────┤
│  GenAI Telco TCO Plugin  │  awslabscost_analysis_mcp_server │
│  ┌─────────────────────┐ │  ┌─────────────────────────────┐ │
│  │ Network Calculator  │ │  │ AWS Pricing APIs            │ │
│  │ Cost Optimizer      │─┼─►│ Cost Report Generator       │ │
│  │ Template Builder    │ │  │ Service Analysis            │ │
│  └─────────────────────┘ │  └─────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Installation
```bash
# Install as Amazon Q CLI plugin
q plugin install genai-telco-tco
```

### Basic Usage
```bash
# 5G Core on AWS Region
q telco build-tco \
  --vcpu 96 --memory 384 \
  --ebs-storage 1000 --efs-storage 500 \
  --eks-clusters 2 --sites 3 \
  --peak-bandwidth 10.0 --monthly-tonnage 1000 \
  --user-plane region

# 5G Core on AWS Outposts  
q telco build-tco \
  --vcpu 96 --memory 384 \
  --ebs-storage 1000 --efs-storage 500 \
  --eks-clusters 2 --sites 3 \
  --peak-bandwidth 10.0 --monthly-tonnage 1000 \
  --user-plane outposts
```

## 📊 Key Features

### Network Cost Intelligence
- **Region Deployment**: Automatic 80/20 split between DX and IGW costs
- **Outposts Deployment**: Zero user traffic charges, minimal control plane costs
- **Traffic Analysis**: Peak bandwidth vs tonnage optimization

### Compute Optimization
- **Instance Selection**: Intelligent EC2 instance type recommendations
- **EKS Scaling**: Multi-cluster, multi-site cost modeling
- **Storage Optimization**: EBS and EFS cost analysis with performance considerations

### Cost Analysis
- **Multi-Site TCO**: Comprehensive 3-year cost projections
- **Service Breakdown**: Detailed per-service cost analysis
- **Optimization Recommendations**: AI-powered cost reduction suggestions

## 📁 Project Structure

```
genai-telco-tco/
├── src/                    # Core plugin source code
├── tests/                  # Unit and integration tests
├── docs/                   # Documentation and guides
├── examples/               # Usage examples and templates
├── templates/              # Cost analysis templates
├── scripts/                # Utility scripts
└── README.md              # This file
```

## 🔧 Development

### Prerequisites
- Amazon Q CLI installed
- Python 3.8+
- Access to awslabscost_analysis_mcp_server

### Local Development
```bash
git clone <repository-url>
cd genai-telco-tco
pip install -r requirements.txt
python -m pytest tests/
```

## 📖 Documentation

- [User Guide](docs/user-guide.md)
- [API Reference](docs/api-reference.md)
- [Architecture Guide](docs/architecture.md)
- [Examples](examples/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- [Issues](../../issues)
- [Discussions](../../discussions)
- [AWS Documentation](https://docs.aws.amazon.com/)

---

**Built with ❤️ for the Telco community by AWS Labs**