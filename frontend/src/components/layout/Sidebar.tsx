import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, FileText, MessageSquare, UploadCloud, ShieldAlert, Settings } from 'lucide-react';
import { cn } from '../../lib/utils';

const navItems = [
  { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard' },
  { icon: FileText, label: 'Complaints', path: '/complaints' },
  { icon: MessageSquare, label: 'AI Copilot', path: '/chat' },
  { icon: UploadCloud, label: 'Upload Documents', path: '/upload' },
  { icon: ShieldAlert, label: 'Risk Assessment', path: '/risk' },
];

export function Sidebar() {
  return (
    <div className="w-64 bg-slate-900 text-slate-100 flex flex-col h-screen fixed left-0 top-0">
      <div className="p-6 border-b border-slate-800">
        <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-400">
          QMS AI Copilot
        </h1>
      </div>
      
      <nav className="flex-1 p-4 space-y-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => cn(
              "flex items-center space-x-3 px-3 py-2 rounded-lg transition-colors group",
              isActive ? "bg-indigo-600 text-white" : "hover:bg-slate-800 text-slate-300 hover:text-white"
            )}
          >
            <item.icon className="w-5 h-5" />
            <span className="font-medium">{item.label}</span>
          </NavLink>
        ))}
      </nav>
      
      <div className="p-4 border-t border-slate-800">
        <button className="flex items-center space-x-3 px-3 py-2 w-full rounded-lg hover:bg-slate-800 text-slate-300 hover:text-white transition-colors">
          <Settings className="w-5 h-5" />
          <span className="font-medium">Settings</span>
        </button>
      </div>
    </div>
  );
}
