 # Directory and Files Information

This document provides comprehensive documentation for every directory and file in the **MCP Auth Bridge Server** project. It explains the purpose, responsibility, and contribution of each component to the overall system architecture.

---

## Root Level Files

### `.dockerignore`
**Purpose**: Specifies files and directories to exclude from Docker build context.
**Contains**: Patterns for `.git`, `__pycache__`, `.env`, `tests/`, `docs/`, build artifacts.
**Contribution**: Reduces Docker image size, prevents secrets leakage, speeds up builds.

### `.env.example`
**Purpose**: Template demonstrating required environment variables.
**Contains**: Key-value pairs with placeholder values (no real secrets).
**Contribution**: Onboarding guide for developers, reference for DevOps, prevents missing config errors.

### `.env.local`
**Purpose**: Local development environment variables (gitignored).
**Contains**: Actual API keys, database URLs, debug flags for developer machines.
**Contribution**: Enables local development without committing secrets. Never tracked in version control.

### `.gitignore`
**Purpose**: Defines files untracked by Git.
**Contains**: Python patterns (`__pycache__`, `*.pyc`), env files, build artifacts, IDE configs.
**Contribution**: Keeps repository clean, prevents accidental secret commits.

### `.pre-commit-config.yaml`
**Purpose**: Configuration for pre-commit hooks.
**Contains**: Hooks for code formatting (Black), linting (Ruff), type checking (mypy), security scanning (Bandit).
**Contribution**: Enforces code quality before commits reach CI/CD, catches issues early.

### `LICENSE`
**Purpose**: Legal license for the project.
**Contains**: MIT/Apache/Proprietary license text.
**Contribution**: Defines usage rights, protects intellectual property, enables open-source distribution if applicable.

### `Makefile`
**Purpose**: Standardized command interface for common operations.
**Contains**: Targets like `make install`, `make test`, `make build`, `make run`, `make lint`.
**Contribution**: Eliminates "works on my machine" issues, documents commands, simplifies CI/CD scripts.

### `pyproject.toml`
**Purpose**: Modern Python project configuration (PEP 621).
**Contains**: Project metadata, dependencies (Poetry/PDM), tool configs (Black, Ruff, mypy, pytest).
**Contribution**: Single source of truth for project config, reproducible builds, dependency locking.

### `README.md`
**Purpose**: Project overview and quick-start guide.
**Contains**: Description, installation steps, usage examples, architecture diagram, contribution guidelines.
**Contribution**: Primary onboarding document, GitHub landing page, reduces support burden.

### `requirements.txt`
**Purpose**: Frozen production dependencies.
**Contains**: Pinned package versions with hashes (`package==1.2.3 --hash=sha256:...`).
**Contribution**: Reproducible deployments, security audit trail, supply chain integrity.

---

## `.github/`

### `.github/workflows/ci.yml`
**Purpose**: Continuous Integration pipeline.
**Contains**: Steps for checkout, Python setup, dependency install, lint, type-check, unit tests, coverage report.
**Contribution**: Validates every PR, prevents broken code merges, maintains code quality standards.

### `.github/workflows/release.yml`
**Purpose**: Automated release pipeline.
**Contains**: Steps for version bump, build `.exe` via PyInstaller, sign artifacts, create GitHub release, upload assets.
**Contribution**: Eliminates manual release errors, ensures consistent artifacts, enables one-click deployments.

### `.github/workflows/security-scan.yml`
**Purpose**: Security analysis pipeline.
**Contains**: SAST (Bandit, Semgrep), dependency scanning (Safety, pip-audit), container scanning (Trivy).
**Contribution**: Detects vulnerabilities before production, compliance requirement for enterprise, automated security posture.

### `.github/PULL_REQUEST_TEMPLATE.md`
**Purpose**: Standardized PR description template.
**Contains**: Sections for description, changes, testing, checklist, screenshots.
**Contribution**: Improves PR quality, ensures reviewers have context, enforces process compliance.

### `.github/CODEOWNERS`
**Purpose**: Defines code review ownership.
**Contains**: File patterns mapped to GitHub usernames/teams (`src/security/ @security-team`).
**Contribution**: Ensures domain experts review changes, prevents unauthorized modifications, distributes review load.

---

## `.vscode/`

### `.vscode/settings.json`
**Purpose**: VS Code workspace settings.
**Contains**: Python interpreter path, formatter/linter settings, file associations.
**Contribution**: Consistent IDE behavior across team, reduces setup friction, enforces formatting rules.

### `.vscode/launch.json`
**Purpose**: Debug configuration.
**Contains**: Launch profiles for FastAPI server, pytest, and PyInstaller build.
**Contribution**: One-click debugging, breakpoints in async code, attach-to-process for running `.exe`.

### `.vscode/extensions.json`
**Purpose**: Recommended extensions.
**Contains**: List of VS Code extensions (Python, Black, Ruff, Thunder Client).
**Contribution**: Suggests tooling for new developers, ensures feature parity across team.

---

## `certs/`

### `certs/.gitkeep`
**Purpose**: Placeholder to track empty directory in Git.
**Contains**: Empty file.
**Contribution**: Ensures directory exists in fresh clones, prevents runtime errors when mounting TLS certs.

### `certs/README.md`
**Purpose**: Documentation for certificate management.
**Contains**: Instructions for generating self-signed certs, obtaining Let's Encrypt certs, rotation procedures.
**Contribution**: Security compliance guide, prevents certificate mismanagement, audit trail.

---

## `config/`

### `config/__init__.py`
**Purpose**: Makes `config` a Python package.
**Contains**: Package exports, version info.
**Contribution**: Enables `from config import settings` pattern, clean imports.

### `config/settings.py`
**Purpose**: Centralized configuration management.
**Contains**: Pydantic `BaseSettings` class with validation, env var parsing, defaults, secrets masking.
**Contribution**: Type-safe configuration, automatic validation, prevents runtime config errors, centralizes env var access.

### `config/environments/development.yaml`
**Purpose**: Development-specific overrides.
**Contains**: Debug flags, verbose logging, local service URLs, mock auth endpoints.
**Contribution**: Isolated dev config, prevents dev settings in production, enables local debugging.

### `config/environments/staging.yaml`
**Purpose**: Staging environment configuration.
**Contains**: Pre-production service URLs, test credentials, moderate logging.
**Contribution**: Mirrors production with test data, validates deployment before production, safe integration testing.

### `config/environments/production.yaml`
**Purpose**: Production environment configuration.
**Contains**: Production endpoints, strict logging levels, high security settings, monitoring endpoints.
**Contribution**: Hardened production defaults, performance optimization, security compliance.

### `config/logging.yaml`
**Purpose**: Structured logging configuration.
**Contains**: Loguru/stdlib formatters, handlers (console, file, syslog), log levels, rotation policies.
**Contribution**: Consistent log format across environments, JSON logging for parsing, audit compliance.

---

## `docs/`

### `docs/architecture/system-context.md`
**Purpose**: High-level system context diagram.
**Contains**: C4 model Level 1 (System Context), external system interactions, user personas.
**Contribution**: Onboarding documentation, stakeholder communication, scope definition.

### `docs/architecture/data-flow.md`
**Purpose**: Data flow documentation.
**Contains**: Sequence diagrams for auth flow, tool execution flow, error handling flow.
**Contribution**: Security review input, debugging reference, compliance documentation.

### `docs/architecture/deployment.md`
**Purpose**: Deployment architecture.
**Contains**: Infrastructure diagrams, Cloudflare Tunnel setup, scaling strategies, failover procedures.
**Contribution**: DevOps playbook, disaster recovery planning, capacity planning.

### `docs/api/openapi-spec.yaml`
**Purpose**: OpenAPI 3.1 specification.
**Contains**: API paths, schemas, security schemes, examples for all endpoints.
**Contribution**: Client SDK generation, API documentation, contract testing.

### `docs/runbooks/troubleshooting.md`
**Purpose**: Operational troubleshooting guide.
**Contains**: Common errors, diagnostic commands, log analysis, escalation procedures.
**Contribution**: Reduces MTTR (Mean Time To Repair), enables self-service support, 24/7 operations.

### `docs/runbooks/incident-response.md`
**Purpose**: Security incident response procedures.
**Contains**: Severity levels, response playbooks, communication templates, post-mortem process.
**Contribution**: Compliance requirement (SOC2), structured incident handling, lessons learned capture.

### `docs/README.md`
**Purpose**: Documentation index.
**Contains**: Navigation guide, document purpose summary, contribution guidelines for docs.
**Contribution**: Discoverability, documentation maintenance, knowledge base structure.

---

## `scripts/`

### `scripts/build-exe.sh`
**Purpose**: PyInstaller build automation.
**Contains**: Commands for cleaning build dirs, running PyInstaller with spec, signing executable, verifying output.
**Contribution**: Reproducible builds, CI/CD integration, eliminates manual build errors.

### `scripts/setup-tunnel.sh`
**Purpose**: Cloudflare Tunnel bootstrap.
**Contains**: cloudflared installation, tunnel creation, DNS record setup, systemd service registration.
**Contribution**: One-command tunnel setup, prevents configuration drift, infrastructure as code.

### `scripts/health-check.sh`
**Purpose**: External health probe script.
**Contains**: curl commands to `/health`, `/ready`, `/live` endpoints, timeout handling, exit codes.
**Contribution**: Load balancer health checks, Kubernetes liveness probes, monitoring integration.

### `scripts/migrate-secrets.sh`
**Purpose**: Secret rotation utility.
**Contains**: Commands for fetching new secrets from vault, updating `.env`, restarting services, rollback procedures.
**Contribution**: Security compliance, automated rotation, zero-downtime secret updates.

---

## `src/`

### `src/__init__.py`
**Purpose**: Makes `src` a Python package.
**Contains**: Version string, package metadata.
**Contribution**: Enables `from src.xxx import yyy`, clean namespace management.

### `src/main.py`
**Purpose**: Application entry point.
**Contains**: FastAPI app factory, lifespan events (startup/shutdown), uvicorn server configuration, signal handlers.
**Contribution**: Single entry for all execution modes, graceful startup/shutdown, process management.

---

## `src/api/`

### `src/api/__init__.py`
**Purpose**: Package initialization.
**Contains**: Router exports.
**Contribution**: Clean imports, namespace management.

### `src/api/dependencies.py`
**Purpose**: FastAPI dependency injection container.
**Contains**: Functions returning shared resources (DB connection, HTTP client, auth service), caching logic.
**Contribution**: Resource lifecycle management, test mocking, DRY principle for shared objects.

### `src/api/middleware/__init__.py`
**Purpose**: Middleware package init.
**Contains**: Middleware exports.
**Contribution**: Organized middleware registration.

### `src/api/middleware/cors.py`
**Purpose**: Cross-Origin Resource Sharing configuration.
**Contains**: Allowed origins, methods, headers, credentials settings.
**Contribution**: Browser security, enables Claude/ChatGPT web clients, prevents unauthorized cross-origin requests.

### `src/api/middleware/rate_limiter.py`
**Purpose**: Request throttling.
**Contains**: Token bucket algorithm, Redis-backed storage, per-IP and per-tool limits.
**Contribution**: DDoS protection, fair resource usage, prevents API quota exhaustion.

### `src/api/middleware/request_validator.py`
**Purpose**: Request validation and sanitization.
**Contains**: Origin header validation, content-type checks, payload size limits, header injection prevention.
**Contribution**: Security hardening, protocol compliance, prevents malformed request attacks.

### `src/api/middleware/security_headers.py`
**Purpose**: HTTP security headers.
**Contains**: HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy.
**Contribution**: OWASP compliance, prevents clickjacking, MIME sniffing, downgrade attacks.

### `src/api/routers/__init__.py`
**Purpose**: Router aggregation.
**Contains**: Router imports and registration list.
**Contribution**: Centralized routing, clean main.py, modular endpoint management.

### `src/api/routers/health.py`
**Purpose**: Health check endpoints.
**Contains**: `/health` (deep check with dependencies), `/ready` (accept traffic?), `/live` (process running?).
**Contribution**: Load balancer integration, Kubernetes probes, monitoring alerts, graceful degradation.

### `src/api/routers/mcp.py`
**Purpose**: MCP Streamable HTTP endpoint.
**Contains**: Route mounting `mcp.streamable_http_app()`, session management, protocol version negotiation.
**Contribution**: Core MCP protocol transport, Claude/ChatGPT integration point, stateless HTTP handling.

### `src/api/routers/metrics.py`
**Purpose**: Prometheus metrics endpoint.
**Contains**: `/metrics` route exposing counters, histograms, gauges for tool calls, latency, errors.
**Contribution**: Observability, alerting, performance monitoring, capacity planning.

### `src/api/exceptions.py`
**Purpose**: Global exception handling.
**Contains**: HTTP exception handlers for domain errors, validation errors, auth failures, MCP protocol errors.
**Contribution**: Consistent error responses, security (no stack traces in prod), client-friendly messages.

---

## `src/core/`

### `src/core/__init__.py`
**Purpose**: Package initialization.
**Contains**: Core exports.
**Contribution**: Clean imports.

### `src/core/constants.py`
**Purpose**: Application-wide constants.
**Contains**: Magic numbers, string literals, timeout values, retry counts, HTTP status code mappings.
**Contribution**: Prevents magic numbers, single source of truth, maintainability.

### `src/core/enums.py`
**Purpose**: Shared enumerations.
**Contains**: `ToolStatus`, `AuthMethod`, `Environment`, `LogLevel`, `RateLimitTier`.
**Contribution**: Type safety, IDE autocomplete, prevents string typos, database enum mapping.

### `src/core/exceptions.py`
**Purpose**: Base exception hierarchy.
**Contains**: `MCPAuthBridgeException`, `AuthError`, `ToolExecutionError`, `RateLimitExceeded`, `ValidationError`.
**Contribution**: Structured error handling, exception filtering in logs, client error mapping.

### `src/core/types.py`
**Purpose**: Type aliases and protocols.
**Contains**: `JSON = dict[str, Any]`, `ToolHandler = Callable[..., Awaitable[str]]`, `AuthToken` TypedDict.
**Contribution**: Code clarity, static analysis support, interface contracts.

---

## `src/domain/`

### `src/domain/__init__.py`
**Purpose**: Package initialization.
**Contains**: Domain exports.
**Contribution**: Clean imports.

### `src/domain/models/__init__.py`
**Purpose**: Model package init.
**Contains**: Model exports.
**Contribution**: Organized imports.

### `src/domain/models/tool_request.py`
**Purpose**: MCP tool input schemas.
**Contains**: Pydantic models for tool arguments, validation rules, examples, field descriptions.
**Contribution**: Input validation, OpenAPI documentation, type safety, prevents invalid tool calls.

### `src/domain/models/tool_response.py`
**Purpose**: MCP tool output schemas.
**Contains**: Pydantic models for tool results, error responses, metadata, pagination.
**Contribution**: Consistent output format, client contract, serialization control.

### `src/domain/models/auth_token.py`
**Purpose**: Internal authentication models.
**Contains**: Token structure, expiry handling, claims, refresh token model.
**Contribution**: Type-safe auth data, JWT handling, session management.

### `src/domain/services/__init__.py`
**Purpose**: Service package init.
**Contains**: Service exports.
**Contribution**: Clean imports.

### `src/domain/services/auth_service.py`
**Purpose**: Custom auth API integration.
**Contains**: Service account authentication, token refresh, credential validation, auth API client methods.
**Contribution**: Bridges public MCP to internal auth, handles token lifecycle, abstracts auth complexity.

### `src/domain/services/tool_registry.py`
**Purpose**: MCP tool discovery and routing.
**Contains**: Tool registration decorator, dynamic tool loading, metadata aggregation, capability negotiation.
**Contribution**: Extensibility (add tools without core changes), runtime tool discovery, MCP protocol compliance.

### `src/domain/services/rate_limit_service.py`
**Purpose**: Quota enforcement logic.
**Contains**: Per-tool and per-user limits, window calculations, Redis coordination, burst handling.
**Contribution**: Fair usage, cost control, prevents abuse, tiered access support.

### `src/domain/interfaces/__init__.py`
**Purpose**: Interface package init.
**Contains**: Protocol exports.
**Contribution**: Clean imports.

### `src/domain/interfaces/auth_provider.py`
**Purpose**: Abstract auth interface.
**Contains**: `AuthProvider` Protocol with `authenticate()`, `refresh()`, `validate()` methods.
**Contribution**: Dependency inversion, test mocking, enables multiple auth backends (OAuth, SAML, API key).

---

## `src/infrastructure/`

### `src/infrastructure/__init__.py`
**Purpose**: Package initialization.
**Contains**: Infrastructure exports.
**Contribution**: Clean imports.

### `src/infrastructure/cache/__init__.py`
**Purpose**: Cache package init.
**Contains**: Cache exports.
**Contribution**: Organized imports.

### `src/infrastructure/cache/redis_client.py`
**Purpose**: Redis connection management.
**Contains**: Connection pool, retry logic, serialization, key naming conventions.
**Contribution**: Shared cache for rate limits, sessions, tool results, horizontal scaling support.

### `src/infrastructure/cache/memory_cache.py`
**Purpose**: In-memory fallback cache.
**Contains**: LRU cache implementation, TTL handling, thread safety.
**Contribution**: Zero-dependency caching for single-instance deployments, Redis failover.

### `src/infrastructure/database/__init__.py`
**Purpose**: Database package init.
**Contains**: DB exports.
**Contribution**: Clean imports.

### `src/infrastructure/database/connection.py`
**Purpose**: Database connection management.
**Contains**: Connection pool, session factory, transaction handling, connection health checks.
**Contribution**: Resource efficiency, transaction safety, connection leak prevention.

### `src/infrastructure/database/migrations/`
**Purpose**: Schema evolution.
**Contains**: Alembic revision files, migration scripts, rollback procedures.
**Contribution**: Safe schema changes, version control for database, zero-downtime migrations.

### `src/infrastructure/http/__init__.py`
**Purpose**: HTTP package init.
**Contains**: HTTP exports.
**Contribution**: Clean imports.

### `src/infrastructure/http/client_factory.py`
**Purpose**: HTTP client lifecycle management.
**Contains**: `httpx.AsyncClient` factory with timeouts, connection pooling, SSL config, proxy support.
**Contribution**: Resource reuse, consistent client config, connection pooling, test mocking.

### `src/infrastructure/http/retry_policy.py`
**Purpose**: Resilient HTTP communication.
**Contains**: Exponential backoff, circuit breaker, jitter, retry condition predicates.
**Contribution**: Handles transient failures, prevents cascade failures, improves reliability.

### `src/infrastructure/monitoring/__init__.py`
**Purpose**: Monitoring package init.
**Contains**: Monitoring exports.
**Contribution**: Clean imports.

### `src/infrastructure/monitoring/metrics.py`
**Purpose**: Prometheus metrics collection.
**Contains**: Counter, Histogram, Gauge definitions for tool calls, auth latency, error rates.
**Contribution**: Observability, performance tracking, alerting triggers.

### `src/infrastructure/monitoring/tracing.py`
**Purpose**: Distributed tracing setup.
**Contains**: OpenTelemetry configuration, span creation, context propagation, exporter setup.
**Contribution**: Request tracing across services, performance bottleneck identification, debug complex flows.

### `src/infrastructure/monitoring/alerting.py`
**Purpose**: Alert notification system.
**Contains**: PagerDuty/Slack webhook integrations, alert severity routing, escalation policies.
**Contribution**: Proactive incident response, on-call integration, SLA monitoring.

---

## `src/mcp_server/`

### `src/mcp_server/__init__.py`
**Purpose**: Package initialization.
**Contains**: Server exports.
**Contribution**: Clean imports.

### `src/mcp_server/server.py`
**Purpose**: MCP server lifecycle management.
**Contains**: `FastMCP` instance creation, lifespan events, tool/prompt/resource registration, stateless mode config.
**Contribution**: Core MCP protocol implementation, server initialization, protocol compliance.

### `src/mcp_server/tools/__init__.py`
**Purpose**: Tools package init.
**Contains**: Tool exports.
**Contribution**: Clean imports.

### `src/mcp_server/tools/base_tool.py`
**Purpose**: Abstract base class for all MCP tools.
**Contains**: `BaseTool` class with `execute()`, `validate()`, `get_metadata()` methods, error handling template.
**Contribution**: Consistent tool interface, shared logic, enforce tool contracts.

### `src/mcp_server/tools/tool_loader.py`
**Purpose**: Dynamic tool discovery and registration.
**Contains**: Module scanning, decorator-based registration, lazy loading, hot-reload support.
**Contribution**: Extensibility, plugin architecture, zero-downtime tool updates.

### `src/mcp_server/tools/implementations/__init__.py`
**Purpose**: Implementation package init.
**Contains**: Concrete tool exports.
**Contribution**: Clean imports.

### `src/mcp_server/tools/implementations/data_query.py`
**Purpose**: Data query tool implementation.
**Contains**: SQL/natural language query tool, parameter validation, result formatting, auth integration.
**Contribution**: Exposes internal data via MCP, safe query execution, result streaming.

### `src/mcp_server/tools/implementations/document_search.py`
**Purpose**: Document search tool implementation.
**Contains**: Full-text search, vector search, filtering, ranking, result pagination.
**Contribution**: Knowledge base access, semantic search, document retrieval.

### `src/mcp_server/prompts/__init__.py`
**Purpose**: Prompts package init.
**Contains**: Prompt exports.
**Contribution**: Clean imports.

### `src/mcp_server/prompts/system_prompts.py`
**Purpose**: MCP prompt templates.
**Contains**: System prompt definitions, variable substitution, context injection, prompt versioning.
**Contribution**: Consistent AI behavior, prompt engineering, A/B testing support.

### `src/mcp_server/resources/__init__.py`
**Purpose**: Resources package init.
**Contains**: Resource exports.
**Contribution**: Clean imports.

### `src/mcp_server/resources/static_resources.py`
**Purpose**: Static resource definitions.
**Contains**: File resources, text resources, binary resources, MIME type handling.
**Contribution**: File access via MCP, documentation serving, asset management.

---

## `src/security/`

### `src/security/__init__.py`
**Purpose**: Package initialization.
**Contains**: Security exports.
**Contribution**: Clean imports.

### `src/security/crypto/__init__.py`
**Purpose**: Crypto package init.
**Contains**: Crypto exports.
**Contribution**: Clean imports.

### `src/security/crypto/key_manager.py`
**Purpose**: Encryption key lifecycle management.
**Contains**: KMS integration (AWS/Azure/GCP), key rotation, key versioning, secure key storage.
**Contribution**: Key security, compliance (FIPS 140-2), automated rotation.

### `src/security/crypto/token_encryptor.py`
**Purpose**: Symmetric encryption for sensitive tokens.
**Contains**: AES-256-GCM implementation, nonce management, authenticated encryption, decryption verification.
**Contribution**: Token confidentiality, tamper detection, secure storage.

### `src/security/audit/__init__.py`
**Purpose**: Audit package init.
**Contains**: Audit exports.
**Contribution**: Clean imports.

### `src/security/audit/logger.py`
**Purpose**: Immutable audit trail.
**Contains**: Structured audit events, append-only storage, tamper-evident hashing, retention policies.
**Contribution**: Compliance (SOC2, GDPR), forensic analysis, non-repudiation.

### `src/security/audit/compliance_reporter.py`
**Purpose**: Compliance report generation.
**Contains**: Report templates, data aggregation, scheduled generation, export formats (PDF, CSV).
**Contribution**: Audit readiness, automated compliance, regulator reporting.

### `src/security/validators/__init__.py`
**Purpose**: Validators package init.
**Contains**: Validator exports.
**Contribution**: Clean imports.

### `src/security/validators/input_sanitizer.py`
**Purpose**: Input cleaning and validation.
**Contains**: SQL injection prevention, XSS filtering, command injection detection, regex validation.
**Contribution**: Prevents injection attacks, data integrity, OWASP compliance.

### `src/security/validators/origin_checker.py`
**Purpose**: DNS rebinding and origin validation.
**Contains**: Whitelist validation, DNS resolution checks, Host header verification, referer validation.
**Contribution**: Prevents DNS rebinding attacks, ensures request legitimacy, protects internal services.

---

## `tests/`

### `tests/__init__.py`
**Purpose**: Test package init.
**Contains**: Test utilities.
**Contribution**: Shared test helpers.

### `tests/conftest.py`
**Purpose**: Pytest configuration and fixtures.
**Contains**: Fixtures for app client, DB, cache, auth mocks, test data, monkeypatch helpers.
**Contribution**: DRY test setup, consistent test environment, faster test writing.

### `tests/pytest.ini`
**Purpose**: Pytest configuration.
**Contains**: Test discovery paths, marker definitions, coverage settings, parallel execution config.
**Contribution**: Standardized test execution, coverage enforcement, test organization.

### `tests/unit/__init__.py`
**Purpose**: Unit test package init.
**Contains**: Unit test utilities.
**Contribution**: Organized unit tests.

### `tests/unit/api/`
**Purpose**: API layer unit tests.
**Contains**: Router tests, middleware tests, dependency tests with mocked services.
**Contribution**: Validates HTTP layer isolation, fast execution, no external dependencies.

### `tests/unit/domain/`
**Purpose**: Domain layer unit tests.
**Contains**: Service tests, model validation tests, business logic tests with mocked infrastructure.
**Contribution**: Validates business rules, pure function testing, fast feedback.

### `tests/unit/infrastructure/`
**Purpose**: Infrastructure layer unit tests.
**Contains**: Client tests with mocked responses, cache tests with mocked backends.
**Contribution**: Validates integration patterns, error handling, retry logic.

### `tests/unit/security/`
**Purpose**: Security layer unit tests.
**Contains**: Crypto tests, validator tests, audit log tests.
**Contribution**: Validates security controls, algorithm correctness, edge cases.

### `tests/integration/__init__.py`
**Purpose**: Integration test package init.
**Contains**: Integration test utilities.
**Contribution**: Organized integration tests.

### `tests/integration/test_auth_flow.py`
**Purpose**: End-to-end authentication flow testing.
**Contains**: Full auth cycle tests, token refresh, session management, error scenarios.
**Contribution**: Validates auth integration, real service interaction, security flow verification.

### `tests/integration/test_mcp_protocol.py`
**Purpose**: MCP protocol compliance testing.
**Contains**: Initialize, tool listing, tool call, error handling, stateless mode tests.
**Contribution**: Protocol compliance, client compatibility, regression prevention.

### `tests/integration/test_rate_limiting.py`
**Purpose**: Rate limiting integration tests.
**Contains**: Burst tests, window boundary tests, distributed limit tests.
**Contribution**: Validates throttling behavior, prevents abuse, ensures fair usage.

### `tests/e2e/__init__.py`
**Purpose**: E2E test package init.
**Contains**: E2E test utilities.
**Contribution**: Organized E2E tests.

### `tests/e2e/test_claude_integration.py`
**Purpose**: Claude Desktop integration testing.
**Contains**: Real Claude connection, tool discovery, tool execution, response validation.
**Contribution**: Validates real-world usage, client-specific behavior, production readiness.

### `tests/e2e/test_cloudflare_tunnel.py`
**Purpose**: Tunnel connectivity testing.
**Contains**: Tunnel establishment, public URL access, latency tests, failover tests.
**Contribution**: Validates deployment architecture, network reliability, external accessibility.

### `tests/fixtures/__init__.py`
**Purpose**: Test fixture package init.
**Contains**: Fixture utilities.
**Contribution**: Organized test data.

### `tests/fixtures/mock_responses/auth_api.json`
**Purpose**: Mock auth API responses.
**Contains**: Sample success/error responses from internal auth service.
**Contribution**: Consistent mocking, realistic test data, offline testing.

### `tests/fixtures/mock_responses/mcp_messages.json`
**Purpose**: Mock MCP protocol messages.
**Contains**: Sample initialize, tool call, notification messages.
**Contribution**: Protocol testing, client simulation, regression suites.

### `tests/fixtures/factories.py`
**Purpose**: Test data factories.
**Contains**: Factory functions/classes for generating valid test objects.
**Contribution**: DRY test data creation, randomized testing, maintainable test data.

### `tests/load/__init__.py`
**Purpose**: Load test package init.
**Contains**: Load test utilities.
**Contribution**: Organized load tests.

### `tests/load/locustfile.py`
**Purpose**: Locust load testing scenarios.
**Contains**: User behaviors, task weights, ramp-up configuration, success criteria.
**Contribution**: Performance benchmarking, capacity planning, bottleneck identification.

### `tests/load/k6-scripts/mcp-endpoint.js`
**Purpose**: k6 performance testing script.
**Contains**: HTTP request scenarios, threshold definitions, metrics collection.
**Contribution**: CI/CD performance gates, infrastructure scaling validation, SLA verification.

---

## `build/`

### `build/.gitkeep`
**Purpose**: Placeholder for build directory.
**Contains**: Empty file.
**Contribution**: Ensures directory exists, prevents build script errors.

### `build/mcp-auth-bridge.spec`
**Purpose**: PyInstaller specification file.
**Contains**: Build configuration, binary name, icon, hidden imports, data files, UPX compression.
**Contribution**: Reproducible executable builds, custom build logic, asset bundling.

### `build/hooks/`
**Purpose**: PyInstaller custom hooks.
**Contains**: Hook scripts for hidden imports, runtime library detection.
**Contribution**: Resolves import issues, includes runtime dependencies, ensures standalone executable.

---

## `deploy/`

### `deploy/docker/Dockerfile`
**Purpose**: Container image definition.
**Contains**: Multi-stage build, Python base, dependency install, .exe copy, health check, non-root user.
**Contribution**: Consistent runtime environment, scalable deployment, security hardening.

### `deploy/docker/docker-compose.yml`
**Purpose**: Local container orchestration.
**Contains**: App service, Redis service, volume mounts, network config, env file mapping.
**Contribution**: Local production-like environment, dependency management, easy startup.

### `deploy/docker/.dockerignore`
**Purpose**: Docker build context exclusions.
**Contains**: Git files, tests, docs, local env files, build artifacts.
**Contribution**: Smaller images, faster builds, secret prevention.

### `deploy/systemd/mcp-auth-bridge.service`
**Purpose**: Linux service definition.
**Contains**: Service unit file, auto-restart, logging, environment loading, resource limits.
**Contribution**: Production process management, auto-recovery, system integration.

### `deploy/cloudflare/config.yml`
**Purpose**: Cloudflare Tunnel configuration.
**Contains**: Tunnel UUID, ingress rules, origin settings, log level, metrics endpoint.
**Contribution**: Infrastructure as code, version-controlled tunnel config, reproducible deployments.

### `deploy/cloudflare/tunnel-credentials.json.enc`
**Purpose**: Encrypted tunnel credentials.
**Contains**: AES-encrypted Cloudflare tunnel token.
**Contribution**: Secure credential storage, prevents secret leakage, decryption at runtime.

### `deploy/kubernetes/namespace.yaml`
**Purpose**: K8s namespace definition.
**Contains**: Namespace metadata, resource quotas, network policies.
**Contribution**: Resource isolation, multi-tenancy, access control.

### `deploy/kubernetes/deployment.yaml`
**Purpose**: K8s deployment definition.
**Contains**: Replica count, container spec, resource limits, probe config, env vars.
**Contribution**: Scalable deployment, rolling updates, self-healing.

### `deploy/kubernetes/service.yaml`
**Purpose**: K8s service definition.
**Contains**: Service type, port mapping, selector labels.
**Contribution**: Internal networking, load balancing, service discovery.

### `deploy/kubernetes/ingress.yaml`
**Purpose**: K8s ingress definition.
**Contains**: Host rules, TLS config, path routing, annotations.
**Contribution**: External access, SSL termination, path-based routing.

---

## `tools/`

### `tools/lint.sh`
**Purpose**: Code quality verification.
**Contains**: Ruff lint, mypy type check, Bandit security scan, import sorting check.
**Contribution**: Pre-commit validation, CI/CD quality gate, consistent code style.

### `tools/format.sh`
**Purpose**: Code formatting.
**Contains**: Black formatter, isort import sorting, trailing whitespace removal.
**Contribution**: Consistent formatting, eliminates style debates, automated cleanup.

### `tools/pre-commit.sh`
**Purpose**: Git hook installer.
**Contains**: Symlink creation for `.git/hooks/pre-commit`, hook script copy.
**Contribution**: Enforces quality before commit, local CI simulation, prevents bad commits.

### `tools/generate-openapi.sh`
**Purpose**: OpenAPI spec export.
**Contains**: FastAPI app import, spec generation, file write, validation.
**Contribution**: API documentation sync, client SDK generation, contract testing input.

---

## Summary Table

| Directory | Primary Concern | Scalability Vector |
|-----------|----------------|-------------------|
| `src/api/` | HTTP transport | Add new routers/middleware |
| `src/domain/` | Business logic | Add new services/models |
| `src/infrastructure/` | External systems | Swap cache/database/monitoring |
| `src/mcp_server/` | Protocol implementation | Add new tools/prompts/resources |
| `src/security/` | Cross-cutting security | Add new validators/crypto |
| `tests/` | Quality assurance | Add new test categories |
| `deploy/` | Deployment targets | Add new platforms (AWS, Azure) |
| `docs/` | Knowledge management | Add new runbooks/architecture |