%global packname  TTR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.21.0
Release:          1%{?dist}
Summary:          Technical Trading Rules

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.21-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xts 


BuildRequires:    R-devel tex(latex) R-xts



%description
Functions and data to construct technical trading rules with R.

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
%doc %{rlibdir}/TTR/DESCRIPTION
%doc %{rlibdir}/TTR/html
%{rlibdir}/TTR/NAMESPACE
%{rlibdir}/TTR/Meta
%{rlibdir}/TTR/R
%{rlibdir}/TTR/help
%{rlibdir}/TTR/INDEX
%{rlibdir}/TTR/libs
%{rlibdir}/TTR/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.21.0-1
- initial package for Fedora