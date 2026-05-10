# Service API Documentation

## Base URL
```
http://localhost:8000/api/service/
```

---

## Endpoints

### 1. Service Section
**Endpoint:** `GET /api/service/service-sections/`

**Description:** Returns the service section data with nested services and CTA in the format matching home.json structure.

**Response Format:**
```json
{
  "subtitle": "WHAT WE OFFER",
  "title": "Our Tax Services",
  "description": "Comprehensive tax consultation and FBR compliance services tailored to your needs",
  "services": [
    {
      "id": 1,
      "icon": "Description",
      "title": "Tax Return Filing",
      "description": "Complete tax return preparation and filing services for individuals and businesses with FBR compliance.",
      "features": [
        "Income Tax Returns",
        "Sales Tax Returns",
        "Withholding Tax",
        "Annual Information Returns"
      ],
      "popular": true
    }
  ],
  "cta": {
    "title": "Need Expert Tax Consultation?",
    "description": "Get professional tax advice from experienced consultants specializing in Pakistani tax law and FBR compliance",
    "primaryButton": "Schedule Consultation",
    "secondaryButton": "View All Services"
  }
}
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include (e.g., `?include=title,description`)
- `exclude` - Comma-separated list of fields to exclude (e.g., `?exclude=created_at,updated_at`)

---

### 2. Services
**Endpoint:** `GET /api/service/services/`

**Description:** Returns individual service items with all details.

**Response Format:**
```json
[
  {
    "id": 1,
    "title": "Tax Return Filing",
    "description": "Complete assistance with filing income tax returns for individuals and businesses with FBR.",
    "icon": "Description",
    "color": "#EE1C27",
    "button_text": "Learn More",
    "badge": "Popular",
    "popular": true,
    "features": [
      "Individual Tax Returns",
      "Corporate Tax Returns",
      "NRP Tax Filing",
      "E-Filing Support"
    ],
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include (e.g., `?include=title,description`)
- `exclude` - Comma-separated list of fields to exclude (e.g., `?exclude=created_at,updated_at`)

---

### 3. Hero
**Endpoint:** `GET /api/service/hero/`

**Description:** Returns the hero section data.

**Response Format:**
```json
[
  {
    "id": 1,
    "title": "Our Services",
    "subtitle": "Comprehensive tax solutions tailored to your needs. Expert guidance for individuals and businesses.",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include
- `exclude` - Comma-separated list of fields to exclude

---

### 4. Statistics
**Endpoint:** `GET /api/service/statistics/`

**Description:** Returns statistics data (number and label pairs).

**Response Format:**
```json
[
  {
    "id": 1,
    "number": "500+",
    "label": "Clients Served",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  },
  {
    "id": 2,
    "number": "15+",
    "label": "Years Experience",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  },
  {
    "id": 3,
    "number": "98%",
    "label": "Success Rate",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include
- `exclude` - Comma-separated list of fields to exclude

---

### 5. Benefits
**Endpoint:** `GET /api/service/benefits/`

**Description:** Returns benefits data (icon and text pairs).

**Response Format:**
```json
[
  {
    "id": 1,
    "icon": "VerifiedUser",
    "text": "Certified Tax Experts",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  },
  {
    "id": 2,
    "icon": "Security",
    "text": "Confidential & Secure",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  },
  {
    "id": 3,
    "icon": "TrendingUp",
    "text": "Maximize Savings",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  },
  {
    "id": 4,
    "icon": "CheckCircle",
    "text": "100% Compliance",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include
- `exclude` - Comma-separated list of fields to exclude

---

### 6. CTA
**Endpoint:** `GET /api/service/cta/`

**Description:** Returns the call-to-action section data.

**Response Format:**
```json
[
  {
    "id": 1,
    "title": "Need Professional Tax Assistance?",
    "description": "Get expert guidance from certified tax professionals. Schedule a consultation today.",
    "button_text": "Get Free Consultation",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

**Query Parameters:**
- `include` - Comma-separated list of fields to include
- `exclude` - Comma-separated list of fields to exclude

---

## Dynamic Field Filtering

All endpoints support dynamic field filtering via query parameters:

### Include Fields
Only return specified fields:
```
GET /api/service/services/?include=title,description,icon
```

### Exclude Fields
Return all fields except specified:
```
GET /api/service/services/?exclude=created_at,updated_at
```

### Combined Usage
You can use either `include` or `exclude`, but not both simultaneously.

---

## Model Relationships

The service models have the following relationships:

- **ServiceSection** is the parent model
- **Service** → ServiceSection (ForeignKey)
- **ServiceCTA** → ServiceSection (ForeignKey)
- **ServiceHero** → ServiceSection (ForeignKey)
- **ServiceStatistic** → ServiceSection (ForeignKey)
- **ServiceBenefit** → ServiceSection (ForeignKey)

In the Django admin, all related models are displayed as inlines under ServiceSection.

---

## Authentication

All endpoints are publicly accessible (no authentication required) as they use `AllowAny` permission class.

---

## Response Codes

- `200 OK` - Successful request
- `404 Not Found` - Resource not found
- `400 Bad Request` - Invalid query parameters
- `500 Internal Server Error` - Server error
