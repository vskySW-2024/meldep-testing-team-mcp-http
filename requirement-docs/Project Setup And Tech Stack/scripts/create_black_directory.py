
import os

# Define the project structure as a nested dictionary
project_structure = {
    ".github": {
        "workflows": {
            "ci.yml": None,
            "release.yml": None,
            "security-scan.yml": None,
        },
        "PULL_REQUEST_TEMPLATE.md": None,
        "CODEOWNERS": None,
    },
    ".vscode": {
        "settings.json": None,
        "launch.json": None,
        "extensions.json": None,
    },
    "certs": {
        ".gitkeep": None,
        "README.md": None,
    },
    "config": {
        "__init__.py": None,
        "settings.py": None,
        "environments": {
            "development.yaml": None,
            "staging.yaml": None,
            "production.yaml": None,
        },
        "logging.yaml": None,
    },
    "docs": {
        "architecture": {
            "system-context.md": None,
            "data-flow.md": None,
            "deployment.md": None,
        },
        "api": {
            "openapi-spec.yaml": None,
        },
        "runbooks": {
            "troubleshooting.md": None,
            "incident-response.md": None,
        },
        "README.md": None,
    },
    "scripts": {
        "build-exe.sh": None,
        "setup-tunnel.sh": None,
        "health-check.sh": None,
        "migrate-secrets.sh": None,
    },
    "src": {
        "__init__.py": None,
        "main.py": None,
        "api": {
            "__init__.py": None,
            "dependencies.py": None,
            "middleware": {
                "__init__.py": None,
                "cors.py": None,
                "rate_limiter.py": None,
                "request_validator.py": None,
                "security_headers.py": None,
            },
            "routers": {
                "__init__.py": None,
                "health.py": None,
                "mcp.py": None,
                "metrics.py": None,
            },
            "exceptions.py": None,
        },
        "core": {
            "__init__.py": None,
            "constants.py": None,
            "enums.py": None,
            "exceptions.py": None,
            "types.py": None,
        },
        "domain": {
            "__init__.py": None,
            "models": {
                "__init__.py": None,
                "tool_request.py": None,
                "tool_response.py": None,
                "auth_token.py": None,
            },
            "services": {
                "__init__.py": None,
                "auth_service.py": None,
                "tool_registry.py": None,
                "rate_limit_service.py": None,
            },
            "interfaces": {
                "__init__.py": None,
                "auth_provider.py": None,
            },
        },
        "infrastructure": {
            "__init__.py": None,
            "cache": {
                "__init__.py": None,
                "redis_client.py": None,
                "memory_cache.py": None,
            },
            "database": {
                "__init__.py": None,
                "connection.py": None,
                "migrations": {},
            },
            "http": {
                "__init__.py": None,
                "client_factory.py": None,
                "retry_policy.py": None,
            },
            "monitoring": {
                "__init__.py": None,
                "metrics.py": None,
                "tracing.py": None,
                "alerting.py": None,
            },
        },
        "mcp_server": {
            "__init__.py": None,
            "server.py": None,
            "tools": {
                "__init__.py": None,
                "base_tool.py": None,
                "tool_loader.py": None,
                "implementations": {
                    "__init__.py": None,
                    "data_query.py": None,
                    "document_search.py": None,
                },
            },
            "prompts": {
                "__init__.py": None,
                "system_prompts.py": None,
            },
            "resources": {
                "__init__.py": None,
                "static_resources.py": None,
            },
        },
        "security": {
            "__init__.py": None,
            "crypto": {
                "__init__.py": None,
                "key_manager.py": None,
                "token_encryptor.py": None,
            },
            "audit": {
                "__init__.py": None,
                "logger.py": None,
                "compliance_reporter.py": None,
            },
            "validators": {
                "__init__.py": None,
                "input_sanitizer.py": None,
                "origin_checker.py": None,
            },
        },
    },
    "tests": {
        "__init__.py": None,
        "conftest.py": None,
        "pytest.ini": None,
        "unit": {
            "__init__.py": None,
            "api": {},
            "domain": {},
            "infrastructure": {},
            "security": {},
        },
        "integration": {
            "__init__.py": None,
            "test_auth_flow.py": None,
            "test_mcp_protocol.py": None,
            "test_rate_limiting.py": None,
        },
        "e2e": {
            "__init__.py": None,
            "test_claude_integration.py": None,
            "test_cloudflare_tunnel.py": None,
        },
        "fixtures": {
            "__init__.py": None,
            "mock_responses": {
                "auth_api.json": None,
                "mcp_messages.json": None,
            },
            "factories.py": None,
        },
        "load": {
            "__init__.py": None,
            "locustfile.py": None,
            "k6-scripts": {
                "mcp-endpoint.js": None,
            },
        },
    },
    "build": {
        ".gitkeep": None,
        "mcp-auth-bridge.spec": None,
        "hooks": {},
    },
    "deploy": {
        "docker": {
            "Dockerfile": None,
            "docker-compose.yml": None,
            ".dockerignore": None,
        },
        "systemd": {
            "mcp-auth-bridge.service": None,
        },
        "cloudflare": {
            "config.yml": None,
            "tunnel-credentials.json.enc": None,
        },
        "kubernetes": {
            "namespace.yaml": None,
            "deployment.yaml": None,
            "service.yaml": None,
            "ingress.yaml": None,
        },
    },
    "tools": {
        "lint.sh": None,
        "format.sh": None,
        "pre-commit.sh": None,
        "generate-openapi.sh": None,
    },
    ".dockerignore": None,
    ".env.example": None,
    ".env.local": None,
    ".gitignore": None,
    ".pre-commit-config.yaml": None,
    "LICENSE": None,
    "Makefile": None,
    "pyproject.toml": None,
    "README.md": None,
    "requirements.txt": None,
}


def create_structure(base_path, structure, current_depth=0):
    """Recursively create directories and files."""
    items_created = []
    
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        if content is None:
            # It's a file
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                open(path, 'a').close()
                items_created.append(f"{'  ' * current_depth}📄 {name}")
            else:
                items_created.append(f"{'  ' * current_depth}⏭️  {name} (exists)")
        else:
            # It's a directory
            os.makedirs(path, exist_ok=True)
            items_created.append(f"{'  ' * current_depth}📁 {name}/")
            
            # Recursively create contents
            if isinstance(content, dict):
                items_created.extend(create_structure(path, content, current_depth + 1))
    
    return items_created

# Set the base directory (current working directory)
base_dir = os.getcwd()
project_path = base_dir

print(f"🚀 Creating project structure at: {project_path}")
print("=" * 60)

# Create the structure
result = create_structure(base_dir, project_structure)

# Print results
for line in result:
    print(line)

print("=" * 60)
print(f"✅ Project structure created successfully!")
print(f"📂 Location: {project_path}")

# Count items
def count_items(structure):
    files = 0
    dirs = 0
    for name, content in structure.items():
        if content is None:
            files += 1
        else:
            dirs += 1
            if isinstance(content, dict):
                f, d = count_items(content)
                files += f
                dirs += d
    return files, dirs

files, dirs = count_items(project_structure)
print(f"📊 Statistics:")
print(f"   • Directories: {dirs}")
print(f"   • Files: {files}")
print(f"   • Total items: {dirs + files}")
