import css from '../style/styles.module.css';

function ItemHover({ color }) {
    return (
        <div className={css['item-hover']} style={{ backgroundColor: color, color: color }}>
            <div className={css['item-hover-handle']} style={{ backgroundColor: color }}></div>
        </div>
    );
}

export default ItemHover;
