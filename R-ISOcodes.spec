%global packname  ISOcodes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.07.31
Release:          1%{?dist}
Summary:          Selected ISO codes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
ISO language, territory, currency, script and character codes. Provides
ISO 639 language codes, ISO 3166 territory codes, ISO 4217 currency codes,
ISO 15924 script codes, and the ISO 8859 character codes as well as the UN
M.49 area codes.

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
%doc %{rlibdir}/ISOcodes/DESCRIPTION
%doc %{rlibdir}/ISOcodes/html
%{rlibdir}/ISOcodes/Meta
%{rlibdir}/ISOcodes/data
%{rlibdir}/ISOcodes/help
%{rlibdir}/ISOcodes/NAMESPACE
%{rlibdir}/ISOcodes/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.07.31-1
- initial package for Fedora