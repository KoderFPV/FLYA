import styles from "./Footer.module.scss";

export const Footer = () => {
  return <div className={styles.footer}>
    <div className={styles.footerLeft}>
      © 2025 ShopChat AI. All rights reserved.
    </div>
    <div className={styles.footerRight}>
      <div>Terms</div>
      <div>Privacy</div>
      <div>Help</div>

    </div>
  </div>
}
