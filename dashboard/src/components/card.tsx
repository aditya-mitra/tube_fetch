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
        <Card
            overrides={{ Root: { style: { width: "328px" } } }}
            headerImage={thumbnailUrl}
            title={title}
        >
            <StyledBody>{description}</StyledBody>
            <StyledAction>
                <Button
                    overrides={{ BaseButton: { style: { width: "100%" } } }}
                >
                    {videoId}
                </Button>
            </StyledAction>
        </Card>
    );
}
