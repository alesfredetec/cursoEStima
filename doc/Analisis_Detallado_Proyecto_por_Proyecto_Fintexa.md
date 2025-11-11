# Análisis Detallado Proyecto por Proyecto - Ecosistema Fintexa

## Introducción

Este documento proporciona un análisis exhaustivo de cada proyecto individual dentro del ecosistema Fintexa, describiendo su funcionalidad específica, dominio de negocio, arquitectura técnica y responsabilidades dentro del sistema general.

---

## 📋 ÍNDICE DE ECOSISTEMAS

### 1. [Bind Aceptador (Payment Acceptor)](#bind-aceptador)
### 2. [Wallet Service (Billetera Digital)](#wallet-service)
### 3. [CVU Collect (Servicios CVU)](#cvu-collect)
### 4. [Bind Configuration (Configuración)](#bind-configuration)
### 5. [Boton Simple (Legacy)](#boton-simple)
### 6. [Archivos RI (Regulatory Information)](#archivos-ri)

---

## 🔧 BIND ACEPTADOR

### Servicios Core

#### **Shared.Comercio**
**Dominio**: Gestión integral de comercios y entidades comerciales
**Funcionalidad**:
- **Onboarding de comercios**: Registro, validación y activación de nuevos comercios
- **Gestión de sucursales**: Administración de múltiples ubicaciones por comercio
- **Configuración de cajas**: Setup de terminales POS y puntos de venta
- **Datos maestros**: Almacenamiento de información comercial, documentación legal
- **Integración CVU**: Gestión de cuentas virtuales uniformes para comercios
- **Compliance**: Validaciones de cumplimiento y documentación regulatoria

**Repositorios Integrados**:
- `Shared.Comercio.BusinessRules.Repository`: Reglas de negocio específicas
- `Shared.Comercio.Comisiones.Repository`: Cálculo de comisiones comerciales
- `Shared.Comercio.Cvu.Repository`: Gestión de CVUs comerciales
- `Shared.Comercio.Debin.Repository`: Integración con sistema DEBIN
- `Shared.Comercio.Payment.Repository`: Procesamiento de pagos
- `Shared.Comercio.WalletCuenta.Repository`: Integración con billeteras

#### **Shared.Vault.Card**
**Dominio**: Tokenización y almacenamiento seguro de datos de tarjetas
**Funcionalidad**:
- **Tokenización PCI**: Conversión de PANs a tokens seguros
- **Gestión de usuarios**: Control de acceso a datos tokenizados
- **Identificación de emisores**: Determinación automática de entidades emisoras
- **Almacenamiento seguro**: Vault cifrado para datos sensibles
- **Gestión de códigos**: Administración de códigos de seguridad
- **Compliance PCI DSS**: Cumplimiento de estándares de seguridad

**Componentes Especializados**:
- `DataAccess.Bins`: Gestión de rangos BIN
- `DataAccess.Codes`: Administración de códigos de verificación
- `DataAccess.Pans`: Manejo seguro de números de tarjeta
- `DataAccess.Users`: Control de usuarios del vault

#### **Shared.WebhookSender**
**Dominio**: Sistema de notificaciones webhook
**Funcionalidad**:
- **Envío asíncrono**: Delivery garantizado de notificaciones
- **Retry logic**: Reintentos automáticos con backoff exponencial
- **Configuración por comercio**: Webhooks personalizados por entidad
- **Monitoreo de estado**: Tracking de entrega y fallos
- **Filtrado de eventos**: Selective delivery basado en tipos de evento

### BFF (Backend for Frontend)

#### **BFF.BackofficeComercio**
**Dominio**: API para interfaces administrativas de comercios
**Funcionalidad**:
- **Dashboard comercial**: Métricas y KPIs en tiempo real
- **Gestión de configuraciones**: Setup de parámetros operativos
- **Reportes transaccionales**: Consultas y exportaciones de datos
- **Administración de usuarios**: Gestión de accesos del comercio
- **Configuración de webhooks**: Setup de notificaciones

**Integraciones**:
- `DataAccess.HttpRest`: Comunicación con servicios backend
- `DataAccess.EntityFramework`: Persistencia local de configuraciones

#### **BFF.CardNotPresent**
**Dominio**: Procesamiento de pagos sin tarjeta física presente
**Funcionalidad**:
- **E-commerce payments**: Procesamiento para comercio electrónico
- **Validaciones 3DS**: Integración con 3D Secure
- **Gestión de riesgo**: Evaluación de transacciones sospechosas
- **Recurrencia**: Manejo de pagos recurrentes y suscripciones
- **Multi-adquirencia**: Routing a diferentes procesadores

**Componentes de Integración**:
- `DataAccess.DeudaApi`: Gestión de deudas y pagos diferidos
- `DataAccess.IdentityApi`: Validación de identidades
- `DataAccess.PaymentApi`: Procesamiento core de pagos
- `DataAccess.VaultManagerApi`: Acceso a datos tokenizados

#### **BFF.CardPresent**
**Dominio**: Procesamiento de pagos con tarjeta presente
**Funcionalidad**:
- **POS Integration**: Conexión con terminales físicos
- **EMV Processing**: Manejo de chip y PIN
- **Contactless**: Procesamiento NFC/RFID
- **Cashback**: Gestión de retiros en efectivo
- **Offline mode**: Procesamiento sin conectividad

**Gateway Integration**:
- `DataAccess.Gateway`: Comunicación con redes de pago
- `DataAccess.HttpRest`: APIs de procesadores externos

#### **BFF.MobileNotPresent**
**Dominio**: API especializada para aplicaciones móviles
**Funcionalidad**:
- **SDK Mobile**: Endpoints optimizados para apps nativas
- **Push payments**: Notificaciones push de transacciones
- **QR Payments**: Generación y procesamiento de códigos QR
- **Geolocalización**: Validaciones basadas en ubicación
- **Biometría**: Integración con validación biométrica

### Servicios de Procesamiento

#### **PaymentAcceptor.CardBusinessRules**
**Dominio**: Motor de reglas de negocio para pagos con tarjeta
**Funcionalidad**:
- **Validación pre-transaccional**: Checks antes del procesamiento
- **Cálculo de comisiones**: Algoritmos dinámicos de pricing
- **Límites transaccionales**: Enforcement de límites por comercio/usuario
- **Promociones**: Aplicación de descuentos y beneficios
- **Compliance check**: Validaciones regulatorias automáticas

**Integraciones Especializadas**:
- `DataAccess.ComplianceCheck`: Validaciones de cumplimiento
- `DataAccess.Promotion`: Motor de promociones
- `GlobalProcesing.Repository`: Integración con Global Processing

#### **PaymentAcceptor.CardOrchestrator**
**Dominio**: Orquestación de flujos de pago complejos
**Funcionalidad**:
- **Workflow management**: Coordinación de procesos multi-step
- **Routing dinámico**: Selección automática de procesadores
- **Compensación**: Rollback automático en caso de fallos
- **Estado transaccional**: Tracking de estados intermedios
- **Optimización de rutas**: Machine learning para routing óptimo

#### **PaymentAcceptor.CardWorkflow**
**Dominio**: Gestión de workflows y estados de transacciones
**Funcionalidad**:
- **State machine**: Máquina de estados para transacciones
- **Proceso asíncrono**: Manejo de operaciones de larga duración
- **Conciliación**: Matching con archivos de procesadores
- **Rendición**: Generación de archivos para liquidación
- **Monitoreo**: Alertas por transacciones stuck

### Servicios Especializados

#### **PaymentAcceptor.Deuda**
**Dominio**: Gestión de deudas y pagos diferidos
**Funcionalidad**:
- **Gestión de vencimientos**: Control automático de fechas de pago
- **Intereses y punitorios**: Cálculo automático de recargos
- **Planes de pago**: Estructuración de cuotas y refinanciación
- **Cobranza**: Workflows automatizados de gestión de cobros
- **Integración CVU**: Gestión de débitos automáticos

#### **PaymentAcceptor.Qr**
**Dominio**: Generación y procesamiento de códigos QR
**Funcionalidad**:
- **QR dinámicos**: Generación con montos y datos específicos
- **QR estáticos**: Códigos reutilizables para comercios
- **Validación EMVCo**: Compliance con estándares internacionales
- **Timeout management**: Expiración automática de códigos
- **Analytics**: Métricas de uso y conversión

#### **PaymentAcceptor.Promotions**
**Dominio**: Motor de promociones y descuentos
**Funcionalidad**:
- **Reglas configurables**: Engine flexible de condiciones
- **Descuentos dinámicos**: Cálculos en tiempo real
- **Límites de uso**: Control de frecuencia y montos
- **Segmentación**: Promociones por grupo de usuarios
- **A/B Testing**: Experimentos de marketing

### Servicios de Infraestructura

#### **Shared.AccessManagement**
**Dominio**: Gestión centralizada de accesos y permisos
**Funcionalidad**:
- **Autenticación**: OAuth 2.0/OpenID Connect
- **Autorización**: RBAC (Role-Based Access Control)
- **JWT Management**: Emisión y validación de tokens
- **Single Sign-On**: SSO across múltiples aplicaciones
- **Audit trail**: Logging de accesos y permisos

#### **Shared.ApiBank**
**Dominio**: Abstracción para integración con múltiples bancos
**Funcionalidad**:
- **Multi-banco**: Conectores estandarizados para diferentes entidades
- **Protocol abstraction**: Normalización de APIs bancarias
- **Failover**: Switching automático entre bancos
- **Rate limiting**: Control de frecuencia de requests
- **Transformación de datos**: Mapeo entre formatos diferentes

#### **Shared.ComplianceCheck**
**Dominio**: Validaciones de cumplimiento regulatorio
**Funcionalidad**:
- **Listas de control**: Verificación contra listas negras
- **Validación ARDID**: Integración con sistemas antifraude
- **KYC automation**: Know Your Customer automatizado
- **Scoring**: Evaluación automática de riesgo
- **Reporting**: Generación de reportes regulatorios

#### **Shared.AuthExternalService**
**Dominio**: Autenticación con servicios externos
**Funcionalidad**:
- **OAuth providers**: Integración con Google, Facebook, etc.
- **SAML SSO**: Single Sign-On empresarial
- **Token management**: Gestión de tokens externos
- **Identity federation**: Federación de identidades
- **Profile sync**: Sincronización de perfiles

#### **Shared.BulkUploadProcess**
**Dominio**: Procesamiento masivo de archivos
**Funcionalidad**:
- **File validation**: Validación de formatos y estructura
- **Batch processing**: Procesamiento asíncrono de lotes
- **Error handling**: Gestión detallada de errores
- **Progress tracking**: Seguimiento de progreso
- **Rollback capabilities**: Reversión de procesamientos

#### **Shared.CardVault**
**Dominio**: Vault alternativo para datos de tarjetas
**Funcionalidad**:
- **Card storage**: Almacenamiento seguro adicional
- **MongoDB integration**: Persistencia NoSQL
- **High availability**: Disponibilidad mejorada
- **Backup vault**: Vault de respaldo
- **Performance optimization**: Optimizaciones de rendimiento

#### **Shared.CloudServiceInfrastructure**
**Dominio**: Infraestructura de servicios en la nube
**Funcionalidad**:
- **Service discovery**: Descubrimiento automático de servicios
- **Load balancing**: Balanceador de carga inteligente
- **Health monitoring**: Monitoreo de salud de servicios
- **Auto-scaling**: Escalado automático
- **Resource management**: Gestión de recursos cloud

#### **Shared.Coelsa.Alias**
**Dominio**: Gestión de alias para COELSA
**Funcionalidad**:
- **Alias management**: Gestión de alias de cuentas
- **CVU mapping**: Mapeo CVU-Alias
- **Resolution**: Resolución de alias a cuentas
- **Validation**: Validación de alias
- **Directory services**: Servicios de directorio

#### **Shared.ComercioQuery**
**Dominio**: Servicio de consultas de comercios (Read-Only)
**Funcionalidad**:
- **Merchant queries**: Consultas optimizadas de comercios
- **Performance**: Alto rendimiento para consultas
- **Reporting**: Reportes específicos de comercios
- **Analytics**: Análisis de datos comerciales
- **Caching**: Cache especializado

#### **Shared.Comisiones**
**Dominio**: Motor de cálculo de comisiones
**Funcionalidad**:
- **Commission engine**: Motor de cálculo avanzado
- **Rules management**: Gestión de reglas de comisiones
- **Tiered pricing**: Precios escalonados
- **Promotions**: Promociones en comisiones
- **Audit trail**: Trazabilidad de cálculos

#### **Shared.CustomTemplates**
**Dominio**: Gestión de plantillas personalizables
**Funcionalidad**:
- **Template engine**: Motor de plantillas
- **Dynamic content**: Contenido dinámico
- **Multi-format**: Múltiples formatos (HTML, PDF, etc.)
- **Branding**: Personalización de marca
- **Versioning**: Control de versiones

#### **Shared.Cvu**
**Dominio**: Gestión principal de CVUs COELSA
**Funcionalidad**:
- **CVU lifecycle**: Gestión completa del ciclo de vida
- **Account creation**: Creación automatizada
- **Status management**: Gestión de estados
- **Integration**: Integración con COELSA
- **Validation**: Validaciones específicas

#### **Shared.Cvu.Generator**
**Dominio**: Generador de números CVU
**Funcionalidad**:
- **CVU generation**: Generación de números únicos
- **Algorithm**: Algoritmo de generación
- **Validation**: Validación de dígitos verificadores
- **Collision detection**: Detección de colisiones
- **Performance**: Generación de alto rendimiento

#### **Shared.Debin**
**Dominio**: Integración con sistema DEBIN
**Funcionalidad**:
- **DEBIN API**: Integración con API oficial
- **Request processing**: Procesamiento de solicitudes
- **Status tracking**: Seguimiento de estados
- **Notifications**: Notificaciones de DEBIN
- **Reconciliation**: Conciliación de operaciones

#### **Shared.EmailService**
**Dominio**: Servicio de envío de emails
**Funcionalidad**:
- **SMTP management**: Gestión de servidores SMTP
- **Template engine**: Motor de plantillas de email
- **Delivery tracking**: Seguimiento de entrega
- **Queue management**: Gestión de colas de envío
- **Bounce handling**: Manejo de rebotes

#### **Shared.FileManager**
**Dominio**: Gestión de archivos y documentos
**Funcionalidad**:
- **File storage**: Almacenamiento de archivos
- **Document management**: Gestión documental
- **Metadata**: Gestión de metadatos
- **Access control**: Control de acceso a archivos
- **Versioning**: Control de versiones

#### **Shared.GlobalProcesing**
**Dominio**: Integración con Global Processing
**Funcionalidad**:
- **Payment processing**: Procesamiento internacional
- **Multi-currency**: Soporte multi-moneda
- **Risk management**: Gestión de riesgo global
- **Compliance**: Cumplimiento internacional
- **Settlement**: Liquidación global

#### **Shared.InternalAudit**
**Dominio**: Auditoría interna de transacciones
**Funcionalidad**:
- **Audit logging**: Logging detallado de auditoría
- **Transaction monitoring**: Monitoreo transaccional
- **Compliance checks**: Verificaciones de cumplimiento
- **Report generation**: Generación de reportes
- **Alert system**: Sistema de alertas

#### **Shared.IssuerIdentification**
**Dominio**: Identificación de emisores de tarjetas
**Funcionalidad**:
- **BIN range management**: Gestión de rangos BIN
- **Issuer lookup**: Búsqueda de emisores
- **Card type detection**: Detección de tipo de tarjeta
- **Country identification**: Identificación de país
- **Network detection**: Detección de red (Visa, MC, etc.)

#### **Shared.PagoExterno**
**Dominio**: Procesamiento de pagos externos
**Funcionalidad**:
- **External payments**: Pagos a terceros
- **Provider integration**: Integración con proveedores
- **Routing**: Enrutamiento de pagos
- **Settlement**: Liquidación externa
- **Monitoring**: Monitoreo de pagos

**Repositorios Especializados**:
- `Repository.Coelsa`: Integración COELSA
- `Repository.PaymentObservability`: Observabilidad de pagos
- `Repository.Promotions`: Motor de promociones
- `Repository.WorkFlowPagos`: Workflow de pagos

#### **Shared.PaymentsObservability**
**Dominio**: Observabilidad y monitoreo de pagos
**Funcionalidad**:
- **Real-time monitoring**: Monitoreo en tiempo real
- **Metrics collection**: Recolección de métricas
- **Alerting**: Sistema de alertas avanzado
- **Dashboard**: Dashboards de observabilidad
- **Performance analytics**: Analytics de rendimiento

#### **Shared.Pdf**
**Dominio**: Generación de documentos PDF
**Funcionalidad**:
- **PDF generation**: Generación de PDFs
- **Template system**: Sistema de plantillas
- **Digital signatures**: Firmas digitales
- **Compression**: Compresión de archivos
- **Batch processing**: Procesamiento masivo

#### **Shared.Posicionamiento**
**Dominio**: Gestión de posiciones financieras
**Funcionalidad**:
- **Position tracking**: Seguimiento de posiciones
- **Balance calculation**: Cálculo de balances
- **Movement history**: Historial de movimientos
- **Reconciliation**: Conciliación de posiciones
- **Real-time updates**: Actualizaciones en tiempo real

#### **Shared.ReportManager**
**Dominio**: Gestión centralizada de reportes
**Funcionalidad**:
- **Report generation**: Generación de reportes
- **Scheduling**: Programación de reportes
- **Distribution**: Distribución automática
- **Template management**: Gestión de plantillas
- **Export formats**: Múltiples formatos de exportación

#### **Shared.Retencion**
**Dominio**: Gestión de retenciones fiscales
**Funcionalidad**:
- **Tax retention**: Retenciones fiscales automáticas
- **Calculation engine**: Motor de cálculo
- **Certificate generation**: Generación de certificados
- **AFIP integration**: Integración con AFIP
- **Compliance**: Cumplimiento fiscal

#### **Shared.Vault.Admin**
**Dominio**: Administración del vault de datos
**Funcionalidad**:
- **Vault administration**: Administración del vault
- **Access management**: Gestión de accesos
- **Key rotation**: Rotación de claves
- **Backup management**: Gestión de backups
- **Security monitoring**: Monitoreo de seguridad

#### **Shared.VaultManager**
**Dominio**: Gestión unificada de vaults
**Funcionalidad**:
- **Multi-vault management**: Gestión de múltiples vaults
- **Data orchestration**: Orquestación de datos
- **Security policies**: Políticas de seguridad
- **Access control**: Control granular de accesos
- **Audit logging**: Logging de auditoría

### Servicios de Procesamiento Adicionales

#### **PaymentAcceptor.Conciliacion**
**Dominio**: Conciliación de transacciones
**Funcionalidad**:
- **Transaction matching**: Matching de transacciones
- **Discrepancy detection**: Detección de discrepancias
- **Automated reconciliation**: Conciliación automatizada
- **Manual review**: Revisión manual de casos
- **Reporting**: Reportes de conciliación

#### **PaymentAcceptor.Iep**
**Dominio**: Integración con IEP (Instant Electronic Payments)
**Funcionalidad**:
- **IEP processing**: Procesamiento de pagos instantáneos
- **Real-time settlement**: Liquidación en tiempo real
- **Status tracking**: Seguimiento de estados
- **Error handling**: Manejo de errores
- **Compliance**: Cumplimiento IEP

#### **PaymentAcceptor.Liquidacion**
**Dominio**: Liquidación de transacciones
**Funcionalidad**:
- **Settlement processing**: Procesamiento de liquidaciones
- **Batch liquidation**: Liquidación por lotes
- **File generation**: Generación de archivos
- **Bank integration**: Integración bancaria
- **Reconciliation**: Conciliación de liquidaciones

#### **PaymentAcceptor.Notificacion**
**Dominio**: Sistema de notificaciones especializadas
**Funcionalidad**:
- **Event-driven notifications**: Notificaciones por eventos
- **Multi-channel delivery**: Entrega multi-canal
- **Template management**: Gestión de plantillas
- **Delivery confirmation**: Confirmación de entrega
- **Retry mechanisms**: Mecanismos de reintento

#### **PaymentAcceptor.Rendicion**
**Dominio**: Rendición de cuentas y reportes
**Funcionalidad**:
- **Account reconciliation**: Rendición de cuentas
- **Financial reporting**: Reportes financieros
- **Compliance reports**: Reportes de cumplimiento
- **Automated generation**: Generación automatizada
- **Distribution**: Distribución de reportes

#### **PaymentAcceptor.Transacciones**
**Dominio**: Gestión de transacciones (Commands)
**Funcionalidad**:
- **Transaction processing**: Procesamiento de transacciones
- **State management**: Gestión de estados
- **Validation**: Validaciones de transacciones
- **Event publishing**: Publicación de eventos
- **Error handling**: Manejo de errores

#### **PaymentAcceptor.TransactionQuery**
**Dominio**: Consultas de transacciones (Queries)
**Funcionalidad**:
- **Transaction queries**: Consultas optimizadas
- **Historical data**: Datos históricos
- **Search capabilities**: Capacidades de búsqueda
- **Reporting**: Reportes de transacciones
- **Performance**: Alto rendimiento

#### **PaymentAcceptor.WorkFlowPagos**
**Dominio**: Workflow completo de pagos
**Funcionalidad**:
- **End-to-end workflow**: Workflow completo
- **Multi-step processing**: Procesamiento multi-etapa
- **State coordination**: Coordinación de estados
- **Error recovery**: Recuperación de errores
- **Monitoring**: Monitoreo de workflow

**Integraciones del Workflow**:
- `DataAccess.ApiBank`: Integración bancaria
- `DataAccess.CardBusinessRules`: Reglas de negocio
- `DataAccess.Debin`: Integración DEBIN
- `DataAccess.Deuda`: Gestión de deudas
- `DataAccess.PagoExterno`: Pagos externos
- `DataAccess.Rendicion`: Rendición
- `DataAccess.StateMonitor`: Monitoreo de estados
- `DataAccess.WalletComprobantes`: Comprobantes wallet

### BFF Adicionales

#### **Bff.SimpleButton**
**Dominio**: BFF para botón de pago simple
**Funcionalidad**:
- **Simple payment flow**: Flujo de pago simplificado
- **One-click payments**: Pagos de un click
- **Minimal UI**: Interfaz minimalista
- **High performance**: Alto rendimiento
- **Easy integration**: Integración sencilla

### Servicios Web

#### **Web.BackofficeComercio**
**Dominio**: Interfaz web para backoffice de comercios
**Funcionalidad**:
- **Web dashboard**: Dashboard web completo
- **Transaction management**: Gestión de transacciones
- **Reporting interface**: Interfaz de reportes
- **Configuration UI**: UI de configuración
- **User management**: Gestión de usuarios

#### **Web.CardNotPresent**
**Dominio**: Interfaz web para pagos card not present
**Funcionalidad**:
- **Payment forms**: Formularios de pago
- **3DS integration**: Integración 3D Secure
- **Responsive design**: Diseño responsivo
- **Security**: Seguridad web avanzada
- **UX optimization**: Optimización UX

#### **Web.SimpleButton**
**Dominio**: Interfaz web para botón simple
**Funcionalidad**:
- **Simple payment UI**: UI de pago simple
- **Minimal integration**: Integración mínima
- **Fast loading**: Carga rápida
- **Mobile optimized**: Optimizado móvil
- **One-step checkout**: Checkout de un paso

### Servicios de Testing y Desarrollo

#### **Fake.Coelsa**
**Dominio**: Simulador de servicios COELSA
**Funcionalidad**:
- **Mock services**: Servicios simulados
- **Testing environment**: Ambiente de testing
- **Response simulation**: Simulación de respuestas
- **Scenario testing**: Testing de escenarios
- **Performance testing**: Testing de rendimiento

### Jobs y Procesos

#### **Jobs.Bind**
**Dominio**: Jobs relacionados con BIND
**Funcionalidad**:
- **Scheduled jobs**: Jobs programados
- **Data synchronization**: Sincronización de datos
- **Batch processing**: Procesamiento por lotes
- **Maintenance tasks**: Tareas de mantenimiento
- **Monitoring**: Monitoreo de jobs

#### **Jobs.Internal**
**Dominio**: Jobs internos del sistema
**Funcionalidad**:
- **System maintenance**: Mantenimiento del sistema
- **Data cleanup**: Limpieza de datos
- **Report generation**: Generación de reportes
- **Archive processes**: Procesos de archivo
- **Health checks**: Verificaciones de salud

---

## 💰 WALLET SERVICE

### Servicios Core

#### **Wallet.Cuenta**
**Dominio**: Gestión integral de cuentas digitales y onboarding
**Funcionalidad**:
- **Onboarding KYC**: Proceso de alta con validación de identidad
- **Gestión de CVUs**: Creación y administración de cuentas virtuales
- **Validación biométrica**: Integración con sistemas de reconocimiento
- **Estados de cuenta**: Tracking de status y limitaciones
- **Compliance**: Validaciones ARDID y listas de control
- **Datos personales**: Gestión de información de usuarios

**Repositorios Especializados**:
- `Ardid.Repository`: Validaciones antifraude
- `Bind.Repository`: Integración bancaria
- `CalculadorCostos.Repository`: Cálculo de comisiones
- `Comprobante.Repository`: Generación de comprobantes
- `InvestmentService.Repository`: Servicios de inversión
- `Posicionamiento.Repository`: Gestión de posiciones
- `Siscri.Repository`: Reportes regulatorios

#### **Wallet.Operaciones**
**Dominio**: Motor de procesamiento de operaciones financieras
**Funcionalidad**:
- **Transferencias**: P2P, a cuentas bancarias, CVU to CVU
- **Pagos QR**: Procesamiento de pagos via códigos QR
- **DEBIN**: Integración con débito inmediato
- **Carga de saldo**: Top-up desde tarjetas/cuentas bancarias
- **Retiros**: Cash-out a cuentas bancarias
- **Operaciones programadas**: Scheduling de transacciones futuras

**Integraciones Críticas**:
- `Ardid.Repository`: Validaciones antifraude en tiempo real
- `Bind.Repository`: Ejecución de operaciones bancarias
- `Consentimiento.Repository`: Gestión de autorizaciones
- `Debin.Repository`: Procesamiento de débitos inmediatos
- `Dispatcher.Repository`: Routing de operaciones
- `StateMonitor.Repository`: Monitoreo de estados

#### **Wallet.Bind**
**Dominio**: Integración con plataforma bancaria BIND
**Funcionalidad**:
- **API Gateway**: Proxy hacia servicios bancarios core
- **Transformación de datos**: Mapeo entre modelos Wallet y BIND
- **Circuit breaker**: Protección contra fallos bancarios
- **Caching**: Cache de respuestas para optimización
- **Rate limiting**: Control de frecuencia hacia el banco
- **Monitoring**: Métricas de integración bancaria

#### **Wallet.CalculadorCostos**
**Dominio**: Cálculo dinámico de comisiones y costos
**Funcionalidad**:
- **Pricing dinámico**: Cálculos basados en múltiples variables
- **Segmentación**: Precios diferenciados por tipo de usuario
- **Promociones**: Aplicación de descuentos temporales
- **Escalas**: Comisiones progresivas por volumen
- **Simulaciones**: Preview de costos antes de ejecutar

### Servicios de Inversión

#### **Wallet.InvestmentService**
**Dominio**: Plataforma de inversiones integrada
**Funcionalidad**:
- **Dólar MEP**: Compra/venta de dólares via MEP
- **Criptomonedas**: Trading de crypto (BTC, ETH, etc.)
- **Fondos comunes**: Inversión en FCI
- **Plazo fijo**: Gestión de plazos fijos digitales
- **Portfolio**: Visualización de cartera integrada
- **Cotizaciones**: Real-time pricing de instrumentos

**Integraciones Especializadas**:
- `Lirium.Repository`: Crypto exchange integration
- `Poincenot.Repository`: Market data provider
- `Feriados.Repository`: Calendario de días hábiles
- `Comprobante.Repository`: Certificados de inversión

#### **Shared.Crypto.Lirium**
**Dominio**: Integración con exchange de criptomonedas
**Funcionalidad**:
- **Trading API**: Órdenes de compra/venta automatizadas
- **Wallet custody**: Custodia segura de crypto assets
- **Price feeds**: Streaming de precios en tiempo real
- **Settlement**: Liquidación de operaciones crypto
- **Risk management**: Límites de exposición

#### **Shared.Poincenot.Market**
**Dominio**: Integración con proveedor de datos de mercado
**Funcionalidad**:
- **Market data**: Cotizaciones de acciones, bonos, FCI
- **Historical data**: Información histórica para analytics
- **Corporate actions**: Eventos corporativos (dividendos, splits)
- **Risk metrics**: Cálculo de VaR y métricas de riesgo
- **Compliance**: Validaciones de mercado

### BFF y Aplicaciones Cliente

#### **Wallet.BFF**
**Dominio**: Backend for Frontend para aplicación móvil
**Funcionalidad**:
- **API aggregation**: Unificación de múltiples servicios backend
- **Response optimization**: Responses optimizadas para mobile
- **Caching inteligente**: Cache específico para UX móvil
- **Push notifications**: Coordinación de notificaciones
- **Session management**: Gestión de sesiones móviles

#### **Wallet.APP**
**Dominio**: Aplicación móvil multiplataforma (MAUI)
**Funcionalidad**:
- **UI/UX nativa**: Experiencia optimizada iOS/Android
- **Biometric auth**: Autenticación biométrica local
- **Offline capabilities**: Funcionalidades sin conexión
- **Push handling**: Manejo de notificaciones push
- **Deep linking**: Navegación via links externos

#### **Wallet.AppSDK**
**Dominio**: SDK para desarrollo de aplicaciones wallet
**Funcionalidad**:
- **Component library**: Componentes UI reutilizables
- **API wrappers**: Abstracciones de APIs backend
- **Security utilities**: Herramientas de seguridad
- **Testing utilities**: Mocks y helpers para testing
- **Documentation**: Guías de integración

### Servicios de Soporte

#### **Wallet.Comprobante**
**Dominio**: Generación y gestión de comprobantes fiscales
**Funcionalidad**:
- **AFIP Integration**: Generación de comprobantes fiscales
- **PDF Generation**: Comprobantes en formato PDF
- **Email delivery**: Envío automático por email
- **Digital storage**: Almacenamiento digital de comprobantes
- **Búsqueda**: Query engine para comprobantes históricos

#### **Wallet.Notificaciones**
**Dominio**: Sistema integral de notificaciones
**Funcionalidad**:
- **Multi-channel**: Email, SMS, Push, Webhooks
- **Templating**: Templates personalizables por evento
- **Scheduling**: Programación de notificaciones
- **Delivery tracking**: Seguimiento de entrega
- **Preferences**: Gestión de preferencias de usuario

#### **Wallet.Reporte**
**Dominio**: Generación de reportes financieros y regulatorios
**Funcionalidad**:
- **Reportes AML**: Anti-Money Laundering reports
- **UIF**: Reportes para Unidad de Información Financiera
- **Estados de cuenta**: Resúmenes periódicos automatizados
- **Analytics**: Dashboards y métricas de negocio
- **Export**: Múltiples formatos (PDF, Excel, CSV)

#### **Wallet.Consentimiento**
**Dominio**: Gestión de consentimientos para Open Banking
**Funcionalidad**:
- **PCP Integration**: Payment Initiation Services
- **Account aggregation**: Agregación de cuentas externas
- **Consent lifecycle**: Gestión completa de consentimientos
- **Revocation**: Revocación de permisos
- **Audit**: Trazabilidad de consentimientos

### Servicios de Queries

#### **Wallet.Cuenta.Queries**
**Dominio**: Servicio de consultas optimizado para cuentas
**Funcionalidad**:
- **Read-only API**: Queries optimizadas sin escritura
- **High performance**: Designed for high throughput
- **Complex queries**: Consultas analíticas complejas
- **Materialized views**: Vistas precalculadas
- **Caching**: Múltiples niveles de cache

#### **Wallet.Operaciones.Queries**
**Dominio**: Servicio de consultas optimizado para operaciones
**Funcionalidad**:
- **Transaction queries**: Consultas de transacciones optimizadas
- **Historical data**: Acceso a datos históricos
- **Real-time status**: Estados en tiempo real
- **Analytics**: Análisis de operaciones
- **Performance**: Alto rendimiento para consultas

#### **Wallet.Comprobante.Queries**
**Dominio**: Servicio de consultas de comprobantes
**Funcionalidad**:
- **Receipt queries**: Consultas de comprobantes
- **Search engine**: Motor de búsqueda avanzado
- **Filtering**: Filtros complejos
- **Export capabilities**: Capacidades de exportación
- **Audit trail**: Trazabilidad de consultas

#### **Wallet.CargaMasiva**
**Dominio**: Carga masiva de datos para Wallet
**Funcionalidad**:
- **Bulk account creation**: Creación masiva de cuentas
- **Data import**: Importación de datos masivos
- **Validation**: Validación de archivos masivos
- **Progress tracking**: Seguimiento de progreso
- **Error reporting**: Reportes de errores detallados

#### **Wallet.BFF.PCPConsentimiento**
**Dominio**: BFF específico para consentimientos PCP
**Funcionalidad**:
- **Consent management**: Gestión de consentimientos
- **PCP integration**: Integración específica PCP
- **User flow**: Flujos de usuario optimizados
- **Security**: Seguridad especializada
- **Audit**: Auditoría de consentimientos

#### **Wallet.StateMonitor**
**Dominio**: Monitoreo de estados de operaciones Wallet
**Funcionalidad**:
- **State tracking**: Seguimiento de estados
- **Real-time monitoring**: Monitoreo en tiempo real
- **Alerting**: Sistema de alertas
- **Recovery**: Procesos de recuperación
- **Metrics**: Métricas de estados

#### **Wallet.IdentityServer**
**Dominio**: Servidor de identidades para Wallet
**Funcionalidad**:
- **Identity management**: Gestión completa de identidades
- **OAuth/OIDC**: Servidor OAuth 2.0/OpenID Connect
- **Multi-factor auth**: Autenticación multifactor
- **Federation**: Federación de identidades
- **Admin interface**: Interfaz administrativa

**Componentes del IdentityServer**:
- `Wallet.IdentityServer.Admin`: Interfaz administrativa
- `Wallet.IdentityServer.STS.Identity`: Security Token Service
- `Wallet.IdentityServer.Admin.EntityFramework`: Persistencia EF
- `Wallet.IdentityServer.Shared`: Componentes compartidos

#### **Wallet.QrCodes**
**Dominio**: Gestión de códigos QR para Wallet
**Funcionalidad**:
- **QR generation**: Generación de códigos QR
- **Dynamic QR**: QR dinámicos con datos variables
- **Static QR**: QR estáticos reutilizables
- **Validation**: Validación de códigos
- **Analytics**: Métricas de uso

#### **Wallet.Tin**
**Dominio**: Integración con TIN (Travel Identification Number)
**Funcionalidad**:
- **TIN processing**: Procesamiento TIN
- **Travel payments**: Pagos relacionados con viajes
- **Integration**: Integración con Micronauta
- **Compliance**: Cumplimiento regulatorio
- **Reporting**: Reportes específicos TIN

#### **Wallet.AzureFunction**
**Dominio**: Funciones serverless de Azure para Wallet
**Funcionalidad**:
- **Serverless processing**: Procesamiento serverless
- **Event-driven**: Funciones dirigidas por eventos
- **Scaling**: Escalado automático
- **Cost optimization**: Optimización de costos
- **Integration**: Integración con servicios Azure

### Servicios Compartidos Wallet

#### **Shared.DispatcherCoelsaBind**
**Dominio**: Dispatcher para integración COELSA-BIND
**Funcionalidad**:
- **Request routing**: Enrutamiento de requests
- **Protocol translation**: Traducción de protocolos
- **Load balancing**: Balanceo de carga
- **Failover**: Manejo de fallos
- **Monitoring**: Monitoreo de integraciones

**Repositorios Integrados**:
- `Bind.Repository`: Integración BIND
- `CVU.Repository`: Gestión CVU
- `Debin.Repository`: Integración DEBIN

#### **Shared.PixRoaming**
**Dominio**: Integración con PIX (Brasil) para roaming
**Funcionalidad**:
- **PIX integration**: Integración con sistema PIX
- **Cross-border payments**: Pagos transfronterizos
- **Currency conversion**: Conversión de monedas
- **Compliance**: Cumplimiento internacional
- **Settlement**: Liquidación internacional

#### **Shared.QueueSentinel**
**Dominio**: Monitoreo y gestión de colas
**Funcionalidad**:
- **Queue monitoring**: Monitoreo de colas
- **Dead letter handling**: Manejo de mensajes fallidos
- **Performance metrics**: Métricas de rendimiento
- **Auto-recovery**: Recuperación automática
- **Alerting**: Sistema de alertas

#### **Shared.Recycle**
**Dominio**: Reciclaje y reutilización de recursos
**Funcionalidad**:
- **Resource recycling**: Reciclaje de recursos
- **Memory optimization**: Optimización de memoria
- **Performance**: Mejoras de rendimiento
- **Cleanup**: Limpieza de recursos
- **Monitoring**: Monitoreo de recursos

#### **Shared.Remunera**
**Dominio**: Gestión de remuneraciones y rendimientos
**Funcionalidad**:
- **Yield calculation**: Cálculo de rendimientos
- **Interest payments**: Pagos de intereses
- **Compound interest**: Interés compuesto
- **Tax handling**: Manejo de impuestos
- **Reporting**: Reportes de remuneraciones

**Repositorios Especializados**:
- `Comprobante.Queries.Repository`: Consultas de comprobantes
- `Cuenta.Queries.Repository`: Consultas de cuentas
- `Feriados.Repository`: Gestión de feriados
- `Inversion.Repository`: Gestión de inversiones

#### **Shared.RetencionWallet**
**Dominio**: Retenciones fiscales específicas para Wallet
**Funcionalidad**:
- **Tax retention**: Retenciones automáticas
- **Calculation**: Cálculos específicos wallet
- **Compliance**: Cumplimiento fiscal
- **Certificates**: Certificados de retención
- **Integration**: Integración con AFIP

### Herramientas y Utilidades

#### **Wallet.Cuenta.SwaggerMergeAPI**
**Dominio**: Herramienta para merge de documentación Swagger
**Funcionalidad**:
- **API documentation**: Documentación unificada
- **Swagger merge**: Fusión de especificaciones
- **Versioning**: Control de versiones de API
- **Testing**: Herramientas de testing
- **Generation**: Generación automática

#### **Wallet.PrototipoQueries**
**Dominio**: Prototipo para nuevas funcionalidades de queries
**Funcionalidad**:
- **Query prototyping**: Prototipado de consultas
- **Performance testing**: Testing de rendimiento
- **New features**: Nuevas funcionalidades
- **Experimentation**: Experimentación
- **Validation**: Validación de conceptos

#### **Wallet.MassReport**
**Dominio**: Generación masiva de reportes
**Funcionalidad**:
- **Bulk reporting**: Reportes masivos
- **Scheduled generation**: Generación programada
- **Distribution**: Distribución automática
- **Performance**: Alto rendimiento
- **Customization**: Personalización de reportes

### Jobs y Procesos Wallet

#### **Jobs.Bind** (Wallet)
**Dominio**: Jobs específicos para integración BIND en Wallet
**Funcionalidad**:
- **Synchronization**: Sincronización con BIND
- **Reconciliation**: Conciliación de datos
- **Batch processing**: Procesamiento por lotes
- **Data validation**: Validación de datos
- **Error recovery**: Recuperación de errores

#### **Jobs.Internal** (Wallet)
**Dominio**: Jobs internos específicos de Wallet
**Funcionalidad**:
- **Maintenance**: Mantenimiento del sistema
- **Data cleanup**: Limpieza de datos
- **Archive**: Archivado de datos históricos
- **Performance**: Optimizaciones de rendimiento
- **Health checks**: Verificaciones de salud

---

## 🏦 CVU COLLECT

### Servicios Principal

#### **Middleware.Aggregator**
**Dominio**: Agregación y consolidación de cuentas CVU
**Funcionalidad**:
- **Account discovery**: Búsqueda automática de CVUs
- **Data aggregation**: Consolidación de información de múltiples fuentes
- **Normalization**: Estandarización de formatos de datos
- **Deduplication**: Eliminación de registros duplicados
- **Reconciliation**: Conciliación entre sistemas

#### **Middleware.Financial**
**Dominio**: Motor de operaciones financieras CVU
**Funcionalidad**:
- **Batch processing**: Procesamiento masivo de transacciones
- **Settlement**: Liquidación de operaciones CVU
- **Clearing**: Compensación entre entidades
- **Reporting**: Generación de reportes de liquidación
- **Exception handling**: Gestión de transacciones fallidas

**Repositorios Integrados**:
- `Aggregator.Repository`: Integración con agregador
- `ApiBank.Repository`: Conectividad bancaria
- `Lirium.Repository`: Procesamiento crypto
- `PagoExterno.Repository`: Pagos a terceros
- `StateMonitor.Repository`: Monitoreo de estados

#### **Middleware.BulkUploadProcess**
**Dominio**: Procesamiento masivo de archivos CSV/Excel
**Funcionalidad**:
- **File parsing**: Análisis y validación de archivos masivos
- **Data validation**: Validaciones de formato y contenido
- **Async processing**: Procesamiento en background
- **Progress tracking**: Seguimiento de progreso de carga
- **Error reporting**: Detalle de errores por registro
- **Rollback**: Reversión de cargas fallidas

#### **Middleware.StateMonitor**
**Dominio**: Monitoreo en tiempo real de estados de transacciones
**Funcionalidad**:
- **Real-time monitoring**: Tracking en tiempo real
- **Alerting**: Alertas automáticas por anomalías
- **SLA monitoring**: Control de tiempos de procesamiento
- **Dashboard**: Visualización de métricas operativas
- **Historical analysis**: Análisis de tendencias

### Servicios Compartidos

#### **Shared.ApiBank**
**Dominio**: Abstracción para integración con múltiples bancos (CVU)
**Funcionalidad**:
- **Multi-bank connectivity**: Conectores para diferentes bancos
- **Protocol normalization**: Estandarización de protocolos
- **Load balancing**: Distribución de carga entre bancos
- **Circuit breaker**: Protección contra fallos bancarios
- **Audit logging**: Registro de todas las interacciones

---

## ⚙️ BIND CONFIGURATION

### Servicios de Configuración

#### **Bind.Configuration.Admin**
**Dominio**: Interfaz administrativa web para configuraciones
**Tecnología**: React + Vite
**Funcionalidad**:
- **Configuration UI**: Interfaz moderna para administración
- **Real-time updates**: Actualización en tiempo real
- **Role-based access**: Control de accesos por roles
- **Audit trail**: Historial de cambios de configuración
- **Backup/Restore**: Backup y restauración de configuraciones

#### **Bind.Configuration.BFF**
**Dominio**: Backend for Frontend para administración
**Funcionalidad**:
- **Configuration API**: API para gestión de configuraciones
- **Validation**: Validación de configuraciones
- **Versioning**: Control de versiones de configuraciones
- **Distribution**: Distribución a servicios consumidores
- **Caching**: Cache de configuraciones frecuentes

---

## 🔵 BOTON SIMPLE (Legacy)

### Servicios Core Legacy

#### **BotonSimple.Payment**
**Dominio**: Motor de pagos legacy
**Funcionalidad**:
- **Payment processing**: Procesamiento de pagos base
- **Card tokenization**: Tokenización básica de tarjetas
- **Settlement**: Liquidación de transacciones
- **Reporting**: Reportes básicos de transacciones
- **Event handling**: Manejo de eventos de pago
- **Consumer services**: Servicios de consumo de eventos

**Componentes Especializados**:
- `Payment.Services.Core`: Servicios core de pagos
- `Payment.Service.EventHandlers`: Manejadores de eventos
- `Payment.Service.Consumer`: Consumidores de eventos
- `Payment.Service.Proxies`: Proxies de integración
- `Liquidations.Service.EventHandlers`: Manejadores de liquidaciones

#### **BotonSimple.Identity**
**Dominio**: Gestión de identidades legacy
**Funcionalidad**:
- **User management**: Gestión básica de usuarios
- **Authentication**: Autenticación legacy
- **Session management**: Gestión de sesiones
- **Event handling**: Manejo de eventos de identidad
- **Query services**: Servicios de consultas

**Componentes del Identity**:
- `Identity.Service.EventHandlers`: Manejadores de eventos
- `Identity.Service.Queries`: Servicios de consultas
- `Identity.Persistence.Database`: Persistencia de datos

#### **BotonSimple.Backoffice**
**Dominio**: Interfaz administrativa legacy
**Funcionalidad**:
- **Admin interface**: Interfaz administrativa básica
- **User management**: Gestión de usuarios del sistema
- **Configuration**: Configuraciones básicas del sistema
- **Reporting**: Reportes administrativos
- **QR generation**: Generación de códigos QR

**Componentes del Backoffice**:
- `Backoffice.Services`: Servicios del backoffice
- `Backoffice.Web`: Interfaz web

#### **BotonSimple.Security**
**Dominio**: Servicios de seguridad legacy
**Funcionalidad**:
- **Access control**: Control de accesos básico
- **Audit logging**: Logging de seguridad
- **Event handling**: Manejo de eventos de seguridad
- **Query services**: Servicios de consultas de seguridad

#### **BotonSimple.Notificacion**
**Dominio**: Sistema de notificaciones legacy
**Funcionalidad**:
- **Multi-channel notifications**: Notificaciones multi-canal
- **Email services**: Servicios de email
- **SMS services**: Servicios de SMS
- **Event handling**: Manejo de eventos de notificación
- **Consumer services**: Consumidores de eventos

**Componentes de Notificación**:
- `Notification.Service.Consumer`: Consumidor de eventos
- `Notification.Service.EventHandlers`: Manejadores de eventos
- `Notification.Service.Proxies`: Proxies de integración
- `Notification.Service.Queries`: Servicios de consultas

### Servicios de Boveda (Vault)

#### **BotonSimple.Boveda.Api**
**Dominio**: API de la bóveda de datos sensibles
**Funcionalidad**:
- **Secure storage**: Almacenamiento seguro
- **Data encryption**: Cifrado de datos
- **Key management**: Gestión de claves
- **Access control**: Control de accesos
- **Audit trail**: Trazabilidad de accesos

**Componentes de la Bóveda**:
- `Boveda.Service.EventHandlers`: Manejadores de eventos
- `Boveda.Service.Proxies`: Proxies de integración
- `Boveda.Service.Queries`: Servicios de consultas
- `Boveda.Repository`: Repositorio de datos

#### **BotonSimple.Boveda.Identity**
**Dominio**: Gestión de identidades para la bóveda
**Funcionalidad**:
- **Identity verification**: Verificación de identidades
- **Access tokens**: Tokens de acceso
- **Multi-factor auth**: Autenticación multifactor
- **Session management**: Gestión de sesiones
- **Event handling**: Manejo de eventos

#### **BotonSimple.Boveda.Iframe**
**Dominio**: Interfaz iframe para la bóveda
**Funcionalidad**:
- **Embedded interface**: Interfaz embebida
- **Secure communication**: Comunicación segura
- **Cross-origin**: Manejo de CORS
- **Responsive design**: Diseño responsivo
- **Security**: Seguridad web

#### **BotonSimple.Boveda.Backoffice**
**Dominio**: Backoffice de la bóveda
**Funcionalidad**:
- **Vault administration**: Administración de la bóveda
- **User management**: Gestión de usuarios
- **Security policies**: Políticas de seguridad
- **Audit reports**: Reportes de auditoría
- **Configuration**: Configuración del sistema

### Servicios de Formularios

#### **BotonSimple.PaymentForm.BFF**
**Dominio**: BFF para formularios de pago
**Funcionalidad**:
- **Form optimization**: Optimización de formularios
- **Payment flow**: Flujos de pago
- **Validation**: Validaciones de campos
- **Error handling**: Manejo de errores
- **Event processing**: Procesamiento de eventos

**Componentes del PaymentForm**:
- `PaymentForm.Service.Commands`: Comandos de formulario
- `PaymentForm.Service.EventHandlers`: Manejadores de eventos
- `PaymentForm.Service.Proxies`: Proxies de integración
- `PaymentForm.Service.Queries`: Servicios de consultas

#### **BotonSimple.PaymentForm.Web**
**Dominio**: Interfaz web para formularios de pago
**Funcionalidad**:
- **Payment UI**: Interfaz de pago
- **Responsive forms**: Formularios responsivos
- **Real-time validation**: Validación en tiempo real
- **Security**: Seguridad web
- **UX optimization**: Optimización UX

### Gestión de Vault

#### **BotonSimple.VaultManager**
**Dominio**: Gestión del vault legacy
**Funcionalidad**:
- **Vault orchestration**: Orquestación del vault
- **Data management**: Gestión de datos
- **Security policies**: Políticas de seguridad
- **Access control**: Control de accesos
- **Integration**: Integración con servicios

**Repositorios del VaultManager**:
- `Shared.Vault.Card.Repository`: Repositorio de tarjetas

### Procesadores Legacy

#### **Shared.Cybersource**
**Dominio**: Integración con procesador Cybersource
**Funcionalidad**:
- **Payment processing**: Procesamiento via Cybersource
- **Fraud detection**: Detección de fraude básica
- **Risk scoring**: Scoring de riesgo
- **API integration**: Integración con API
- **Settlement**: Liquidación de transacciones

**Componentes Cybersource**:
- `DataAccess.APiCybersource`: Acceso a API de Cybersource

#### **Shared.Decidir**
**Dominio**: Integración con procesador Decidir
**Funcionalidad**:
- **Payment processing**: Procesamiento via Decidir
- **Local payments**: Métodos de pago locales argentinos
- **API integration**: Integración con API Decidir
- **Settlement**: Liquidación local
- **Compliance**: Cumplimiento local

---

## 📄 ARCHIVOS RI

### Servicios Regulatorios

#### **Shared.RegulatoryInformation**
**Dominio**: Gestión de información regulatoria
**Funcionalidad**:
- **Regulatory reporting**: Generación de reportes regulatorios
- **Data collection**: Recolección de datos requeridos
- **Compliance monitoring**: Monitoreo de cumplimiento
- **Archive management**: Gestión de archivos históricos
- **Submission**: Envío automático a organismos
- **Data validation**: Validación de datos regulatorios
- **Template management**: Gestión de plantillas

**Componentes del Sistema RI**:
- `Shared.RegulatoryInformation.Api`: API principal
- `Shared.RegulatoryInformation.Application`: Lógica de aplicación
- `Shared.RegulatoryInformation.Domain`: Dominio de negocio
- `Shared.RegulatoryInformation.DataAccess.EntityFramework`: Persistencia
- `Shared.RegulatoryInformation.EventBus`: Eventos de dominio
- `Shared.RegulatoryInformation.Common`: Componentes comunes
- `Shared.Cache`: Cache especializado
- `Shared.Contract`: Contratos y DTOs

#### **ArchivosRI**
**Dominio**: Procesamiento específico de archivos regulatorios
**Funcionalidad**:
- **File processing**: Procesamiento de archivos RI
- **Format validation**: Validación de formatos
- **Data extraction**: Extracción de datos
- **Error handling**: Manejo de errores de procesamiento
- **Batch processing**: Procesamiento por lotes

### Infraestructura RI

#### **Infra** (ArchivosRI)
**Dominio**: Infraestructura específica para ArchivosRI
**Funcionalidad**:
- **Infrastructure as Code**: IaC para ArchivosRI
- **Deployment scripts**: Scripts de despliegue
- **Configuration management**: Gestión de configuraciones
- **Environment setup**: Setup de ambientes
- **Monitoring setup**: Configuración de monitoreo

---

## 🔧 PATRONES ARQUITECTÓNICOS COMUNES

### Estructura Clean Architecture
Todos los proyectos siguen una estructura consistente:

```
Proyecto.Api/                 # Controllers y endpoints
Proyecto.Application/         # Use cases y handlers  
Proyecto.Domain/             # Entidades y reglas de negocio
Proyecto.DataAccess.*/       # Adaptadores de datos
Proyecto.Common/             # DTOs y configuraciones
Proyecto.EventBus/          # Eventos de dominio
Proyecto.Test.*/            # Tests unitarios e integración
```

### Patrones de Integración
- **Repository Pattern**: Abstracción de acceso a datos
- **CQRS**: Separación entre comandos y queries
- **Event-Driven**: Comunicación asíncrona via eventos
- **Circuit Breaker**: Protección contra fallos de servicios
- **Retry Policy**: Reintentos automáticos con backoff

### Tecnologías Comunes
- **.NET 6/8**: Runtime principal
- **Entity Framework Core**: ORM principal
- **MediatR**: Mediación y CQRS
- **FluentValidation**: Validaciones
- **AutoMapper**: Mapeo de objetos
- **Serilog**: Logging estructurado
- **Redis**: Caching distribuido
- **RabbitMQ/Azure Service Bus**: Messaging

---

## 📊 MÉTRICAS Y OBSERVABILIDAD

### Monitoring Stack
- **Application Insights**: Telemetría de aplicaciones
- **Prometheus + Grafana**: Métricas de infraestructura
- **ELK Stack**: Centralización de logs
- **Jaeger**: Distributed tracing

### Health Checks
Todos los servicios implementan:
- **Liveness probes**: Verificación de vida del servicio
- **Readiness probes**: Verificación de disponibilidad
- **Dependency checks**: Validación de dependencias

---

## 🚀 DEPLOYMENT Y DEVOPS

### Containerización
- **Docker**: Containerización de servicios
- **Kubernetes (AKS)**: Orquestación en Azure
- **Helm Charts**: Gestión de deployments

### CI/CD
- **Azure DevOps**: Pipelines de build y deploy
- **GitFlow**: Gestión de branches
- **Blue-Green**: Estrategia de deployment

---

## 📋 CONCLUSIONES

El ecosistema Fintexa demuestra una arquitectura madura y bien estructurada que abarca todos los aspectos de una plataforma financiera moderna:

### Fortalezas Arquitectónicas
1. **Separación clara de responsabilidades** por dominio de negocio
2. **Patrones consistentes** aplicados across todos los proyectos
3. **Escalabilidad horizontal** mediante microservicios
4. **Observabilidad completa** con monitoring y tracing
5. **Seguridad robusta** con tokenización y compliance

### Cobertura Funcional
- **Pagos completos**: Card present/not present, QR, móvil
- **Billetera digital**: Cuenta, operaciones, inversiones
- **Open Banking**: Consentimientos y agregación
- **Compliance**: Regulatorio y antifraude
- **B2B Services**: CVU collect y APIs bancarias
- **Legacy systems**: Soporte para sistemas legacy
- **Multi-processor**: Integración con múltiples procesadores

### Infraestructura y DevOps

#### **AKS-Manifests** (Todos los ecosistemas)
**Dominio**: Manifiestos de Kubernetes para cada ecosistema
**Funcionalidad**:
- **Kubernetes deployment**: Manifiestos de despliegue
- **Service configuration**: Configuración de servicios
- **Resource management**: Gestión de recursos
- **Scaling policies**: Políticas de escalado
- **Health checks**: Verificaciones de salud

#### **Infra** (Todos los ecosistemas)
**Dominio**: Infraestructura como código por ecosistema
**Funcionalidad**:
- **Infrastructure as Code**: Terraform, ARM templates
- **Environment management**: Gestión de ambientes
- **CI/CD pipelines**: Pipelines de integración y despliegue
- **Configuration management**: Gestión centralizada de configs
- **Monitoring setup**: Setup de observabilidad

### Herramientas de Desarrollo

#### **ArquetipoBase**
**Dominio**: Template base para nuevos proyectos
**Funcionalidad**:
- **Project scaffolding**: Estructura base de proyectos
- **Best practices**: Implementación de mejores prácticas
- **Code templates**: Plantillas de código
- **Architecture patterns**: Patrones arquitectónicos
- **Testing setup**: Setup de testing

#### **Prueba.Repo** (Todos los ecosistemas)
**Dominio**: Repositorios de prueba y ejemplos
**Funcionalidad**:
- **Testing samples**: Ejemplos de testing
- **Integration examples**: Ejemplos de integración
- **Documentation**: Documentación de ejemplos
- **Best practices**: Mejores prácticas de desarrollo
- **Proof of concepts**: Pruebas de concepto

## 📊 ESTADÍSTISTICAS DEL ECOSISTEMA

### Resumen Cuantitativo

#### **Bind Aceptador**: 60+ proyectos
- 4 BFF especializados
- 15+ servicios core de procesamiento
- 25+ servicios de infraestructura compartidos
- 8+ servicios de workflow y orquestación
- 3+ interfaces web
- 5+ jobs y procesos

#### **Wallet Service**: 45+ proyectos
- 8+ servicios core
- 6+ servicios de inversión
- 10+ servicios de queries
- 8+ servicios compartidos
- 5+ herramientas y utilidades
- 3+ aplicaciones cliente
- 5+ jobs y procesos

#### **CVU Collect**: 8+ proyectos
- 4 servicios principales
- 2 servicios compartidos
- 2+ proyectos de infraestructura

#### **Bind Configuration**: 5+ proyectos
- 1 frontend React
- 1 BFF
- 3+ proyectos de soporte

#### **Boton Simple (Legacy)**: 15+ proyectos
- 5+ servicios core legacy
- 4+ servicios de bóveda
- 2+ servicios de formularios
- 2+ procesadores legacy
- 2+ herramientas de gestión

#### **ArchivosRI**: 3+ proyectos
- 1 servicio principal
- 1 procesador de archivos
- 1+ infraestructura

### **TOTAL GENERAL**: 135+ proyectos individuales

### Tecnologías por Ecosistema

#### **.NET Ecosystem** (120+ proyectos)
- .NET 6/8 como runtime principal
- Entity Framework Core para persistencia
- MediatR para CQRS y mediación
- Clean Architecture en todos los servicios

#### **Frontend Technologies**
- React + Vite (Bind.Configuration.Admin)
- .NET MAUI (Wallet.APP)
- Web interfaces (múltiples proyectos Web.*)

#### **Infrastructure**
- Kubernetes (AKS) para orquestación
- Azure como cloud provider principal
- Docker para containerización
- Infrastructure as Code (Terraform/ARM)

### Patrones Arquitectónicos Implementados

1. **Microservices Architecture**: Cada proyecto es un microservicio independiente
2. **Clean Architecture**: Separación clara de capas en todos los proyectos
3. **CQRS**: Separación entre commands y queries
4. **Event-Driven Architecture**: Comunicación asíncrona via eventos
5. **BFF Pattern**: Backend for Frontend especializado
6. **Repository Pattern**: Abstracción de acceso a datos
7. **Circuit Breaker**: Protección contra fallos
8. **Saga Pattern**: Para transacciones distribuidas

Esta arquitectura posiciona a Fintexa como una plataforma financiera integral capaz de competir en el mercado actual de fintech, con capacidades tanto B2C como B2B, y un fuerte enfoque en compliance y seguridad.

--- 

**Fecha de Análisis**: 2025 
**Versión**: 2.0 (Completa)  
**Total de Proyectos Analizados**: 135+  
**Ecosistemas Cubiertos**: 6  
**Autor**: Análisis Detallado Automatizado del Ecosistema Fintexa
