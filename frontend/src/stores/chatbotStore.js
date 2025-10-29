import { defineStore } from 'pinia'
import axios from 'axios'

export const useChatbotStore = defineStore('chatbot', {
  state: () => ({
    prompt: '',
    response: '',
    loading: false,
    error: ''
  }),

  actions: {
    async sendMessage() {
      this.loading = true
      this.error = ''
      try {
        const res = await axios.post('http://localhost:8080/api/chatbot/chat/', {
          prompt: this.prompt
        })
        this.response = res.data.response
      } catch (err) {
        console.error(err)
        this.error = 'خطا در ارتباط با مدل.'
      } finally {
        this.loading = false
      }
    }
  }
})
