import { Input, SIZE } from "baseui/input";
import { StateUpdater } from "preact/hooks";

interface ISearchBar {
    value: string;
    setValue: StateUpdater<string>;
}

export default function SearchBar({ value, setValue }: ISearchBar) {
    return (
        <Input
            value={value}
            onChange={(e) => setValue(e.currentTarget.value)}
            positive
            size={SIZE.large}
            placeholder="Search any video on Football"
            clearable
            clearOnEscape
        />
    );
}
