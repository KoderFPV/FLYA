import { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const API_URL = process.env.API_URL;

const nextConfig: NextConfig = {
  devIndicators: false,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${API_URL}/:path*`,
      },
    ];
  },
  sassOptions: {
    prependData: `
        @import 'src/styles/variables.module.scss';
        @import 'src/styles/breakpoints.module.scss';
        @import 'src/styles/functions.module.scss';
      `,
  }
};

const withNextIntl = createNextIntlPlugin();

export default withNextIntl(nextConfig);

