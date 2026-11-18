variable "container_name" {
  description = "Name of the Nginx container"
  type        = string
  default     = "terraform-nginx"
}

variable "external_port" {
  description = "Host port for Nginx"
  type        = number
  default     = 8082
}
