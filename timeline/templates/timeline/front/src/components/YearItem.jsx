import { useMemo } from 'react';
import { observer } from 'mobx-react';
import { state } from '../state';
import css from '../style/styles.module.css';

const YearItem = observer(({ item, index, handleSelect, selectedItem }) => {
    const { colors, availableYears, selectedColor } = state;

    const selected = useMemo(() => {
        const selection = selectedItem === item;
        return selection;
    }, [selectedItem, item]);

    const color = useMemo(() => {
        return selected ? selectedColor : colors[index];
    }, [index, colors, selected, selectedColor]);

    return (
        <div
            key={index}
            onClick={() => handleSelect(item)}
            style={{ backgroundColor: color }}
            className={
                index === 0
                    ? `${css['timeline-slot']} ${css['slot-first']}`
                    : index === availableYears.length - 1
                    ? `${css['timeline-slot']} ${css['slot-last']}`
                    : css['timeline-slot']
            }
        >
            {item}
        </div>
    );
});
export default YearItem;
