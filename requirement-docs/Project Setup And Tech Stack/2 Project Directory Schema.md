 # Project Directory Schema

## Overview

This document defines the standardized directory structure for the **MCP Auth Bridge Server** — a production-grade, enterprise-ready application. The schema follows modular architecture principles, ensuring scalability, maintainability, and clear separation of concerns.

---

## Directory Tree

```
mcp-auth-bridge/
│
├── 📁 .github/                          # CI/CD & GitHub automation
│   ├── workflows/
│   │   ├── ci.yml                       # Lint, test, build on PR
│   │   ├── release.yml                  # Build & publish .exe artifacts
│   │   └── security-scan.yml            # SAST/DAST pipeline
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
│
├── 📁 .vscode/                          # Editor configuration
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
│
├── 📁 certs/                            # TLS certificates (gitignored)
│   ├── .gitkeep
│   └── README.md
│
├── 📁 config/                           # Configuration layer
│   ├── __init__.py
│   ├── settings.py                      # Pydantic Settings (env vars)
│   ├── environments/
│   │   ├── development.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   └── logging.yaml                     # Loguru / stdlib logging config
│
├── 📁 docs/                             # Project documentation
│   ├── architecture/
│   │   ├── system-context.md
│   │   ├── data-flow.md
│   │   └── deployment.md
│   ├── api/
│   │   └── openapi-spec.yaml
│   ├── runbooks/
│   │   ├── troubleshooting.md
│   │   └── incident-response.md
│   └── README.md
│
├── 📁 scripts/                          # Automation & utility scripts
│   ├── build-exe.sh                     # PyInstaller build script
│   ├── setup-tunnel.sh                  # Cloudflare tunnel bootstrap
│   ├── health-check.sh                  # Liveness probe script
│   └── migrate-secrets.sh               # Secret rotation utility
│
├── 📁 src/                              # Application source code
│   ├── __init__.py
│   │
│   ├── 📁 api/                          # HTTP layer (FastAPI)
│   │   ├── __init__.py
│   │   ├── dependencies.py              # FastAPI Depends() injectors
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── cors.py                  # CORS configuration
│   │   │   ├── rate_limiter.py          # Throttling middleware
│   │   │   ├── request_validator.py     # Origin/header validation
│   │   │   └── security_headers.py      # HSTS, CSP, etc.
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── health.py                # /health, /ready, /live
│   │   │   ├── mcp.py                   # MCP Streamable HTTP endpoint
│   │   │   └── metrics.py               # Prometheus /metrics
│   │   └── exceptions.py                # HTTP exception handlers
│   │
│   ├── 📁 core/                         # Domain-agnostic core
│   │   ├── __init__.py
│   │   ├── constants.py                 # App-wide constants
│   │   ├── enums.py                     # Shared enumerations
│   │   ├── exceptions.py                # Base exception classes
│   │   └── types.py                     # Type aliases & protocols
│   │
│   ├── 📁 domain/                       # Business logic layer
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── tool_request.py          # MCP tool input schemas
│   │   │   ├── tool_response.py         # MCP tool output schemas
│   │   │   └── auth_token.py            # Internal auth models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py          # Custom auth API client
│   │   │   ├── tool_registry.py         # MCP tool discovery & routing
│   │   │   └── rate_limit_service.py    # Quota enforcement
│   │   └── interfaces/
│   │       ├── __init__.py
│   │       └── auth_provider.py         # Abstract auth interface
│   │
│   ├── 📁 infrastructure/               # External integrations
│   │   ├── __init__.py
│   │   ├── cache/
│   │   │   ├── __init__.py
│   │   │   ├── redis_client.py          # Redis connection pool
│   │   │   └── memory_cache.py          # In-memory fallback
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   └── migrations/              # Alembic / manual migrations
│   │   ├── http/
│   │   │   ├── __init__.py
│   │   │   ├── client_factory.py        # httpx.AsyncClient factory
│   │   │   └── retry_policy.py          # Exponential backoff config
│   │   └── monitoring/
│   │       ├── __init__.py
│   │       ├── metrics.py               # Prometheus metrics
│   │       ├── tracing.py               # OpenTelemetry setup
│   │       └── alerting.py              # PagerDuty/Slack webhooks
│   │
│   ├── 📁 mcp_server/                   # MCP protocol implementation
│   │   ├── __init__.py
│   │   ├── server.py                    # FastMCP instance & lifecycle
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── base_tool.py             # Abstract tool class
│   │   │   ├── tool_loader.py           # Dynamic tool registration
│   │   │   └── implementations/         # Concrete tool modules
│   │   │       ├── __init__.py
│   │   │       ├── data_query.py
│   │   │       └── document_search.py
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   └── system_prompts.py
│   │   └── resources/
│   │       ├── __init__.py
│   │       └── static_resources.py
│   │
│   ├── 📁 security/                     # Security & compliance
│   │   ├── __init__.py
│   │   ├── crypto/
│   │   │   ├── __init__.py
│   │   │   ├── key_manager.py           # KMS integration
│   │   │   └── token_encryptor.py       # AES-256-GCM wrapper
│   │   ├── audit/
│   │   │   ├── __init__.py
│   │   │   ├── logger.py                # Immutable audit trail
│   │   │   └── compliance_reporter.py   # SOC2/GDPR reports
│   │   └── validators/
│   │       ├── __init__.py
│   │       ├── input_sanitizer.py       # SQLi/XSS prevention
│   │       └── origin_checker.py        # DNS rebinding protection
│   │
│   └── main.py                          # Application entry point
│
├── 📁 tests/                            # Test suite
│   ├── __init__.py
│   ├── conftest.py                      # Pytest fixtures & hooks
│   ├── pytest.ini
│   │
│   ├── 📁 unit/                         # Unit tests (no I/O)
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   └── security/
│   │
│   ├── 📁 integration/                  # Integration tests (with I/O)
│   │   ├── __init__.py
│   │   ├── test_auth_flow.py
│   │   ├── test_mcp_protocol.py
│   │   └── test_rate_limiting.py
│   │
│   ├── 📁 e2e/                          # End-to-end tests
│   │   ├── __init__.py
│   │   ├── test_claude_integration.py
│   │   └── test_cloudflare_tunnel.py
│   │
│   ├── 📁 fixtures/                     # Test data & mocks
│   │   ├── __init__.py
│   │   ├── mock_responses/
│   │   │   ├── auth_api.json
│   │   │   └── mcp_messages.json
│   │   └── factories.py                 # Factory Boy / dataclasses
│   │
│   └── 📁 load/                         # Performance tests
│       ├── __init__.py
│       ├── locustfile.py                # Locust scenarios
│       └── k6-scripts/
│           └── mcp-endpoint.js
│
├── 📁 build/                            # Build artifacts
│   ├── .gitkeep
│   ├── mcp-auth-bridge.spec             # PyInstaller spec
│   └── hooks/                           # PyInstaller custom hooks
│
├── 📁 deploy/                           # Deployment configurations
│   ├── docker/
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   └── .dockerignore
│   ├── systemd/
│   │   └── mcp-auth-bridge.service
│   ├── cloudflare/
│   │   ├── config.yml                   # cloudflared config
│   │   └── tunnel-credentials.json.enc  # Encrypted credentials
│   └── kubernetes/
│       ├── namespace.yaml
│       ├── deployment.yaml
│       ├── service.yaml
│       └── ingress.yaml
│
├── 📁 tools/                            # Development tools
│   ├── lint.sh                          # Ruff, mypy, bandit
│   ├── format.sh                        # Black + isort
│   ├── pre-commit.sh                    # Git hook installer
│   └── generate-openapi.sh              # Export OpenAPI spec
│
├── .dockerignore
├── .env.example                         # Template for env vars
├── .env.local                           # Local dev secrets (gitignored)
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile                             # Standardized commands
├── pyproject.toml                       # Poetry / PEP 621 config
├── README.md
└── requirements.txt                     # Frozen dependencies
```

---

## Schema Rationale

### Layered Architecture
| Layer | Responsibility | Key Modules |
|-------|---------------|-------------|
| **API** | HTTP transport, routing, middleware | `src/api/` |
| **Domain** | Business logic, models, services | `src/domain/` |
| **Infrastructure** | External systems, persistence | `src/infrastructure/` |
| **MCP Server** | Protocol implementation | `src/mcp_server/` |
| **Security** | Cross-cutting security concerns | `src/security/` |

### Scalability Vectors
- **Horizontal**: Stateless design allows multiple `.exe` instances behind a load balancer
- **Vertical**: Modular tool registration supports adding new MCP tools without touching core
- **Protocol**: Streamable HTTP supports both stateful and stateless modes for future migration

### Enterprise Readiness
- **Observability**: Structured logging, metrics, distributed tracing in `infrastructure/monitoring/`
- **Compliance**: Immutable audit logs, encryption at rest, input sanitization in `security/`
- **Operations**: Health checks, graceful shutdown, circuit breakers in `api/middleware/`
- **CI/CD**: Automated security scanning, artifact signing in `.github/workflows/`

---

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Directories | `snake_case` | `rate_limiter.py` |
| Python modules | `snake_case` | `tool_registry.py` |
| Classes | `PascalCase` | `AuthService` |
| Functions | `snake_case` | `validate_origin()` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT` |
| Private members | `_leading_underscore` | `_internal_token` |

---

## Future Expansion Points

1. **Multi-tenant support**: Add `src/tenant/` layer for isolated customer contexts
2. **Plugin system**: Extend `src/mcp_server/tools/implementations/` with dynamic loading
3. **GraphQL gateway**: Add `src/api/routers/graphql.py` for alternative transport
4. **WebSocket support**: Extend `src/mcp_server/server.py` with WS transport option
5. **Admin dashboard**: Add `src/admin/` with FastAPI admin views