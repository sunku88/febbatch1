output "instance_ids" {
  description = "IDs of the created EC2 instances"
  value       = aws_instance.example[*].id
}

output "instance_public_ips" {
  description = "Public IP addresses of the created instances"
  value       = aws_instance.example[*].public_ip
}
