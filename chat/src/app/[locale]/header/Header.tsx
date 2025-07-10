import React from 'react';
import { LogoIcon } from './icons/LogoIcon';
import { UserIcon } from './icons/UserIcon';
import { CartIcon } from './icons/CartIcon';

const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-12xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex justify-between items-center h-8">

          <div className="flex items-center space-x-2">
            <LogoIcon />
            <span className="text-xl text-gray-800">ShopChat AI</span>
          </div>

          <div className="flex items-center space-x-4">
            <button
              aria-label="Cart"
              className="p-2 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <CartIcon />
            </button>
            <button
              aria-label="User profile"
              className="p-2 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <UserIcon />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
