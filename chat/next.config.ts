import { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const nextConfig: NextConfig = {
  devIndicators: false,
  // async redirects() {
  //   return [
  //     {
  //       source: '/',
  //       destination: '/chat',
  //       permanent: false,
  //     },
  //   ];
  // },
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

