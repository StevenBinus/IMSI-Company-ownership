package utils

import (
	"bytes"
	"crypto/tls"
	"fmt"
	"html/template"
	"os"
	"path/filepath"
	"user-service/api/config"

	"github.com/k3a/html2text"
	"gopkg.in/gomail.v2"
)

type EmailData struct {
	URL     string
	Subject string
}

// ? Email template parser

func ParseTemplateDir(dir string) (*template.Template, error) {
	var paths []string
	fmt.Println(dir)
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			paths = append(paths, path)
		}
		return nil
	})

	if err != nil {
		return nil, err
	}
	return template.ParseFiles(paths...)
}

func SendEmail(email string, data *EmailData, emailTemp string) (bool, error) {
	config.InitEnvConfigs(true, "")

	// Sender data.
	from := config.EnvConfigs.SmtpEmailFrom
	smtpPass := config.EnvConfigs.SmtpPass
	smtpUser := config.EnvConfigs.SmtpUser
	to := email
	smtpHost := config.EnvConfigs.SmtpHost
	smtpPort := config.EnvConfigs.SmtpPort
	var body bytes.Buffer

	template, err := ParseTemplateDir("api/templates")
	if err != nil {
		return false, err
	}

	template.ExecuteTemplate(&body, emailTemp, &data)

	m := gomail.NewMessage()

	m.SetHeader("From", from)
	m.SetHeader("To", to)
	m.SetHeader("Subject", data.Subject)
	m.SetBody("text/html", body.String())
	m.AddAlternative("text/plain", html2text.HTML2Text(body.String()))

	d := gomail.NewDialer(smtpHost, smtpPort, smtpUser, smtpPass)
	d.TLSConfig = &tls.Config{InsecureSkipVerify: true}

	// Send Email
	if err := d.DialAndSend(m); err != nil {
		return false, err
	}
	return true, nil
}
