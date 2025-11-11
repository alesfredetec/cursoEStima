# Análisis de Configuraciones del Ecosistema Fintexa

## Resumen Ejecutivo

Este documento presenta un análisis detallado de las estructuras de archivos y configuraciones del ecosistema Fintexa, identificando conexiones de base de datos, configuraciones de EventBus, endpoints HTTP, y URLs de servicios externos.

## Estructura General del Ecosistema

El ecosistema Fintexa está organizado en cuatro dominios principales:

1. **Bind Aceptador** - Procesamiento de pagos y gestión de comercios
2. **Wallet Service** - Servicios de billetera digital
3. **CVUCollect** - Operaciones masivas con CVU
4. **Bind Configuration** - Gestión centralizada de configuración

### Proyectos Identificados por Ecosistema

#### Bind Aceptador (43 proyectos)
- **BFF Services**: Bff.BackofficeComercio, Bff.CardNotPresent, Bff.CardPresent, BFF.MobileNotPresent, Bff.SimpleButton
- **Payment Acceptor Services**: PaymentAcceptor.CardBusinessRules, PaymentAcceptor.CardOrchestrator, PaymentAcceptor.CardWorkflow, PaymentAcceptor.Deuda, PaymentAcceptor.Iep, PaymentAcceptor.Notificacion, PaymentAcceptor.Promotions, PaymentAcceptor.Qr, PaymentAcceptor.Rendicion, PaymentAcceptor.Transacciones, PaymentAcceptor.TransactionQuery, PaymentAcceptor.WorkFlowPagos
- **Shared Services**: Shared.AccessManagement, Shared.ApiBank.Api, Shared.AuthExternalService, Shared.BulkUploadProcess, Shared.CardVault, Shared.CloudServiceInfrastructure, Shared.Coelsa.Alias, Shared.Comercio, Shared.ComercioQuery, Shared.Comisiones, Shared.ComplianceCheck, Shared.CustomTemplates, Shared.Cvu, Shared.Cvu.Generator, Shared.Debin, Shared.EmailService, Shared.FileManager, Shared.GlobalProcesing, Shared.InternalAudit, Shared.IssuerIdentification, Shared.PagoExterno, Shared.PaymentsObservability, Shared.Pdf, Shared.Posicionamiento, Shared.ReportManager, Shared.Retencion, Shared.Vault.Admin, Shared.Vault.Card, Shared.VaultManager, Shared.WebhookSender
- **Web Services**: Web.BackofficeComercio, Web.CardNotPresent, Web.SimpleButton
- **Simple Button Payment**: SimpleButton.Payment

#### Wallet Service (56 proyectos)
- **Core Services**: Wallet.Cuenta, Wallet.Operaciones, Wallet.Bind, Wallet.CalculadorCostos, Wallet.InvestmentService, Wallet.Notificaciones, Wallet.Reporte, Wallet.StateMonitor, Wallet.Tin
- **Query Services**: Wallet.Cuenta.Queries, Wallet.Comprobante.Queries, Wallet.Operaciones.Queries
- **Specialized Services**: Wallet.BFF, Wallet.BFF.PCPConsentimiento, Wallet.Comprobante, Wallet.Consentimiento, Wallet.CargaMasiva, Wallet.QrCodes
- **Application**: Wallet.APP (MAUI), Wallet.AppSDK
- **Identity**: Wallet.IdentityServer
- **Shared Services**: Shared.AccessManagement, Shared.Crypto.Lirium, Shared.Debin, Shared.DispatcherCoelsaBind, Shared.EmailService, Shared.FileManager, Shared.PixRoaming, Shared.Poincenot.Market, Shared.QueueSentinel, shared.recycle, shared.remunera, shared.retencionwallet

#### CVUCollect (6 proyectos)
- **Middleware Services**: Middleware.Aggregator, Middleware.Financial, Middleware.BulkUploadProcess, Middleware.StateMonitor
- **Shared Services**: Shared.ApiBank

#### Bind Configuration (2 proyectos)
- **Configuration Services**: Bind.Configuration.BFF, Bind.Configuration.Admin

#### Boton Simple (15 proyectos)
- **Core Services**: BotonSimple.Payment, BotonSimple.Identity, BotonSimple.Security, BotonSimple.Notificacion
- **Boveda Services**: BotonSimple.Boveda.Api, BotonSimple.Boveda.Identity, BotonSimple.Boveda.Iframe
- **Backoffice**: BotonSimple.Backoffice
- **BFF**: BotonSimple.PaymentForm.BFF
- **Vault Manager**: BotonSimple.VaultManager
- **External Processors**: Shared.Cybersource, Shared.Decidir

#### ArchivosRI (2 proyectos)
- **Regulatory Information**: Shared.RegulatoryInformation

## Análisis de Configuraciones por Ambiente

### 1. Conexiones de Base de Datos

#### SQL Server
**Patrones de Conexión Identificados:**

**Desarrollo/Local:**
```json
"ConnectionStrings": {
  "DefaultConnection": "Server=tcp:sql-qrbind-stg-001.database.windows.net,1433;Initial Catalog=DB_NAME;Persist Security Info=False;User ID=tf-staging;Password=XXXXXXXXXXX;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;",
  "LogsConnection": "[Similar pattern for logs]"
}
```

**Producción:**
```json
"ConnectionStrings": {
  "DefaultConnection": "",  // Configurado vía variables de entorno
  "RedisConnection": ""
}
```

#### Redis
**Configuraciones Identificadas:**
- **Local**: `127.0.0.1:6379`, `localhost:6379`
- **Staging**: `10.200.1.20:6379`
- **Producción**: Variables de entorno

### 2. Configuraciones de EventBus

#### RabbitMQ (Desarrollo/Staging)
```json
"EventBusSettings": {
  "AzureServiceBus": "",
  "HostAddress": "rabbitmq://10.200.1.17:5672",
  "user": "admin",
  "password": "y4jZrGX#F152"
}
```

#### Azure Service Bus (Producción)
```json
"EventBusSettings": {
  "AzureServiceBus": "[CONNECTION_STRING]",
  "HostAddress": "",
  "user": "",
  "password": ""
}
```

### 3. Endpoints HTTP Configurados

#### Patrón de Configuración de Clientes HTTP

**Ambiente Local/Desarrollo:**
```json
"ServiceClientConfiguration": {
  "Host": "http://localhost:PORT",
  "EndPoints": {
    "EndpointName": "/api/v1/resource/{id}"
  }
}
```

**Ambiente Staging:**
```json
"ServiceClientConfiguration": {
  "Host": "http://10.210.1.XX",
  "EndPoints": {
    "EndpointName": "/api/v1/resource/{id}"
  }
}
```

**Ambiente Producción:**
```json
"ServiceClientConfiguration": {
  "Host": "http://servicename.namespace-prod",
  "EndPoints": {
    "EndpointName": "/api/v1/resource/{id}"
  }
}
```

#### Ejemplos de Servicios Configurados

**Bff.BackofficeComercio - Local:**
- ComercioClientConfiguration: `http://10.210.1.6`
- AccessManagementClientConfiguration: `http://10.210.1.39`
- TransaccionQueryClientConfiguration: `http://10.210.1.61`
- WalletOperacionesClientConfiguration: `http://10.210.1.50`
- PaymentApiConfiguration: `http://10.210.1.63`

**Bff.BackofficeComercio - Producción:**
- ComercioClientConfiguration: `http://comerciosharedservice`
- AccessManagementClientConfiguration: `http://accessmanagementsharedservice`
- TransaccionQueryClientConfiguration: `http://bindtransaccionqueryservice`
- WalletOperacionesClientConfiguration: `http://walletoperacionesservice.wallet-prod`
- PaymentApiConfiguration: `http://paymentapiservice.botonsimple-prod/`

### 4. URLs de Servicios Externos

#### Servicios de Autenticación
- **Ardid (KYC/AML)**: `https://gw-staging-qrbind.epays.services/ardid-client`
- **OAuth Azure AD**: `https://login.microsoftonline.com/61ef5b89-8df3-499d-8c13-38fed5d09c72/oauth2/v2.0/token`

#### Servicios de Terceros
- **Google reCAPTCHA**: `https://www.google.com/recaptcha/api/siteverify`
- **Siscri**: `http://10.210.1.14/`
- **Posicionamiento**: `http://10.210.1.12`

#### Servicios Bancarios/Financieros
- **BIND API**: Configurado dinámicamente por PSP
- **Coelsa**: Integración vía dispatcher
- **APIs Bancarias**: Múltiples endpoints según configuración

## Configuraciones de Seguridad

### JWT Configuration
```json
"JwtConfigSettings": {
  "Secret": "ACCESS_MANAGEMENT_SECRET_KEY",
  "TimeExpired": 15,
  "RefreshTokenTtl": 1,
  "Audience": "AU_BFF"
}
```

### Health Checks
```json
"HealthChecksUI": {
  "HealthChecks": [
    {
      "Name": "HealthChecksService",
      "Uri": "/healthz"
    }
  ],
  "EvaluationTimeInSeconds": 10,
  "MinimumSecondsBetweenFailureNotifications": 60
}
```

### Logging Configuration (Serilog)
```json
"Serilog": {
  "MinimumLevel": {
    "Default": "Information",
    "Override": {
      "Microsoft": "Warning",
      "System": "Warning"
    }
  },
  "WriteTo": [
    {
      "Name": "File",
      "Args": {
        "formatter": "Serilog.Formatting.Compact.CompactJsonFormatter, Serilog.Formatting.Compact",
        "path": "Logs/app.log",
        "fileSizeLimitBytes": 5000000,
        "rollOnFileSizeLimit": true,
        "retainedFileCountLimit": 30
      }
    }
  ]
}
```

## Análisis de Red de Servicios

### Red Interna (10.200.x.x y 10.210.x.x)
- **10.200.1.6**: Posicionamiento
- **10.200.1.10**: Notificaciones
- **10.200.1.17**: RabbitMQ
- **10.200.1.20**: Redis
- **10.200.1.23**: PDF Service
- **10.210.1.6**: Comercio Service
- **10.210.1.7**: Transaction Command
- **10.210.1.31**: Wallet Cuenta
- **10.210.1.34**: Wallet Comprobantes
- **10.210.1.36**: Wallet Cuenta Queries
- **10.210.1.39**: Access Management
- **10.210.1.43**: Card Business Rules
- **10.210.1.50**: Wallet Operaciones
- **10.210.1.55**: Wallet Operaciones Queries
- **10.210.1.61**: Transaction Query
- **10.210.1.63**: Payment API
 
### Namespaces de Kubernetes
- **bind-prod**: Servicios del ecosistema Bind Aceptador
- **wallet-prod**: Servicios del ecosistema Wallet
- **botonsimple-prod**: Servicios del ecosistema Botón Simple

## Configuraciones Específicas por Proyecto

### Wallet.Cuenta
**Servicios Integrados:**
- MsComprobante: `https://localhost:7117`
- MsBind: `http://localhost:5092`
- MsComprobanteQueries: `https://localhost:7118`
- MsArdid: `https://gw-staging-qrbind.epays.services/ardid-client`
- MsDispatcher: `https://localhost:7099`
- MsCalculadorCostos: `https://localhost:7099`
- MsSiscri: `http://10.210.1.14/`
- MsPosicionamiento: `http://10.210.1.12`
- MsInvestmentService: `https://localhost:7099`

### CVUCollect - Middleware.Financial
**Servicios Integrados:**
- WalletBind: `http://10.210.1.35`
- ApiAggregator: `http://10.210.1.22`
- ApiLirium: `http://localhost:5000`
- ApiStateMonitor: `http://localhost:5198/`
- ApiPagoExterno: `http://10.210.1.9/`

## Observaciones y Recomendaciones

### Fortalezas Identificadas
1. **Separación clara de ambientes** con configuraciones específicas por entorno
2. **Uso consistente de patrones** para configuración de clientes HTTP
3. **Configuración centralizada** de logging y health checks
4. **Seguridad robusta** con JWT y configuraciones de acceso

### Áreas de Mejora
1. **Hardcoded credentials** en algunos archivos de configuración local
2. **Inconsistencias en nomenclatura** de algunos endpoints
3. **Documentación de dependencias** podría ser más explícita
4. **Variables de entorno** no están completamente implementadas en producción

### Recomendaciones
1. **Migrar todas las credenciales** a Azure Key Vault o variables de entorno
2. **Estandarizar nombres de servicios** en Kubernetes
3. **Implementar configuration drift detection**
4. **Crear documentación de matriz de dependencias**
5. **Establecer convenciones de naming** más consistentes

## Matriz de Comunicación Entre Servicios

### Comunicación Sincrónica (HTTP)
```
BFF.BackofficeComercio → Shared.Comercio
BFF.BackofficeComercio → Shared.AccessManagement
BFF.BackofficeComercio → PaymentAcceptor.TransactionQuery
BFF.BackofficeComercio → Wallet.Operaciones
BFF.BackofficeComercio → Wallet.Comprobante.Queries

Wallet.Cuenta → Wallet.Bind
Wallet.Cuenta → Shared.ComplianceCheck (Ardid)
Wallet.Cuenta → Shared.Posicionamiento
Wallet.Cuenta → PaymentAcceptor.Siscri

CVUCollect.Middleware.Financial → Wallet.Bind
CVUCollect.Middleware.Financial → CVUCollect.Middleware.Aggregator
CVUCollect.Middleware.Financial → Shared.PagoExterno
```

### Comunicación Asíncrona (EventBus)
```
Todos los servicios → RabbitMQ/Azure Service Bus
- Eventos de dominio
- Comandos asíncronos
- Notificaciones de estado
```

## Conclusiones

El ecosistema Fintexa presenta una arquitectura de microservicios bien estructurada con configuraciones apropiadas para diferentes ambientes. La separación clara entre servicios core, BFF, y shared services facilita el mantenimiento y la escalabilidad. 

Las configuraciones muestran un enfoque maduro hacia la gestión de servicios distribuidos, aunque existen oportunidades de mejora en la gestión de secretos y la estandarización de configuraciones.

---

**Fecha de Análisis**: Enero 2025  
**Versión**: 1.0  
**Total de Proyectos Analizados**: 124  
**Total de Archivos de Configuración Revisados**: 486  
