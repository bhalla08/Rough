@code {
    private RegionModel TempRegion { get; set; }
    private bool IsSaveDisabled => string.IsNullOrWhiteSpace(TempRegion.Code) || string.IsNullOrWhiteSpace(TempRegion.Name);

    protected override void OnParametersSet()
    {
        // Clone the original Region to TempRegion for editing
        TempRegion = new RegionModel
        {
            Code = Region.Code,
            Name = Region.Name,
            ShortDescription = Region.ShortDescription,
            Description = Region.Description,
            Status = Region.Status
        };
    }

    private void Save()
    {
        // Commit the changes from TempRegion back to Region
        Region.Code = TempRegion.Code;
        Region.Name = TempRegion.Name;
        Region.ShortDescription = TempRegion.ShortDescription;
        Region.Description = TempRegion.Description;
        Region.Status = TempRegion.Status;

        MudDialog.Close(DialogResult.Ok(Region));
    }

    private void Cancel()
    {
        MudDialog.Cancel();
    }
}

<MudDialog>
    <DialogContent>
        <MudTextField @bind-Value="TempRegion.Code" Label="Code" Required="true" Disabled="@IsEditMode" />
        <MudTextField @bind-Value="TempRegion.Name" Label="Name" Required="true" />
        <MudTextField @bind-Value="TempRegion.ShortDescription" Label="Short Description" />
        <MudTextField @bind-Value="TempRegion.Description" Label="Description" />
        <MudSelect T="string" @bind-Value="TempRegion.Status" Label="Status">
            <MudSelectItem Value="Active">Active</MudSelectItem>
            <MudSelectItem Value="Inactive">Inactive</MudSelectItem>
        </MudSelect>
    </DialogContent>
    <DialogActions>
        <MudButton Variant="Variant.Filled" Color="Color.Primary" OnClick="Save" Disabled="IsSaveDisabled">
            SAVE
        </MudButton>
        <MudButton Variant="Variant.Text" Color="Color.Secondary" OnClick="Cancel">
            CANCEL
        </MudButton>
    </DialogActions>
</MudDialog>
