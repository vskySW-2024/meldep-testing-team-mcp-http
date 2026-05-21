  
 Here is your comprehensive **Tech Stack Decision Document** for the MCP Server HTTP Transport project.

---

# Tech Stack Documentation: MCP Server with HTTP Transport

## 1. Executive Summary

**Goal**: Build an MCP server that proxies authenticated tools from an existing application, making them available to Claude, ChatGPT, and other AI platforms that expect unauthenticated MCP endpoints.

**Core Strategy**: 
- Build a **Python (FastAPI)** MCP server using the official SDK
- Package it as a **standalone Windows executable (.exe)**
- Expose via **Cloudflare Tunnel** for public access
- Implement **custom auth bridging** between the public MCP endpoint and your internal API

---

## 2. Protocol Decision: Streamable HTTP (Not SSE)

**Critical Decision**: Use **Streamable HTTP** transport, not the legacy HTTP+SSE.

| Aspect | HTTP+SSE (Legacy) | Streamable HTTP (Recommended) |
|--------|-------------------|------------------------------|
| **Status** | Deprecated since MCP spec 2026-03-26 | Current standard since 2026-03-26 |
| **Endpoints** | Two separate endpoints (`/sse` + POST endpoint) | Single endpoint (`/mcp`) |
| **State** | Stateful, requires persistent connections | Supports both stateful and stateless |
| **Scalability** | Limited (long-lived connections) | High (stateless-friendly) |
| **Auth** | Complex with SSE headers | Standard HTTP headers |
| **Client Support** | Legacy only | All modern clients (Claude, ChatGPT, etc.) |

**Why Streamable HTTP for your use case**:
- **Single endpoint** simplifies Cloudflare Tunnel configuration
- **Stateless mode** (`stateless_http=True`) is perfect for your architecture—you don't need session persistence between the AI platform and your bridge
- **Standard HTTP POST/GET** means Cloudflare handles it like any web traffic
- **Better security**: No long-lived connections to manage through the tunnel 

---

## 3. Language & Framework Decision: Python (FastAPI)

### Recommended Stack: **Python + FastAPI + Official MCP SDK**

```python
# Core dependencies
mcp[cli]          # Official MCP Python SDK (1.8.0+)
fastapi           # ASGI framework
uvicorn           # ASGI server
httpx             # Async HTTP client for calling your auth API
pyinstaller       # For .exe packaging
python-dotenv     # Configuration management
```

### Why Python/FastAPI over Node.js:

| Criteria | Python/FastAPI | Node.js |
|----------|---------------|---------|
| **Your Team Skill** | ✅ Primary expertise | Secondary |
| **MCP SDK Maturity** | ✅ Official SDK, actively maintained | Community SDKs |
| **Streamable HTTP Support** | ✅ Native in SDK 1.8.0+ | Available but less documented |
| **FastAPI Integration** | ✅ `mcp.streamable_http_app()` mounts directly | Requires custom HTTP handling |
| **Async/Await** | ✅ Native | ✅ Native |
| **EXE Packaging** | ✅ PyInstaller (mature) | pkg/nexe (more complex) |
| **Cloudflare Tunnel** | ✅ Works identically | ✅ Works identically |

**Key SDK Feature**: The official Python SDK provides `FastMCP.streamable_http_app()` which returns a production-ready ASGI app that mounts directly into FastAPI 

---

## 4. Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Claude/ChatGPT │────▶│  Cloudflare      │────▶│  Your MCP       │
│   (No Auth)      │     │  Tunnel          │     │  Server (.exe)  │
│                  │     │  Public URL      │     │  localhost:8080 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                          │
                                                          ▼
                                                  ┌─────────────────┐
                                                  │  Your Custom    │
                                                  │  Auth API       │
                                                  │  (Internal)     │
                                                  └─────────────────┘
```

---

## 5. Authentication Bridge Strategy

Since Claude/ChatGPT cannot send custom auth headers, your MCP server acts as a **trusted proxy**:

### Option A: Environment-Based Auth (Recommended for .exe)
```python
# .env file (embedded in .exe or local)
INTERNAL_API_KEY=your_service_account_key
INTERNAL_API_URL=https://your-app.com/api

# MCP server loads these on startup and uses them
# for ALL requests to your internal API
```

### Option B: Pre-Authenticated Session
```python
# On .exe startup, authenticate with your custom auth API
# Store tokens in memory (never expose to clients)
# All MCP tool calls use this stored token
```

### Security Considerations:
- The **public MCP endpoint remains unauthenticated** (as required by Claude/ChatGPT)
- **Your internal API calls are fully authenticated** using service account credentials
- Bind to `127.0.0.1:8080` locally (not `0.0.0.0`) to prevent direct access 
- Validate `Origin` headers to prevent DNS rebinding attacks
- Use HTTPS via Cloudflare Tunnel (automatic)

---

## 6. Implementation Plan

### Phase 1: MCP Server Development
```python
# server.py
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
import httpx
import os

# Initialize MCP in stateless mode (perfect for tunneling)
mcp = FastMCP("AuthBridge", stateless_http=True)

@mcp.tool()
async def query_internal_data(query: str) -> str:
    """Tool that proxies to your authenticated API"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{os.getenv('INTERNAL_API_URL')}/query",
            json={"query": query},
            headers={"Authorization": f"Bearer {os.getenv('INTERNAL_API_KEY')}"}
        )
        return response.json()

# Create FastAPI app with MCP mounted
app = FastAPI()
app.mount("/mcp", mcp.streamable_http_app())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
```

### Phase 2: Packaging as .exe
```bash
# Install PyInstaller
pip install pyinstaller

# Create spec file for single executable
pyinstaller --onefile --name mcp-auth-bridge server.py

# Output: dist/mcp-auth-bridge.exe
```

### Phase 3: Cloudflare Tunnel Setup
```bash
# Install cloudflared
# Run tunnel pointing to your local MCP server
cloudflared tunnel --url http://localhost:8080

# Or create a permanent tunnel
cloudflared tunnel create mcp-bridge
cloudflared tunnel route dns mcp-bridge mcp.yourdomain.com
cloudflared tunnel run mcp-bridge
```

### Phase 4: Claude Configuration
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "auth-bridge": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.yourdomain.com/mcp",
        "--transport",
        "http-first"
      ]
    }
  }
}
```

---

## 7. Deployment Modes

| Mode | Use Case | Command |
|------|----------|---------|
| **Development** | Local testing | `uvicorn server:app --reload` |
| **Local Binary** | Single user, personal machine | Run `.exe` directly |
| **Cloudflare Tunnel** | Public access for Claude/ChatGPT | `cloudflared tunnel --url http://localhost:8080` |
| **Server Deployment** | Always-on service | Run `.exe` as Windows service + permanent tunnel |

---

## 8. Security Checklist

- [ ] **Bind to localhost only**: `host="127.0.0.1"` (never `0.0.0.0`)
- [ ] **Origin validation**: Whitelist known origins in FastAPI middleware
- [ ] **No client-side auth**: MCP endpoint is public by design
- [ ] **Service account auth**: Internal API uses strong, rotated keys
- [ ] **HTTPS only**: Cloudflare Tunnel provides TLS termination
- [ ] **Rate limiting**: Implement per-IP limits via FastAPI middleware
- [ ] **Input validation**: Sanitize all tool parameters before internal API calls
- [ ] **Logging**: Audit all internal API calls without logging sensitive data 

---

## 9. Why This Stack Wins

1. **FastAPI + MCP SDK**: The official Python SDK's `streamable_http_app()` gives you a spec-compliant server in ~10 lines of code 
2. **Stateless Mode**: No session management headaches across Cloudflare Tunnel disconnects
3. **Single Endpoint**: One `/mcp` URL for Cloudflare to proxy—no SSE complexity
4. **EXE Packaging**: PyInstaller creates a distributable that non-technical users can run
5. **Your Expertise**: Python/FastAPI is your team's strength—don't fight the toolchain

---

## 10. Next Steps

1. **Prototype**: Build a single-tool MCP server using the code above
2. **Test Locally**: Verify with `curl` and MCP Inspector
3. **Package**: Create the `.exe` with PyInstaller
4. **Tunnel**: Test with a temporary Cloudflare tunnel
5. **Integrate**: Add to Claude Desktop and verify end-to-end
6. **Harden**: Implement the security checklist before production

**Recommended Reading**:
- [MCP Streamable HTTP Spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) 
- [Cloudflare Tunnel Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [MCP Python SDK Examples](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/servers/simple-streamablehttp-stateless) 