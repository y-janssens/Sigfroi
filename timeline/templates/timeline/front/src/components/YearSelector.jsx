import { useState, useCallback } from 'react';
import { observer } from 'mobx-react';
import { state } from '../state';
import YearItem from './YearItem';
import css from '../style/styles.module.css';

const YearSelector = observer(() => {
    const { availableYears } = state;
    const [selected, setSelected] = useState(1164);

    const handleSelect = useCallback((item) => {
        setSelected(item);
        state.setSelectedYear(item);
        state.setSelectedItem([]);
    }, []);

    return (
        <div className={css['slots-container']}>
            {availableYears.map((item, index) => {
                return <YearItem key={index} item={item} index={index} handleSelect={handleSelect} selectedItem={selected} />;
            })}
        </div>
    );
});
export default YearSelector;
