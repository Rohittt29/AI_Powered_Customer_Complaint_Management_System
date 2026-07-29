import React from 'react';
import { useAppSelector, useAppDispatch } from '../../redux/hooks';
import { removeToast } from '../../redux/slices/uiSlice';
import { AlertCircle, CheckCircle, Info, X, AlertTriangle } from 'lucide-react';

export function ToastContainer() {
  const toasts = useAppSelector(state => state.ui.toasts);
  const dispatch = useAppDispatch();

  if (toasts.length === 0) return null;

  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
      {toasts.map(toast => {
        let Icon = Info;
        let bgColor = "bg-white";
        let iconColor = "text-blue-500";
        let borderColor = "border-blue-200";

        if (toast.type === 'success') {
          Icon = CheckCircle;
          iconColor = "text-green-500";
          borderColor = "border-green-200";
        } else if (toast.type === 'error') {
          Icon = AlertCircle;
          iconColor = "text-red-500";
          borderColor = "border-red-200";
        } else if (toast.type === 'warning') {
          Icon = AlertTriangle;
          iconColor = "text-amber-500";
          borderColor = "border-amber-200";
        }

        return (
          <div key={toast.id} className={`flex items-start p-4 border rounded-lg shadow-lg ${bgColor} ${borderColor} w-80 transform transition-all animate-in slide-in-from-right-4`}>
            <Icon className={`w-5 h-5 mt-0.5 mr-3 shrink-0 ${iconColor}`} />
            <div className="flex-1 text-sm font-medium text-slate-700">{toast.message}</div>
            <button onClick={() => dispatch(removeToast(toast.id))} className="text-slate-400 hover:text-slate-600 shrink-0 ml-4">
              <X className="w-4 h-4" />
            </button>
          </div>
        );
      })}
    </div>
  );
}
