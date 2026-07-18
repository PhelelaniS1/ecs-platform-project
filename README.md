# ecs-platform-project

Containerised web app deployed on AWS ECS using Terraform and GitHub Actions



\# ECS Platform Project



A production-style platform engineering project demonstrating containerised application deployment on AWS using Terraform, Docker, and GitHub Actions.



\## Live Demo



> Deployed on AWS ECS Fargate behind an Application Load Balancer



\*\*URL:\*\* http://platform-project-alb-618869543.us-east-1.elb.amazonaws.com



\---



\## Architecture



\---



\## What This Project Demonstrates



\- \*\*Infrastructure as Code\*\* — All AWS infrastructure provisioned using Terraform with reusable, modular configuration

\- \*\*Containerisation\*\* — Application packaged as a Docker image using a minimal Python slim base

\- \*\*Container Orchestration\*\* — Docker image stored in ECR and deployed on ECS Fargate (serverless containers — no EC2 management)

\- \*\*Load Balancing\*\* — Application Load Balancer routing traffic across availability zones with health checks

\- \*\*CI/CD Pipeline\*\* — GitHub Actions automatically builds, pushes, and redeploys on every push to main

\- \*\*Networking\*\* — Custom VPC with public subnets, route tables, and internet gateway following AWS best practices

\- \*\*Observability\*\* — Container logs shipped to CloudWatch Logs with 7-day retention



\---



\## Tech Stack



| Layer | Technology |

|---|---|

| Cloud | AWS (ECS, ECR, ALB, VPC, CloudWatch) |

| Infrastructure as Code | Terraform |

| Containerisation | Docker |

| CI/CD | GitHub Actions |

| Application | Python, Flask, Gunicorn |

| Networking | VPC, Subnets, Internet Gateway, Route Tables |



\---



\## Project Structure



\---



\## How It Works



\### Infrastructure Deployment

```bash

cd terraform

terraform init

terraform plan

terraform apply

```



\### Application Deployment

Every push to `main` triggers the GitHub Actions pipeline which:

1\. Builds a new Docker image tagged with the git commit SHA

2\. Pushes the image to Amazon ECR

3\. Forces a new ECS deployment

4\. Waits for ECS to confirm the new task is running



\### Manual Image Push

```bash

\# Authenticate to ECR

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 640168441707.dkr.ecr.us-east-1.amazonaws.com



\# Build and push

docker build -t platform-project app/

docker tag platform-project:latest 640168441707.dkr.ecr.us-east-1.amazonaws.com/platform-project:latest

docker push 640168441707.dkr.ecr.us-east-1.amazonaws.com/platform-project:latest

```



\---



\## AWS Resources Created



| Resource | Name |

|---|---|

| VPC | platform-project-vpc |

| Subnets | platform-project-subnet-public-a/b |

| Internet Gateway | platform-project-igw |

| Security Groups | platform-project-alb-sg, platform-project-ecs-tasks-sg |

| ECR Repository | platform-project |

| ECS Cluster | platform-project-cluster |

| ECS Service | platform-project-service |

| Load Balancer | platform-project-alb |

| CloudWatch Log Group | /ecs/platform-project |

| IAM Role | platform-project-ecs-task-execution-role |



\---



\## Author



\*\*Phelelani Sithole\*\* — CloudOps Engineer | Platform Engineering | AWS | Terraform | Docker



\- GitHub: \[github.com/PhelelaniS1](https://github.com/PhelelaniS1)

\- LinkedIn: \[linkedin.com/in/phelelanisithole](https://linkedin.com/in/phelelanisithole)

