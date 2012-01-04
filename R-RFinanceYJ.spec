%global packname  RFinanceYJ
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          RFinanceYJ

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-xts 


BuildRequires:    R-devel tex(latex) R-XML R-xts



%description
Japanese stock market from Yahoo!-finance-Japan

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/RFinanceYJ/DESCRIPTION
%doc %{rlibdir}/RFinanceYJ/html
%{rlibdir}/RFinanceYJ/R
%{rlibdir}/RFinanceYJ/Meta
%{rlibdir}/RFinanceYJ/INDEX
%{rlibdir}/RFinanceYJ/NAMESPACE
%{rlibdir}/RFinanceYJ/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora