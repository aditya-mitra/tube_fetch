import { Card, StyledBody, StyledAction } from "baseui/card";
import { Button } from "baseui/button";
import { Label2, Paragraph2 } from "baseui/typography";

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
    publishedDate,
}: IYoutubeCard) {
    return (
        <Card headerImage={thumbnailUrl} title={title}>
            <StyledBody>
                <Paragraph2>{description}</Paragraph2>
                <Label2 marginLeft="5rem">
                    <strong>{new Date(publishedDate).toLocaleString()} </strong>
                </Label2>
            </StyledBody>
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
