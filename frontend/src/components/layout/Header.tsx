import React from 'react';
import { Bell, Search, User } from 'lucide-react';
import { Input } from '../common/Input';
import { Button } from '../common/Button';

export function Header() {
  return (
    <header className="h-16 border-b bg-white flex items-center justify-between px-6 sticky top-0 z-10 w-full">
      <div className="flex items-center flex-1">
        <div className="relative w-96 hidden md:block">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
          <Input 
            placeholder="Search complaints, batches..." 
            className="pl-10 bg-slate-50 border-none focus-visible:ring-1"
          />
        </div>
      </div>
      
      <div className="flex items-center space-x-4">
        <Button variant="ghost" size="icon" className="relative text-slate-500">
          <Bell className="w-5 h-5" />
          <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-white"></span>
        </Button>
        <div className="h-8 w-8 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-700 font-medium border border-indigo-200">
          <User className="w-4 h-4" />
        </div>
      </div>
    </header>
  );
}
