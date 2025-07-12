import React from 'react';
import styles from './Header.module.scss';

export const Header = () => {
  return <div className={styles.header}>
    <div className={styles.headerLeft}>
      <span className={styles.title}>ShopChat AI</span>
    </div>
    <div className={styles.headerRight}>
      <button className={styles.button}>Login</button>
      <button className={styles.button}>Sign Up</button>
      <button className={styles.button}>Cart</button>
    </div>
  </div>
}
