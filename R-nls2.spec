%global packname  nls2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Non-linear regression with brute force

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-proto 

BuildRequires:    R-devel tex(latex) R-proto 

%description
Adds algorithm="brute-force" and multiple starting values to nls.

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
%doc %{rlibdir}/nls2/html
%doc %{rlibdir}/nls2/NEWS
%doc %{rlibdir}/nls2/DESCRIPTION
%{rlibdir}/nls2/THANKS
%{rlibdir}/nls2/Meta
%{rlibdir}/nls2/NAMESPACE
%{rlibdir}/nls2/INDEX
%{rlibdir}/nls2/R
%{rlibdir}/nls2/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora