import React, { useState } from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent } from '../components/common/Card';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';
import { Send, Bot, User } from 'lucide-react';

interface Message {
  id: number;
  text: string;
  sender: 'ai' | 'user';
}

export function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([
    { id: 1, text: "Hello! I am your QMS AI Copilot. I can help you log a new complaint, extract data from documents, or generate a risk assessment. What would you like to do?", sender: "ai" }
  ]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    const newMsg: Message = { id: Date.now(), text: input, sender: 'user' };
    setMessages([...messages, newMsg]);
    setInput("");
    
    // Simulate AI response
    setTimeout(() => {
      setMessages(prev => [...prev, {
        id: Date.now() + 1,
        text: "I have parsed your request. I am updating the complaint state internally. Is there anything else you need to add?",
        sender: 'ai'
      }]);
    }, 1000);
  };

  return (
    <PageContainer>
      <div className="max-w-4xl mx-auto h-[calc(100vh-8rem)] flex flex-col">
        <div className="mb-6">
          <h1 className="text-2xl font-semibold tracking-tight">AI Copilot</h1>
          <p className="text-slate-500">Interact with the conversational AI to manage complaints efficiently.</p>
        </div>

        <Card className="flex-1 flex flex-col overflow-hidden shadow-md">
          <CardContent className="flex-1 overflow-y-auto p-6 space-y-6 bg-slate-50/50">
            {messages.map((msg) => (
              <div key={msg.id} className={`flex gap-4 ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                {msg.sender === 'ai' && (
                  <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center shrink-0">
                    <Bot className="w-4 h-4 text-indigo-600" />
                  </div>
                )}
                <div className={`px-4 py-3 rounded-2xl max-w-[80%] ${
                  msg.sender === 'user' 
                    ? 'bg-indigo-600 text-white rounded-br-sm shadow-sm' 
                    : 'bg-white border text-slate-800 rounded-bl-sm shadow-sm'
                }`}>
                  <p className="text-sm leading-relaxed">{msg.text}</p>
                </div>
                {msg.sender === 'user' && (
                  <div className="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center shrink-0">
                    <User className="w-4 h-4 text-slate-600" />
                  </div>
                )}
              </div>
            ))}
          </CardContent>
          <div className="p-4 border-t bg-white">
            <form 
              onSubmit={(e) => { e.preventDefault(); handleSend(); }}
              className="flex items-center space-x-2"
            >
              <Input 
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Describe the complaint in natural language..." 
                className="flex-1 h-12 rounded-full px-6 bg-slate-50"
              />
              <Button type="submit" size="icon" className="h-12 w-12 rounded-full shrink-0">
                <Send className="w-5 h-5 ml-1" />
              </Button>
            </form>
          </div>
        </Card>
      </div>
    </PageContainer>
  );
}
