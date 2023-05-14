[# library_thothttps://stackoverflow.com/questions/50793876/rocket-chat-realtime-api-in-browser](https://stackoverflow.com/questions/50793876/rocket-chat-realtime-api-in-browser)
Конечно, вот пример кода на Kotlin с использованием Ktor для подключения к Rocket.Chat Realtime API и получения уведомлений о новых сообщениях:

import io.ktor.client.*
import io.ktor.client.features.websocket.*
import io.ktor.client.request.*
import io.ktor.http.*
import io.ktor.http.cio.websocket.*
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

data class Message(val id: String, val roomId: String, val text: String)

suspend fun main() {
    val client = HttpClient {
        install(WebSockets)
    }

    client.webSocket(
        method = HttpMethod.Get,
        host = "localhost",
        port = 3000,
        path = "/websocket"
    ) {
        // Авторизация на сервере
        send("""{"msg": "connect", "version": "1", "support": ["1", "pre2", "pre1"]}""")

        // Подписываемся на событие stream-room-messages
        send("""{"msg": "sub", "id": "stream-room-messages", "name": "stream-room-messages", "params": ["<room_id>", false]}""")

        // Получаем сообщения
        while (true) {
            val message = incoming.receive() as? Frame.Text ?: continue
            val text = message.readText()

            // Обрабатываем сообщение
            when {
                text.contains("stream-room-messages") -> {
                    val json = text.substringAfter("{").substringBeforeLast("}")
                    val message = Message(
                        json.substringAfter("id\":").substringBefore(",").trim('"'),
                        json.substringAfter("rid\":").substringBefore(",").trim('"'),
                        json.substringAfter("msg\":\"").substringBeforeLast("\"").replace("\\n", "\n")
                    )
                    println(message)
                }
            }
        }
    }
}


В этом примере мы создаем HTTP-клиент с помощью Ktor и подключаемся к серверу Rocket.Chat через WebSocket. Затем отправляем запрос на авторизацию и подписываемся на событие stream-room-messages, чтобы получать уведомления о новых сообщениях в комнате.

После подписки на событие stream-room-messages, мы используем бесконечный цикл для получения и обработки сообщений, которые приходят в WebSocket-соединение. Для обработки новых сообщений мы разбираем JSON-данные и создаем объект Message, который содержит идентификатор сообщения, идентификатор комнаты и текст сообщения.

Обратите внимание, что в примере выше <room_id> должен быть заменен на идентификатор комнаты, для которой вы хотите получать уведомления о новых сообщениях.
