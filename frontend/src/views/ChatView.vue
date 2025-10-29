<script setup>
import { storeToRefs } from 'pinia'
import { useChatbotStore } from '@/stores/chatbotStore'

const chatbot = useChatbotStore()
const { prompt, response, loading, error } = storeToRefs(chatbot)

const sendMessage = () => {
  chatbot.sendMessage()
}
</script>

<template>
  <div class="chat-container">
    <h2>💬 چت با مدل آفلاین</h2>

    <textarea v-model="prompt" placeholder="پیام خود را بنویس..."></textarea>
    <button @click="sendMessage" :disabled="loading">ارسال</button>

    <div v-if="loading">در حال پردازش...</div>

    <div v-if="error" style="color:red">{{ error }}</div>

    <div v-if="response">
      <h3>پاسخ مدل:</h3>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  width: 600px;
  margin: 40px auto;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
}
textarea {
  width: 100%;
  height: 150px;
  margin-bottom: 10px;
}
button {
  padding: 8px 16px;
}
</style>
