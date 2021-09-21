import { Client as Styletron } from "styletron-engine-atomic";
import { Provider as StyletronProvider } from "styletron-react";
import { LightTheme, BaseProvider, styled } from "baseui";
import Results from "./views/Results";

const engine = new Styletron();

const Centered = styled("div", {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100%",
    marginLeft: "1rem",
});

export default function App() {
    return (
        <StyletronProvider value={engine}>
            <BaseProvider theme={LightTheme}>
                <Centered>
                    <Results />
                </Centered>
            </BaseProvider>
        </StyletronProvider>
    );
}
