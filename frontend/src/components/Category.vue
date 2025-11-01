<script setup>
import { ref } from "vue";

const prompt = ref("");
const response = ref("");

async function sendPrompt() {
  try {
    const res = await fetch("http://192.168.9.73:8086/api/chatbot/chat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: prompt.value }),
    });
    const data = await res.json();
    response.value = data.response;
  } catch (e) {
    response.value = "خطا در اتصال به مدل.";
    console.error(e);
  }
}
</script>

<template>
  <div class="chatbox">
    <textarea v-model="prompt" placeholder="پیام خودت رو بنویس..."></textarea>
    <button @click="sendPrompt">ارسال</button>
    <pre>{{ response }}</pre>
  </div>
</template>

<style scoped>
.chatbox {
  width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
textarea {
  min-height: 80px;
}
</style>
