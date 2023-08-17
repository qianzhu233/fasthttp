# fasthttp

A simple local file server using http.server.

一個使用 http.server 的簡單本地檔案伺服器。

The basic code is from https://pythonjishu.com/gmagntbjhgwxgmr/

基礎程式碼來自https://pythonjishu.com/gmagntbjhgwxgmr/

You can set environment variables, then you can work from the command line in any folder.

您可以設定環境變數，即可在任何資料夾下的命令列下工作。

After executing the program, append `:1145` (example: `127.0.0.1:1145`, the port can be changed in `fasthttp.py`) to access local files.

執行程式後，訪問裝置的IP位址後附加`:1145`（例：`127.0.0.1:1145`，可以在`fasthttp.py`中更改埠），即可訪問本地檔。

Use `pyinstaller -F -c fasthttp.py` to make executables.

使用`pyinstaller -F -c fasthttp.py`來製作可執行檔案。