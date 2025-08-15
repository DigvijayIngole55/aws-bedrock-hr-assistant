# AWS Bedrock HR Assistant

A comprehensive HR assistant built with AWS Bedrock Agents, Lambda functions, and SQLite database. This project demonstrates how to create an intelligent agent that can help employees manage vacation time and HR policies.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   User Query    ├───►│ Bedrock Agent   ├───►│ Lambda Function │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────┬───────────┘
                                                    │
                                                    ▼
                                            ┌─────────────────┐
                                            │                 │
                                            │ SQLite Database │
                                            │                 │
                                            └─────────────────┘
```

## 🚀 Features

- **Employee Vacation Management**: Check available vacation days
- **Vacation Booking**: Reserve vacation time with date validation
- **Database Integration**: SQLite database with employee and vacation data
- **Natural Language Interface**: Interact using natural language queries
- **AWS Integration**: Built on AWS Bedrock, Lambda, and IAM

## 📁 Project Structure

```
aws-bedrock-hr-assistant/
├── scripts/                          # Jupyter notebooks for setup and testing
│   ├── create_employee_DB.ipynb      # Create and populate SQLite database
│   ├── create_deploy_lambda_functions.ipynb  # Deploy Lambda functions
│   ├── configure_agent.ipynb         # Configure Bedrock Agent
│   ├── create_deploy_agent.ipynb     # Create and deploy the agent
│   ├── invoke_agent_api.ipynb        # Test agent functionality
│   └── delete_agent.ipynb            # Cleanup resources
├── lambda-functions/                  # Lambda function source code
│   ├── lambda_function.py            # Main Lambda handler
│   ├── get_available_vacations_days.py  # Get vacation days function
│   ├── reserve_vacation_time.py      # Reserve vacation function
│   └── employee_database.db          # Sample database
├── docs/                             # Documentation
├── config/                           # Configuration files
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🛠️ Setup Instructions

### Prerequisites

- AWS Account with appropriate permissions
- Python 3.8+ with Jupyter Notebook
- AWS CLI configured
- Boto3 SDK installed

### Required AWS Permissions

Your AWS credentials need the following permissions:
- `bedrock:*` (for Bedrock Agent operations)
- `lambda:*` (for Lambda function management)
- `iam:*` (for role and policy management)
- `logs:*` (for CloudWatch logs access)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure AWS Credentials

```bash
aws configure
# Enter your AWS Access Key ID, Secret Access Key, and region
```

### Step 3: Run Setup Scripts (in order)

1. **Create Database**:
   ```bash
   jupyter notebook scripts/create_employee_DB.ipynb
   ```
   - Creates SQLite database with sample employee data
   - Generates 10 employees with vacation records

2. **Deploy Lambda Functions**:
   ```bash
   jupyter notebook scripts/create_deploy_lambda_functions.ipynb
   ```
   - Creates IAM roles and policies
   - Packages and deploys Lambda function
   - Sets up proper permissions

3. **Configure Agent**:
   ```bash
   jupyter notebook scripts/configure_agent.ipynb
   ```
   - Defines agent functions and schemas
   - Sets up action groups

4. **Create and Deploy Agent**:
   ```bash
   jupyter notebook scripts/create_deploy_agent.ipynb
   ```
   - Creates Bedrock Agent
   - Links Lambda functions
   - Creates agent alias

5. **Test the Agent**:
   ```bash
   jupyter notebook scripts/invoke_agent_api.ipynb
   ```
   - Test agent with sample queries
   - Verify functionality

## 📝 Usage Examples

### Check Available Vacation Days

```
Human: "How much vacation does the employee with employee_id set to 1 have available?"
Agent: "The employee with employee_id 1 has 10 vacation days available."
```

### Reserve Vacation Time

```
Human: "Reserve vacation time for employee 2 from 2025-09-01 to 2025-09-05"
Agent: "Vacation reserved successfully from 2025-09-01 to 2025-09-05 (5 days)"
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file (optional):
```
AWS_REGION=us-east-1
AWS_PROFILE=default
```

### Customization

- **Database Schema**: Modify `create_employee_DB.ipynb` to change database structure
- **Agent Instructions**: Update agent description in `create_deploy_agent.ipynb`
- **Lambda Functions**: Add new functions in `lambda-functions/` folder
- **Function Schema**: Update function definitions in `configure_agent.ipynb`

## 🧪 Testing

The project includes comprehensive testing through the Jupyter notebooks:

1. **Database Testing**: Verify database creation and data integrity
2. **Lambda Testing**: Test individual Lambda functions
3. **Agent Testing**: End-to-end agent functionality tests
4. **Error Handling**: Test error scenarios and edge cases


## 🧹 Cleanup

To avoid AWS charges, run the cleanup script:

```bash
jupyter notebook scripts/delete_agent.ipynb
```

This will delete:
- Bedrock Agent and aliases
- Lambda functions
- IAM roles and policies
- CloudWatch log groups

## 💰 Cost Considerations

This project uses several AWS services that may incur costs:

- **Bedrock Agent**: Pay per request
- **Lambda Functions**: Pay per invocation and compute time
- **CloudWatch Logs**: Storage and data transfer costs
- **IAM**: No additional costs

Estimated cost for testing: < $5/month for light usage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review AWS CloudWatch logs for detailed error messages
3. Verify your AWS permissions and configuration
4. Open an issue in this repository with detailed error information

---

**Built with ❤️ using AWS Bedrock, Lambda, and Python**

*This project demonstrates practical implementation of AWS Bedrock Agents for enterprise HR use cases.*
