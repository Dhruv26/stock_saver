$(function () {
    var fieldNum = 1;
    $("#addNewField").click(function () {
        var current = $("#indicators");

        $("#indicators").append(createParameter(fieldNum));
        fieldNum += 1;
        console.log(`New parameter added! Parameter count: ${fieldNum}`);
    });
});

function createParameter(count) {
    var toAppend = `
         <li>
            <label for="indicators-${count}">Indicators-${count}</label>
            <table id="indicators-${count}">
                <tr>
                    <th>
                        <label for="indicators-${count}-type">Parameter Type</label>
                    </th>
                    <td>
                        <select id="indicators-${count}-type" name="indicators-${count}-type" required>
                        </select>
                    </td>
                </tr>
                <tr>
                    <th>
                        <label for="indicators-${count}-period">Period</label>
                    </th>
                    <td>
                        <select id="indicators-${count}-period" name="indicators-${count}-period" required>
                            <option value="DAILY">DAILY</option>
                            <option value="WEEKLY">WEEKLY</option>
                            <option value="MONTHLY">MONTHLY</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <th>
                        <label for="indicators-${count}-name">Indicator</label>
                    </th>
                    <td>
                        <select id="indicators-${count}-name" name="indicators-${count}-name" required>
                            <option value="SMA">SMA</option>
                            <option value="EMA">EMA</option>
                            <option value="RSI">RSI</option>
                            <option value="OTHER">OTHER</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <th>
                        <label for="indicators-${count}-other_name">Other Indicator(optional)</label>
                    </th>
                    <td>
                        <input id="indicators-${count}-other_name" name="indicators-${count}-other_name" required type="text" value="">
                    </td>
                </tr>
                <tr>
                    <th>
                        <label for="indicators-${count}-value">Value</label>
                    </th>
                    <td>
                        <input id="indicators-${count}-value" name="indicators-${count}-value" required type="text" value="">
                    </td>
                </tr>
            </table>
         </li>`;
    console.log("" + toAppend);
    return toAppend;
}