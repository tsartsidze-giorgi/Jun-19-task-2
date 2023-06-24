import argparse

parser = argparse.ArgumentParser(description="CLI script")
subparsers = parser.add_subparsers(title="Commands", dest="command")

bucket_parser = subparsers.add_parser("bucket", help="Upload file to a repository")
bucket_parser.add_argument("repository_name", help="Name of the repository")
bucket_parser.add_argument("-upload_file", help="Name of the file to upload")

vpc_parser = subparsers.add_parser("vpc", help="Create private subnet")
vpc_parser.add_argument("VpcId", help="VPC ID")
vpc_parser.add_argument("-create_private_subnet", help="CIDR block for private subnet")

ec2_parser = subparsers.add_parser("ec2", help="Add SSH access to security group")
ec2_parser.add_argument("-security_group_id", help="Security Group ID")
ec2_parser.add_argument("-ssh_my_ip", action="store_true", help="Add access from the machine's IP")

args = parser.parse_args()

if args.command == "bucket":
    if args.upload_file:
        print(f"Uploading file '{args.upload_file}' to repository '{args.repository_name}'")
    else:
        print("No file specified for upload.")

elif args.command == "vpc":
    if args.create_private_subnet:
        print(f"Creating private subnet with CIDR block '{args.create_private_subnet}' for VPC '{args.VpcId}'")
    else:
        print("No CIDR block specified for private subnet creation.")

elif args.command == "ec2":
    if args.security_group_id:
        print(f"Adding SSH access to security group '{args.security_group_id}'")
        if args.ssh_my_ip:
            print("Allowing access from the machine's IP address")
        else:
            print("No action specified for SSH access.")
    else:
        print("No security group specified.")

else:
    print("No command specified.")
