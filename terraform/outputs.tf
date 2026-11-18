output "container_name" {
  value = docker_container.web.name
}

output "application_url" {
  value = "http://localhost:8082"
}

output "container_id" {
  value = docker_container.web.id
}
