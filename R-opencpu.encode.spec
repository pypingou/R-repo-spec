%global packname  opencpu.encode
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.21
Release:          1%{?dist}
Summary:          opencpu object encoder/decoder

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 
Requires:         R-RJSONIO R-base64 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-RJSONIO R-base64 


%description
Encodes R objects to a standardized JSON format

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
%doc %{rlibdir}/opencpu.encode/DESCRIPTION
%doc %{rlibdir}/opencpu.encode/html
%{rlibdir}/opencpu.encode/R
%{rlibdir}/opencpu.encode/Meta
%{rlibdir}/opencpu.encode/NAMESPACE
%{rlibdir}/opencpu.encode/INDEX
%{rlibdir}/opencpu.encode/help
RPM build errors:

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.21-1
- initial package for Fedora