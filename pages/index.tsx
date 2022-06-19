import Head from 'next/head';
import Image from 'next/image';
import type { NextPage } from 'next';

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>0x0</title>
      </Head>
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          height: '100vh',
        }}
      >
        <div style={{ width: '100%' }}>
          <Image
            src="https://i.imgur.com/iFjI9Oq.png"
            alt="0x0"
            width={2779}
            height={1564}
            layout="responsive"
          />
        </div>
      </div>
    </>
  );
};

export default Home;
