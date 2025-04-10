# API эндпоинты

Базовый префикс: `/init/api/`

### Адреса

- `GET /addresses/` — список адресов  
- `POST /addresses/` — создать адрес  
- `GET /addresses/<id>/` — получить адрес  
- `PUT /addresses/<id>/` — обновить  
- `DELETE /addresses/<id>/` — удалить  

### Продукты

- `GET /products/` — список продуктов  
- `POST /products/` — создать продукт  
- `GET /products/<id>/` — получить продукт  
- `PUT /products/<id>/` — обновить  
- `DELETE /products/<id>/` — удалить  

### Звенья цепи (SupplyChainNode)

- `GET /nodes/` — список звеньев  
- `POST /nodes/` — создать звено  
- `GET /nodes/<id>/` — получить звено  
- `PUT /nodes/<id>/` — обновить  
- `DELETE /nodes/<id>/` — удалить  

### Сотрудники

- `GET /employees/` — список  
- `POST /employees/` — создать  
- `GET /employees/<id>/` — получить  
- `PUT /employees/<id>/` — обновить  
- `DELETE /employees/<id>/` — удалить  

### Отправка QR-кода

`POST /send-qr/` — отправка QR-кода на почту сотрудника  

***Payload:***
```json
{
  "email": "user@example.com"
}
```

[← Назад к README](../README.md)