import { Card, StyledBody, StyledAction } from "baseui/card";
import { Button } from "baseui/button";

interface IYoutubeCard {
    thumbnailUrl: string;
    title: string;
    description: string;
    videoId: string;
    publishedDate: string;
}

export default function YoutubeCard({
    title,
    thumbnailUrl,
    description,
    videoId,
}: IYoutubeCard) {
    return (
        <Card headerImage={thumbnailUrl} title={title}>
            <StyledBody>{description}</StyledBody>
            <StyledAction>
                <Button
                    onClick={() =>
                        window
                            .open(`https://youtu.be/${videoId}`, "_blank")
                            ?.focus()
                    }
                    overrides={{ BaseButton: { style: { width: "100%" } } }}
                >
                    Open In New Tab
                </Button>
            </StyledAction>
        </Card>
    );
}
