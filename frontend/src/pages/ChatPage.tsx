import React, { useState, useEffect, useRef } from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent } from '../components/common/Card';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';
import { Send, Bot, User } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../redux/hooks';
import { sendMessage, addUserMessage } from '../redux/slices/chatSlice';
import { addToast } from '../redux/slices/uiSlice';

export function ChatPage() {
  const [input, setInput] = useState("");
  const dispatch = useAppDispatch();
  const { messages, status } = useAppSelector(state => state.chat);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, status]);

  const handleSend = async () => {
    if (!input.trim() || status === 'loading') return;
    
    const userText = input;
    setInput("");
    
    dispatch(addUserMessage(userText));
    
    try {
      await dispatch(sendMessage(userText)).unwrap();
    } catch (err: any) {
      dispatch(addToast({ type: 'error', message: err.message || "Failed to communicate with AI Copilot." }));
    }
  };

  return (
    <PageContainer>
      <div className="max-w-4xl mx-auto h-[calc(100vh-8rem)] flex flex-col">
        <div className="mb-6">
          <h1 className="text-2xl font-semibold tracking-tight">AI Copilot</h1>
          <p className="text-slate-500">Interact with the conversational AI to manage complaints efficiently.</p>
        </div>

        <Card className="flex-1 flex flex-col overflow-hidden shadow-md">
          <CardContent className="flex-1 overflow-y-auto p-6 space-y-6 bg-slate-50/50" ref={scrollRef}>
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
            {status === 'loading' && (
              <div className="flex gap-4 justify-start">
                <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center shrink-0">
                  <Bot className="w-4 h-4 text-indigo-600" />
                </div>
                <div className="px-4 py-3 rounded-2xl bg-white border text-slate-800 rounded-bl-sm shadow-sm flex items-center space-x-1">
                  <div className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                  <div className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                  <div className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                </div>
              </div>
            )}
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
                disabled={status === 'loading'}
              />
              <Button type="submit" size="icon" className="h-12 w-12 rounded-full shrink-0" disabled={status === 'loading' || !input.trim()}>
                <Send className="w-5 h-5 ml-1" />
              </Button>
            </form>
          </div>
        </Card>
      </div>
    </PageContainer>
  );
}
