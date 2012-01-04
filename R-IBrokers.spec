%global packname  IBrokers
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          R API to Interactive Brokers Trader Workstation

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xts 


BuildRequires:    R-devel tex(latex) R-xts



%description
Provides native R access to Interactive Brokers Trader Workstation API.

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
%doc %{rlibdir}/IBrokers/html
%doc %{rlibdir}/IBrokers/DESCRIPTION
%doc %{rlibdir}/IBrokers/doc
%{rlibdir}/IBrokers/NAMESPACE
%{rlibdir}/IBrokers/help
%{rlibdir}/IBrokers/Meta
%{rlibdir}/IBrokers/INDEX
%{rlibdir}/IBrokers/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora